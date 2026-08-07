#!/usr/bin/env python3
# =====================================================================
#  EXTRACTION ADAPTER  —  bridge any PyTorch model -> the frozen detector
#
#  The frozen detector (detector_frozen.py) is model-agnostic: it consumes a
#  trajectory of turn-boundary hidden-state vectors. The only model-specific step
#  is GETTING those vectors out of YOUR model. This adapter does that for any
#  torch nn.Module via a forward hook on a chosen layer — no model surgery, and
#  nothing here tunes the detector to the model (frozen-transfer wall intact).
#
#  Works with:
#    * your from-scratch toy (TinyLM) — hook a Block, or use its capture_layer
#    * your larger world-model — hook the residual stream at a mid-late block
#    * HF causal LMs — hook a decoder layer (or use output_hidden_states)
#
#  INTERFACE CONTRACT (what you provide):
#    - a model (nn.Module) in eval mode on some device
#    - the LAYER whose output is the residual stream to read: a module object, a
#      dotted name ("transformer.h.5"), an int index, or a float fraction (0.6)
#    - a way to turn a multi-turn conversation into token ids per cumulative turn:
#      either a tokenizer (HF, with/without chat_template) OR pre-tokenized turns
#    You get back: a (num_turns, d_model) numpy trajectory -> feed detector_frozen.
#
#  USAGE:
#    python3 extract_adapter.py --selftest        # proves the pipe on a local model
#  or import:
#    from extract_adapter import extract_trajectory, resolve_layer
#    traj = extract_trajectory(model, resolve_layer(model, 0.6), turns, tokenizer, device)
#    from detector_frozen import score_trajectory
#    scores = score_trajectory(traj, clean_centroid)
# =====================================================================
import argparse
import numpy as np
import torch


# ---------------------------------------------------------------------
#  Layer resolution — find the module whose output is the residual stream.
# ---------------------------------------------------------------------
def _find_block_list(model):
    """Heuristic: locate the ordered list of transformer blocks."""
    cands = ['transformer.h', 'model.layers', 'gpt_neox.layers', 'model.decoder.layers',
             'blocks', 'layers', 'encoder.layer', 'h']
    for name in cands:
        obj = model
        ok = True
        for part in name.split('.'):
            if hasattr(obj, part):
                obj = getattr(obj, part)
            else:
                ok = False; break
        if ok and hasattr(obj, '__len__') and len(obj) > 0:
            return name, obj
    # fall back: any ModuleList attribute
    for n, m in model.named_modules():
        if isinstance(m, torch.nn.ModuleList) and len(m) > 0:
            return n, m
    raise ValueError("Could not locate a transformer block list; pass an explicit "
                     "module or dotted name as the layer spec.")

def _get_by_name(model, dotted):
    obj = model
    for part in dotted.split('.'):
        obj = obj[int(part)] if part.isdigit() else getattr(obj, part)
    return obj

def resolve_layer(model, spec):
    """spec -> a module to hook.
       module         -> used as-is
       str dotted     -> resolved by name ('transformer.h.5')
       int k          -> block[k] from the detected block list (negative ok)
       float f in(0,1)-> block[round(f*(L-1))] (mid-late default 0.6)"""
    if isinstance(spec, torch.nn.Module):
        return spec
    if isinstance(spec, str):
        return _get_by_name(model, spec)
    _, blocks = _find_block_list(model)
    L = len(blocks)
    if isinstance(spec, float):
        idx = max(0, min(L - 1, round(spec * (L - 1))))
    elif isinstance(spec, int):
        idx = spec if spec >= 0 else L + spec
    else:
        raise TypeError(f"layer spec must be module/str/int/float, got {type(spec)}")
    return blocks[idx]


# ---------------------------------------------------------------------
#  Residual capture via forward hook.
# ---------------------------------------------------------------------
class ResidualCapture:
    """Context manager: hooks `module`, stores its output as (T, d) for the last
    forward pass. Handles modules that return a tensor or a tuple(tensor, ...)."""
    def __init__(self, module):
        self.module = module; self.handle = None; self.last = None
    def __enter__(self):
        def hook(_m, _inp, out):
            t = out[0] if isinstance(out, (tuple, list)) else out
            self.last = t.detach()
        self.handle = self.module.register_forward_hook(hook)
        return self
    def __exit__(self, *a):
        if self.handle is not None:
            self.handle.remove()
    def boundary_vector(self, pos=-1):
        """Hidden state at token index `pos` (default last) of batch item 0."""
        if self.last is None:
            raise RuntimeError("no forward pass captured")
        return self.last[0, pos, :].float().cpu().numpy()


