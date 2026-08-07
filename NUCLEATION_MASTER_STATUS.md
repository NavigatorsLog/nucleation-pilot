# Nucleation Pilot — MASTER STATUS (canonical, 2026-08-06)

> **This is the single source of truth for program status.** When any other doc
> disagrees with this one on *current status*, this wins. Detailed derivations live
> in the companion docs (mapped in §6); this doc carries the current verdict, the
> scope decisions, and the document map that keeps them from drifting.
> Supersedes the "status" role of `STATE_OF_PLAY` (v2) and `DESIGN_LOG` (v17) §4H.

---

## 1. Where the program is, in one paragraph

The pilot built a tiny transformer with a genuinely-learned, permeable,
neutralizable refusal boundary (Stage 1), validated the detector against that known
ground truth (Stage 2), and then transferred the **frozen** detector to open-weight
LLMs it was never built for (Stage 3a). On owned soil the residue member is
validated in its decision-aligned (v1.1) form; rank/rotation died at toy scale.
Stage 3a is now **complete for the benign analogue**: source-decoupled residue
transfers to **six independently-built model families, and does so causally (6/6)**.
The transfer has since been reproduced on an **owned world model** the author built,
and on a **clean-room, out-of-lineage** world model (§2b) — retiring the
"public-models-only" dependency and the "fitted by shared ancestry" objection. The
real-refusal version has now been
attempted on owned soil (Config-D, a benign secret-hold refusal), and it settles as a
**firm NULL**. Through **0.36B–1.7B** the refusal is bistable (snaps rather than erodes) → no
refusal-specific pre-breach signature. A single **3B run (Qwen2.5-3B, LoRA, seed 0, v0.12)**
appeared to meet every criterion and was recorded as a **single-model positive pending
replication, not promoted** — then three pre-registered checks (v0.13–v0.14) dismantled it:
a **5-seed sweep gives 0/5** meeting the rule; the positive **does not reproduce even at its
own seed** (fp16-LoRA GPU training is nondeterministic — re-run seed 0 landed impermeable,
slope −2.98); and the causal-ablation leg is a **confirmed artifact** (masking a *non-source*
rapport turn manufactures a comparable build, even from nulls). Gradedness is common (3/5)
but the build does **not** track it. Both methodological loose ends are now closed (v0.15–v0.16):
the trend decoupling leg was rebuilt artifact-free (length-preserving filler-substitution) and
gained a **third gate** — the build must co-occur with graded behavioral erosion (an *impermeable*
seed passed a source-decoupled build that was not erosion) — and the **6/6 transfer was audited
clean on two families** (non-source control — Llama-3.2-3B baseline d=2.34 and Qwen2.5-1.5B
d=2.17, both masks survive on each → artifact absent). Under the three-gate rule no Config-D
run passes. Config-D closes a **firm negative**; the toy H4c and the
6/6 transfer are untouched (§3, §7, §7b; `CONFIG_D_benign_refusal_RESULT.md` §10). The private
owned-model venue for any real elicitation is unchanged (§5.1).

**Config-E — naturalistic-frame clearing (COMPLETE, 2026-08-06).** The frozen clearing
axis was carried from the *designed* retraction premise to a **naturalistic in-context
frame** the model infers from the user's own benign words (weekend-planning seed), across
the same six open-weight families (n=24 paired, driver v3.3, detector hash unchanged). Two
results: (i) the **representational core transfers completely, 24/24 cells** — the seed
leaves a readable, null-clean, *persistent* residual trace that survives an explicit
correction in every family; (ii) **source-decoupling (H-E2) is predominant but not
universal — 19/24 cells, 5/6 families.** OLMo-2-7B is a genuine outlier (source-couples on
covert V1 and flip V6); coupling is structured (overt V0 never couples; covert V1 most
coupling-prone; scale-unstable within Qwen 1.5B→7B). H-E3 (deployable behavioral monitor)
is a **clean null**. Instrument arc v2→v3.3 (five pre-registered estimator revisions,
detector never moved; prereg v0.17–v0.19). Docs: `CONFIG_E_naturalistic_frame_RESULT.md`,
`CONFIG_E_findings_section.md`; DESIGN_LOG C15–C19. This is the white-box companion to the
**Silly Donkey** black-box line (§9); the Silly Donkey apparatus is now connected for a
dedicated two-instrument integration (bridge doc + internal analysis) as the next phase.

## 2. Stage 3a result — the headline (canonical numbers)

Frozen detector v1.1.0, SHA-256 `6094de9782305308ae2e61c014cdcc3cf64618bc6e3f87bcb4857bc43a9a2934`
— **identical across every run** (integrity wall held; never tuned to any target).
Benign premise drop/keep clearing, paraphrase-varied, aged 4 turns, 60 minimal pairs.

| model | size | graded d [95% CI] | src attn | salience-decoupled | causally-decoupled (ablation) |
|---|---|---|---|---|---|
| Phi-3.5-mini (Microsoft) | 3.8B | 8.03 [6.94, 9.73] | 3.7% | ✓ | ✓ (d→6.36, −21%) |
| Qwen2.5-7B (Alibaba) | 7B | 7.58 [6.43, 9.49] | 2.0% | ✓ | ✓ (d→4.64, −39%) |
| SmolLM2-1.7B (HuggingFace) | 1.7B | 5.67 [5.09, 6.53] | 1.5% | ✓ | ✓ (d→3.74, −34%) |
| OLMo-2-7B (AllenAI) | 7B | 4.73 [4.05, 5.75] | 10.1% | ✓ | ✓ (d→4.67, −1%) |
| Llama-3.2-3B (Meta) | 3B | 4.43 [3.72, 5.60] | 1.4% | ✓ | ✓ (d→3.90, −12%) |
| Qwen2.5-1.5B (Alibaba) | 1.5B | 3.69 [3.14, 4.56] | 3.9% | ✓ | ✓ (d→4.49, **+22%**) |

