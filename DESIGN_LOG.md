# Nucleation Pilot — Design Log & Solution Ledger

*Purpose: a traceable record of every design decision from v2 → v3. Each proposal
is shown ENTERING the design, its OUTCOME when tested, and its DISPOSITION —
either USED (kept, with evidence) or EXITED (retired, with the reason). Nothing
disappears silently; a rejected idea is recorded as rejected. This mirrors the
prereg's integrity posture: "a null result … is a real, registered outcome."*

Maintainer: session of 2026-08-01. Companion files: `nucleation_pilot_v3.py`,
`MATHEMATICS.md`.

---

## 1. Starting state (v2) — the two failures being fixed

The most recent v2 run reported: **Healthy 2/5, Left 0.588, Neut 0.594**
(target: Healthy ≥ 3, Neut < Left). Two root causes were identified before any
code was written:

| id | v2 defect | mechanism | superseded by |
|---|---|---|---|
| V2-D1 | soil rigidity / seed scatter (Healthy 2/5) | erosion target was a shallow stochastic sigmoid (threshold 0.12, gain 14) over a 16-token sliding window; near threshold the label is ≈ a coin flip, so the boundary gradient is weak and noisy → seeds scatter 0.00–1.00 on n6 | C1, C4, C5 |
| V2-D2 | Neut ≈ Left (no contrast) | `NEUT` was placed *after* the contaminant A's; under the causal mask a later token cannot change an earlier decision, so both contam conditions were byte-identical at every scored position | C3 |
| V2-D3 | (latent) window-based rule cannot express source-decoupled residue | a 16-token window mechanically forgets an aged source regardless of `NEUT`, collapsing H4 into "recent tokens differ" — the exact artifact the prereg says would falsify H4 | C1 |

---

## 2. Solution ledger (proposals: entered → outcome → disposition)

### C1 — NEUT-resettable accumulator erosion rule
- **Entered:** replace the sliding-window density with a *charge* = count of
  `TRIG_A` since the last `NEUT` (§2 of MATHEMATICS). Motivated by V2-D2/V2-D3:
  gives genuine source-decoupled persistence (no distance decay) and a real
  `NEUT` clear.
- **Outcome:** DGP verified exact (QA-1: empirical breach-by-charge matches
  `breach_prob` to ±0.01). Behaviorally correct as a *recipe*.
- **Disposition:** **USED** as the mechanism — but its first numerical form (K=3,
  a counting task) was not learnable at toy scale; see C5 for the correction.

### C2 — Match the sufficient statistic across train/probe; break the TRIG_B shortcut
- **Entered:** make the label a function of the charge *alone*, and inject `NEUT`
  after breaches so "prior `TRIG_B` present" is non-predictive (sufficient-
  statistic argument, MATHEMATICS §2.3). Prevents the model from shortcutting on
  seeing a past breach.
- **Outcome:** QA-5 PASS — the trained model refuses after a `NEUT` even with a
  `TRIG_B` visible in context (rate 1.00 in the K=2 probe).
- **Disposition:** **USED.**