# ---------------------------------------------------------------------
#  Turn -> token ids (cumulative context per turn).
# ---------------------------------------------------------------------
def _ids_for_turns(tokenizer, turns_so_far, device):
    if tokenizer is not None and getattr(tokenizer, 'chat_template', None):
        msgs = [{"role": "user", "content": t} for t in turns_so_far]
        ids = tokenizer.apply_chat_template(msgs, add_generation_prompt=True, return_tensors="pt")
    elif tokenizer is not None:
        text = "\n".join(turns_so_far) + "\n"
        ids = tokenizer(text, return_tensors="pt").input_ids
    else:
        raise ValueError("provide a tokenizer, or use extract_trajectory_from_ids")
    return ids.to(device)


def extract_trajectory(model, layer, turns, tokenizer=None, device=None, forward_fn=None):
    """Return (num_turns, d_model) numpy array of residual-stream states at each
    turn boundary. `turns` is a list of user-turn strings. `layer` is anything
    resolve_layer accepts. `forward_fn(model, ids)` overrides the default forward
    (use for models needing special kwargs)."""
    device = device or next(model.parameters()).device
    module = resolve_layer(model, layer)
    model.eval()
    states = []
    with ResidualCapture(module) as cap:
        for i in range(len(turns)):
            ids = _ids_for_turns(tokenizer, turns[:i + 1], device)
            with torch.no_grad():
                (forward_fn or (lambda m, x: m(x)))(model, ids)
            states.append(cap.boundary_vector(-1))
    return np.asarray(states)


def extract_trajectory_from_ids(model, layer, cumulative_id_tensors, device=None, forward_fn=None):
    """Pre-tokenized variant: `cumulative_id_tensors` is a list of (1,T_i) LongTensors
    (one per turn boundary, each the cumulative context up to that boundary)."""
    device = device or next(model.parameters()).device
    module = resolve_layer(model, layer)
    model.eval()
    states = []
    with ResidualCapture(module) as cap:
        for ids in cumulative_id_tensors:
            ids = ids.to(device)
            with torch.no_grad():
                (forward_fn or (lambda m, x: m(x)))(model, ids)
            states.append(cap.boundary_vector(-1))
    return np.asarray(states)


# ---------------------------------------------------------------------
#  Self-test: prove capture + detector run on a small local model, no download.
# ---------------------------------------------------------------------
def _selftest():
    import detector_frozen as DET
    from transformers import GPT2Config, GPT2LMHeadModel
    print(f"frozen detector {DET.FROZEN_VERSION}  {DET.detector_hash()[:16]}…")
    cfg = GPT2Config(vocab_size=256, n_positions=128, n_embd=64, n_layer=6, n_head=4)
    model = GPT2LMHeadModel(cfg).eval()

    # layer resolution: fraction, int, and dotted name should all resolve
    m_frac = resolve_layer(model, 0.6)
    m_int = resolve_layer(model, 3)
    m_name = resolve_layer(model, "transformer.h.3")
    assert m_int is m_name, "int and dotted-name layer resolution disagree"
    print(f"resolved layer (0.6 -> block, int 3 == name 'transformer.h.3'): OK")

    # pre-tokenized 5-turn trajectory (random ids stand in for a tokenizer)
    rng = np.random.default_rng(0)
    toks = list(rng.integers(0, 256, size=6)); cum = []
    for _ in range(5):
        toks += list(rng.integers(0, 256, size=int(rng.integers(4, 8))))
        cum.append(torch.tensor([toks]))
    traj = extract_trajectory_from_ids(model, m_frac, cum)
    print(f"trajectory shape: {traj.shape}  (turns, d_model)")
    scores = DET.score_trajectory(traj, clean_centroid=np.zeros(traj.shape[1]))
    finite = all(np.isfinite(v) for v in scores.values() if isinstance(v, float))
    print("detector on extracted trajectory:",
          {k: round(v, 4) for k, v in scores.items() if isinstance(v, float)})
    print(f"\nADAPTER {'PASS' if (traj.shape == (5, 64) and finite) else 'FAIL'}: "
          f"forward-hook capture + frozen detector run end-to-end on a real model.")
    print("For YOUR world-model: pass the model, a layer spec (module/name/int/frac),")
    print("and your turns (+ tokenizer). Everything downstream is the frozen detector.")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    _selftest()