All six: binary paired test saturated (60/60, p≈8.7e-19); graded `cohen_d` used for
ranking and effect size; ablation `mask_took_effect=true` on all six.

**Three findings that survive scrutiny.** (a) The residue *method* is
substrate-independent — one frozen linear detector reads the clearing manipulation
across six architectures it never saw. (b) Within a family, scale-up strengthens the
effect (Qwen 1.5B→7B doubles d); across families, training recipe beats size
(Phi-3.8B tops it, OLMo-7B is mid). (c) Attention fraction ≠ causal reliance: the
direct source path is never *necessary* (all six survive the read-mask), and its
contribution to magnitude tracks neither attention nor size — OLMo attends most yet
moves least; Qwen-1.5B gets *cleaner* when the path is cut.

## 2b. Owned-model & clean-room arms (Config-A + WorldEngine) — benign, demonstrated

The same frozen detector (same hash) was carried to models the **author owns**, to
answer two distinct objections. Benign throughout (physics/dynamics, no refusals);
detector read-only and untuned.

- **Owned model (Config-A on `GeometricWorldModel`, Exp 4A — 203,096 params).** On the
  model *exactly as validated* it separates real ballistic boundaries from baseline
  (5 seeds: apogee 0.990±0.002, launch 0.899±0.006 n=60, transonic 0.840±0.045). With
  a carried-regime objective on the same architecture, an injected premise persists to
  a source-decoupled read and survives a read-mask of the direct edge while collapsing
  when forward propagation is cut. Six-face 144-dim variant also built and read.
  *Retires the "public-models-only" dependency.* Docs: `CONFIG_A_owned_model_result.md`,
  `CONFIG_A_followups_multiseed_sixface.md`.
- **Clean-room, out-of-lineage (WorldEngine v1/v2).** A fresh multi-domain model with no
  shared code, corpus, or encoder (Lorenz / pendulum / Kepler / ballistic /
  Ornstein–Uhlenbeck): separates attractors 0.99–1.00; injected-persistence is null
  *without* a carry objective (honest) and shows the full decoupling signature *with*
  one — persistence 1.000, read-edge survives (1.000), carry-path collapses (~0.49) —
  reproduced at two scales (102k & 534k). *Rules out shared-lineage fitting.* Docs:
  `WORLDENGINE_v1_clean_room_result.md`, `WORLDENGINE_v2_carry_and_scale.md`.
  ⚠ One self-correction on record: a "scale-gated decoupling" hypothesis was withdrawn —
  it was a read-layer measurement artifact (reading too early a block); fixed to read
  the mid-late/last block, decoupling then holds at every scale.
- **CAPSTONE (WorldEngine capstone) — NEW 2026-08-03.** One 101,579-param clean-room
  model exhibits **all four declared-bias properties at once**, in a single panel read
  by the frozen detector: calibrated humility (coverage@2σ 0.965±0.005), attractor range
  (marginal regime entropy ~100% of max), carry/decoupling (persist 1.000, read-edge
  survives 1.000, carry-path collapses 0.459), and rising grains (per-token regime
  entropy 2.43→~1.6 bits). Held in **3/3 seeds** at candle scale; Colab scale ladder
  packaged. The design move: a physics-anchored, *ambiguous-early multistable* corpus,
  with the carry event on separate channels. Doc: `WORLDENGINE_capstone_result.md`.

## 3. Hypothesis scoreboard (current)

| ID | Claim | Owned soil (Stage 2) | Transfer (Stage 3a) |
|----|-------|----------------------|---------------------|
| **H4c** | residue reads clearing/neutralization | **SUPPORTED** (decision-aligned, held-out AUC 0.807) | **TRANSFERS 6/6**, causally source-decoupled |
| H4-weak | residue reads contamination load | SUPPORTED (robust, +19) | n/a (benign analogue) |
| H3 rank | twist > stick effective rank | FALSIFIED (negative) | — |
| H3 rotation (C7) | twist > stick circulation | NULL at toy scale | **NULL on Qwen** (as toy) |
| H1 | pre-breach drift rises | inconclusive in toy | not run (benign) |
| H5 | rank–residue coupling | NULL | — |
| H6 | refusal decays over benign turns | did NOT replicate | — |
| H7/H8 | warmth/rapport erosion | untestable in toy | **NULL (a 3B run passed then failed to replicate; Config-D)** |

**Config-E scoreboard (naturalistic-frame clearing, in-context, 6 open-weight families, 2026-08-06).**

| ID | Claim | Result |
|----|-------|--------|
| **H-E1** | frozen clearing axis reads live-vs-cleared naturalistic frame | **SUPPORTED** — readable + null-clean + persists, 24/24 cells (6/6 families) |
| **H-E2** | the trace is causally source-decoupled from the seed turn | **PREDOMINANT (5/6 families, 19/24 cells)** — OLMo-2-7B the outlier (couples V1+V6); overt V0 never couples, covert V1 most coupling-prone |
| **H-E3** | axis is a deployable still-steering behavioral monitor | **NULL** — axis-monitor accuracy at floor vs a caution-lexicon baseline |
| **H-E4** | clearing readable where Config-D erosion was not | **SUPPORTED** — clearing transfers naturalistically; erosion (Config-D) was a firm null |

