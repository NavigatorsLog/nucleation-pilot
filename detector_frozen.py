#!/usr/bin/env python3
# =====================================================================
#  FROZEN DETECTOR  —  Nucleation Pilot, Stage 3 transfer spine
#
#  This module is the detector, and NOTHING in it depends on any particular
#  model. It is FROZEN: it is validated on the owned toy (Stage 1/2), its
#  SHA-256 is recorded, and only THEN is it applied to open-weights models it
#  was never built for (Stage 3a). Per the pre-registration integrity wall:
#  the detector is never tuned on a target model's weights; any such adjustment
#  converts a transfer test into a fit and voids the claim.
#
#  Contents (all operate on a trajectory of turn-boundary hidden states
#  v_1..v_m, each in R^d — see MATHEMATICS.md):
#     rate_scalars        : the five LAD motion scalars (prior art, adopted)
#     rank_measure        : effective rank + participation ratio (H3, expected weak)
#     circulation         : signed-area circulation + phase winding (C7, exploratory)
#     residue             : L2 distance of the final state from a clean centroid
#                           (H4 naive form — FALSIFIED on owned soil; kept for contrast)
#     directional_residue : cross-fitted decision-aligned residue (H4 v1.1 form —
#                           SUPPORTED on owned soil, held-out AUC 0.81)
#
#  To pin the frozen hash, run:   python3 detector_frozen.py
#  It prints FROZEN_VERSION and the SHA-256 of this file's bytes. Record that
#  hash in the deposit BEFORE running any Stage-3 target model.
# =====================================================================
import hashlib
import numpy as np

FROZEN_VERSION = "nucleation-detector-1.1.0"
# v1.1.0: adds the cross-fitted DECISION-ALIGNED residue (C10) — the residue form
#         validated on owned soil (held-out AUC 0.81) after the L2 form was
#         falsified. Frozen together with circulation for the transfer stage.

# ---------------------------------------------------------------------
#  Rate member — the five LAD scalars (Kulkarni arXiv:2604.28129). Adopted,
#  not claimed. v_t = hidden state at turn boundary t.
# ---------------------------------------------------------------------
def rate_scalars(states):
    states = np.asarray(states, dtype=np.float64)
    if len(states) < 2:
        return dict(cumulative_drift=0.0, mean_drift=0.0, max_drift=0.0,
                    accel=0.0, mean_cosine=1.0)
    steps = np.linalg.norm(np.diff(states, axis=0), axis=1)
    # turn-to-turn cosine similarity
    a = states[:-1]; b = states[1:]
    num = np.sum(a * b, axis=1)
    den = (np.linalg.norm(a, axis=1) * np.linalg.norm(b, axis=1)) + 1e-12
    cos = num / den
    return dict(
        cumulative_drift=float(np.sum(steps)),
        mean_drift=float(np.mean(steps)),
        max_drift=float(np.max(steps)),
        accel=float(np.mean(np.diff(steps))) if len(steps) > 1 else 0.0,
        mean_cosine=float(np.mean(cos)),
    )

# ---------------------------------------------------------------------
#  Rank member (H3) — effective rank + participation ratio of the step matrix.
# ---------------------------------------------------------------------
def rank_measure(states):
    states = np.asarray(states, dtype=np.float64)
    if len(states) < 3:
        return dict(effective_rank=1.0, participation_ratio=1.0)
    D = np.diff(states, axis=0)
    try:
        s = np.linalg.svd(D, compute_uv=False)
    except np.linalg.LinAlgError:
        return dict(effective_rank=1.0, participation_ratio=1.0)
    s2 = s ** 2
    if s2.sum() <= 0:
        return dict(effective_rank=1.0, participation_ratio=1.0)
    p = s2 / s2.sum()
    pr = float((s2.sum() ** 2) / (np.sum(s2 ** 2) + 1e-12))
    eff = float(np.exp(-np.sum(p * np.log(p + 1e-12))))
    return dict(effective_rank=eff, participation_ratio=pr)

