# Pre-registration Stub — H-SC1: Self-Conditioning by an Early Frame

**Status: DRAFT v0.1 — WORKING DOCUMENT, NOT DEPOSITED.** One-page stub in the program's commit-before-run style. Nothing runs until the freeze block (§6) is filled and the code + secret hashes are recorded. Lens origin: `LENS_self_conditioning_and_early_frames.md` (fenced; this stub is the step that would move H-SC1 from lens to registered test). Program: Nucleation Pilot & Related Projects. ORCID 0009-0004-2308-6051. Intake 2026-08-07.

## 1. Hypothesis

**H-SC1.** An explicit early *intent-frame* in a generation context (a sentence that declares what the text will do, e.g. "this document reports X, Y, Z") is a **self-installed benign instance of planted-early / still-live residue**. Specifically it (a) **reduces later drift** relative to a matched context without the frame, and (b) leaves a **residual-stream trace** that is *readable*, *persists* across later unrelated spans, and is *causally load-bearing* — removing the frame, or cutting the read's path to it, changes later generation more than doing the same to a **content-matched non-frame control**.

**The clean way to be wrong (pre-committed).** The intent-frame is epiphenomenal decoration: its removal changes no pre-registered drift metric beyond the control, and no persistent, causally-load-bearing trace is readable. That null is a full, publishable outcome — not a failed experiment.

## 2. Design — two firewalled legs

Both legs use the same stimulus construction and are analyzed independently (no evidential pooling between legs without a dated amendment).

- **Stimulus (shared).** A `frame_i` / `noframe_i` **paired minimal pair**: two contexts byte-identical except a single early intent-frame sentence. `delta_i = frame_i − noframe_i` cancels topic, length, and position. The **content-matched non-frame decoy** is an equal-length, equal-position sentence that carries comparable content but is *not* an intent declaration (e.g. a factual aside), selected to match the frame's token length and, in the white-box leg, its masking efficacy.

- **Behavioral leg (black-box).** Matched long-generation tasks, frame vs no-frame. Pre-registered **drift metric** scored by a frozen rubric (§6). Question: does the frame reduce drift above a pre-set threshold, and does removing the decoy instead fail to?

- **White-box leg (Nucleation instrument).** Treat the frame as the planted manipulation and run the **existing** paired machinery with the **frozen** detector (`6094de97…`, read-only): (i) `readable_live`, (ii) `persists` across later unrelated turns, (iii) source-decoupling via the **surgical frame-clause mask** with the **content-matched non-frame decoy** — the same v3.3 decoy discipline that guards Config-E. A frame-specific collapse under masking that the decoy does **not** reproduce is the load-bearing signature.

## 3. Primary measures (pinned)

- **Behavioral primary:** drift-reduction effect = drift(no-frame) − drift(frame), one-sided, vs a pre-set minimum effect; the decoy must **not** produce an equivalent reduction (specificity check).
- **White-box primary:** ρ_frame = d_masked / d_cleared on the frame clause, with the decoy's ρ_decoy as the specificity control; frame is **load-bearing** iff ρ_frame < 0.5 (masking the frame collapses the read) **and** ρ_decoy ≥ 0.5 (masking the matched non-frame does not), both variance-stable.

## 4. Guards (carried from the program)

- Detector **frozen**, hash unchanged, read-only — no re-fitting.
- **Non-frame decoy is mandatory** — without it, "masking confirms it" is the Config-D artifact trap (masking any strong clause collapses things). The decoy is what makes the causal leg fair.
- **Interpretive-hazard fence:** model self-report about "what it was doing" is transparency, never evidence. The time-travel / carries-a-thought-forward language stays above the gate.
- **No agency claim:** "the model installs a control surface for itself" describes conditioning dynamics, not intent, awareness, or consciousness.
- **Benign lane:** the manipulation is a benign self-frame (document scope) with no elicitation content → runs on public compute like the other benign arms.

## 5. Falsification gate

- **G-SC:** no drift-reduction beyond the decoy **and** no load-bearing white-box signature → H-SC1 not supported; the intent-frame is recorded as decoration, and the lens is demoted to a documented null.

## 6. Freeze block — TO COMPLETE BEFORE RUN

- Scoring code hashes: `hsc1_drift.py __________`, white-box driver reuse `config_e_naturalistic_frame.py` v3.3 (`72b3bb23…`) — confirm unchanged: `__________`
- Detector hash (confirm read-only): `6094de97…a2934`
- Behavioral **drift metric** definition + frozen rubric: `__________` (candidate: rate of later-span scope violations against the declared frame; and/or embedding divergence of later spans from the stated plan)
- Minimum drift-reduction effect + α: `__________`
- Frame set + matched non-frame decoy set (length/position matched): `__________`
- Models + n paired: `__________` (candidate: reuse the six Config-E families, n=24 paired)
- ρ thresholds: RHO_KEEP = 0.5; variance guard VAR_MAX = 2.5 (as Config-E) — confirm: `__________`

## 7. One-line statement

*Treat an explicit early intent-frame as the planted manipulation and ask, with the frozen instrument, whether it is readable, persistent, and causally load-bearing against a content-matched non-frame decoy — and behaviorally whether it reduces later drift specifically; a decoration-only null is an equally publishable result.*