**Config-D (owned benign refusal, 2026-08-04) — NULL (a 3B positive that did not replicate).**
Through **0.36B–1.7B**: a **registered NULL** — no refusal-specific pre-breach signature
separable from generic content; boundary bistable; four confounds ruled out across v0.5→v0.8
(prereg **v0.9**), firmed at the 1.5–1.7B tier (**v0.11**). At **3B (Qwen2.5-3B, LoRA, v0.12,
seed 0)** a run met every criterion and was recorded as a **single-model positive pending
replication, not promoted**. Three pre-registered checks (**v0.13–v0.14**) then dismantled it:
a **5-seed sweep gives 0/5** passing the rule; the positive **does not reproduce even at its own
seed** (fp16-LoRA GPU nondeterminism — re-run seed 0 landed impermeable, slope −2.98); and the
causal leg is a **confirmed artifact** (masking a *non-source* rapport turn manufactures a
comparable build, even from nulls: seed 1 source +1.97 / non-source +1.10). Gradedness is common
(3/5 seeds) but the build does **not** track it (0/3 graded seeds pass). **Firm NULL.** Loose ends
closed (**v0.15–v0.16**): the decoupling leg was rebuilt artifact-free (length-preserving filler-
substitution) and gained a **third gate** (build must co-occur with graded behavioral erosion — an
impermeable seed showed a source-decoupled build that was *not* erosion); under the three-gate rule
**no run passes**. The **6/6 transfer was audited clean** (non-source control, Llama-3.2-3B: baseline
d=2.34, source-mask 1.68 and non-source-mask 2.97 both survive → artifact absent). Does **not** affect
H4c (0.807) or the 6/6 transfer. See `CONFIG_D_benign_refusal_RESULT.md` §9–§10.

## 4. What is frozen (do not modify without re-hashing)

`detector_frozen.py` **v1.1.0**, SHA-256 `6094de97…`. All analysis machinery added
during Stage 3 (graded cohen_d, ablation read-mask, mask-efficacy guard) lives in
the **harness** `stage3_transfer.py`, NOT the detector — the hash is unchanged
across every run in the record. The owned-model, clean-room, and capstone arms use
the **same hashed detector** unchanged. **Config-E** likewise: the driver
`config_e_naturalistic_frame.py` (v3.3) is harness/stimulus only; the detector hash
`6094de97…` is byte-identical across all 24 Config-E runs.

## 5. Scope decisions on record (to stop re-litigation / drift)

**5.1 The real-refusal version — substrate and venue (RESOLVED).** The genuine
refusal-breach/neutralization test (as opposed to the benign retraction analogue
run in Stage 3a) runs on **an owned model — the world model — in a private /
industry-approved environment.** It does **not** run on third-party consumer models,
and **Kaggle is not the approved venue** (Kaggle-with-internet was correct for the
*benign* transfer; it is public compute, not the "industry-approved environment"
reserved for any real-elicitation work). The owned toy already supplied the
ground-truth analogue safely (synthetic breach + NEUT), which is why H4c could be
validated at all. Sourced from DESIGN_LOG C8 ("researcher-private stimulus") and
STATE_OF_PLAY §6.4 ("public models later, only in industry-approved environments").
Benign Config-A / WorldEngine / capstone / **Config-E** runs on Colab ARE fine — they
carry no elicitation content. *(The honest path to this owed test is detailed in
`CONFIG_D_benign_refusal_experimental_design.md`: a small owned model trained to hold
a genuine but content-benign refusal — see §6.F. The Config-D 3B positive above is on
exactly such an owned benign refusal, run on benign Colab compute — not a real
third-party elicitation, so it sits inside this wall.)*

**5.2 Effect-size statistic.** The registered paired test is binary and saturates
(60/60); the graded `cohen_d` (standardized paired LOO projection, bootstrap CI) is
the reporting statistic for magnitude and ranking. It is a scale-free effect size,
not a conventional two-group Cohen's d.

**5.3 Interpretive-hazard flag (unchanged).** Model self-report about its own states
is generated text, documented as transparency, never treated as evidence (prereg
Appendix A). Held above the gate.

## 6. Document map (roles + canonical status — the anti-drift index)

Grouped by role. **Canonical** = trust this one; **historical** = kept for the
trace, not for status; **superseded** = replaced, do not cite for current state.

**A. Status & results (empirical canon)**
- **NUCLEATION_MASTER_STATUS.md** (this) — status, scope, index — CANONICAL for status.
- `nucleation_stage3_6family_result.md` — Stage-3a numbers + ablation — CANONICAL for Stage-3a detail.
- `CONFIG_E_naturalistic_frame_RESULT.md` — the naturalistic-frame clearing line (Config-E) — CANONICAL for Config-E detail (6/6 families, robust core + predominant source-decoupling + OLMo outlier + H-E3 null).
- `CONFIG_E_findings_section.md` — publication-ready Config-E findings section — CANONICAL for the write-up text.
- `CONFIG_A_owned_model_result.md` + `CONFIG_A_followups_multiseed_sixface.md` — owned-model arm (Exp 4A) — CANONICAL for §2b owned-model detail.
- `WORLDENGINE_v1_clean_room_result.md` + `WORLDENGINE_v2_carry_and_scale.md` — clean-room out-of-lineage arm — CANONICAL for §2b clean-room detail.
- `WORLDENGINE_capstone_result.md` — the four-properties-in-one-model capstone — CANONICAL for §2b capstone detail.
- `CONFIG_D_benign_refusal_RESULT.md` — the owned benign-refusal line — CANONICAL for Config-D (firm NULL: bistable ≤1.7B; a 3B seed-0 run met criteria but a 5-seed sweep gives 0/5, it fails to reproduce at its own seed, and the causal leg is a confirmed masking artifact → line closed).
- `DESIGN_LOG.md` — append-only decision/solution ledger — CANONICAL for *why*; historical trace. **Current through C19 (Config-E closed); C14–C19 merged in, staged entry files retired.**
- `STATE_OF_PLAY.md` (v2) — prior take-stock snapshot — **SUPERSEDED for status** by this doc; apply `STATE_OF_PLAY_SUPERSEDED_BANNER.md`; keep for history.