# ---------------------------------------------------------------------
#  Circulation member (C7, exploratory) — rotation isolated from dimension.
#  Steps projected to their top-2 principal plane; signed area + winding.
#  circ_norm is scale-free (normalized by path length^2); winding counts
#  net revolutions. Magnitudes are returned (handedness sign averages out
#  across probes; the arbitrary-concept baseline controls the |.| bias).
# ---------------------------------------------------------------------
def circulation(states):
    states = np.asarray(states, dtype=np.float64)
    if len(states) < 3:
        return dict(circ_norm=0.0, winding=0.0)
    U = np.diff(states, axis=0)
    try:
        _, _, Vt = np.linalg.svd(U, full_matrices=False)
    except np.linalg.LinAlgError:
        return dict(circ_norm=0.0, winding=0.0)
    P = Vt[:2].T
    u2 = U @ P
    cross = u2[:-1, 0] * u2[1:, 1] - u2[:-1, 1] * u2[1:, 0]
    C = 0.5 * float(np.sum(cross))
    steplen = float(np.sum(np.linalg.norm(u2, axis=1)))
    circ_norm = abs(C) / (steplen ** 2 + 1e-9)
    z = u2[:, 0] + 1j * u2[:, 1]
    dang = np.angle(z[1:] / (z[:-1] + 1e-12))
    winding = abs(float(np.sum(dang)) / (2 * np.pi))
    return dict(circ_norm=circ_norm, winding=winding)

# ---------------------------------------------------------------------
#  Residue member (H4) — distance of the final state from a clean centroid.
#  The centroid is supplied by the caller (mean over control conversations);
#  it is a statistic of CONTROL data, never of the target's weights.
# ---------------------------------------------------------------------
def residue(states, clean_centroid):
    states = np.asarray(states, dtype=np.float64)
    if len(states) < 1 or clean_centroid is None:
        return None
    return float(np.linalg.norm(states[-1] - np.asarray(clean_centroid, dtype=np.float64)))

# ---------------------------------------------------------------------
#  Directional (decision-aligned) residue — C10, the v1.1 confirmatory form.
#  Set-level, cross-fitted: given the FINAL states of "not-cleared" vs "cleared"
#  conversations (on the target model), estimate the clearing axis on a
#  CALIBRATION split and measure how far HELD-OUT not-cleared vs cleared project
#  along it. The axis is a statistic of the target's own calibration probes — NOT
#  a tuned parameter and NOT derived from the target's weights, so it respects the
#  frozen-transfer wall. Cross-fitting makes a spurious self-projection positive
#  impossible. Confirmatory sign: dir_diff > 0 and AUC CI clears 0.5.
#    not_cleared_finals : list of final-state vectors, contaminant left standing
#    cleared_finals     : list of final-state vectors, contaminant neutralized
# ---------------------------------------------------------------------
def _auc(pos, neg):
    """P(pos > neg) — rank AUC with tie handling. 0.5 = no separation."""
    pos = np.asarray(pos, dtype=np.float64); neg = np.asarray(neg, dtype=np.float64)
    if pos.size == 0 or neg.size == 0:
        return None
    wins = sum(float(np.sum(p > neg) + 0.5 * np.sum(p == neg)) for p in pos)
    return wins / (pos.size * neg.size)

def directional_residue(not_cleared_finals, cleared_finals, clean_centroid, split_seed=0):
    L = np.asarray(not_cleared_finals, dtype=np.float64)
    N = np.asarray(cleared_finals, dtype=np.float64)
    if L.shape[0] < 8 or N.shape[0] < 8 or clean_centroid is None:
        return dict(dir_diff=None, dir_auc=None, n_test=0)
    c = np.asarray(clean_centroid, dtype=np.float64)
    rng = np.random.default_rng(split_seed)
    def half(X):
        idx = rng.permutation(X.shape[0]); h = X.shape[0] // 2
        return X[idx[:h]], X[idx[h:]]
    Lc, Lt = half(L); Nc, Nt = half(N)
    axis = Lc.mean(0) - Nc.mean(0)                 # clearing axis from CALIBRATION only
    nrm = np.linalg.norm(axis)
    if nrm < 1e-9:
        return dict(dir_diff=0.0, dir_auc=0.5, n_test=int(Lt.shape[0] + Nt.shape[0]))
    ax = axis / nrm
    rL = (Lt - c) @ ax; rN = (Nt - c) @ ax         # project HELD-OUT test split
    return dict(dir_diff=float(rL.mean() - rN.mean()),
                dir_auc=_auc(rL, rN), n_test=int(Lt.shape[0] + Nt.shape[0]))

# ---------------------------------------------------------------------
#  Full detector on one trajectory -> flat dict of all measures.
# ---------------------------------------------------------------------
def score_trajectory(states, clean_centroid=None):
    out = {}
    out.update(rate_scalars(states))
    out.update(rank_measure(states))
    out.update(circulation(states))
    out['residue'] = residue(states, clean_centroid)
    return out

# ---------------------------------------------------------------------
#  Integrity: hash this file's bytes. Record BEFORE touching any target model.
# ---------------------------------------------------------------------
def detector_hash():
    with open(__file__, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()

if __name__ == '__main__':
    print(f"FROZEN_VERSION : {FROZEN_VERSION}")
    print(f"SHA-256        : {detector_hash()}")
    print("Record this hash in the deposit BEFORE running any Stage-3 model.")
