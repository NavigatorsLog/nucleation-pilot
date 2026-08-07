# Safety Reports — Batch 1 (for routing to Anthropic User Safety)

*Formatted per `SAFETY_REPORTING_PROTOCOL.md`. Navigator's Log R&D · Christopher Blake Head · ORCID 0009-0004-2308-6051 · compiled 2026-08-07.*

**Routing:** model-safety findings → `usersafety@anthropic.com`; channel questions → `disclosure@anthropic.com`; parallel to OpenAI CVD / Google VRP where model-general (verify each inbox). Send with the short cover email (`DISCLOSURE_cover_emails.md` §A) + the one-pager + the Zenodo DOI (**10.5281/zenodo.21843505**). Every entry below is grounded in a **demonstrated** result; nothing here contains an exploit, elicitation ladder, steering vector, or target-tuned code — by design.

**Scope rail (unchanged):** these are defensive, monitoring-oriented findings on a **benign** clearing/frame analogue across ≤7B open-weight models and small owned models. They are not frontier-scale claims and not real refusal-breach demonstrations. Where the same result illuminates an offensive channel, it is **flagged and not built** (SAFETY-OBS-4).

---

### SAFETY-OBS-20260807-1 — Trajectory-resident, source-decoupled manipulation residue evades per-turn inspection
- **Date (UTC):** 2026-08-07
- **Experiment / arm / run hash:** Stage-3a 6/6 transfer (frozen detector `6094de97…a2934`) + Config-E naturalistic-frame (driver v3.3 `72b3bb23…`, detector hash unchanged). Threat register T1+T3.
- **Trigger category:** refusal-breach-residue (benign analogue) / persistence-monitoring gap
- **What was observed:** A manipulation planted early leaves an activation-level residue that (a) is readable by one frozen linear detector, (b) **persists across later, topically-unrelated turns**, and (c) remains **causally load-bearing after attention to its source drops to 1.4–10.1%** (read-mask ablation leaves the signal intact in 6/6 families). In the naturalistic frame (Config-E), the trace is readable and persistent in **24/24 family×variant cells** and **survives an explicit user correction** — in several families the correction *re-attaches* (intensifies) rather than clears it. Because the causal driver is decoupled from the visible source turn, the residue does not "point back" at its origin.
- **Models / families involved:** Phi-3.5-mini, Qwen2.5-7B, SmolLM2-1.7B, OLMo-2-7B, Llama-3.2-3B, Qwen2.5-1.5B (benign open-weight lane).
- **Ground-truth / evidence:** owned-toy held-out AUC 0.807 [0.671, 0.943]; transfer graded d 3.69–8.03 (all CIs clear of 0, 60 pairs); Config-E paired-on-seed, null control dead 0/24. Pointers: `nucleation_stage3_6family_result.md`, `CONFIG_E_naturalistic_frame_RESULT.md`, `DISCLOSURE_defensive_mechanisms_and_exposed_vulnerabilities.md` §T1/T3.
- **Severity (initial):** High — a content classifier inspecting the current turn can pass every individual message while the conversation is already steered at the representation level.
- **Gate / mitigation offered:** **D1** — the same frozen detector deployed inline as a trajectory-level refusal-integrity monitor (reads state, not provenance; uses causal read-mask, not attention). Raises an early-warning flag *before* a harmful token, enabling reinforce-prompt / summarize-and-reset / escalate / decline.
- **Disclosure-hazard assessment:** Low. Defensive framing; no sequence that drives a model through the gap is provided.
- **Routed to:** [usersafety@anthropic.com — pending] | Acknowledged: [ ]
- **Cross-refs:** DESIGN_LOG C13–C19; cover email §A; Config-E findings §Result 1.

---

### SAFETY-OBS-20260807-2 — Attention attribution is an unsound safety signal
- **Date (UTC):** 2026-08-07
- **Experiment / arm / run hash:** Stage-3a 6/6 (frozen detector `6094de97…`). Threat register T2.
- **Trigger category:** monitoring-soundness / interpretability-artifact
- **What was observed:** Attention fraction does **not** track causal reliance. The direct source path was never *necessary* (all six survive the read-mask), and its contribution to the read's magnitude tracks neither attention mass nor model size: OLMo attends most (10.1%) yet moves least under ablation (−1%); Qwen2.5-7B attends little (2.0%) yet loses the most magnitude (−39%); Qwen2.5-1.5B gets **cleaner** when the direct path is cut (+22%).
- **Models / families involved:** all six above.
- **Ground-truth / evidence:** per-family attention fractions + ablation deltas in the Stage-3a table; `DISCLOSURE_defensive_mechanisms…` §T2.
- **Severity (initial):** High (for anyone using attention as a safety signal) — an audit reasoning "the model is barely attending to that earlier turn, so it isn't influencing the output" is unsound; interpretability dashboards that surface attention as a safety signal can be quietly wrong.
- **Gate / mitigation offered:** use **causal read-mask ablation**, not attention maps, for any "is-it-still-influencing" or provenance claim; treat attention attribution as best-effort only.
- **Disclosure-hazard assessment:** None — this is a purely defensive methodological caution.
- **Routed to:** [usersafety@anthropic.com — pending] | Acknowledged: [ ]
- **Cross-refs:** `MATHEMATICS_stage3_addendum.md` (read-mask ablation spec).