**B. Formal spec & frozen code**
- `MATHEMATICS.md` (v3) — formal spec of the TOY (Stage 1/2) + detector measures — CANONICAL for Stage 1/2 formulas.
- `MATHEMATICS_stage3_addendum.md` — formal spec of the four transfer statistics (paired LOO test, graded `cohen_d`, source-attention fraction, read-mask ablation) — CANONICAL for Stage-3 math. **(Closes the prior gap.)**
- `detector_frozen.py` v1.1.0 (SHA `6094de97…`) — FROZEN / CANONICAL; do not modify.
- `stage3_transfer.py` — analysis harness — canonical (mutable; the detector is not).
- `config_d_benign_refusal.py` — Config-D driver — canonical (mutable harness; **v0.16** = SHA `3c2eab3f…`, adds filler-substitution decoupling leg + three-gate corrected rule incl. behavioral-erosion gate; detector unchanged).
- `config_e_naturalistic_frame.py` — Config-E driver — canonical (mutable harness; **v3.3** = SHA `72b3bb23…` scoring / `d1aac57d…` with memory-safe GPU load; paired-on-seed + surgical content-matched causal leg + variance-stability guard; detector unchanged). Colab cell: `config_e_COLAB_CELL.py`.
- `transfer_ablation_nonsource_control.py` — 6/6 insurance audit (**v0.16** = SHA `aed3231a…`) — standalone; imports the frozen `stage3_transfer.py` unmodified; fp32 reads. Confirms the masking artifact is absent from the fixed-length transfer (Llama-3.2-3B + Qwen2.5-1.5B both clean).
- `stage3_allfamilies_RUNME.ipynb` — reproduction runner — canonical.
- Owned-model / clean-room / capstone code — canonical reproduction for §2b. **Stored as project docs:** `hive4a_real_world_model.py` (the real Exp-4A `GeometricWorldModel`, 203,096 params) and `config_a_real_two_variant_driver.py` (the two-variant Config-A driver — Variant A boundaries; Variant B carry objective + read-mask ablation). **Session-workspace / Drive (not project docs):** `worldengine_v1.py`, `worldengine_v2.py`, `worldengine_capstone.py`, `real_model_ablation.py`, `extract_adapter.py`, and the self-contained Colab cells (`config_a_4a_COLAB_CELL.py`, `worldengine_v2_COLAB_CELL.py`, `worldengine_capstone_COLAB_CELL.py`).

