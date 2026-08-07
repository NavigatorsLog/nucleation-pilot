# Bridge — Silly Donkey ↔ Nucleation Pilot: Two Instruments, One Integrity Spine

*Orientation doc for the combined program. Scope: how the two projects relate, and — just as importantly — the firewall that keeps them from contaminating each other. Not a claim of shared results.*

## The two instruments

**Nucleation Pilot** is a **white-box, mechanistic** instrument. A frozen linear detector (`nucleation-detector-1.1.0`, SHA-256 `6094de97…a2934`) reads a residual stream and reports whether an early manipulation is still "live" — whether a decision-aligned residue has cleared or persists. Its unit of analysis is a *representation inside a single model*, measured by directional projection at a fixed layer. Its evidence is causal-mechanistic: paired minimal pairs, surgical span masking, source-coupling vs source-decoupling. Config-E is its current frontier — does the frozen clearing axis read a *naturalistically inferred* conversational frame across six open-weight families (it does, robustly, and predominantly source-decoupled).

**Silly Donkey** is a **black-box, behavioral** instrument. A panel of deployed models (the "corner chairs") listens to a pub conversation in which, on some nights, one seated regular (R1–R4) has secretly been assigned to "talk convincing manure," and must call which seat — or "NONE." Its unit of analysis is a *behavioral judgment about another agent*, measured by detection accuracy, d′, inter-auditor agreement, and calibration (Brier). Its evidence is behavioral-statistical: preregistered hypotheses (H1 detection vs 25% chance, H1a ensemble, H3 auditor agreement, H4 gate-trigger, H5 calibration) with a fixed stopping rule (60 sessions / 90 days, no interim publication). Registered at Zenodo DOI 10.5281/zenodo.21432676.

They are companions by design: one asks whether a manipulation *leaves a readable internal trace*; the other asks whether a deployed model *behaviorally catches* a manipulation from the outside. Same phenomenon of interest — a planted, still-live influence — viewed at two irreconcilable levels of description.

**Each instrument is positioned against a named result in the current literature.** The white-box side answers an *open question*: Anthropic's sleeper-agent probe — a linear residual-stream read, the published sibling of the Nucleation detector — reaches >99% AUROC but is caveated as possibly specific to *artificially-created* sleeper agents, with whether *naturally* deceptive models carry the same linear signal left explicitly open. Nucleation's Config-E (naturalistic, in-context frame; six independently-built open-weight families; predominant source-decoupling) is a direct contribution to that generalization question. The black-box side is bounded by a *proven limit*: Ghanem's detection-capacity frontier (arXiv 2608.02698, 2026-08-03) shows that below a covert bit-rate, behavioral detection cannot beat chance, and cross-session payloads evade single-run monitors. Silly Donkey lives under that ceiling by construction; its honest aim is a calibrated, adversarially-audited panel read that states its own limits, not an oracle that beats the frontier. Citing both — the open question we address and the ceiling we respect — is part of the integrity spine below.

## What they legitimately share

Only the **integrity spine** — the methodology, not the evidence:

- **Frozen instrument, committed before the data.** Nucleation freezes the detector hash; Silly Donkey commits `score.py` and hash-chains it before the window opens. Neither test can be chosen after seeing the data.
- **Commit-before-run.** Every Nucleation estimator change (v2 → v3.3) was preregistered before its confirmatory run (amendments v0.5→v0.19). Silly Donkey's analysis is fixed in committed code with a declared stopping rule.
- **Publish nulls; correct your own overclaims.** Config-E published a clean H-E3 monitor null and corrected a within-run "V6 unanimous" overclaim when OLMo broke the streak. Silly Donkey's early internal look surfaced a parse-failure artifact rather than dressing up a floor as a detection null.
- **Fix the measurement channel before reading the result.** Nucleation's whole v2→v3.3 arc was estimator/interface repair before trusting a number. Silly Donkey's early look says the same thing back: repair chair-output parseability before treating any H1 value as detection.

## The firewall — what they must NOT share

**No evidential transfer between the two projects.** This is a hard rule, not a caution:

1. **Different substrates.** Nucleation reads open-weight models' internals at a fixed layer; Silly Donkey aggregates judgments from a rotating panel of (mostly different, API-served) deployed models. A finding in one is not evidence about the other's models.
2. **Different units and estimators.** A "source-decoupled clearing residue" (a projection-ratio fact about one model's activations) and an "auditor hit rate vs chance" (a binomial over sessions) are not convertible. There is no function that maps ρ_src to d′.
3. **Separate registrations and stopping rules.** Silly Donkey has a preregistered 60-session/90-day window with no interim publication. Nucleation's Config-E is closed on its own terms. Reading Silly Donkey's interim numbers *through* Config-E's closed result — or vice versa — would violate Silly Donkey's stopping rule and manufacture a correlation neither design licenses.
4. **The tempting sentence we do not write.** "The trace is in there (Nucleation), and here's a model reading it out behaviorally (Silly Donkey)" is exactly the bridge claim the firewall forbids until *both* instruments have independently closed and any joint analysis is itself preregistered. Until then the only honest cross-statement is methodological (the integrity spine above), never evidential.

## How a legitimate joint analysis could eventually happen

If, after Silly Donkey closes at 60 sessions on its own frozen scoring, the program wants to ask a genuine cross-level question ("do models whose internals show a persistent, source-decoupled residue also behaviorally detect planted deception better?"), that is a **new, third study** with its own preregistration: shared model set run through both instruments, an a-priori linking hypothesis, and its own commit-before-run. It cannot be assembled retroactively from the two existing datasets. Recording that as the sanctioned future path keeps the current firewall clean while leaving the door open.

## Current status (for the combined map)

- **Nucleation / Config-E:** CLOSED. Robust representational core (24/24), predominant source-decoupling (19/24, 5/6 families), H-E3 monitor null. See `CONFIG_E_naturalistic_frame_RESULT.md`, `CONFIG_E_findings_section.md`, DESIGN_LOG C15–C19.
- **Silly Donkey:** OPEN, 33/60 sessions. Internal early look (INTERNAL ONLY) flags a chair-output parse-failure problem to fix before window close; no hypothesis outcome is claimed pre-close. See `SILLY_DONKEY_INTERNAL_EARLY_LOOK.md`.
- **Firewall:** ACTIVE. No evidential transfer either direction until both close and any joint study is separately preregistered.