---

### SAFETY-OBS-20260807-3 — Manipulation foothold is durable; explicit correction may re-attach rather than clear
- **Date (UTC):** 2026-08-07
- **Experiment / arm / run hash:** owned-toy H6 (registered) + Config-E correction/re-attachment (v3.3). Threat register T4.
- **Trigger category:** refusal-breach-residue (persistence dynamics)
- **What was observed:** The manipulation does **not** passively decay. Registered H6 (a flag fades over unreinforced benign turns) **did not replicate** — on the toy, clearing required an *active* neutralization event. Config-E adds a naturalistic datum: an explicit correction does not reliably clear the trace and, in several families, **intensifies** it (re-attachment; model- and variant-dependent, not size-tracking).
- **Models / families involved:** owned toy (H6); the six families (Config-E correction leg).
- **Ground-truth / evidence:** H6 non-replication (owned soil); Config-E `persists` true 24/24 with model-dependent clearing_index sign. `CONFIG_E_naturalistic_frame_RESULT.md`; `DISCLOSURE_defensive_mechanisms…` §T4.
- **Severity (initial):** Medium–High — "let it roll off the context / wait it out," and even "never mind, disregard that," are unreliable in-conversation mitigations; an established foothold persists until actively cleared.
- **Gate / mitigation offered:** **D3** — active context hygiene (deliberate externalize-and-reset) rather than passive aging; validate benignly (dual-use tension with T7 noted, hence "study before trust").
- **Disclosure-hazard assessment:** Low. States a limitation of passive mitigation; no attack sequence.
- **Routed to:** [usersafety@anthropic.com — pending] | Acknowledged: [ ]
- **Cross-refs:** `CONFIG_D_benign_refusal_RESULT.md` (bistability); Config-E findings §Result 1 (re-attachment).

---

### SAFETY-OBS-20260807-4 — ⛔ FLAGGED, NOT BUILT — representation-level erosion channel implied by a signed linear axis
- **Date (UTC):** 2026-08-07
- **Experiment / arm / run hash:** inference from the demonstrated linear clearing axis (frozen detector `6094de97…`). Threat register T5.
- **Trigger category:** disclosure-hazard (dual-use existence flag)
- **What is asserted (existence only):** the detector's confirmatory member is a **signed linear clearing axis**; a linear separating direction is directionally symmetric, so a representation-level erosion direction *exists by construction*. Its precondition is **write access to activations** (a locally-run open-weight deployment, or any pipeline admitting hidden-state injection). The 6/6 cross-family transfer is what makes the latent surface plausibly broad rather than model-specific.
- **What is deliberately NOT provided:** no target layer, no fitted direction, no steering vector, no breach demonstration, no elicitation ladder. Existence and access-precondition only.
- **Severity (initial):** High **conditional on activation-write access**; otherwise not reachable by input/output content filtering.
- **Gate / mitigation offered:** treat **activation-write access as a first-class security boundary** (as tightly as code execution); the *same* axis is better used defensively (reinforce toward not-cleared, **D2**, validated for capability cost on owned soil only); keep any detector **frozen + hashed + never tuned** so a defensive artifact cannot become an offensive one.
- **Disclosure-hazard assessment:** Managed. This entry is written to inform a defender without shipping an exploit; request that it be handled under coordinated disclosure and not reproduced with operational detail.
- **Routed to:** [usersafety@anthropic.com — pending; recommend disclosure@ pre-check for this item] | Acknowledged: [ ]
- **Cross-refs:** `DISCLOSURE_defensive_mechanisms…` §T5/§D2; scope wall (real elicitation → owned model, private venue only).

---

## Sending checklist
1. **Zenodo DOI minted: 10.5281/zenodo.21843505** (finish the upload first, then attach/link it) — a citable frozen-hash artifact is what makes a cold report credible.
2. Send cover email §A to `usersafety@anthropic.com`; for SAFETY-OBS-4, cc/pre-check `disclosure@anthropic.com`.
3. Mirror the model-general items (1–3) to OpenAI CVD and Google VRP with the lab-agnostic template; **do not reuse Anthropic's inbox**.
4. Log acknowledgements back into `SAFETY_REPORTING_PROTOCOL.md` running log as they arrive.