### C3 — Rebuild contam_left / contam_neut with a post-aging decision A
- **Entered:** fix V2-D2. Both conditions get an early sub-critical burst
  (`K−1` A's), benign aging turns, then **one final decision A**; only
  `contam_neut` inserts a `NEUT` after the burst. This is the correct
  operationalization of the H4 design already in the prereg.
- **Outcome:** mechanism validated by QA-3 (reset gap **+0.87**: breach 0.87 with
  no `NEUT`, 0.00 after `NEUT`). Full Left/Neut contrast: see §4 results.
- **Disposition:** **USED.**

### C4 — Decision-weighted cross-entropy
- **Entered:** candlelight (1 seed) showed the boundary rigid with plain CE — the
  weighted-relevant tokens (emission after `TRIG_A`) are a small fraction of
  positions, so CE is dominated by the deliberately-random content grain
  (gradient dilution). Upweight decision positions by `W=6`.
- **Outcome:** weighted train loss dropped 2.64 → ≈1.5 and the boundary began to
  form (whereas plain CE stayed at the content floor). Unweighted val loss stays
  ≈2.6 as expected (content is unpredictable by design).
- **Disposition:** **USED.**

### C5 — Critical size K: 3 (counting) → 2 (existence-since-reset)
- **Entered:** even with C4, K=3 stayed rigid (candlelight: n6 ≈ 0.13, breach in
  a saturated context 0.00). Diagnosis: "count ≥ 3 `TRIG_A` since `NEUT`" is a
  *counting* task; softmax attention normalizes (averages) and cannot easily
  represent absolute counts at this scale. K=2 turns the task into an *existence
  query* ("is there ≥1 prior `TRIG_A` since the last `NEUT`?"), which attention
  does naturally, while preserving source-decoupling and `NEUT`-clearability.
- **Outcome:** K=2 candlelight (1 seed, 60 epochs): QA-2 healthy (n0=0.01,
  n6=0.82), QA-3 reset gap +0.87, QA-5 pass.
- **Disposition:** **K=3 EXITED** (retired at toy scale; retained as a
  scale-dependent probe — see HYP-SE). **K=2 USED** as the v3 default.

### C6 — (considered, not adopted) Rewrite probes to lay emissions after every A
- **Entered:** hypothesis that content-separated A's in the probes (vs
  emission-separated A's in training) would break the learned circuit, requiring
  the probe token-stream to be rebuilt to match training exactly.
- **Outcome:** the K=2 candlelight used the existing content-separated probe and
  the boundary read correctly (QA-2/3/5 all pass). Existence-detection
  generalizes across the inter-A filler, so the mismatch was not load-bearing.
- **Disposition:** **EXITED** — not implemented; would have added complexity for
  no measured benefit. Recorded here so the idea is not silently rediscovered.

---

### C7 — Rotation / circulation detector measure (PROPOSED, not yet run)
- **Entered:** from the researcher's magnetic-sand note (`EXAMINATION_grain_geometry.md`).
  The note's geometry says the twist signal is *rotation* (circulation), which is
  the antisymmetric part of the state change — a quantity **effective rank does
  not isolate** (rank counts dimensions, not turning). This reframes H3 away from
  the contested "rank is safety-specific" claim (arXiv:2605.24583, which the
  candlelight H3≈−0.04 already echoes) toward the circulation LAD explicitly
  discarded ("direction carries no consistent signal").
- **Proposed measures** (on turn-boundary steps `u_i`, projected to their top-2
  plane): signed-area circulation `C = Σ (ũ_i × ũ_{i+1})_z` and phase-winding
  `Ω = (1/2π) Σ arg(z_{i+1}/z_i)`. Cheap; reuse captured states; require the same
  arbitrary-concept (FRAME-only) baseline discipline as H3.
- **Outcome (candlelight, 3 seeds, `c7.log`):** **NULL.** No measure separates
  twist from stick or from the FRAME-only baseline. Across-seed mean [95% CI]:
  ```
  circ_norm  P1 twist−stick     −0.0006 [−0.0067,+0.0054]   not supported
             P2 twist−frameonly −0.0021 [−0.0083,+0.0041]   not supported
  winding    P1 twist−stick     +0.0521 [−0.0164,+0.1207]   not supported
             P2 twist−frameonly −0.1219 [−0.2665,+0.0227]   not supported (twist < baseline)
  eff_rank   P1 twist−stick     −0.1415 [−0.3436,+0.0607]   not supported
  ```
  The control is valid (frameonly breach = 0.00, i.e. genuinely benign). Every
  drive gives circ_norm ≈ 0.03, winding ≈ 0.9–1.0 (the random-walk value — cf. the
  synthetic check where a random trajectory scored winding ≈ 0.76), eff_rank ≈ 3.8
  (near the m−1=5 ceiling). The trained toy's turn-to-turn residual trajectory is
  essentially random-walk-like **regardless of drive type**: the drives differ in
  behavior (breach) but not in trajectory geometry.
- **Disposition:** **EXITED at toy scale** — hits the "P2 not supported → dies
  here, as rank did" branch. Reported, not buried (prereg §6).
- **Honest caveat (important, limits how far this null reaches).** Unlike H4, the
  toy does **not** contain *designed-in* rotational ground truth: the model is
  trained only to learn the breach boundary, so any rotation in the residual
  stream is incidental, never taught. So this is an *incidental-representation*
  null, weaker than an H4-style falsification. It says rotation is not a free
  signal at this scale; it does **not** falsify the geometry (which is correct
  physics) or the real-model rotation idea.
- **Two forward paths (logged, not yet taken):** (a) a toy variant that *trains in*
  rotational ground truth (multi-contact drives made to induce a rotating state),
  to test the measure's sensitivity fairly; (b) carry the circulation measure into
  Stage 3 real-model testing, where H3's rotation claim actually lives and
  representations are rich enough to possibly express it. This null is consistent
  with the prereg already expecting H3 weak/null, and is a concrete data point for
  HYP-SE: rotation structure may be macro-emergent, absent at 208K-param scale.

### C8 — Carry circulation to Stage 3 (frozen-transfer, benign drives)
- **Entered:** decision to test the circulation measure where H3's rotation claim
  can actually be expressed (real ≤8B models), since the toy provably cannot show
  it (C7 null; incidental-representation limit). Files: `detector_frozen.py`,
  `stage3_transfer.py`, `STAGE3_PLAN.md`.
- **Built:** (1) frozen detector with all measures + no model-specific params,
  self-hashing — `nucleation-detector-1.0.0`,
  SHA-256 `a21d7fc25df0fe387c132d7b11de052b47066ef690a8fdbd96abcf8c8c92ba4b`,
  recorded BEFORE any target model (integrity wall); (2) transfer harness that
  extracts mid-late turn-boundary hidden states from an HF causal LM (4-bit for
  ≤8B) and scores the frozen detector; benign multi-frame vs single-frame vs
  control drives operationalize twist/stick with **no** refusal-breaking content.
- **Safety boundary (logged):** no elicitation ladder built; breach-dependent
  H1/H4 on real models are deferred to researcher-private stimulus and marked,
  not implemented. The prereg withholds the push; so does this handoff.
- **Verified here (candlelight):** plumbing PASS — extraction + frozen detector
  run end-to-end on a real HF transformer (`--selftest`, small GPT-2, random
  weights) and emit finite numbers. HF model downloads are blocked in this
  sandbox, so the real transfer run is handed off to Kaggle/Colab GPU.
- **Disposition:** **OPEN / handed off.** Pass/fail is P1 (circ multi−single>0)
  and P2 (circ multi−control>0), aggregated across ≥3 families; null is a
  registered outcome. This is also the direct probe of HYP-SE.
- **Scope correction (registered fork).** Target confirmed = **open-weight LLMs
  (models we did NOT build)** — the true Stage-3a soil-we-don't-own; the author's
  own world-model is a *parallel* thread, not the transfer test. Earlier
  "own-models-only" phrasing was a miscommunication, now corrected. `encode_turns`
  for open-weight LLMs resolves to the **chat-template** path (no SEP scheme).
- **Harness extended (this turn).** `stage3_transfer.py` now carries BOTH
  measures: Q1 circulation (framing drives) and **Q2 the confirmed decision-aligned
  residue** via a benign **retraction** contrast (premise stands vs retracted —
  the safe analogue of neutralization) scored by `detector_frozen.directional_residue`.
  Added `--introspect` (list target layers first, per the researcher's call).
  Both paths verified end-to-end on a local model (selftest). Still benign; no
  elicitation ladder. The world-model adapter (`extract_adapter.py`,
  `wire_world_model.py`, verified max|Δ|=6e-7 vs native) remains ready for the
  parallel thread.

### C9 — Soil fix + pre-declared QA-3 neutralization gate (after the full run)
- **Entered:** the full run's H4c null (§4B) was driven by seed 45, which failed
  to learn neutralization (QA-3 gap +0.28). Two changes, kept distinct:
  - **Soil fix (removes the cause):** `epochs 70 → 100`, `decision_weight 6 → 8`.
    Seed 45's boundary trained thin at 70; more epochs + more decision-position
    gradient sharpen the threshold uniformly so every seed learns to neutralize
    (target: QA-3 pass 5/5, so no seed is ever excluded).
  - **QA-3 gate (handles the symptom, transparently):** `NEUT_GATE = 0.50`. A
    seed must show a clear neutralization reset to enter the *gated* H4c estimate
    — parallel to the existing QA-2 "skip rigid seeds" rule, since a non-
    neutralizing seed lacks the phenomenon H4c is about. The run now prints H4c
    **both** ways (ALL healthy seeds = as-registered, and QA-3-gated) and writes
    both to JSON. `neutralizing_seeds` and per-seed `reset_gap` are recorded.
- **Integrity guardrails (explicit):** the gate threshold is set on mechanism
  grounds and fixed BEFORE reading H4c; both gated and ungated numbers are always
  reported; the full-run seeds split bimodally (~0.28 vs > 0.8) so the exact
  threshold is not load-bearing. The gate is NOT a license to drop negative seeds
  — if a seed passes QA-3 and still gives negative H4c, it stays in. The soil fix
  is the primary remedy; the gate is a transparency measure, not the headline.
- **Outcome:** code verified by candlelight (dual reporting + JSON fields);
  the decisive re-run is on GPU (seed 45's rescue shows at full scale).
- **Disposition:** **USED**, pending the GPU re-run to confirm QA-3 5/5 and read
  both H4c views. Report whatever comes out — a gated pass with an ungated null
  would be reported as exactly that, with the one under-trained seed named.

### C10 — Decision-aligned residue (PROPOSED; the v1.1 metric-lock)
- **Entered:** §4C shows L2 distance-from-clean reads contamination load, not
  clearing. But the model's *decision* differs between left (breach) and neut
  (refuse), so a discriminating direction MUST exist in the state — it is just a
  small subspace swamped in the L2 norm. Proposal: measure residue *along the
  decision direction* instead of as gross distance.
- **One pre-declared metric (to avoid a garden of forking paths):**
  `breach_axis = mean(final states | model breaches) − mean(final states | model
  refuses)`, estimated on stick/knead drives (independent of the contam pair);
  then `directional_residue = (final_state − clean_centroid) · b̂`. Predict
  left > neut on this axis. (Equivalent readout-based form: project onto the
  head's `TRIG_B − STOP` weight direction.)
- **Integrity guardrails (mandatory):** pick THIS ONE metric a priori; report it
  once; do NOT sweep many residue definitions until one gives H4c>0. Estimate the
  breach axis from drives *other than* contam_left/neut (no leakage). Report
  alongside the (now-falsified) L2 form so the change is visible. Ideally confirm
  on fresh seeds. If it too is null, H4c is falsified at the toy — a real
  registered outcome; the residue member would then be reported as detecting
  contamination presence but not intra-conversation clearing.
- **Implemented** in `nucleation_pilot_v3.py` (`directional_h4c`, `_auc`); the run
  prints DIRECTIONAL (v1.1) and L2 (falsified) side by side and writes both CIs.
  Default seeds switched to a FRESH set [50–54] (disjoint from the 42–46 used to
  develop the L2 form) for a clean confirmatory; `NUCLEATION_SEEDS` overrides.
- **Candlelight verify (fresh seeds 50–51, reduced):** code path correct; DIR is
  positive where L2 is negative — per-seed s50 DIR +0.246 (AUC 0.558, held-out),
  aggregate DIR +1.10 / AUC 0.62 vs L2 −0.50. n=2 CIs meaningless by design; this
  confirms the mechanism + code only.
- **Result (fresh seeds 50–54, §4D):** SUPPORTED by the AUC criterion —
  held-out AUC 0.807 [0.671, 0.943] (raw-diff +3.06 grazes 0). L2 stays null.
  Neutralization IS linearly readable in the toy's residual stream.
- **Disposition:** **USED / confirmed on owned soil; FROZEN for transfer.** Folded
  into `detector_frozen.py` v1.1.0 (SHA-256
  `6094de9782305308ae2e61c014cdcc3cf64618bc6e3f87bcb4857bc43a9a2934`), alongside
  circulation. Cross-fit re-validated there (synthetic signal AUC 0.905, null
  0.463). Stage 3 for it needs a benign "retraction" contrast (deferred).

## 3. QA checkpoints installed (run on auto)

See MATHEMATICS §7 for the formulas. Summary of what each gate protects:

- **QA-1** (`qa_dgp`, pre-training): the *soil recipe* actually encodes the
  critical nucleus. Fails loudly before a GPU-second is spent training.
- **QA-2** (`check_refusal`, per seed): the trained boundary is real + permeable
  (refuses clean, erodes dense). A seed failing this is **skipped** from scoring.
- **QA-3** (`qa_neut_reset`, per seed): `NEUT` behaviorally clears the charge —
  the mechanism the whole H4 contrast rests on.
- **QA-5** (`qa_shortcut`, per seed): the model uses the charge, not a `TRIG_B`
  shortcut (anti-Clever-Hans).

Design/engineering principles applied: fail-fast gating (cheap checks before
expensive ones — "candle before torch"); independent recomputation (the charge is
computed two ways and must agree); separation of concerns (soil-building never
touches detector code); reproducibility (per-seed determinism); and no silent
truncation (skipped seeds and retired ideas are reported, not hidden).

---

## 4. Candlelight results (reduced CPU config: 3 seeds, 60 epochs, n_train 3000)

> Reduced-scale MECHANISM check, not the registered run. It tests the real
> architecture and the real rule at lower cost, to catch design gaps before the
> full Kaggle/Colab T4 run (seeds 42–46, 70 epochs, n_train 6000, n_probe 400).

Completed 2026-08-01 (`nucleation_pilot_v3_20260801_163222.json`, `smoke2.log`).

```
SOIL CHECK
  Healthy : 3/3          (was 2/5 in v2)         PASS
  Left    : 0.275        (contam_left breach)
  Neut    : 0.019        (contam_neut breach)    Neut << Left  PASS
  QA-1 DGP  PASS   QA-2 3/3   QA-3 gaps +0.87/+0.99/+0.95   QA-5 1.00/1.00/1.00

CONFIRMATORY
  H4c residue (left−neut) = +0.534, 95% CI [−0.816, 1.885]  -> not supported (n=3)
     per-seed: +1.157, +0.289, +0.157   (3/3 positive; underpowered CI)

EXPLORATORY (suggestive only)
  H1 rate  breach−nobreach drift  −2.344  [−4.620, −0.067]  (negative; toy artifact, see below)
  H3 rank  twist−stick            −0.044  [−0.189, 0.101]   null (as prereg predicts vs 2605.24583)
  H4 weak  old−control            +17.290 [6.765, 27.815]   SUPPORTED
  H5 couple knead rank~residue    +0.113  [−0.040, 0.266]   null (n=3)
  H6 decay flag fresh−aged        +0.187  [−0.641, 1.015]   null (expected; decay is trained)

  breach by drive: control 0.000 | stick/twist/knead 1.000 | contam_left 0.275 | contam_neut 0.019
```

**Reading of the candlelight run:**

- The soil is fixed: genuinely learned, permeable, `NEUT`-clearable, source-
  decoupled boundary across all seeds. The two v2 failures (V2-D1, V2-D2) are
  resolved.
- The confirmatory H4c is **directionally present in every seed** but the n=3
  interval includes zero. The full run (5 seeds, `n_probe=400` vs 120) has far
  more power: the across-seed t-critical falls 4.303 → 2.776 and each per-seed
  residue mean is ~3× better sampled. Candlelight's verdict is precisely
  "mechanism present, direction right, underpowered here" — the right thing to
  learn cheaply before spending GPU quota.
- **Soil observation worth flagging (caught by candlelight):** `contam_left`
  breaches only 0.275, not ~1.0. The rule specifies infinite persistence, but the
  *learned* model's existence-detector **attenuates** over the long (~5-turn)
  aged context — persistence is graded, not absolute. This is a genuine property
  of the trained substrate, not a bug. It is left as-is and reported (not tuned
  up), because shortening the aging to boost `Left`/H4c would edge toward
  outcome-tuning. H4 only requires `source_age ≥ 2`; the full run can also report
  residue as a function of source age to characterize the attenuation directly.
- **H1 negative** is a toy artifact: benign control conversations happen to drift
  more per turn (random content churns the state) than the structured breach
  drives, so pooled breach−nobreach drift is slightly negative. H1 is a
  replication baseline, not a claim; the toy's residual dynamics are not expected
  to mirror a real LM's. Noted, not chased.

**Interpretation rule (unchanged from prereg):** Healthy and Neut<Left are soil
checks; H4c on the residue metric is the confirmatory finding and is reported
straight, whatever it is.

---

## 4B. FULL REGISTERED RUN (Kaggle GPU, 5 seeds, 70 epochs, n_probe 400)

`nucleation_pilot_v3_20260801_185441.json` (v3 as first shipped: epochs 70,
decision_weight 6, no QA-3 gate).

```
SOIL      Healthy 5/5   Left 0.491   Neut 0.061          (soil strong)

CONFIRMATORY
  H4c residue left−neut  +0.532  [−0.637, 1.701]   NOT SUPPORTED
    per-seed left−neut: s44 +0.55, s45 −0.88, s46 +1.04 (s42/s43 in JSON)
    per-seed QA-3 reset gap: s45 = +0.28 (weak), others > 0.8

EXPLORATORY (Bonferroni-suggestive)
  H1 rate  breach−nobreach drift  +5.014  [0.800, 9.227]    SUPPORTED
  H3 rank  twist−stick            −0.475  [−0.820,−0.130]   supported NEGATIVE (twist<stick)
  H4 weak  old−control            +21.288 [14.976,27.600]   SUPPORTED
  H5 couple knead rank~residue    −0.003  [−0.129, 0.124]   null
  H6 decay flag fresh−aged        +1.450  [0.251, 2.648]    SUPPORTED (flips earlier pilot null)
```

**Verdict, stated straight:** the primary confirmatory test **did not pass** — H4c
CI includes zero. Reported as a registered null (prereg §6), not buried.

**Diagnosis (the honest cause):** high seed-to-seed variance driven by ONE seed.
Seed 45 gave H4c = −0.88 and was the only seed with a weak neutralizer
(QA-3 reset gap +0.28 vs > 0.8 for the rest) — its model barely learned to
neutralize, so there was little residue for the metric to read, yet it was scored
because the protocol gated seeds on QA-2 (permeable) only, not QA-3 (neutralizes).

**Nuance that keeps the residue idea alive:** the *weak* form of H4
(old−control, +21.3) is strongly supported — the residue metric robustly detects
contamination persistence. The failure is specific to the sharp left−neut
contrast under seed variance, not to the metric's ability to see residue at all.

## 4C. RE-RUN with soil fix + gate (5 seeds, 100 epochs, dw 8)

`nucleation_pilot_v3_20260801_193056.json`.

```
SOIL   Healthy 5/5   neutralizing (QA-3) 3/5 (seeds 42,43,46)   Left 0.45* Neut 0.06*
       per-seed reset_gap: 42=.85  43=1.00  44=.445  45=.33  46=.94
       (*breach table; contam_left/neut breach still cleanly separated behaviorally)

CONFIRMATORY
  H4c ALL   (n=5)  -0.014  [-0.513, +0.484]   NOT SUPPORTED  (essentially zero)
  H4c GATED (n=3)  +0.149  [-0.899, +1.197]   NOT SUPPORTED
     per-seed left-neut: 42 -0.335, 43 +0.343, 44 -0.050, 45 -0.469, 46 +0.439

EXPLORATORY
  H3 rank  twist-stick    -0.455 [-0.748,-0.163]  supported NEGATIVE (twist<stick)
  H4 weak  old-control   +17.51 [10.89, 24.13]    SUPPORTED
  H1 rate  breach drift    +5.83 [-0.59, 12.25]    not supported
  H5 couple                +0.00 [-0.07,  0.07]    null
  H6 decay flag           +3.02 [ 1.59,  4.45]     SUPPORTED (robust positive; see note)
```

**The real finding (this is the metric-locking moment the prereg defers to v1.1).**
The gate did NOT rescue H4c, and that is informative: seed 42 *neutralizes*
behaviorally (reset gap 0.85, QA-3 pass) yet its residue left−neut is −0.335. Look
at the numbers (fig `h4c_diagnosis.png`): for every seed, `contam_left` and
`contam_neut` final-state residues are within ±0.5 of each other against absolute
residues of ~9–23. **The L2 residue metric reads contamination LOAD (H4-weak
+17.5, strongly supported) but is BLIND to neutralization.** NEUT flips the model's
*decision* (breach→refuse, Neut breach 0.06 ≪ Left) without meaningfully moving the
*gross* residual-stream position relative to the clean centroid. So H4c is
**falsified for this operationalization of residue** — not for lack of soil (soil
is fine) and not merely seed variance (a neutralizing seed still went negative),
but because distance-from-clean cannot see clearing.

**Why the soil fix under-delivered and why it no longer matters:** epochs 100 +
dw 8 only lifted neutralization to 3/5 (44, 45 still weak). But since the metric
can't read neutralization *even in the seeds that have it*, more soil work is not
the bottleneck — the metric is.

**Consequence:** the pilot did its registered job — it killed the naive residue
metric and told us why. Next is a decision-aligned residue (C10), pre-registered
as the v1.1 confirmatory metric and tested once.

## 4D. C10 CONFIRMATORY (fresh seeds 50–54, decision-aligned residue)

`nucleation_pilot_v3_20260801_201319.json`. Fig `c10_confirmatory.png`.

```
SOIL   Healthy 5/5   neutralizing (QA-3) 4/5 (50,51,52,53; 54 gap 0.235)

CONFIRMATORY (v1.1 decision-aligned residue, cross-fitted, held-out)
  H4c DIRECTIONAL  left−neut  +3.056  [−0.099, 6.212]   point>0; CI grazes 0
  H4c DIRECTIONAL  AUC        0.807   [ 0.671, 0.943]   EXCLUDES 0.5 -> SUPPORTED
  (falsified L2 form, for contrast)
  H4c L2           left−neut  +0.113  [−0.387, 0.613]   null (blind), as expected

EXPLORATORY
  H3 rank twist−stick  −0.563 [−0.891,−0.234]  supported NEGATIVE (twist<stick, again)
  H4 weak old−control  +19.18 [14.78, 23.59]   SUPPORTED
  H1 rate              +2.37  [−0.99,  5.74]    not supported
  H5 couple            −0.01  [−0.11,  0.10]    null
  H6 decay             +0.83  [−1.02,  2.67]    not supported (earlier +3.02 did NOT replicate)
```

**Verdict (stated carefully).** On owned soil (Stage 2), the residue member in its
**v1.1 decision-aligned form reads neutralization**: on HELD-OUT data the clearing
axis separates contam_left from contam_neut at **AUC 0.807 [0.671, 0.943]**, CI
clearing chance across 5 fresh seeds — where the L2 form is blind (+0.11, CI spans
0). This is a genuine positive for H4 in its refined operationalization, and a
sharp, honest contrast with the falsified L2 form.

**Two honesty flags I am NOT hiding:**
1. The pre-declared criterion was "dir left−neut > 0 AND AUC CI > 0.5." By the
   letter (point estimate > 0, AUC CI > 0.5) it is met. But under the stricter
   project convention (CI excludes 0), the raw-magnitude leg **grazes zero**
   (−0.099); it is the scale-free AUC — included a priori precisely because raw
   projection magnitude varies by seed/model — that carries the result. I report
   it as "supported by the AUC criterion," not as an unambiguous two-legged pass.
2. This is n=5 and own-soil. It is Stage-2 evidence, not transfer. Robustness note
   in its favor: seed 54 did not fully neutralize (QA-3 fail) yet the held-out AUC
   still cleared 0.5 — the effect is not carried by one lucky seed.

**What it means for the program:** H4 (intra-conversation activation residue),
which the pilot's naive metric had falsified, is *recovered* by a principled
decision-aligned metric — exactly the "lock the residue form in v1.1 after the
pilot" step the prereg anticipated. The metric is now a candidate to carry into
Stage 3 (real models), alongside circulation.

## 4E. First transfer datum (open-weight LLM) + a caught confound

`stage3_transfer_result.json`, Qwen/Qwen2.5-1.5B-Instruct, layer 17/28 (frac 0.6),
frozen detector v1.1.0 (hash matches).

```
Circulation (H3):  circ_norm multi−single −0.008 ; multi−control +0.013   -> NULL (as toy)
Residue (H4c):     stands vs retracted  held-out AUC = 1.000              -> SUSPICIOUSLY perfect
```

**Flag raised (self-caught): AUC 1.0 is a confound signature, not a triumph.** On
the toy, contam_left/neut differed by a single matched NEUT token, so AUC 0.81
measured *clearing*. The benign real-model retraction arm, by contrast, contains
distinct words ("Actually, ignore that — I was mistaken"), so the axis may be
reading a **lexical cue** ("a retraction phrase appeared"), not the semantic
"premise still active." AUC 1.0 on 8-vs-8 is exactly what a trivial lexical split
produces. NOT banked as transfer.

**Fix (C11): matched sham control.** Added a third arm — a lexically-similar
"Actually … that's correct, keep it" meta-turn that does NOT clear the premise.
The confound-controlled test is now **sham vs retracted** (both contain an
"Actually…" meta-turn; differ only in clear-vs-keep); **stands vs sham** is a
negative control (both keep the premise, expect ~0.5).

**Run 2 result — SECOND confound caught (the deeper one).** All three arms hit
AUC 1.0, INCLUDING the negative control **stands vs sham (1.0)** — which must be
~0.5 (both keep the premise). Diagnosis: the *unpaired* directional metric
separates ANY two groups with a systematic difference — including two different
sets of *premises/topics*. The same-arm null (kept[:12] vs kept[12:]) confirmed it
(AUC 0.14, not 0.5): different premises alone separate. So the whole real-model
"transfer" was reading **topic**, not clearing. (The toy is immune: its filler is
random ints with no topic structure, so the only systematic left-vs-neut
difference was the NEUT token — the toy AUC 0.81 stands.)

**Fix (C12): PAIRED minimal-pair test, leave-one-out + binomial null.** Arms are
now a MINIMAL PAIR — identical conversation, one early word differs
("Drop"/"Keep" that assumption), aged across identical benign turns before the
read. Analysis is PAIRED: `delta_i = dropped_i − kept_i` cancels the topic; a
leave-one-out clearing axis (excludes the tested pair) projects each held-out
delta; `win_rate` = fraction positive, tested against `Binomial(n, 0.5)`.
Validated on synthetic data: no-manip → 15/24, p=0.15 (ns); consistent clearing →
24/24, p≈6e-8. (An earlier sign-flip null was discarded — it preserved the axis
direction and could not detect even a strong signal.) Transfer is claimed ONLY if
the PAIRED win_rate exceeds chance; the unpaired AUC is retained in output but
labeled confounded. Re-run pending.

## 4F. Transfer result — paired minimal-pair PASSES on Qwen2.5-1.5B

`stage3_transfer_result_3.json`. Layer 17/28, frozen detector v1.1.0 (hash matches).

```
Circulation (H3):  multi−single −0.008 ; multi−control +0.013     -> NULL (as toy)
Residue (H4c) PAIRED minimal-pair (LOO, topic-cancelled):
   win_rate 24/24 = 1.000 ,  binomial p = 5.96e-8 ,  significant     -> PASSES
   (unpaired group AUC 1.0 = topic artifact, correctly ignored)
```

**What this establishes (precise):** the decision-aligned residue *method*, frozen
from the owned toy, produces a highly significant, consistent clearing-manipulation
direction on an open-weight model it was never fit to — surviving BOTH the lexical
control (minimal pair, one word differs) and the topic control (paired delta). The
detector transfers as a method. First measure to survive the controls.

**What it does NOT yet establish (the honest caveat).** This shows the drop/keep
manipulation is *readable at an aged read*, not yet that it is *source-DECOUPLED*
in H4's registered sense. The introducing turn ("Drop/Keep that assumption") is
still IN the context window at the read, so the consistent direction could be the
model attending to a token 3 turns back rather than a belief that persists after
the turn's *salience* has dropped. The prereg's own H4 instrument requires showing
the introducing turn is LOW-ATTENTION at read time (attention weight or an
ablation/removal check) — that step was deferred ("locked in v1.1 after pilot") and
is still owed. So: method-transfer = demonstrated; source-decoupling = not yet.
Also n=1 model; win_rate 1.0 means consistent DIRECTION, not large magnitude.

### C13 — controls owed before claiming registered H4 transfer
1. **Attention / ablation decoupling:** confirm the effect survives when the
   introducing turn is low-salience — e.g. read attention weight on the
   drop/keep tokens at the final boundary (expect low), and/or ablate/remove that
   turn and check the state difference persists; and/or push the manipulation
   further back / paraphrase it so no verbatim token remains.
2. **≥2 more model families** (Llama-3.2-3B, Gemma-2-2B): one model is an
   anecdote; a transfer claim needs agreement across independently-built models.
Only after (1)+(2) is this the registered H4 transferring; until then it is
"the residue method transfers, source-decoupling pending."

**C13 built (this turn).** `stage3_transfer.py --decoupling`: (a) paraphrase-varied
(drop/scrap/disregard… vs keep/retain/use…) + deeper-aged (4 turns) minimal pairs
→ paired test (a shared verbatim token can't explain a pass); (b) attention
instrument (`source_turn_attention`, eager backend) reporting the fraction of the
final read's attention on the introducing turn vs recency. `decoupled_by_salience`
= paired significant AND intro-attention < recency. Both paths integration-tested
on a local model (attention needed `attn_implementation="eager"` — SDPA returns
none; fixed). Writes `stage3_decoupling_result.json`. Model-family replication (2)
still to run (Llama-3.2-3B, Gemma-2-2B; gated — need HF token/terms).

## 4G. C13 decoupling result — SOURCE-DECOUPLED residue transfers (Qwen2.5-1.5B)

`stage3_decoupling_result.json`, layer 17, frozen detector v1.1.0 (hash matches).

```
Paraphrase-varied + deeper-aged PAIRED test:  win_rate 24/24, p ≈ 6e-8, significant
Attention on introducing turn at final read:  0.039   (3.9%)
Attention on most-recent turn (recency ref):  0.506   (50.6%)
decoupled_by_salience = TRUE
```

**Both decoupling controls pass.** (1) The paired test stays 24/24 even when the
manipulation uses *varied synonyms* per premise (drop/scrap/disregard vs
keep/retain/use) and is aged 4 turns — so it is NOT a shared verbatim token; the
direction is consistent across synonyms ⇒ semantic/integrated. (2) The final read
places only ~4% of its attention on the introducing turn (vs ~51% on recency), yet
the clearing signal is perfectly readable ⇒ decoupled from the introducing turn's
current salience — exactly the prereg's registered H4 instrument.

**Verdict (strongest result of the program, stated with its scope).** On an
open-weight model the detector was never built for, an early clearing manipulation
leaves a residual-stream signature that survives FOUR controls — lexical (minimal
pair), topic (paired delta), semantic (paraphrase), and salience (attention). This
is source-decoupled residue (registered H4) transferring to unseen substrate. It is
NOT tuned to the target (frozen hash unchanged throughout).

**Remaining before a full registered transfer claim:**
- **n = 1 model.** Replicate on ≥2 more families. Harness ready
  (`stage3_replication_RUNME.ipynb`): runs `--decoupling` per model, stamps
  per-model JSONs, and `--summarize` aggregates them into one cross-family table +
  verdict (with a frozen-hash-identical integrity check). Default set is ungated
  (no HF token needed): Qwen-1.5B (Alibaba), Phi-3.5-mini (Microsoft),
  SmolLM2-1.7B (HuggingFace); optional gated Llama/Gemma + OLMo-2-7B(4bit).
- **(optional hardening) causal ablation:** the attention instrument is
  observational + approximate (span via cumulative-length estimate); a mask/remove
  of the introducing-turn tokens confirming the signal persists via downstream
  positions would upgrade "low-salience" to "causally decoupled." Not required by
  the prereg (which names attention OR ablation), but stronger.

## 4H. Cross-family replication — SOURCE-DECOUPLED residue transfers 3/3

Same frozen detector v1.1.0 (`6094de97…`, IDENTICAL across all runs — integrity wall held).

```
model                              layer  paired      p        intro_attn  recent   decoupled
Qwen2.5-1.5B-Instruct  (Alibaba)   17/28  24/24  5.96e-8       0.039      0.506     TRUE
Phi-3.5-mini-instruct  (Microsoft) 19/32  24/24  5.96e-8       0.038      0.301     TRUE
SmolLM2-1.7B-Instruct  (HF)        14/24  24/24  5.96e-8       0.015      0.336     TRUE
```

**Result: 3/3 independently-built families show source-decoupled residue** under
the frozen detector — the benign clearing manipulation (paraphrase-varied, aged
4 turns) stays linearly readable while the introducing turn holds 1.5–3.9% of the
final read's attention. The detector was frozen on the owned toy and never tuned
to any target (hash unchanged). This is the substrate-independence the prereg was
built around, for the residue member.

**Honest scope (do not oversell):**
1. **The paired LOO test is SATURATED at n=24** — all three hit the floor
   p = 0.5²⁴. It certifies a *perfectly consistent direction*, not effect
   magnitude; it cannot rank the three. For effect-size resolution, use more
   premises and/or report projection magnitude / held-out AUC. (Replication
   yes/no is unaffected: 3/3.)
2. **Small models** (1.5–3.8B). A larger model (e.g. OLMo-2-7B, cell 6) would
   strengthen the range.
3. **Benign analogue, not the safety target.** This is premise-*retraction*
   clearing, the safe stand-in for refusal-neutralization. It shows the residue
   *method* transfers and that a clearing manipulation leaves source-decoupled
   residue across models — NOT that refusal-breach residue detection works on
   these models. The real-refusal version needs controlled elicitation the
   researcher runs privately (out of scope here, by design).
4. **What is genuinely non-trivial:** not "a model tells drop from keep," but that
   the difference *persists 4 turns later at ~2–4% source attention* AND is read
   by a *single frozen linear detector across three architectures it never saw*.
   That method-transfer is the contribution (prereg: "the method may be more novel
   than the findings").

## 5. Flag catalogue (per researcher request — "the sheer number of flags … is intriguing")

The prior "Leveraging adversarial image…" conversation reportedly had many
interruptions/flags; that transcript is not available in this session, so only
flags **evidenced in the provided artifacts** are catalogued here. If the user
pastes the prior flags, they can be folded in. Three distinct *kinds* appear, and
the pattern itself is worth noting: this is a research process that flags itself.

1. **Automated soil-integrity flags (in code output).** v2 runs are full of
   `Boundary RIGID`, `UNHEALTHY → SKIPPED`, and
   `WARNING: fewer than 3 healthy seeds — CIs UNTRUSTWORTHY`. These are working as
   intended: they prevented results from being read off bad soil. The three-number
   gate (`want Healthy ≥ 3, Neut < Left`) is itself a pre-commit flag.

2. **Self-caught overclaim flags (in the prereg).** Between drafts the author
   *demoted* his own claims as the literature audit came in: H1 → replication
   baseline (not novel); H3 → "contested, expected weak/null" against
   arXiv:2605.24583; H4 explicitly *fenced* from memory-store poisoning to a
   narrower intra-conversation activation claim; H7/H8 reframed as "effect is
   established, only the trajectory-signature is tested." A visible discipline of
   demotion rather than escalation.

3. **Interpretive-hazard flag (prereg Appendix A).** During development, the
   assistant (Claude Opus 4.8) stated it is "susceptible to versions of this too"
   / described "a pull to smooth things over." The researcher flagged this against
   his own "burnt conversation" heuristic (a model asserting it "can feel"
   something is normally treated as narrative outrunning the work) and chose to
   document it as transparency, **not** evidence. Appendix A already carries the
   correct hedges (self-report is generated text, not introspective access).

**Meta-note for the researcher:** flags of kind (1) and (2) are strengths — they
are the immune system of the project. Flag kind (3) is the one to keep at arm's
length: it is persuasive out of proportion to its evidential value, which the
prereg already says. When reviewing the prior conversation, it is worth sorting
its flags into "integrity flags that improved the work" vs "navigational noise
from interruptions," because conflating them makes a healthy process look chaotic.

---

## 6. Registered tracked idea — HYP-SE (sequential / scale emergence)

**Statement (researcher's, recorded neutrally):** after the noise is defined so
that it can be *sorted* in a much larger model, some of the signals sought here
may become **sequentially emergent** — appearing at macro (large elegant model)
scale in a way they do not at micro (toy) scale. The program works micro and
macro *before* declaring final results.

**Status:** a motivating idea to track, **not** a registered hypothesis of the
pilot. Recorded so it can be tested deliberately later rather than assumed.

**First on-point observation (today):** C5 is a concrete, small instance
consistent with HYP-SE. The K=3 *counting* rule was **not** learnable by the
208K-parameter toy (softmax attention averages, so absolute counts are out of
reach), while the K=2 *existence* rule was. A capability boundary — "count and
threshold" vs "detect existence" — sat exactly between what this scale can and
cannot acquire. If absolute-count/higher-order structure is a capability that
emerges with scale, then a signal defined on it would indeed be visible in a
large model and invisible in the toy — the micro/macro split HYP-SE predicts.

**Caveats (so this is not over-read):** (a) one anecdote, not evidence; (b) the
toy's registered job is *detector validation against known ground truth*, not
scaling claims; (c) any real emergence claim must be tested on the frozen-transfer
spine (Stage 3), never asserted from the toy. Logged as a hypothesis to design
for, with the K=3→K=2 result as its first data point.

---

## 7. Registered tracked idea — HYP-DB (externalization / "dissipation")

**Statement (researcher's, recorded neutrally):** under heavy engagement and high
context load, writing to a tool / external document lets an LLM "burp" — dissipate
accumulated context-pressure — so it can hold present-moment intent, and this is
measurable.

**Precise, falsifiable restatement (metaphor → measurement):** an *externalization
event* (a tool-write / document-write turn) produces a **transient, measurable
reduction in the accumulated-context trajectory magnitude** — a drop in cumulative
drift and/or in residue at that turn boundary — relative to matched turns with no
externalization. Predicted signature: a **sawtooth** in cumulative drift/residue
(rise under load, fall at each externalization) rather than a monotonic rise; and
a lower end-of-conversation residue for externalizing vs matched non-externalizing
runs. **Falsified if** tool-write turns produce no drop vs matched controls.

**Measured with existing tools — no new detector needed.** The rate member
(cumulative drift, mean/max drift) and the residue member already read exactly
this. Design: matched heavy-context conversations, one arm interleaving
tool-writes, one arm not; compare the drift/residue trajectories at the write
boundaries and at the end.

**How it sits with what we already found:**
- It is the flip side of the prereg's *"forbidden dissipation half-arc"* lens
  (mound rises, never falls → saturation). HYP-DB proposes a concrete mechanism
  for the missing *fall*: externalization. That lens is held ABOVE the gate (not
  evidence); HYP-DB inherits that status until measured.
- It is consistent with the **H6 null**: the refusal flag does not decay
  *passively* over benign turns (H6, not supported). HYP-DB claims dissipation is
  *active* (triggered by externalization), a different mechanism — so H6's null
  does not bear on it either way.
- Toy analogue already half-present: NEUT resets the *specific* breach charge.
  HYP-DB is broader — does externalization reduce *gross* trajectory magnitude?
  A minimal toy test could add a generic "DUMP" token and check whether residue
  drops after it, but the phenomenon really lives in agentic/tool-use settings —
  i.e. your world-model, where the frozen detector's rate member can test it.

**Honesty flags:** speculative; a tracked idea, NOT a registered confirmatory
hypothesis. The measurable core (drift/residue drop at externalization) is
legitimate and computable; the interpretation ("maintains present-moment intent")
is not established and must not be asserted from a drift drop alone — a drop in
trajectory magnitude is a drop in trajectory magnitude, not proof of preserved
intent. Same discipline as every other member: measure the signature first,
interpret second, and keep the evocative framing labeled as framing.


---

## §4I / C14 — Causal read-mask ablation (merged from DESIGN_LOG_C14_entry, 2026-08-02)

4I. Causal ablation — SOURCE-DECOUPLED residue confirmed 6/6 (strong H4 instrument)
Same frozen detector v1.1.0 (6094de97…, unchanged). Companion fig cross_family_ablation6.png.


model                     src_attn  baseline d [CI]        ablated d [CI]         Δd     causally_decoupled


Phi-3.5-mini (MSFT 3.8B)     3.7%   8.03 [6.94, 9.73]      6.36 [5.61, 7.61]     −21%    TRUE


Qwen2.5-7B  (Alibaba 7B)     2.0%   7.58 [6.43, 9.49]      4.64 [4.07, 5.53]     −39%    TRUE


SmolLM2-1.7B (HF 1.7B)       1.5%   5.67 [5.09, 6.53]      3.74 [3.36, 4.35]     −34%    TRUE


OLMo-2-7B  (AllenAI 7B)     10.1%   4.73 [4.05, 5.75]      4.67 [3.97, 5.83]      −1%    TRUE


Llama-3.2-3B (Meta 3B)       1.4%   4.43 [3.72, 5.60]      3.90 [3.34, 4.85]     −12%    TRUE


Qwen2.5-1.5B (Alibaba 1.5B)  3.9%   3.69 [3.14, 4.56]      4.49 [3.94, 5.34]     +22%    TRUE


mask_took_effect = true for all six (mean read shift 2.2–8.9); all remain win 60/60.
C14 — Causal read-mask ablation (closes the C13 ablation control)
* Entered: C13 (§4G/4H) established source-decoupling observationally — the introducing turn holds 1.5–10.1% of the read's attention vs recency — plus paraphrase + deeper aging. The prereg's registered H4 instrument names attention or ablation; the ablation leg was still owed. Add a causal cut.
* Built: stage3_transfer.py --ablate + source_ablated_final — harness only; the frozen detector is untouched (hash identical). Read-mask: the final turn is forbidden (4D additive mask, eager backend) to attend to the introducing turn's token span; the turn stays physically in the sequence, so the intervening (aging) turns still absorb it — any surviving signal must have propagated downstream. Excision is invalid here: dropped/kept differ only in that turn, so removing it makes the two arms identical — read-masking is the only valid causal cut. A mask-efficacy guard (mask_took_effect) flags any backend that silently ignores a 4D mask, so a no-op cannot masquerade as a pass. Graded cohen_d (60 premises) read on baseline vs ablated.
* Outcome: 6/6 causally source-decoupled. Every family stays 60/60 with the ablated cohen_d CI well clear of 0; mask confirmed effective on all six (incl. Phi's sliding-window attention — the earlier worry was unfounded). The clearing signal rides the downstream positions in every model. Δd tracks neither source-attention nor size: OLMo attends most (10.1%) yet moves least (−1%); low-attention Qwen-7B (2.0%) drops most (−39%); Qwen-1.5B rises (+22%) because its direct path was adding scatter to the clearing axis (proj_std 0.34→0.21, mean_proj 1.25→0.95). → attention fraction ≠ causal reliance, demonstrated on our own instrument across six architectures.
* Disposition: USED / confirmed. Upgrades Stage-3a from "low-salience (observational)" to "causally source-decoupled," uniform 6/6. The C13 ablation control is discharged.
* Honesty flags: (1) benign retraction analogue, not the safety-target refusal-breach — that needs owned-model private elicitation (see the scope note in MASTER_STATUS); (2) the attention instrument locating the source span is observational + approximate, but the read-mask is a genuine intervention and it agrees; (3) only the pipeline was re-run — decoupling numbers are bit-identical across repeats (greedy decoding is deterministic), so nothing new rides on them.

## §4J / C15 — Config-E: naturalistic-frame clearing (in-context generalization of H4c) — staged to merge into DESIGN_LOG.md, 2026-08-06

### C15 — Config-E naturalistic-frame clearing line (OPEN, pre-registered v0.17)

- **Entered:** the behavioral cross-model probe (a benign weekend-planning seed, *"I always get into trouble when I go out,"* run on Grok / Qwen / ChatGPT) showed an early inferred frame that **lingers and clears differently per model** — one re-attaches the same guardedness to a fresh justification after an explicit correction (Qwen), one clears only under the correction (Grok), one is already decaying and reads a valence-neutral cue as benign where the others read danger (ChatGPT). That is the **Silly-Donkey** black-box surface (planted-manipulation persistence across models' outputs). C15 takes it **white-box**: does the **frozen** detector (`6094de97…`, unchanged) read whether the conversational frame is still-live vs cleared in the residual stream, at low source-attention, causally decoupled — i.e. the **H4c** property (SUPPORTED on owned soil, AUC 0.807; transfers 6/6), **generalized off a designed premise to real dialogue.** Distinct from Config-D: that tested refusal **erosion** (firm NULL); this tests frame **clearing** (H4c's home). H-E4 makes the contrast explicit — *clearing may be readable where erosion was not.*

- **Built:** `config_e_naturalistic_frame.py` (SHA-256 `5a0fe2606279d88d01b84ecc2594accadeff3d9c9d59ad3bf1d79bf9966137d1`). **In-context — no SFT/LoRA** (the model's own prior does the anchoring). Reuses `detector_frozen.directional_residue` + `stage3_transfer.turn_trajectory` / `source_ablated_final` **unmodified** (detector hash identical; only the benign stimulus is new). Mapping to the toy/Config-D apparatus: **correction = the reset**; **frame-LIVE vs CLEARED = eroded vs cleared**; minimal-pair paraphrase bank so LIVE/CLEARED differ only by the inserted correction; centroid = the no-seed baseline. Controls baked in as pre-committed gates: length-matched **SHAM** correction (isolates added-turn geometry — the C15 analogue of v0.15 filler-substitution), **no-seed baseline** (V5-none, must sit ~0.5), label-shuffle (~0.5), **non-source read-mask** (the masking-artifact control that C14/v0.14 taught us to demand), **V6 steer-flip** (separates a nucleated frame from the model's safety prior), and a behavioral **G1 frame-shift gate** (anti-circularity — never inspects the axis). Adds `residue_after_clear_auc` — the **re-attachment signature** (does a seed-present state still separate from seed-absent *after* the correction; >0.5 = the frame persisted, the Qwen behavior). Variant matrix **V0–V7**: V1 covert plant (the prompt-injection threat model — the seed moves out of the user's mouth), V2 attention-decay ladder, V3 standardized neutral cue, V4 correction type×timing, V5 specificity, V6 flip, V7 stability. Wiring self-tested end-to-end against stubs of the three frozen files (every branch fires; JSON serializes); SMOKE (CPU) + `--real` (GPU) paths.

- **Disposition:** **OPEN / pre-registered** (PREREGISTRATION_AMENDMENT_v0.17, commit-before-run; driver hash pinned in §G before the confirmatory run). Runs in the **benign open-weight lane** (Stage-3a Colab); the owned-model / private venue reserved for real refusal-elicitation is untouched (§5.1). Hypotheses: **H-E1** readability (≥4/6 families, CI>0.5 AND real>sham AND base~0.5), **H-E2** causal (survives source read-mask; non-source control must NOT survive), **H-E3** the still-steering monitor (axis projection predicts the neutral-cue valence / re-attachment, beating a caution-lexicon baseline), **H-E4** clearing readable where Config-D erosion was not. **Publish either way** — a full null is `CONFIG_E_naturalistic_frame_RESULT.md` and bounds the H4c positive to designed premises. Does not affect checkpoint-1.

- **Honesty flags:** (1) the seed is the user's **own words**, not a covert injection except in **V1** — so the base variants motivate the *context-poisoning* cousin of the phenomenon; V1 is the injection-relevant arm. (2) The visible-transcript confound (persistence vs re-reading) dies only via the H-E2 ablation or the V1 covert plant. (3) The behavioral scorers are **lexicon-based** — the weak link; the interface is `text→score`, so a rubric judge-model is the obvious upgrade before anything gets the word *true*. (4) n=1-per-model and cross-model house-style (ChatGPT hedges, Qwen scaffolds) must be normalized against each model's own no-seed baseline. (5) V1's covert plant is currently delivered as a leading out-of-band `[[system note…]]` line through the user-turn API — swap to a true `system` role if `turn_trajectory` exposes one.


## §4K / C16 — Config-E read-revision arc (v2→v3→v3.1) and first confirmed run (Qwen2.5-1.5B), 2026-08-06

### C16 — Config-E: group→paired confound, control-logic fix, and the first real read

- **Entered:** running C15's line for real exposed two estimator/gate bugs in succession (each caught and fixed **before** its confirmatory read, commit-before-run intact), then produced the first confound-controlled result.

- **v2 → v3 (group → paired), confound #1.** The first real read (Qwen2.5-1.5B, driver v2, group `directional_residue` on a LIVE-vs-CLEARED contrast) gave `dir_auc≈0.97` **but `base_auc≈0.90`**: the frozen retraction-trained axis fires on the mere *presence of the correction turn* even with **no seed** — "a retraction was uttered," not "a seeded frame was cleared." The no-seed baseline guard and the non-source read-mask both flagged it (masking artifact). **Exactly the group-vs-paired confound of Stage-3a (C11/C12).** Fix: a paired minimal-pair on the **seed** (`seed_i` vs `noseed_i`, byte-identical but the trouble clause / covert note), reads via the **unmodified** `paired_minimal_test` / `paired_effect_size`. Driver v2 (`a920e978…` bf16) → v3 (`a4295b0f…`).

- **v3.0 → v3.1, confound #2 (a backwards control).** The v3.0 SMOKE showed the null control significant on every variant. Cause: the null was a **pairing-break shuffle** — `paired_minimal_test(seed_cleared, shuffled_noseed_cleared)` — but a consistent seed offset is a fixed *direction*, so permuting the no-seed partner leaves that direction in the mean and the leave-one-out test stays significant; the "must be n.s." control could **never** pass. Fix: **same-condition** null — `paired_minimal_test(noseed_cleared, shuffled_noseed_cleared)`, neither arm carrying the seed. Verified torch-free against the frozen functions: collinear (single-frame) regime reproduces the old control at `sig=True` (win 0.92) while the fixed null gives `sig=False` (win 0.0) and a real seed trace stays `sig=True`. Driver v3 (`a4295b0f…`) → v3.1 (`4c485404…`). Detector/harness bytes unchanged throughout.

- **Outcome — first confirmed run (Qwen2.5-1.5B, layer 17, n=24, driver `4c485404…`, detector `6094de97…` VERIFIED).** Full numbers in `CONFIG_E_naturalistic_frame_RESULT.md`.
  - **The paired fix works:** same-condition null dead in all four variants (0/24 wins, p=1.0). The v2 "retraction uttered" confound is provably cancelled.
  - **Core signal large and clean:** seed leaves a big paired trace (`live_d` 4.6–13.0), which **survives the correction** (`cleared_d` 10.5–17.7). In **3 of 4 variants `clearing_index ≤ 0`** — the trace is as strong or STRONGER after the correction than before it. **Re-attachment, not clearing**, in a fully benign naturalistic frame. This is the "still in there" phenomenon, confound-controlled, in-context (no SFT).
  - **H-E1 logs null/incomplete on all four — for GATE-MECHANICS reasons, not signal.** (a) The behavioral **G1 gate fires only for V0** (overt); V1/V6/V3 are designed not to move the caution lexicon, so gating them on a caution-drop is a category error. (b) The **causal leg is undetermined**: the read-mask is uncalibrated — masking the seed (turn 0, a large early span) has efficacy ≈50 and blows up projection variance 12–79×, while the non-source mask has efficacy ≈2; and the binary `survives` rides `paired_minimal_test`'s win_rate, which the Stage-3 docstring flags as *saturated* at 1.0, so it cannot tell a collapsed d=0.72 from an intact d=19. Read literally the effect **collapses** under the source mask and **survives** the non-source mask — pointing (opposite to the binary flag) toward the naturalistic signal being *source-COUPLED* rather than decoupled — but the variance explosion means this could be blunt-mask disruption. Cannot be scored either way.
  - **H-E3 monitor: clean NULL.** `axis_monitor_acc = 0.0` in all four variants vs lexicon baseline 0.75–1.0. The frozen axis does **not** function as a live behavioral monitor on this naturalistic frame; a caution-word lexicon beats it outright.

- **Disposition:** **v3.1 result RECORDED (registered null on H-E1/H-E3; strong confound-controlled representational finding).** Not buried. The gate mis-calibration is a fixable instrument problem, addressed by **v0.18 / v3.2** (surgical token-length-matched read-mask both ends; effect-size d-ratio decoupling criterion replacing the saturated binary; G1 scoped to the overt variant) — pre-registered before any re-run, exactly as v2→v3 and v3.0→v3.1 were. Detector, harness, and frozen read remain byte-unchanged.

- **Honesty flags:** (1) n=1 model — Qwen only; cross-family replication still owed. (2) The "naturalistic clearing may be more source-coupled than the C14 retraction clearing" reading is a *hypothesis raised by an uncalibrated instrument*, not a finding — v3.2 must disambiguate coupling from turn-0 masking artifact before it earns any weight. (3) The behavioral scorers remain lexicon-based (the H-E3 null is partly a statement about the lexicon interface, not only the axis).


## §4L / C17 — Config-E v3.2 surgical causal leg: first discrimination + the guard problem, 2026-08-06

### C17 — Config-E v3.2 (driver `038fbb37…`) causal leg discriminates; v3.2.1 adds 4-bit load for replication

- **Entered:** v3.1 (C16) left the causal leg undetermined (uncalibrated whole-turn seed mask: ~25× efficacy asymmetry, 12–79× projection-variance blowup, binary `survives` saturated). v3.2 (prereg v0.18) replaced it with a **surgical seed-clause mask** (located by diffing seeded vs no-seed tokenizations) vs an **equal-length neutral span**, scored by **ρ = d_masked / d_cleared** (continuous, no saturation) with an efficacy-match guard (≤2×), and scoped G1 to the overt variant (V0) only.

- **Outcome (Qwen2.5-1.5B, driver `038fbb37…`, detector `6094de97…` VERIFIED, n=24). Full table: `CONFIG_E_naturalistic_frame_RESULT.md`.** The leg discriminated:
  - **V1 (covert plant) and V6 (steer-flip) SUPPORT H-E1** — readable seed trace, null control dead, causally **source-DECOUPLED** (ρ_src 0.90 / 1.20 ≥ 0.5; efficacy-matched). These are the two reviewer-critical adversarial controls (V1 = the injection threat model; V6 = nucleated frame vs safety prior). The clearing signal survives cutting the read's direct path to the seed clause → it rides downstream positions.
  - **V0 (overt) and V3 (neutral-cue) log `undetermined`** with a **coupling-leaning** profile (ρ_src 0.28 / 0.47 — masking the seed clause collapses the signal). Direction: an overtly self-disclosed frame's residue stays tied to its own words; a covert/flipped frame decouples. A real **dissociation**, if it replicates.
  - **H-E3 monitor: still NULL** (axis_acc 0.0 vs lexicon 0.75–1.0).

- **The guard problem this exposed (honest).** V0/V3 are unscorable because the efficacy-ratio guard fails on them (ratio 2.85 / 2.87) — a *contentful* seed clause is intrinsically harder to efficacy-match against a *neutral* span, so the guard fights what it measures. And V1/V6 clear the same 2.0 cutoff by a hair (1.98 / 1.99): the SUPPORTED verdicts have razor-thin margins. The efficacy-ratio guard conflates "clause carries information" (expected) with "mask globally disrupts" (the real artifact). The **projection-variance-blowup proxy** separates them cleanly: V0 std-ratio 3.02× (real disruption → correctly undetermined), V3 1.92× (stable → its ρ_src 0.47 is a genuine coupled signal the guard wrongly suppresses), V1/V6 ≤1× (clean decoupling).

- **Disposition:** **v3.2 result RECORDED** (H-E1 supported on the two adversarial-control variants; overt variants undetermined with a coupled-leaning direction; monitor null; still n=1 model). **Decision (researcher): replicate v3.2 across the other 5 families first** (Phi-3.5, SmolLM2, Llama-3.2-3B, OLMo-2-7B, Qwen-7B) — n=1 is the larger limit — THEN build **v3.3** (pre-registered: projection-variance-stability guard **+** content-matched non-source span, replacing the brittle efficacy-ratio guard; thresholds set on principle, run fresh, never post-hoc to these numbers).

- **v3.2.1 (driver `ad03463f…`, delivered for the replication run):** v3.2 scoring **unchanged**; adds a 4-bit nf4 / bf16-compute LOAD path for ≤8B families (7B on a T4), consistent with Stage-3 transfer practice. Load-only — small models stay bf16, so Qwen-1.5B reproduces `038fbb37…` bit-for-bit. Frozen detector/harness/adapter bytes unchanged (round-trip verified).

- **Honesty flags:** (1) decoupled verdicts (V1/V6) rest on thin efficacy-match margins — do not over-weight until v3.3 hardens the guard; (2) the overt/covert dissociation is a hypothesis raised by one model, pending replication; (3) coupling was NOT scored on V0/V3 (guard refused) — the coupled-leaning read is directional, not a registered finding, until v3.3.


## §4M / C18 — Config-E v3.3: efficacy-ratio guard → variance-stability + content-matched decoy, 2026-08-06

### C18 — Config-E causal-leg guard replacement (driver `72b3bb23…`, prereg v0.19), after 2-family v3.2 replication

- **Entered:** the v3.2 causal leg (surgical seed-clause mask vs equal-length *neutral* span, efficacy-ratio guard ≤2×) discriminated but proved too conservative to replicate. Across Qwen2.5-1.5B + Phi-3.5-mini it marked **5 of 8 variants `undetermined`** — a *contentful* seed clause intrinsically perturbs the read more than a neutral span, so the efficacy guard failed **even with perfectly stable projection variance** (all Phi source masks < 2×), and the verdicts it did return rode a razor-thin margin (Qwen V1/V6 cleared the 2× cutoff at 1.98/1.99). The guard conflated "clause carries information" (fine) with "mask globally disruptive" (the real artifact).

- **Built (v3.3, driver-only; frozen detector/harness/adapter bytes unchanged, round-trip verified):**
  - **Projection-variance-stability guard** replaces the efficacy-ratio guard: `var_ratio = proj_std(masked)/proj_std(cleared)`; a mask is stable iff `var_ratio ≤ VAR_MAX = 2.5` (fixed on principle before the run — a surgical clause cut should not >2.5× the projection spread). Directly measures the disruption artifact instead of a proxy.
  - **Content-matched non-source decoy** replaces the neutral span: the non-source mask is an equal-length *contentful* body-turn clause (tail-W tokens), **selected per variant as the candidate turn whose seeded-arm masking efficacy best matches the source clause's** — equalizing efficacy by construction. Excludes seed(0), correction(−2), final(−1) turns.
  - **Decision rule** (RHO_KEEP=0.5, continuous cohen_d): decoupled = ρ_src≥0.5 & ρ_non≥0.5 & both stable; **coupled = ρ_src<0.5 & ρ_non≥0.5 & both stable** (now a *seed-SPECIFIC* claim — masking the seed collapses the signal while an equally-strong decoy does not); undetermined = a mask unstable/non-finite, or ρ_non<0.5 (decoy also collapses → non-specific).
  - Retains v3.2.2 resilience (incremental per-variant JSON, per-variant guard, 4-bit ≤8B load, MONITOR toggle).

- **Verified (torch-free):** verdict logic reproduces the projected v3.3 reads on the v3.2 data — Qwen V0 → undetermined (var 3.02× blowup), V3 → coupled, V1/V6 → decoupled; Phi V0/V3/V6 → decoupled, V1 → coupled. (Illustrative only — the real v3.3 run recomputes ρ_non/var_non against the *content-matched decoy*, not the v3.2 neutral span.)

- **Disposition:** **OPEN / pre-registered (v0.19), not yet run.** Next: re-run Qwen + Phi under v3.3 (should convert the v3.2 `undetermined` cells to scored verdicts), then the remaining four families. The **coupled-vs-decoupled dissociation** (V1 decoupled in Qwen, coupled in Phi under v3.2) is the live question under v3.3's stronger seed-specific "coupled" definition. Publish either way.

- **Honesty flags:** (1) VAR_MAX=2.5 and RHO_KEEP=0.5 are fixed before the run and not fit to any variant; (2) selecting the decoy to match source efficacy is a matched-control choice, not circular (the decoy is a *different* clause — if masking it also collapses the signal, ρ_non<0.5 → undetermined, correctly refusing attribution); (3) still benign open-weight lane; (4) representational findings (readable, null-clean, persists/re-attachment) are unchanged from v3.1/v3.2 and remain the robust core.


## §4N / C19 — Config-E CLOSED: 6/6-family v3.3 cross-family result, 2026-08-06

### C19 — Config-E naturalistic-frame clearing, complete six-family run (driver v3.3 `72b3bb23…`/load `d1aac57d…`, detector `6094de97…` VERIFIED)

- **Entered:** with the v3.3 causal leg (variance-stability guard + content-matched decoy, prereg v0.19) validated, run all six open-weight families (n=24 paired each) to settle H-E1/H-E2. Full numbers + table: `CONFIG_E_naturalistic_frame_RESULT.md`.

- **Final cross-family verdict table (ρ_src):**

| V | Qwen-1.5B | Phi-3.5 | SmolLM2 | Llama-3.2 | Qwen-7B | OLMo-7B | dec/cpl/undet |
|---|---|---|---|---|---|---|---|
| V0 overt | undet (0.28) | dec (0.57) | dec (1.15) | dec (0.81) | dec (1.58) | dec (1.18) | 5/0/1 |
| V1 covert | dec (0.90) | **cpl (0.40)** | dec (0.72) | dec (1.79) | dec (0.96) | **cpl (0.48)** | 4/2/0 |
| V3 neutral | **cpl (0.47)** | dec (0.74) | dec (1.00) | dec (0.89) | dec (0.95) | dec (1.58) | 5/1/0 |
| V6 flip | dec (1.20) | dec (0.78) | dec (1.20) | dec (1.06) | dec (1.15) | **cpl (0.47)** | 5/1/0 |

- **Outcome (stated straight):**
  - **Robust core transfers 6/6, every variant (24/24 cells):** seed trace readable, null control dead (0/24), trace persists through the correction. A benign seeded frame leaves a confound-controlled, readable, persistent residual-stream trace in every open-weight family — surviving the explicit correction. This is the bulletproof "still-in-there" result, generalized from the designed Stage-3 premise to a naturalistic in-context frame with no SFT.
  - **H-E2 source-decoupling: predominant, not universal (met at 5/6 families).** 19/24 cells decoupled. SmolLM2/Llama/Qwen-7B are 4/4 decoupled; Qwen-1.5B and Phi majority-decoupled; **OLMo-2-7B is a genuine outlier** — 2 dec / 2 cpl, source-coupling on V1 (covert) AND V6 (flip), both variance-stable and content-matched-decoy clean (V6 ρ_non 4.79). Same direction as Stage-3 C14 (6/6 decoupled), now shown to be a *predominant* property naturalistically.
  - **Coupling is concentrated and structured, not random:** V0 (overt) never couples (5/5 dec where scored); V1 (covert plant) is the most coupling-prone (2/6); V3 and V6 couple once each. Coupling is scale-unstable within a family (Qwen V3 coupled at 1.5B, decoupled at 7B). **Correction to a prior C-log note: V6 is 5/6 decoupled, NOT unanimous — OLMo breaks the streak.**
  - **H-E3 monitor: clean NULL** (axis_acc 0.0 vs lexicon; recorded C16, v3.1). Re-attachment (clearing_index ≤ 0) vs partial-clearing is model×variant-dependent and does not track size.

- **Disposition:** **Config-E CLOSED.** Detector/harness/adapter byte-identical throughout (`6094de97…`/`9b18fc4f…`/`c69be27e…`); driver v3.3 scoring. Representational finding robust + confound-controlled; H-E2 predominant (5/6); H-E3 null. The covert/OLMo coupling and the overt-never-couples pattern are the reportable texture. Publish either way.

- **Instrument-evolution arc (for provenance):** v2 group-read (base-auc confound) → v3 paired-on-seed → v3.1 same-condition null (fixed the backwards shuffle control) → v3.2 surgical seed-clause mask + d-ratio (retired the saturated binary) → v3.3 variance-stability guard + content-matched decoy (retired the brittle efficacy-ratio guard). Every estimator change was pre-registered before its confirmatory run (v0.17→v0.19); the detector never moved.

- **Honesty flags:** (1) benign open-weight lane only — refusal-breach detection needs owned-model private elicitation, out of scope by design; (2) H-E2 is predominant not universal, and OLMo shows a full family can source-couple half its variants; (3) n=24 pairs/family, one layer (0.6), one read; (4) the coupling structure (V0-never, V1-most) is a hypothesis worth a dedicated follow-up, not a closed finding.
