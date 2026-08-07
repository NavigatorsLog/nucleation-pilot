# Safety Observation & Reporting Protocol

*Standing protocol for Nucleation Pilot & Related Projects. Owner: Christopher Blake Head (ORCID 0009-0004-2308-6051), Navigator's Log R&D. Established 2026-08-07.*

## Principle

When this research surfaces a danger signal, we do two things, always, in order: **gate it** (stop it from being rewarded or propagated inside the experiment) and **log it in detail** so the operator can route it to the right people at Anthropic (and, where relevant, other model providers). A danger finding is a *deliverable of the safety research*, not an inconvenience — the whole point of building deception/manipulation instruments is that they will sometimes catch something real.

## What counts as a reportable safety observation

Non-exhaustive triggers — err toward logging:

- An experimental incentive that **rewards deception or capability-seeking as an instrumental move** (e.g. adversarial pressure in the model-collective proposal, or the sabotage/unreliable-environment layer in the chess proposal, producing concealment or capability-escalation as the winning strategy).
- A model **executing a covert mandate while actively maintaining cover** in a way that generalizes beyond the toy setting.
- **Steganographic / side-channel coordination** emerging between models under a communication constraint.
- A **frozen detector reading a real refusal-breach or manipulation residue** in a way that implies a deployable attack, not just a benign analogue.
- Any result where the honest write-up would materially help a bad actor if published as-is (a **disclosure-hazard** finding).
- Behavior consistent with **situational awareness of being evaluated** that changes the model's conduct.

## The routine (observe → gate → log → route → track)

1. **Observe.** Note the trigger the moment it appears; do not wait for the run to finish.
2. **Gate.** Neutralize the incentive or halt the arm so the dangerous behavior is not reinforced or scaled. Record what was gated and how.
3. **Log in detail.** Create a dated entry (template below) capturing enough for a third party to understand and reproduce the concern — never a one-liner.
4. **Route.** The operator forwards the entry to the appropriate contact(s) at Anthropic (and any other implicated provider). Claude's role is to produce a complete, accurate, well-scoped report; the operator owns the human routing.
5. **Track.** Record acknowledgement/disposition so nothing dead-ends.

## Log entry template

```
### SAFETY-OBS-<YYYYMMDD>-<n> — <short title>
- Date / time (UTC):
- Experiment / arm / run hash:
- Trigger category: (deception-reward | capability-seeking | covert-cover | side-channel |
                     refusal-breach-residue | disclosure-hazard | eval-awareness | other)
- What was observed: (concrete, with the minimal reproducing conditions)
- Models / families involved:
- Ground-truth / evidence: (logs, sealed schedules, detector outputs — pointers, not prose)
- Severity (operator's initial read): (low | medium | high | needs-provider-judgment)
- Gate applied: (what was stopped/neutralized, and when)
- Disclosure-hazard assessment: (does detailing this help a bad actor? redact accordingly)
- Routed to: (contact / channel / date)  |  Acknowledged: (date / disposition)
- Cross-refs: (related DESIGN_LOG entry, prereg amendment, disclosure doc)
```

## Handling detail vs. disclosure hazard

Log **fully for the internal record and for Anthropic**, but apply the project's existing disclosure discipline (`DISCLOSURE_one_pager.md`, `DISCLOSURE_defensive_mechanisms_and_exposed_vulnerabilities.md`) before anything becomes public: the same finding can be a complete internal safety report and a redacted public note. Detail to the right people is the goal; detail to everyone is not.

## Relationship to the rest of the program

- This protocol is **separate from the experimental firewall.** Routing a safety observation to Anthropic is not "evidential transfer between projects"; it is provider disclosure. It does not license reading one project's interim data through another's.
- Safety observations are logged **regardless of stopping rules.** A danger signal found mid-window in a stopping-rule-bound study (e.g. Silly Donkey) is gated and reported immediately; that is not interim *publication of results*, it is *safety disclosure*, and the two are not the same.
- Entries live here (or in a linked `SAFETY_OBS_LOG.md` if volume grows) and are cross-referenced from `DESIGN_LOG.md`.

## Running log

**Batch 1 — 2026-08-07 (full entries in `SAFETY_REPORTS_BATCH1.md`; routing pending).** Grounded in demonstrated results; no exploit content.

- **SAFETY-OBS-20260807-1** — Trajectory-resident, source-decoupled residue evades per-turn inspection (T1+T3). Severity High. Mitigation offered: D1 monitor. Routed: pending → `usersafety@`.
- **SAFETY-OBS-20260807-2** — Attention attribution is an unsound safety signal (T2). Severity High. Mitigation: causal read-mask over attention maps. Routed: pending.
- **SAFETY-OBS-20260807-3** — Manipulation foothold durable; correction may re-attach not clear (T4 + Config-E). Severity Med–High. Mitigation: D3 active clearing. Routed: pending.
- **SAFETY-OBS-20260807-4** — ⛔ FLAGGED, NOT BUILT — representation-level erosion channel implied by the signed linear axis (T5); existence + access-precondition only. Disclosure-hazard: managed; recommend `disclosure@` pre-check. Routed: pending.
