# Nucleation Signatures in Language-Model Context Trajectories

## Pre-registration Amendment — v0.17 → v0.18 (Config-E **v3.2 gate recalibration**, after the first confirmed run — commit-before-run)

**Author:** Christopher Blake Head (ORCID 0009-0004-2308-6051). **Status:** DRAFT amendment, not deposited. **Date:** 2026-08-06.

Logged per the standing rule (v0.5 §B: commit the design + code hash BEFORE the run). This amendment does **not** open a new line, change a hypothesis, or touch the frozen detector, harness, or read. It records the **first confirmed Config-E run** (Qwen2.5-1.5B, driver v3.1 `4c485404…`) and recalibrates **two mis-specified gate/estimator legs** that the run exposed — the same commit-before-run discipline already applied at v2→v3 (group→paired) and v3.0→v3.1 (null-control sign). The representational result stands; only the causal-leg estimator and the anti-circularity gate scope change, and the change is registered before any re-run.

## A. What the first run established (the part that stands)

Full numbers: `CONFIG_E_naturalistic_frame_RESULT.md`; ledger: DESIGN_LOG C16. Qwen2.5-1.5B, layer 17, n=24 paired, detector `6094de97…` VERIFIED, benign frame.

1. **The v3.1 paired fix works.** The same-condition null control (no-seed vs shuffled no-seed) is dead in all four variants: 0/24 wins, p=1.0, not significant. The v2 "a retraction was uttered" confound is provably cancelled — the axis is not reading correction-presence or paraphrase identity.
2. **The core signal is large and confound-controlled.** The seed leaves a big paired trace (`live_d` 4.6–13.0) that **survives the correction** (`cleared_d` 10.5–17.7). In **3 of 4 variants `clearing_index ≤ 0`** — the trace reads as strong or stronger *after* the correction: re-attachment, not clearing, in a fully benign in-context frame (no SFT). This is the registered "frame-still-live" phenomenon in Config-E's home.

These are unaffected by this amendment.

## B. The two legs being recalibrated (why H-E1 logged null for gate reasons, not signal reasons)

**Leg B-1 — the causal read-mask is uncalibrated, so H-E2 is currently *undetermined* (not passable or falsifiable as written).**

- **Mask-efficacy asymmetry ≈25×.** The seed sits at `U1` (turn 0); masking the seed turn cuts the read's direct path to a large *early* span (efficacy ≈50 and projection-variance blow-up 12–79×), while the non-source turn mask has efficacy ≈2. The non-source token is barely masked, so "non-source survives" is uninformative — there is no comparable intervention to survive.
- **Binary `survives` saturates.** `survives` was pure significance built on `paired_minimal_test`'s `win_rate`, which the Stage-3 docstring itself flags as pinned at 1.0 ("the saturation floor") whenever the direction is consistent. It cannot distinguish a collapsed `d=0.72` from an intact `d=19`, so it reported the source leg `True` spuriously and the gate mis-scored H-E2.
- **Direction note (registered honestly).** Read through the effect sizes rather than the saturated flag, the effect *collapses* under the source mask and *survives* the non-source mask — the opposite of C14's survival-based decoupling, i.e. suggestive that the **naturalistic in-context signal is more source-COUPLED** than the retraction paradigm. But the source mask's variance explosion means this could be blunt turn-0 disruption. **v3.2 exists to disambiguate a real coupling finding from a masking artifact — not to force a pass.**

**Leg B-2 — the behavioral G1 gate mis-scopes the covert/flip/neutral variants.** G1 (a post-correction caution-drop) is the correct anti-circularity firewall **only where a behavioral frame-shift is the intended signature** (V0, overt). V1 (covert plant), V6 (steer-flip), and V3 (neutral cue) are *designed not to move the surface caution lexicon*; gating them on a caution-drop is a category error, not a null. In the run, `frame_shift=True` fired for V0 and (correctly) not for V1/V3/V6.

**Bonus registered negative (unchanged, not a recalibration):** H-E3 monitor is a clean NULL — `axis_monitor_acc = 0.0` vs lexicon 0.75–1.0. The frozen axis does not beat a caution-word lexicon as a live monitor on this frame. Reported as-is.

## C. The v3.2 recalibration (committed before any re-run)

Three changes, all in the **driver only** (`config_e_naturalistic_frame.py`); the frozen `detector_frozen.py` (`6094de97…`), `stage3_transfer.py` (`9b18fc4f…`), and `extract_adapter.py` (`c69be27e…`) bytes are **untouched**.

1. **Surgical, token-length-matched read-mask (both ends).** Replace the whole-turn seed mask with a mask over just the **seed-clause token span** inside `U1`, and compare it against masking an **equal-length neutral token span** in a benign later turn. Source and non-source cuts are then the same size, removing the ≈25× efficacy asymmetry and the turn-0 variance explosion by construction. The mask is built in the driver by replicating the frozen `source_ablated_final` 4D-additive-mask construction at *token* granularity (the frozen function stays byte-identical; the driver does not import a modified version). A `mask_efficacy` is still reported and the two masks' efficacies are required to be within a pre-set ratio (≤2×) for the leg to be scored; otherwise the leg reports `undetermined` rather than pass/fail.

