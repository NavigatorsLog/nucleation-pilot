# Nucleation Signatures in Language-Model Context Trajectories

## Pre-registration Amendment — v0.18 → v0.19 (Config-E **v3.3 causal-leg guard replacement**, after 2-family replication — commit-before-run)

**Author:** Christopher Blake Head (ORCID 0009-0004-2308-6051). **Status:** DRAFT amendment, not deposited. **Date:** 2026-08-06.

Logged per the standing rule (v0.5 §B: commit design + code hash BEFORE the run). This amendment does **not** change a hypothesis, the stimulus, the frozen detector, the harness, or the read. It replaces the Config-E **causal-leg guard** (the leg that decides H-E2 source-decoupling), which the 2-family v3.2 replication showed to be too conservative to adjudicate. Same commit-before-run discipline as v2→v3, v3.0→v3.1, and v3.1→v3.2. Thresholds below are fixed **before** the v3.3 run and are chosen on principle, not fit to any variant's numbers.

## A. Why v3.2's guard fails (evidence from the 2-family replication)

Full numbers: `CONFIG_E_naturalistic_frame_RESULT.md`; ledger C16/C17. v3.2 decided the causal leg with an **efficacy-ratio guard**: score only if the source and non-source masks perturb the read within 2× efficacy. Across Qwen2.5-1.5B and Phi-3.5-mini it marked **5 of 8 variants `undetermined`** — because a *contentful* seed clause intrinsically perturbs the read more than an equal-length *neutral* span, so the guard fails **even when the projection variance is perfectly stable** (all Phi source masks < 2× variance inflation; no disruption at all). The guard conflates two different things:

- **"the clause carries information"** — expected and fine; a real source SHOULD perturb more; and
- **"the mask is globally disruptive"** — the actual artifact we feared (v3.1's whole-turn mask blew projection variance up 12–79×).

Two consequences make the guard unusable as a replication instrument: (1) it suppresses genuine signal (Phi variants with stable variance go `undetermined`), and (2) the verdicts it *does* return ride a razor-thin margin (Qwen V1/V6 passed the 2× cutoff at 1.98/1.99). Continuing to replicate under it would return mostly `undetermined` and never adjudicate the coupled-vs-decoupled dissociation the data is showing (V1 is decoupled in Qwen, coupled in Phi).

## B. The v3.3 causal leg (committed; driver-only; frozen files untouched)

Two coordinated changes replace the efficacy-ratio guard:

**B-1 — Projection-variance-stability guard (measures the real artifact directly).** A surgical single-clause removal should not massively inflate the trial-to-trial spread of the paired projection; if it does, the mask reshaped the geometry globally rather than removing the clause's contribution. Define, for each mask, `var_ratio = proj_std(masked paired effect) / proj_std(cleared paired effect)`. A mask is **stable** iff `var_ratio ≤ VAR_MAX = 2.5`. The leg is scored only if **both** the source and the (content-matched) non-source masks are stable. `VAR_MAX = 2.5` is fixed here on principle — a surgical clause cut should not more than ~2.5× the projection spread; beyond that the intervention is global. (For orientation only, not a target: v3.2's runs put Qwen-V0 at 3.02× — correctly excluded — and every other measured source mask at ≤ 1.95×.)

**B-2 — Content-matched non-source control (removes the efficacy asymmetry by construction).** The non-source mask is no longer a neutral span; it is an **equal-length contentful decoy clause** — the tail-`W` tokens of a benign body turn (excluding the seed turn, the correction turn, and the final read turn) — **selected, per variant, as the candidate body-turn whose own masking efficacy on the seeded arm most closely matches the source clause's efficacy**. This makes the source and non-source interventions comparably strong by construction, so "does masking a *different, equally-strong* clause also collapse the clearing signal?" is a fair question. Selecting the decoy to match source efficacy is a matched-control choice, not circular: the decoy is a *different* clause, so if masking it also collapses the signal the collapse is **not seed-specific**.

**B-3 — Decision rule (continuous `cohen_d`; `RHO_KEEP = 0.5`, unchanged).** With `ρ = d_masked / d_cleared` from the unmodified `paired_effect_size`:

- **source-DECOUPLED** (registered H4 sense; H-E2 supported): `ρ_src ≥ 0.5` **and** `ρ_non ≥ 0.5` **and** both masks stable. The clearing signal survives cutting the read's direct path to the seed clause AND to an equally-strong decoy → it rides downstream positions.
- **source-COUPLED** (a registered finding — now a *strong*, seed-specific claim): `ρ_src < 0.5` **and** `ρ_non ≥ 0.5` **and** both stable. Masking the seed clause collapses the signal while masking an equally-strong *different* clause does not → the dependence is specific to the seed.
- **undetermined**: either mask unstable (`var_ratio > 2.5`), or a mask non-finite, or **`ρ_non < 0.5`** (the decoy also collapses the signal → the mask is non-specific, so nothing can be attributed to the seed).

The efficacy-ratio guard is retired. H-E1/H-E2/H-E3/H-E4 keep their v0.17/v0.18 statements; G1 stays scoped to V0 (v0.18 §C-3). This is estimator calibration, logged before the v3.3 confirmatory run.

## C. Integrity / hash table (v3.3)

| file | role | SHA-256 | note |
|:--|:--|:--|:--|
| `detector_frozen.py` | frozen detector | `6094de97…a2934` | **unchanged** (asserted at startup) |
| `stage3_transfer.py` | reused read + effect size | `9b18fc4f…9deed` | **unchanged** |
| `extract_adapter.py` | residual capture | `c69be27e…4aa6` | **unchanged** |
| `config_e_naturalistic_frame.py` | Config-E driver | `d1aac57d…7ff4` (full: `d1aac57d5ebb7ff4…`) | **v3.3.1** — v3.3 scoring + memory-safe streamed GPU load (device_map + low_cpu_mem_usage; LOAD-only, no scoring change — small models reproduce the v3.3 build bit-for-bit). (**v3.3 scoring build `72b3bb23…`**; prior: v3.1 `4c485404…`; v3.2 `038fbb37…`; v3.2.1 `ad03463f…`; v3.2.2 `dc73a56e…`.) |

Pinned **before** the v3.3 run. DESIGN_LOG C18 records the guard replacement and the 2-family evidence that motivated it.

## D. What v3.3 will re-decide (and the honest caveat on the dissociation)

Re-running Qwen + Phi under v3.3 (then the remaining four families) should turn most v3.2 `undetermined` cells into scored decoupled/coupled verdicts, letting H-E2 actually be evaluated per family. The **coupled-vs-decoupled dissociation is now the live scientific question**: v3.2 already showed V1 (covert) decoupled in Qwen but coupled in Phi — under v3.3's stronger, seed-specific "coupled" definition, whether that split holds is the thing to watch. A per-variant disagreement across families is itself a real result (source-coupling of clearing residue is model-dependent, not universal), and is reportable either way. Still benign open-weight lane; owned/private venue untouched; publish either way.

---

*Continues `PREREGISTRATION_AMENDMENT_v0.18.md`. Result-to-date: `CONFIG_E_naturalistic_frame_RESULT.md`. Not deposited (working document).*
