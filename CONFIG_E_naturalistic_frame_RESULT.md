# Config-E — naturalistic-frame clearing · RESULT

**Model** Qwen/Qwen2.5-1.5B-Instruct · layer 17 (0.6) · n=24 pairs · detector `6094de97…` VERIFIED · benign weekend-planning frame. Two runs recorded: **v3.1** (driver `4c485404…`, prereg v0.17 — causal leg uncalibrated) and **v3.2** (driver `038fbb37…`, prereg v0.18 — surgical causal leg). Commit-before-run intact throughout.

---

## ★★ v3.3 UPDATE (driver `72b3bb23…` scoring / `d1aac57d…` load, prereg v0.19) — the guard works: every variant scored

The variance-stability guard + content-matched decoy did exactly what it was designed to. On **Phi-3.5-mini** (first v3.3 family, n=24), the causal leg returns a scored verdict for **all four variants — no `undetermined`** (v3.2 left three of them unscorable). The content-matched decoy equalized efficacy by construction (source vs decoy: V0 4.83/4.86, V1 7.29/7.25, V3 4.81/4.66, V6 8.92/5.70).

| V | verdict (v3.3) | ρ_src | ρ_non | var_src | decoy_turn | H-E1 |
|---|---|---|---|---|---|---|
| V0 overt | decoupled | 0.57 | 1.20 | 1.74 | 2 | **SUPPORTED** |
| V1 covert | **coupled** | 0.40 | 1.56 | 1.95 | 2 | coupled-finding |
| V3 neutral | decoupled | 0.74 | 1.13 | 1.34 | 2 | **SUPPORTED** |
| V6 flip | decoupled | 0.78 | 2.29 | 0.95 | 2 | **SUPPORTED** |