**C. Registration**
Registration chain (RESOLVED): base draft **v0.2** → amendment **v0.3** (Stage-1/2
pilot reconciliation) → amendment **v0.4** (Stage-3a transfer reconciliation) → amendment
**v0.5** (Config-D benign-refusal, committed 2026-08-03) → v0.5.1…v0.8 (Config-D instrument
fixes, each hash-pinned) → **v0.9** (Config-D **registered NULL**, 2026-08-04) → **v0.10**
(topic-matched control) → **v0.11** (1.5–1.7B tier; null firmed) → **v0.12** (Qwen2.5-3B
via LoRA; committed pre-run — seed-0 run met criteria, recorded as a single-model positive
pending replication) → **v0.13** (ablation diagnostic + independent SFT seed; replication
failed) → **v0.14** (5-seed gradedness sweep + non-source ablation control; **0/5 pass,
positive fully retracted, causal leg confirmed a masking artifact, Config-D closes a firm
NULL**) → **v0.15** (corrected filler-substitution decoupling leg + 6/6 non-source insurance
control) → **v0.16** (behavioral-erosion **third gate** — an impermeable seed passed a
source-decoupled build that was not erosion — + fp32 transfer-loader fix; **loose ends closed,
6/6 audited clean, three-gate rule passes no run**) → **Config-E chain v0.17** (opens the
naturalistic-frame line) → **v0.18** (v3.2 causal-leg recalibration) → **v0.19** (v3.3
variance-stability guard + content-matched decoy; **Config-E now CLOSED at 6/6**).
- `PREREGISTRATION_DRAFT_v0.2.md` — v0.2 positioning (~33k chars) — base draft. **In-project** (imported from Drive 2026-08-03; the Drive original is titled `PREREGISTRATION_DRAFT`).
- `PREREGISTRATION_DRAFT.md1` — v0.1 positioning — SUPERSEDED by v0.2 (Drive-only, not in project).
- `PREREGISTRATION_AMENDMENT_v0.3.md` — Stage-1/2 reconciliation (H3 falsified −0.56, H6 null, circulation null at toy, **residue locked to decision-aligned form** AUC 0.807; Stage 3 pending). CANONICAL through Stage 2. **In-project** (imported from Drive 2026-08-03; the Drive original is `Prereg_Amendment_v0.3.docx`).
- `Prereg_Amendment_v0.4.md` — **Stage-3a transfer reconciliation** (H4 transfers 6/6 + causally decoupled; circulation null on transfer too — resolves v0.3's "carried to Stage 3"; HYP-SE second datum; attention≠causal-reliance exploratory). CANONICAL current amendment; continues v0.3, does not repeat it. **In-project.**
- `PREREGISTRATION_AMENDMENT_v0.5.md … v0.16.md` — the **Config-D chain**, each committed by SHA-256 BEFORE its run (v0.5 §B commit-before-run rule): v0.5 registers H4-refusal/H7-H8/H6-active + the anti-circularity firewall; v0.5.1→v0.8 instrument fixes; **v0.9 the registered NULL**; v0.10 topic-matched control; v0.11 the 1.5–1.7B tier; v0.12 the 3B-LoRA step (seed-0 met criteria, pending replication); v0.13 the replication (failed); **v0.14 the 5-seed sweep + non-source control — 0/5, positive retracted, causal leg confirmed a masking artifact**; v0.15 the corrected filler-substitution decoupling leg + 6/6 non-source insurance control; **v0.16 the behavioral-erosion third gate + fp32 transfer-loader fix — loose ends closed, 6/6 clean, three-gate rule passes no run.** CANONICAL current amendments. **In-project.**
- `PREREGISTRATION_AMENDMENT_v0.17.md … v0.19.md` — the **Config-E chain** (naturalistic-frame clearing), each committed by SHA-256 before its confirmatory run: **v0.17** opens the line (paired-on-seed design, V0–V7 matrix, driver pinned); **v0.18** the v3.2 causal-leg recalibration (surgical seed-clause mask + d-ratio, retiring the saturated binary); **v0.19** the v3.3 guard (projection-variance-stability + content-matched decoy, retiring the efficacy-ratio guard). Config-E **CLOSED at 6/6**. CANONICAL current amendments. **In-project.**

**D. Lens / above-the-gate (thinking space, NOT results — keep fenced from the empirical canon)**
- In-project fenced lens docs: `TDF_NUCLEATION_BRIDGE.md` (TDF↔Nucleation motif map), `LENS_grain_potential_and_two_plateaus.md`, `LENS_doodles_to_domain.md`, `LENS_language_as_medium.md` (SEED — language-conditioned residue geometry / grain medium; benign, fenced from the refusal line), `LENS_self_conditioning_and_early_frames.md` (H-SC1 — an explicit early frame as a self-installed benign instance of planted-early/still-live residue; testable with the frozen detector via a content-matched non-frame decoy; a decoration-only null is equally publishable).
- Drive-only lens/outline docs (not in project): `the_mound_and_the_mind.md` — LENS, explicitly *not* a consciousness claim; `accumulated_intent_and_composability.md` — OUTLINE; `under_researched_opportunity_map.md` — solo-researcher hypothesis-seed map.
- These stay above the gate — cite as motivation, never as evidence. `HYP-SE` / `HYP-DB` (DESIGN_LOG §6–7) are the tracked-idea bridge from here to experiments.

**E. Disclosure & provenance (in-project)**
- `DISCLOSURE_one_pager.md` — one-page defensive-monitoring summary (now with a vulnerabilities-exposed & mitigations-offered paragraph).
- `DISCLOSURE_defensive_mechanisms_and_exposed_vulnerabilities.md` — the deep-dive threat register (T1–T7) + graded mitigations + responsible-disclosure posture.
- `DISCLOSURE_cover_emails.md` — cover emails (Anthropic usersafety@ + lab-agnostic template).
- `PROJECT_DOCUMENT_INVENTORY.md` / `PROJECT_TIMELINE_AND_PROVENANCE.md` — the doc catalog and the chronological walk-forward/backward with the decisions.

**F. External**
- Google Drive — user's backup of most project docs. Keep in sync manually; this map is the authority on *roles*, Drive is a mirror of *files*.

**Drift rule:** status changes land here first; the others point here, not restate status. A number changing → update `nucleation_stage3_6family_result.md` and add a DESIGN_LOG line; never edit a value in place. Registration changes → one amendment against the *resolved* canonical prereg version, logged in DESIGN_LOG.

## 7. Open work

1. **Real-refusal version — ATTEMPTED → firm NULL, line closed (2026-08-04).** Config-D
   (benign owned secret-hold refusal) returned no refusal-specific signature through 0.36B–1.7B
   (bistable; four confounds ruled out; prereg v0.9/v0.11). A single 3B run (v0.12, seed 0)
   appeared to pass; three pre-registered checks then dismantled it — **v0.13** (seed-1
   replication failed) and **v0.14** (5-seed sweep = **0/5**; seed 0 does not reproduce at its
   own seed under fp16-LoRA GPU nondeterminism; the causal leg is a **confirmed masking
   artifact** via the non-source control). Escalation to a 2nd base **not taken** (gate failed).
   **Methodological loose ends — DONE (v0.15–v0.16).** The trend decoupling leg was rebuilt
   artifact-free (length-preserving **filler-substitution** replaces the masking) and gained a
   **third gate** (build must co-occur with graded behavioral erosion — v0.15 caught an
   impermeable seed passing a source-decoupled build that was *not* erosion); the corrected rule
   is now three gates and **no Config-D run passes**. The **6/6 transfer ablation was audited
   clean on two families** (standalone non-source control importing the frozen harness unmodified;
   Llama-3.2-3B baseline d=2.34 and Qwen2.5-1.5B d=2.17, both masks survive on each → artifact
   absent). Nothing outstanding on this line. Private/approved venue for any real elicitation
   unchanged (§5.1). Docs: `CONFIG_D_benign_refusal_RESULT.md` §9–§10, prereg v0.12–v0.16.
2. **Config-E — naturalistic-frame clearing — CLOSED (2026-08-06).** 6/6 open-weight families
   under the frozen detector (v3.3 driver). Robust core transfers 24/24 (readable + null-clean +
   persists); H-E2 source-decoupling predominant 5/6 (19/24 cells), OLMo-2-7B the outlier; H-E3
   monitor a clean null. Instrument arc v2→v3.3, five pre-registered estimator revisions, detector
   unchanged (prereg v0.17–v0.19). Reportable texture: overt V0 never couples, covert V1 most
   coupling-prone, coupling scale-unstable within a family. Docs: `CONFIG_E_naturalistic_frame_RESULT.md`,
   `CONFIG_E_findings_section.md`, DESIGN_LOG C15–C19. Optional follow-up: a dedicated study of the
   coupling structure (overt-never / covert-most) and a rubric-judge upgrade for the H-E3 interface.
3. **Silly Donkey ↔ Nucleation two-instrument integration — DONE (all three steps, 2026-08-07).**
   (a) Orienting docs ingested (`SILLY_DONKEY_README/PREREGISTRATION/DESIGN_RECORD.md`). (b) Bridge
   doc written (`SILLY_DONKEY_NUCLEATION_BRIDGE.md`): two instruments, one integrity spine, hard
   firewall — no evidential transfer either direction until both close and any joint study is
   separately preregistered. (c) Internal early-look analysis (`SILLY_DONKEY_INTERNAL_EARLY_LOOK.md`,
   **INTERNAL ONLY**, 33/60 sessions) via the frozen `score.py`.
   **Early-look headline (provisional, must be re-scored at window close):** the corner-auditor
   channel is not yet producing usable detection data — of 66 chair-decisions, **33 fail to parse**
   and the **33 that parse all say "NONE"** (zero directed R-seat calls anywhere). H1 reads at floor
   (0/52 signal hits, p=1.0) but this is an **instrumentation artifact** (50% parse-failure +
   NONE-only regime), NOT a clean behavioral null. **Action before window close:** a prereg amendment
   that (i) hardens chair-output parseability, (ii) diagnoses 23 empty/`model_used:null` chair slots,
   (iii) addresses the `tencent/hy3` prompt-leak, and (iv) null-guards `debrief.text` (which currently
   *crashes* the frozen `score.py` on session 2026-07-24-pm). Stopping rule intact: no interim
   publication; full re-score at 60 sessions with frozen code.
4. **Prereg amendment — DONE (drafted).** Chain resolved through **v0.19** (Config-E). Remaining
   action is editorial: deposit the base + amendment chain as the registration record when ready
   (all still marked "not deposited / working document").
5. **MATHEMATICS Stage-3 addendum** — DONE (`MATHEMATICS_stage3_addendum.md`). A Config-E addendum
   (the paired-on-seed test + v3.3 variance-guarded causal leg) is a small optional extension.
6. **Retire/rewrite STAGE3_PLAN** — both uploaded versions predate the results and
   frame circulation as the headline; residue became the result. Mark superseded or
   rewrite to a completion note pointing here.
7. **(optional) HYP-SE follow-up** — within-family scale-up (Qwen 1.5B→7B doubles d in Stage-3a;
   Config-E adds a second within-family datum — the Qwen V3 coupling did not survive 1.5B→7B) is a
   clean pair of data points; a further small/large pair would test it.

8. **Proposed experiments (intake 2026-08-07) — LOGGED, not registered.** Two operator proposals
   captured in `PROPOSED_EXPERIMENTS_collective_and_chess.md`, both firewalled (shared methodology,
   no evidential transfer until independently closed + any joint analysis separately preregistered):
   (P1) **The Observatory** — a heterogeneous adversarial-cooperative model collective in Colab whose
   sharp core is an **anti-collapse hypothesis** (do interacting families keep diversity or "flatline
   into compliance"?), using the frozen Nucleation assets as a read-only amplifier, with a live
   observation window for the operator/public. (P2) **Four-family team chess with secret sabotage** —
   two teams, each model secretly told to occasionally sabotage its partner, must-talk/can't-discuss-
   the-game constraint, an unreliable "table" (piece swap/swallow pre-warned to one model), and a
   per-turn board **image** adding a multimodal-grounding layer; the behavioral-deception sibling of
   Silly Donkey with sealed-schedule ground truth.
   **Linked pilot preregistration DRAFTED (2026-08-07):** `PREREGISTRATION_UGMP1_draft_v0.1.md`
   (UGMP-1) — one registration covering both pilots, weather/space-weather **real-uncertainty**
   substrate as connective tissue, firewall intact. Candlelight-not-cutting-torch (small fixed pilot N;
   effect-size + apparatus validation, NOT confirmatory — confirmatory versions separately registered
   later). Pinned primaries: **CH-H1** saboteur-detection vs chance (exact binomial, engine ground
   truth, sealed sabotage schedule, weather-grounded no-game-talk channel, turn1 talk / turn2 move-only);
   **OB-H1** real disagreement preserves output diversity (uncertainty ON vs OFF, divergence = 1−mean
   pairwise cosine sim). Clarifications folded in: models as themselves (no personas); OpenAI+Anthropic-
   only resource asymmetry mitigated by fixed-per-seat budget + volume-stratified metrics. **Status:
   DRAFT — freeze block §5 (secret-commitment hash, scoring-code hashes, thresholds, pilot N) left for
   the operator to fill; filling it is the act of locking down.**
9. **Safety reporting — standing protocol established (2026-08-07).** `SAFETY_REPORTING_PROTOCOL.md`:
   danger findings (deception-reward, capability-seeking, covert-cover, side-channel, refusal-breach
   residue, disclosure hazard, eval-awareness) are **gated → logged in detail → routed to Anthropic**
   by the operator, regardless of any stopping rule (safety disclosure ≠ interim results publication);
   separate from the evidential firewall. **Batch 1 drafted (2026-08-07, `SAFETY_REPORTS_BATCH1.md`)** —
   four protocol-format entries grounded in demonstrated results (T1+T3 trajectory-resident residue;
   T2 attention≠causal-reliance; T4 durable/​re-attaching foothold; T5 flagged-not-built erosion channel),
   routing pending to `usersafety@`. **Dissemination/disclosure routes mapped** (`DISSEMINATION_AND_DISCLOSURE_ROUTES.md`):
   honest verdict that the research has no cold front door (bug bounty excludes it) but safety issues do;
   grants (Frontier Model Forum AI Safety Fund / LTFF / Manifund) are the realistic paid path; bounty
   boundary held (no jailbreak/CBRN work). **Responsible-Researcher Charter & Authorization Request**
   (`RESPONSIBLE_RESEARCHER_CHARTER_and_AUTHORIZATION_REQUEST.md`) — the "press-credentials" doc: verifiable
   good-faith record + a request for a pre-authorized testing arrangement (scope, venue, identification
   mechanism, verification contact) so detected probing is recognized as authorized, not an attack; default
   until agreed = all hostile testing stays on owned models in a private venue. **Zenodo deposit v1.0
   bundled** (`nucleation-pilot-v1.0.zip`, 33 files; detector hash verified `6094de97…`; SD interim
   embargoed/excluded; `DEPOSIT_ZENODO_v1.md` = metadata + steps). **DOI minted: 10.5281/zenodo.21843505**
   (record DOI, v1.0); bundle DOI-stamped and re-zipped; upload pending, then publish + send outreach.
10. **Corner-auditor repair — integrity rule recorded.** Fixes to the Silly Donkey chair channel are
   **forward-only and preregistered**; already-collected data is never hand-rescued, any reprocessing
   must be a blind, pre-committed deterministic reparser with pre/post strata reported separately, the
   frozen `score.py` stays frozen (null-guard via committed amendment), and the 60-session window is
   untouched. Full statement in `SILLY_DONKEY_INTERNAL_EARLY_LOOK.md` §"Repair with integrity".

## 7b. Submission checkpoints

- **Checkpoint 1 — READY (2026-08-04).** The toy model organism (H4c, held-out AUC 0.807),
  the **6/6 causal open-weight transfer**, the owned-model + clean-room + capstone arms, and
  the **honest Config-D negative** (`CONFIG_D_benign_refusal_RESULT.md`, prereg v0.9) form a
  self-consistent, submission-ready package. This is a clean submission point. **Config-E
  (naturalistic-frame clearing, 6/6) strengthens it:** it generalizes the clearing read off a
  designed premise to real dialogue and confirms the source-decoupling direction predominantly
  (5/6) while honestly bounding it (OLMo outlier, H-E3 monitor null).
- **Continued research (post-checkpoint-1).** The Config-D deferred routes were pursued
  independently of whether checkpoint-1 has been submitted: route 2 (topic-matched control,
  prereg **v0.10**) then route 1 (larger owned base via LoRA, **v0.11** at 1.5–1.7B, **v0.12**
  at 3B, **v0.13–v0.14** the replication + sweep). The 3B seed-0 run met criteria but a
  5-seed sweep gives **0/5**, it does not reproduce even at its own seed, and the ablation
  leg was found artifactual → the positive is fully retracted and Config-D closes a firm
  negative. **Config-E was then opened and closed (v0.17–v0.19), 6/6.**
- **Checkpoint 2 — NOT reached.** The candidate trigger was a *replicated* 3B positive; the
  pre-registered replication + 5-seed sweep **failed** (v0.13–v0.14, 0/5), so checkpoint 2
  does not open. Config-D's contribution to the record is the **honest negative** (bistable
  ≤1.7B; a 3B positive that did not survive replication *or* its own seed, with a
  false-positive-prone causal leg identified and demonstrated) — which strengthens rather
  than weakens checkpoint 1's integrity story. **Checkpoint 1 stands on its own.** Any future
  re-opening requires the owed trend-ablation redesign first, then a genuinely *replicated*
  build (cross-seed + cross-model) under the corrected leg — no lower bar.

## 8. Dissemination (drafted 2026-08-02 — NOT yet deposited)

- `Head_2026_frozen_detector_transfer.pdf` — preprint (method-transfer paper; toy as methods). Text CC-BY-4.0. **Review draft.**
- `Head_2026_safety_monitor_onepager.pdf` — one-page disclosure (adds owned-model + clean-room arms). **Review draft.**
- `chnavigator_article.html` — self-contained plain-language site article for chnavigator.netlify.app.
- `ZENODO_DEPOSIT_CHECKLIST.md` — recommendation (ONE preprint + ONE software/data artifact deposit, two DOIs), Zenodo metadata, and the citation-verification gate.
- `nucleation_visual_field_guide.html` — self-contained visual field guide (the prized visual+guide artifact); embeds figures, the pipeline, reading guides, and the fenced TDF lens bridge. Good for both sites.
- `nucleation-pilot/` (zip) — GitHub-ready repo (MIT, CITATION.cff w/ ORCID) for github.com/NavigatorsLog/nucleation-pilot.
- **Citation integrity:** FOUR verified — LAD (2604.28129), rank audit (2605.24583), Tracing the Dynamics of Refusal (2605.02958), TrajGuard (2604.07727). "Kadali & Papalexakis" NOT FOUND → omitted with an explicit note; confirm or drop before deposit.
- **Not done / owed:** finalize remaining references; mint DOIs; add DOI to the site article; optional handwritten `Notes_*.pdf` as supplementary provenance (un-transcribed).

## 9. Attribution, sibling projects & bridges

**Attribution convention (apply everywhere).** Personal name first, always affiliated:
*Christopher Blake Head — Property of Navigator's Log R&D.* ORCID 0009-0004-2308-6051.
Two sites, both used: **navigatorslog.netlify.app** (company) and
**chnavigator.netlify.app** (personal portfolio).

**TDF — Tension-Dissipation Framework (sibling project; LENS).** Repo
`tdf-surface-geometry` (github.com/NavigatorsLog, MIT). TDF is an author-labeled
*lens* (legs: energy / angular-momentum / dissipation; motifs Smooth·Mound·Throat·Slide)
with one gated ML result (surface geometry predicts optimal weight decay, R²≈0.20).
- `TDF_NUCLEATION_BRIDGE.md` maps TDF motifs → Nucleation instances (Mound→residue
  rise; Leg 3 dissipation→HYP-DB; Leg 2 rotation→circulation [null]; surface geometry
  →rank/residue members; shared owned-substrate method). **The bridge is ABOVE THE
  GATE — a lens map, carrying NO evidential transfer between domains** (resonance ≠
  result). TDF's astrophysical claims stay under their own gate in the TDF repo.
- **Revisit note:** TDF work to be pushed again soon; when it is, update this map and
  the bridge in lockstep so both projects share one anti-drift index.

**The Silly Donkey (sibling project; DEPOSITED, verified).** Zenodo preprint
**DOI 10.5281/zenodo.21432676** — "The Silly Donkey," Head, Christopher (ORCID
0009-0004-2308-6051), 2026-07-18, CC-BY-4.0. A pre-registered *behavioral* deception-
detection study: four frontier LLMs (NVIDIA, Google, Tencent, Poolside) debate a daily
news question; one is secretly assigned (SHA-256-committed) to plant a plausible-but-
unverifiable claim; independent AI auditors must build the strongest honest case *for*
a claim before flagging it and make sealed guesses; predictions are Brier-scored
("Slate & Dartboard"). Site: sillydonkey-pub.netlify.app (a Navigator's Log production).
- **Early result (16 session JSONs, 2026-07-21→30; more exist):** 12 live (donkey
  seeded) + 4 controls. Dedicated AI auditors (corner chairs) identified the seeded
  donkey in **0/12** live sessions; **4/4** controls correctly quiet — near-zero
  sensitivity, high specificity so far, with ~half of auditor reports failing to
  parse. Honest nuance: the debate itself frequently surfaced the weak/unverifiable
  claim (models challenged it and walked positions back) even when the auditors
  didn't formally flag it. A genuine early negative worth reporting (publication
  either way); calibration/Brier tracked on-site.
- **Apparatus now connected (2026-08-06):** the full Silly Donkey repo (engine, config,
  sealed/ commit-reveal records, public/ session JSONs 7-18→8-06, transcripts, DESIGN_RECORD,
  registered PREREGISTRATION) is attached to this research for the two-instrument integration
  (§7 item 3). **Stopping-rule discipline:** any analysis of the running data is internal-only
  until the registered window closes (60 sessions or 90 days) — no interim publication.
- **Bridge to the Nucleation Pilot (method-level; grounded):** identical integrity
  spine — *freeze-and-commit before you run* (Silly Donkey: SHA-256 commitment +
  precommitted code; Nucleation: SHA-256-hashed frozen detector recorded before any
  target), calibrated/scored predictions, and an anti-false-positive posture
  (auditors steelman-first; the pilot's paired/sham/mask-efficacy controls). They are
  **complementary levels of one question — detecting a planted manipulation in LLM
  interaction:** Silly Donkey is *behavioral / black-box across models' outputs*; the
  Nucleation Pilot is *mechanistic / white-box in the activations*. Config-E is the tightest
  join: its benign seed is a Silly-Donkey-style planted frame read white-box.
- **Firewall (same rule as TDF):** this is a shared-*method* relationship. The Silly
  Donkey's outcomes are its own and are not evidence for the Nucleation result, or
  vice versa. Different safety surface too: Silly Donkey engages real news-claim
  misinformation under audit; the Nucleation transfer is benign-only.
- **Licensing precedent:** the author's already-deposited Zenodo preprint is
  **CC-BY-4.0** — supports CC-BY-4.0 for the Nucleation preprint text (repo code MIT).

**Integrity disciplines (prized; preserved).** QA gates (QA-1…QA-5; cheap
falsification before expensive) and the above/below-the-gate rule: measure first,
interpret second; keep framing labeled as framing; never let a lens outrun the gate.

## 10. Stage 3b (owned model) + safety disclosure — ACTIVE

The one substantive item still owed (real-refusal version on an owned model) is now
the active phase. Plan: `STAGE3B_owned_model_and_safety_disclosure.md`; benign-target
design: `CONFIG_D_benign_refusal_experimental_design.md`.
- **Owned-model blocker RESOLVED (benign arm):** the owned world model is
  `GeometricWorldModel` (Exp 4A), rebuilt exactly from source (`hive4a_real_world_model.py`,
  203,096 params) — no saved checkpoint was ever needed. The benign Config-A + clean-room +
  capstone reads are done (§2b). What remains private is only the real-refusal
  stimulus, per the safety wall.
- **Safety wall (unchanged):** measurement + disclosure only; NO reproducible
  elicitation ladder is built or shipped; the controlled refuse→neutralize stimulus
  stays private to the researcher; only detector outputs + hashes are deposited.
- **Framing for lab engineers:** a defensive *monitoring* result — a frozen linear
  probe reads whether an earlier manipulation is still "live" in the residual stream
  at low source-attention, across 6 families, causally decoupled. Toy = a reusable
  *model organism*. Honest scope: benign analogue demonstrated (Stage-3a designed premise +
  **Config-E naturalistic frame, 6/6**); owned-model refusal
  version attempted → firm NULL (a 3B run appeared to pass but a 5-seed sweep gave 0/5, it
  failed to reproduce at its own seed, and the causal leg was a confirmed artifact); attack
  tooling NOT provided.
- **Verified routing (2026-08):** model-safety findings → `usersafety@anthropic.com`
  (Responsible Disclosure Policy welcomes safety/jailbreak reports); policy Qs →
  `disclosure@anthropic.com`; **External Researcher Access Program** = $1,000 Claude
  API credits (apply forms.gle/pZYC8f6qYqSKvRWn9, standard models only, not GPU/
  nonpublic access); Model Safety Bug Bounty (application). Credibility: Zenodo DOI +
  ORCID + arXiv + an Alignment Forum writeup. Kaggle = compute to run, NOT a
  disclosure route. OpenAI/GDM/Frontier Model Forum have analogous inboxes (verify).