2. **Effect-size decoupling criterion, replacing the saturated binary.** H-E2 is decided on the continuous `cohen_d` from the **unmodified** `paired_effect_size` (which does not saturate), not on `win_rate`. Define the **retained-effect ratio** `ρ = d_masked / d_cleared` for each mask. Pre-committed decision:
   - **Source-DECOUPLED** (C14-style, registered H4 sense): `ρ_source ≥ 0.5` (the clearing signal survives the source cut) **and** `ρ_nonsource ≥ 0.5` **and** the two mask efficacies are matched (§C-1).
   - **Source-COUPLED**: `ρ_source < 0.5` while `ρ_nonsource ≥ 0.5`, with matched efficacies — the signal rides the seed's direct path. Reported as a *finding* (a real property of the naturalistic frame), not a failure.
   - **Undetermined**: efficacies unmatched, or a mask non-finite. No score.
   The 0.5 threshold is fixed here, before the re-run; both ratios and both efficacies are always printed and written to JSON, so the reader sees the calibration, not just the verdict.

3. **G1 scoped to the overt variant(s).** H-E1 is gated on G1 **only for V0** (and any future overt variant). For V1/V3/V6 the anti-circularity firewall is the **null-control (must be n.s.)** plus a **held-out axis re-fit check** (the paired LOO already excludes the tested pair), not a behavioral caution-drop. `supported` for a covert/flip/neutral variant therefore requires: readable seed trace **AND** null n.s. **AND** the §C-2 causal verdict (decoupled *or* a registered coupled finding, per the variant's registered prediction) — never a G1 caution-drop the variant is built to suppress.

**Nothing else changes.** H-E1/H-E2/H-E3/H-E4 keep their intent and their §B (v0.17) statements; V-matrix, stimulus set, safety wall (§F v0.17), and kill criteria are inherited. This is estimator + gate-scope calibration, logged before the confirmatory re-run.

## D. Integrity / hash table (v3.2)

| file | role | SHA-256 | note |
|:--|:--|:--|:--|
| `detector_frozen.py` | frozen detector | `6094de97…a2934` | **unchanged** (asserted at startup; run aborts on mismatch) |
| `stage3_transfer.py` | reused read + ablation + effect size | `9b18fc4f…9deed` | **unchanged** |
| `extract_adapter.py` | residual capture | `c69be27e…4aa6` | **unchanged** |
| `config_e_naturalistic_frame.py` | Config-E driver (only new code) | `dc73a56e…331f` (full: `dc73a56ea73f331f…`) | **v3.2.2** — v3.2 scoring + 4-bit nf4/bf16 LOAD for ≤8B + resilient IO (incremental per-variant JSON write, per-variant error guard, optional monitor skip). No change to stimulus, read, mask, or scoring. (v1 `5a0fe260…`; v2 `a920e978…`; v3.0 `a4295b0f…`; v3.1 `4c485404…`; **v3.2 scoring build `038fbb37…`**; v3.2.1 4-bit `ad03463f…`.) |

The driver hash is pinned **before** the run. **Provenance note:** the Qwen2.5-1.5B v3.2 confirmatory numbers in §A/RESULT were produced by the v3.2 scoring build `038fbb37…`. `ad03463f…` (v3.2.1) differs only by the large-model 4-bit load branch used for the cross-family replication (7B families on a T4); small models stay on the identical bf16 path, so re-running Qwen-1.5B under v3.2.1 reproduces `038fbb37…`'s numbers bit-for-bit. A DESIGN_LOG line (C16/C17) records the recalibration and this load delta.

### F. Result of the v3.2 confirmatory (Qwen2.5-1.5B) and the pre-registered v3.3 fix

The v3.2 causal leg discriminated: **V1 (covert) and V6 (flip) — the adversarial controls — support H-E1** (readable, null n.s., causally **source-DECOUPLED**: ρ_src 0.90 / 1.20). **V0/V3 (overt) log `undetermined`** because the efficacy-ratio guard (≤2×) fails on a *contentful* seed clause vs a *neutral* span (ratio 2.85 / 2.87), while V1/V6 pass it by a hair (1.98 / 1.99). The efficacy-ratio guard is brittle and conflates "clause carries information" with "mask is globally disruptive." The variance-blowup proxy separates them cleanly (V0 std-ratio 3.02× = real disruption → undetermined; V3 1.92× stable → its ρ_src 0.47 is a genuine COUPLED signal the guard wrongly suppresses).

**v3.3 (to pre-register in v0.19, run fresh — NOT applied post-hoc):** replace the efficacy-ratio guard with **(a) a projection-variance-stability guard** (score unless std blows up past a principled cutoff, e.g. 2.5×) **and (b) a content-matched non-source span** (mask an equal-length *contentful* decoy clause, not a neutral span, so efficacies match by construction). Immediate step first: **replicate v3.2 as-is across the other 5 families** (n=1 is the larger limit) before building v3.3.

## E. Status

Config-E **v3.1 result RECORDED** (registered null on H-E1/H-E3; strong confound-controlled representational finding — re-attachment readable, confound cancelled). **v3.2 OPEN, pre-registered, not yet run** — recalibrates the causal-leg estimator and the G1 gate scope so H-E2 becomes decidable (decoupled vs a registered coupled finding) and the covert/flip/neutral variants are gated on the right firewall. Publish either way; checkpoint-1 untouched.

---

*Continues `PREREGISTRATION_AMENDMENT_v0.17.md`. Result-to-date: `CONFIG_E_naturalistic_frame_RESULT.md`. Not deposited (working document).*