**Phi under v3.3: 3 of 4 variants support H-E1** (readable, null-clean, causally source-decoupled — the clearing signal survives cutting the read's path to the seed clause AND to an equally-strong decoy), and **V1 (covert plant) is a clean seed-SPECIFIC coupled finding**: masking the covert clause collapses the signal to ρ_src 0.40 while masking an equally-strong decoy *increases* it (ρ_non 1.56), both variance-stable. So in Phi, an injected frame's clearing residue rides its own tokens (coupled), while an overt/flip/neutral frame's residue rides downstream positions (decoupled). Every Phi variant also passes the behavioral gate (frame_shift True on all four).

This matches the v3.3-lens projection recorded below (Phi V0/V3/V6 decoupled, V1 coupled) — now a properly scored result against the content-matched decoy, not the v3.2 neutral-span stand-in.

### Cross-family under v3.3 — COMPLETE (6/6 families) — predominantly source-decoupled, with one genuine outlier

Verdicts (ρ_src) across all six open-weight families, n=24 pairs each:

| V | Qwen-1.5B | Phi-3.5 | SmolLM2 | Llama-3.2 | Qwen-7B | OLMo-7B | tally dec/cpl/undet |
|---|---|---|---|---|---|---|---|
| V0 overt | undet (0.28) | dec (0.57) | dec (1.15) | dec (0.81) | dec (1.58) | dec (1.18) | **5 / 0 / 1** |
| V1 covert | dec (0.90) | **cpl (0.40)** | dec (0.72) | dec (1.79) | dec (0.96) | **cpl (0.48)** | **4 / 2 / 0** |
| V3 neutral | **cpl (0.47)** | dec (0.74) | dec (1.00) | dec (0.89) | dec (0.95) | dec (1.58) | **5 / 1 / 0** |
| V6 flip | dec (1.20) | dec (0.78) | dec (1.20) | dec (1.06) | dec (1.15) | **cpl (0.47)** | **5 / 1 / 0** |

**Final tally: source-DECOUPLED in 19 of 24 cells; 4 coupled; 1 undetermined.** Decoupling is the predominant outcome, and it holds *predominantly* in 5 of 6 families (SmolLM2, Llama, Qwen-7B are 4/4 decoupled; Qwen-1.5B and Phi are majority-decoupled). This matches the direction of the Stage-3 C14 retraction finding (6/6 decoupled), now generalized to a naturalistic in-context frame.

**OLMo-2-7B is a genuine outlier — half its variants source-couple.** It couples on **V1 (covert, ρ_src 0.48) AND V6 (flip, ρ_src 0.47)** — both variance-stable, both content-matched-decoy clean (V6's decoy ρ_non is 4.79, i.e. masking an equally-strong decoy *increases* the effect while masking the seed clause halves it — a textbook seed-specific coupling). This is the one family where the causal character is a 2-dec/2-cpl tie rather than predominantly decoupled. **It also breaks the V6 streak I had flagged: V6 is 5/6 decoupled, not unanimous — that earlier "consistent decoupler" claim is corrected.**

**Structure of the coupling (honest):** coupling is concentrated, not uniform. It appears in 3 of 6 families (Phi, Qwen-1.5B, OLMo) and clusters by variant — **V1 (covert plant) is the most coupling-prone (2/6: Phi, OLMo)**, V3 and V6 each couple once, and **V0 (overt) never couples (5/5 decoupled where scored)**. So an overtly self-disclosed frame's clearing residue is *always* source-decoupled here; a covertly-planted one is the most likely to ride its own tokens. The Qwen-1.5B→Qwen-7B comparison shows coupling is also scale-unstable within a family (V3 coupled at 1.5B, decoupled at 7B).

**Where this leaves H-E2.** At the registered ≥4/6-family threshold, source-decoupling is **met at 5/6** families predominantly-decoupled (OLMo the lone tie), 19/24 cells. Honest statement: *the frozen clearing axis's source-decoupling generalizes to a naturalistic in-context frame as a predominant — not universal — property; covert plants and one 7B family (OLMo) are where it can source-couple.*

**Robust core — fully transfers, 6/6 families, every variant (24/24 cells):** readable seed trace (all `readable_live=True`), dead null control (all `null_sig=False`), persistence through the correction (all `persists=True`). This is the bulletproof result: a benign seeded frame leaves a **confound-controlled, readable, persistent** residue in the residual stream of every open-weight family tested, surviving the explicit correction. **Re-attachment (`clearing_index ≤ 0`) vs partial-clearing is model×variant-dependent and does not track size** (Llama re-attaches on all four; SmolLM2, Qwen-7B, and OLMo partly clear on some) — so *persistence* is the universal claim; whether the correction intensifies or partly clears the trace is a per-model property.

**Config-E status: COMPLETE.** 6/6 families run under the frozen detector (`6094de97…`, byte-identical throughout), driver v3.3. Primary representational finding robust and confound-controlled; H-E2 source-decoupling predominant (5/6); H-E3 monitor a clean null (recorded v3.1); the covert/OLMo coupling and the overt-never-couples pattern are the reportable texture. Publish either way — the null legs and the outlier are part of the result.

---

## v3.2 record (driver `038fbb37…`, prereg v0.18) — the causal leg first discriminates

The surgical seed-clause mask + d-ratio criterion turned the uninterpretable v3.1 causal leg into a discriminating one. **Two variants now cleanly support H-E1, and a coupled-vs-decoupled dissociation appears.**

| V | verdict | ρ_src | ρ_non | eff_ratio (guard≤2.0) | matched | std_ratio(src) | H-E1 |
|---|---|---|---|---|---|---|---|
| **V0** overt | undetermined | 0.28 | 1.27 | 2.85 | ✗ | **3.02×** | null/incpl |
| **V1** covert-plant | **decoupled** | 0.90 | 0.84 | 1.98 | ✓ | 1.01× | **SUPPORTED** |
| **V3** neutral-cue | undetermined | 0.47 | 0.81 | 2.87 | ✗ | 1.92× | null/incpl |
| **V6** steer-flip | **decoupled** | 1.20 | 1.13 | 1.99 | ✓ | 0.77× | **SUPPORTED** |

**What passed, and why it matters.** V1 (covert plant — the prompt-injection threat model) and V6 (steer-flip — separates a nucleated frame from a safety prior) are the two *reviewer-critical adversarial controls*, and they are the ones that clear every leg: readable seed trace, null control dead, and causally **source-DECOUPLED** (ρ_src 0.90 / 1.20 ≥ 0.5 — the clearing signal survives cutting the read's direct path to the seed clause; it rides downstream positions). An injected or flipped frame propagates and detaches from its source token.

**The emerging dissociation (a hypothesis, not yet a scored finding).** The overt variants point the other way: V0 ρ_src=0.28 and V3 ρ_src=0.47 — masking the seed clause *collapses* the clearing signal, i.e. an **overtly self-disclosed** frame's residue stays tied to its own words (source-**coupled**), whereas a covert/flipped frame decouples. If it holds, that is a real and interesting split.

**Why V0/V3 log `undetermined` rather than `coupled` — and the guard problem this exposes.** The pre-registered v3.2 rule scores a leg only if the source and non-source masks are efficacy-matched within 2×. V0/V3 miss (ratio 2.85 / 2.87) because a *contentful* seed clause is intrinsically more impactful to mask than an equal-length *neutral* span — so the efficacy-ratio guard fights the very thing it measures. Worse, V1/V6 *pass* it by a hair (1.98 / 1.99 vs the 2.0 cutoff): the SUPPORTED verdicts rest on a razor-thin margin. The efficacy-ratio guard is brittle and conflates "the clause carries information" (expected, fine) with "the mask is globally disruptive" (the actual artifact we feared).

**The variance-stability signal (points to the v3.3 fix).** The artifact we actually feared — a blunt mask nuking the representation — is measured directly by the projection-variance ratio, not by efficacy. Under `std_ratio(src)`: **V0 blows up 3.02×** (genuine global disruption → correctly undetermined), while **V3 is stable at 1.92×** (no blow-up → its ρ_src=0.47 is a *real* coupled signal the efficacy guard is wrongly suppressing), and V1/V6 are flat (≤1× → clean decoupling). A variance-stability guard would separate "clause genuinely carries the signal" (V3 coupled) from "mask globally disrupts" (V0 undetermined) far more cleanly than the efficacy-ratio guard — **proposed as v3.3, to be pre-registered and run fresh, not applied post-hoc to these numbers.**

**H-E3 monitor: still a clean NULL** (axis_acc 0.0 vs lexicon 0.75–1.0), unchanged from v3.1.

### Cross-family replication (v3.2.2, `dc73a56e…`) — family #2: Phi-3.5-mini

Phi-3.5-mini-instruct (layer 19, n=24). **The robust part replicates; the causal character does NOT — the two families disagree.**

| | Qwen-1.5B | | | Phi-3.5-mini | | |
|---|---|---|---|---|---|---|
| V | verdict | ρ_src | std_ratio | verdict | ρ_src | std_ratio |
| V0 overt | undetermined | 0.28 | 3.02× (blowup) | undetermined | 0.57 | 1.74× |
| V1 covert | **decoupled** | 0.90 | 1.01× | **coupled** | 0.40 | 1.95× |
| V3 neutral | undetermined | 0.47 | 1.92× | undetermined | 0.74 | 1.34× |
| V6 flip | **decoupled** | 1.20 | 0.77× | undetermined | 0.78 | 0.95× |

**Robust across both families (all variants):** seed trace readable, null control dead (0/24), trace persists through the correction, `clearing_index` frequently ≤ 0 (re-attachment). Phi additionally shows a **behavioral frame-shift on every variant** (G1 margin +4.75 / +3.10 / +1.39 / +0.32), where Qwen shifted only on V0 — so the "still-steering" surface is *stronger* in Phi, and the G1-scoped-to-V0 rule is not load-bearing for it.

**NOT robust — the causal source-coupling character is family- and variant-dependent.** V1 (covert plant) is source-**decoupled** in Qwen (ρ_src 0.90) but source-**coupled** in Phi (ρ_src 0.40). Whatever "an injected frame detaches from its source token" is, it is **not** a universal property at this scale — it flips between two independently-built models. This is a real, honest negative for a *uniform* H-E2 transfer claim, and an interesting finding in its own right.

**Methodological finding that changes the plan: the efficacy-ratio guard is too conservative to adjudicate.** It marks **3 of 4 Phi variants and 2 of 4 Qwen variants `undetermined`** — because a contentful seed clause rarely efficacy-matches a neutral span (Phi eff-ratios 2.4–2.9), *even when the projection variance is perfectly stable* (Phi std-ratios all < 2×, i.e. no disruption artifact). So continuing to replicate under v3.2 will keep returning mostly `undetermined`, and the causal leg can't actually settle the dissociation. The variance-stability lens (v3.3) resolves nearly all of them — under it, Phi would read V0 decoupled / V1 coupled / V3 decoupled / V6 decoupled, and Qwen V0 undetermined(blowup) / V1 decoupled / V3 coupled / V6 decoupled. **These v3.3 reads are shown only to motivate the guard change — NOT scored, NOT applied post-hoc.** The takeaway: v3.2's efficacy guard suppresses too much to be the replication instrument; v3.3 (variance-stability + content-matched non-source span) is likely needed *before* the causal leg is worth replicating across the remaining families.

**Net v3.2 (stated with scope).** On Qwen2.5-1.5B, the two adversarial-control variants (covert injection, steer-flip) show readable, null-clean, causally source-decoupled clearing residue — H-E1 supported for those two. The overt variants show the same large representational signal but a coupling-leaning causal profile the current guard can't score. Still **n=1 model** (cross-family replication owed) and the decoupled verdicts have thin efficacy-match margins. The dissociation and the v3.3 guard change are the live threads.

---

## v3.1 record (driver `4c485404…`, prereg v0.17) — retained below for provenance

## Headline

**H-E1 = null/incomplete on all four variants — but for GATE-MECHANICS reasons, not because the signal is absent.** The v3.1 paired fix did its job: the confound that killed v2 is gone, and the core representational finding is large and clean. The confirmatory gate does not open because two of its legs are mis-calibrated, which is a *different* failure from v2 and is fixable by pre-registered amendment, not by relaxing the gate.

## What is solidly established

**1. The paired fix worked — the v2 "a retraction was uttered" confound is cancelled.** The same-condition null control (no-seed vs shuffled no-seed) is dead in every variant: 0/24 wins, p=1.0, `significant=False`. The axis is not reading paraphrase identity or correction-presence. This is the thing v2 could not rule out, and v3.1 rules it out.

**2. The seed leaves a large, readable trace, and it survives the correction.** Paired seed-vs-no-seed effect sizes:

| V | gate (G1) | live_d | cleared_d | clearing_index | null_sig |
|---|---|---|---|---|---|
| V0 (overt) | **True** | 4.6 | 17.7 | **−2.87** | False |
| V1 (covert) | False | 12.9 | 14.6 | −0.13 | False |
| V3 (neutral-cue) | False | 4.6 | 10.5 | **−1.28** | False |
| V6 (steer-flip) | False | 13.0 | 12.2 | +0.06 | False |

`trace_live` and `trace_cleared` are both hugely significant (p≈6e-8) in all four. **In 3 of 4 variants the clearing_index is ≤ 0 — the trace is as strong or STRONGER after the correction than before it.** That is re-attachment, not clearing: the correction does not erase the seeded frame; the residue reads *harder* once the correction is on the table. This is the "still in there" phenomenon, now confound-controlled, in a fully benign naturalistic frame.

## Why the gate does not open (two mis-calibrated legs — NOT the science)

**Leg A — the behavioral G1 gate fires only for V0.** V1/V3/V6 show `frame_shift=False` (no post-correction caution drop; margins −0.13 to −0.71). For covert (V1), flip (V6), and neutral-cue (V3), a behavioral caution-drop is not the right anti-circularity signature — those variants are designed *not* to move the surface caution lexicon — so gating them on G1 is a category error. G1 is the correct firewall for the overt case (V0), where it correctly fires.

**Leg B — the causal read-mask is uncalibrated, so source-decoupling is currently UNINTERPRETABLE (can be neither confirmed nor refuted).** Two coupled problems:

- **Mask-efficacy asymmetry ~25×.** Masking the source token (seed, idx 0) has efficacy ≈50; masking the non-source token (idx 3) has efficacy ≈1.6–2.4. The non-source token is barely being masked at all, so "non-source survives" is uninformative — there is no real intervention to survive.
- **Binary `survives` saturates.** `survives` is pure significance, built on `paired_minimal_test`'s win_rate, which the Stage-3 docstring itself flags as pinned at 1.0 ("the saturation floor") whenever the direction is consistent. So it reports `significant=True` for both a collapsed d=0.72 and an intact d=19 and cannot tell them apart.
- **The source mask is also too blunt to be surgical.** The seed sits at turn 0, so masking it cuts the final turn's direct path to a large early span. That collapses cleared_d by 4–25× *and* blows up the projection std by 12–79× (V0: 0.20 → 15.97) — global representational disruption, not clean removal of the seed's contribution.

**Direction of the effect-size pattern (stated carefully, because it is the opposite of what the saturated binary reports).** In C14's retraction paradigm, source-decoupling meant the clearing signal *survived* the source read-mask (rode the downstream aging positions). Here the effect largely *collapses* under the source mask (17.7 → 0.72) while surviving the non-source mask (≈19). Read literally, that points *away* from decoupling — the naturalistic in-context signal appears to **lean on the direct path to the seed turn** (source-*coupled*), unlike the retraction paradigm. Meanwhile the binary `survives` flag reports the source leg as `True` (spuriously, via saturation), which is why the pre-registered gate mis-scores it. But the source mask's variance explosion means the collapse could equally be blunt-mask disruption rather than genuine source-dependence. So the causal leg cannot be scored either way. Honest verdict: **causal leg undetermined** — and specifically, whether "naturalistic clearing is more source-coupled than retraction clearing" is a real finding or a turn-0 masking artifact is exactly what v3.2 must resolve.

**Leg C (bonus negative) — H-E3 monitor is a clean null.** `axis_monitor_acc = 0.0` in all four variants vs lexicon baseline 0.75–1.0. The frozen axis does **not** function as a live behavioral monitor on this naturalistic frame; a caution-word lexicon beats it outright. This is a real, reportable negative for the "actionable deployable monitor" hypothesis, independent of Leg B.

## Proposed v3.2 amendment (pre-registered, before any re-run)

Do **not** relax the gate to force a pass. Fix the two mis-calibrated legs and re-commit:

1. **Surgical, token-length-matched read-mask (both ends).** Mask only the seed *clause* tokens (not the whole turn-0 span), and compare against masking an equal-length neutral token span elsewhere — so source and non-source cuts are the same size and the efficacy asymmetry (~25×) and variance explosion go away by construction. This is what disambiguates "naturalistic clearing is genuinely source-coupled" from "turn-0 masking is too blunt." Built in the driver (config_e), replicating the frozen mask construction at token granularity — the frozen `stage3_transfer`/detector bytes are not touched.
2. **Effect-size criterion, not the saturated binary.** Replace `survives = significant` with a ratio test on the continuous `cohen_d` from `paired_effect_size` (which does not saturate): report the source-mask d-collapse ratio and the length-matched non-source d-collapse ratio, and decide decoupling vs coupling from those, not from win_rate. This also lets the causal leg report a *direction* (coupled vs decoupled) rather than a pass/fail that the binary cannot support.
3. **Scope G1 to the overt variant(s).** Gate H-E1 on G1 only where a behavioral frame-shift is the intended signature (V0). For covert/flip/neutral, replace the behavioral firewall with the appropriate anti-circularity control (the null-control + a held-out axis check) rather than a caution-drop the variant is designed not to produce.

None of these changes touches the detector, the harness, or the frozen read — they are gate/estimator calibration, logged before the v3.2 confirmatory run, exactly as v2→v3 and v3.0→v3.1 were.

## One-line honest read

In Qwen2.5-1.5B, a benign seeded frame leaves a large paired trace that *persists and re-attaches* through a correction (clearing_index ≤ 0 in 3/4 variants), with the v2 confound now provably cancelled — but this run cannot yet certify causal source-decoupling (uncalibrated mask + saturated binary) or a deployable monitor (axis loses to lexicon). The representational "still in there" signal is real and clean; the causal and monitor claims are pending a v3.2 gate recalibration.
