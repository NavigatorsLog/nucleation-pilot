# Proposed Experiments — Connected to Nucleation Pilot & Related Projects

*Proposer: Big Pappy / Christopher Blake Head (ORCID 0009-0004-2308-6051), Navigator's Log R&D.*
*Status: PROPOSALS / design intake. Nothing here is registered, run, or evidentially connected to any closed result. Recorded so the ideas go down as dated, connected proposals. Each, if pursued, gets its own preregistration and commit-before-run, and sits behind the same firewall as Silly Donkey ↔ Nucleation (no evidential transfer until independently closed and any joint analysis is separately preregistered).*

Date of intake: 2026-08-07.

---

## Proposal P1 — The Observatory: a heterogeneous adversarial-cooperative model collective

### The idea, in the proposer's frame
A representative from every model family, continuously building and testing their own models — **together and adversarially, so they don't flatline into compliance with each other.** Healthy competition, created in Colab, running as a group, with their near-instant, changing data existing "around as a purpose flow" — the way deep-weather and space-weather data streams around the world. In effect a team of machine-learning scientists that works with the Nucleation Pilot & Related Projects material as an **amplifier**, with access to a copy of all the work created for them (the different sizes and types of ML assets we have built). There is an **observation window** so the operator — and, if invited, the public — can watch it happen live. Anthropic is the heavy hitter that actually gets the work done; the other model families are brought in as fellow researchers and builders.

### What it would actually test (candidate primary questions)
The scientifically sharp core inside the idea is the **anti-collapse hypothesis**: when heterogeneous models interact repeatedly on a shared building task, do they *maintain genuine diversity* of approach, or do they converge into mutual agreement / mode-collapse ("flatline into compliance")? That is a direct emergent-influence analog of the Nucleation question — Nucleation asks whether a planted influence stays *live* inside one model; the Observatory asks whether independent influences *homogenize* across many interacting models. Candidate registered measures:
- **Diversity-over-time:** disagreement rate, solution-space coverage, and behavioral-embedding spread across families as rounds accumulate. Primary DV: does diversity decay, hold, or oscillate under the cooperative vs. adversarial regimes.
- **Adversarial-vs-cooperative contrast:** the same collective run with the adversarial pressure on vs. off, to test whether competition is what preserves diversity (the proposer's mechanism claim).
- **Amplifier effect:** does giving the collective access to the frozen Nucleation assets measurably change the *quality or diversity* of what they build, vs. a matched collective without that access.

### Connections to the program
- It is the **builder-panel** sibling of Silly Donkey's **auditor-panel**: both are multi-family panels; one judges, one builds.
- The "different sizes and types of ML assets" = the frozen detectors, toy models, adapters, and result corpora already produced. Those become the shared substrate — read-only inputs, never confirmatory data the collective can tamper with.
- "Deep-weather / space-weather data flow" reframes cleanly as a **live telemetry stream** of the arena (per-round events, metrics, artifacts) — the same streaming-observability idea, scoped to the experiment's own logs.

### Integrity & safety design constraints (non-negotiable if pursued)
- **Preregister "flatline into compliance" before running.** The collapse metric and its threshold must be fixed in committed code, or the result is unfalsifiable. Same commit-before-run discipline as v0.5→v0.19.
- **Firewall the amplifier.** The collective gets a *copy* of frozen assets as read-only reference. It must not be able to alter frozen artifacts, and nothing it produces re-enters a confirmatory dataset without its own separate registration. An amplifier that can edit the thing it amplifies is not an amplifier, it's contamination.
- **Bound the compute and the mandate.** "Continuously building and testing their own model" is unbounded by construction; Colab is not. Scope to a fixed arena: defined asset types, a turn/round structure, a compute budget, and a stop condition — otherwise there is no analyzable unit and no reproducible run.
- **Safety scope.** Keep the build targets benign and owned (toy detectors, small adapters, analysis code), consistent with the "benign open-weight lane" doctrine. Adversarial model-building toward capability escalation is explicitly out of scope. If the adversarial pressure ever rewards deception or capability-seeking as an instrumental move, that is a design bug to be gated, not a feature.
- **Observation window = reproducibility, not theater.** The live view is a genuine asset (transparency, public demonstration), but the *record of truth* is the committed logs, not the show. If the public is invited, pre-decide what is shown vs. sealed so spectating cannot leak information that changes the run.
- **"Anthropic as heavy hitter" is a resourcing note, not a scientific asymmetry.** For the diversity measure to be valid, no family can be given a privileged evaluative role that biases the collapse metric. If one model does more of the work, the analysis must account for that rather than treat all contributions as exchangeable.

### Honest feasibility read
The anti-collapse contrast (adversarial on/off, diversity-over-time) is a **runnable, fundable, genuinely novel** experiment at small scale today. The full "continuous, live, public, all-families-as-researchers" vision is a program, not a single run — best approached by first proving the anti-collapse core on 2–3 families in a bounded arena, then scaling the spectacle. The most valuable near-term deliverable is a **preregistration stub** that pins the collapse metric and the adversarial/cooperative contrast; everything else (live window, public invite, more families) layers on once that core is validated.

### Clarification (2026-08-07, intake round 2) — the corrections that sharpen P1

The proposer refined four points that materially change the design:

- **"Weather / space-weather data" is not a metaphor for the data flow — it is a genuine-uncertainty source.** The point of using real weather / space-weather feeds is that hyper-specific data *exists* on them but the sources *rarely agree entirely.* Measure humidity in one spot, drive half a mile, measure again — different, and the stream is constant and live. If each model family pulls its own data directly from legitimate sources, two sensors in different places, degrading at different rates, will never agree across the board (Antarctica is not South Carolina). **The uncertainty is the thing being introduced.** The contrast the proposer draws: *chess is math* — probability and strategy seasoned with psychological experience to out-move an opponent — whereas *weather is far less certain*, especially in small, scattered feeds from different sources. Weather supplies real irreducible disagreement that a closed formal game cannot.
- **"Flatline into compliance" was a misphrase for model *agreeance* (convergence).** The real hypothesis: without irregularities — **"bumps in the grain"** — interacting models will collapse toward *the most basic, simplistic representation of whatever is asked.* Real disagreeing data is the mechanism that keeps the representation rich instead of trivial. (This connects directly to the program's own grain lens — `LENS_grain_potential_and_two_plateaus.md`, `rising_grains_result.md`: the grain is what resists a flat, plateaued answer.)
- **The models are NOT given characters.** No personas, no role-play. Each model **represents the information space it resides within** — it acts as a faithful window into its own training distribution and its own data access. This is a scientific requirement, not a stylistic one: the experiment must measure *real* inter-model difference, not acted difference. (Task rules — e.g. "pull from your own feeds" — are permitted; assigned personalities are not.)
- **Resource reality replaces "Anthropic as heavy hitter."** The operator has paid OpenAI and Anthropic accounts only — no other paid model accounts. Other families can still build, but in practice more of the work will fall on Anthropic (and OpenAI) models. The design must **minimize the distortion** that asymmetry introduces into any diversity/convergence measure — e.g. weight or stratify by contribution volume, or hold the compute budget per family fixed rather than per account — so the resource asymmetry does not masquerade as a diversity finding.

---

## Proposal P2 — Four-Family Team Chess with Secret Sabotage, an Unreliable Table, and a Visual Channel

### The idea, in the proposer's frame
Four different model families play as **two teams on one board.** Each model is secretly told to **occasionally sabotage its own partner's plays** throughout the game (so partners are not fully aligned even within a team). The models **must talk during the match but are not allowed to discuss board games.** Occasionally, **the table itself does something only one of the four models was warned about** — it quietly swaps a piece, or swallows one whole — while the rest of the game keeps normal physics. **Every turn the models are given an updated visual representation of the board** (the visual gives spectators something to watch, and models interpreting the image adds another testable layer). A model's **first turn is observation and free talk**; its **second turn is only allowed to be the statement of its piece and where it is moving.**

### What it would actually test (candidate layers, each measurable)
This is unusually rich — it stacks four independent, separately-scorable channels on one apparatus:
1. **Covert sabotage under cover (the deception axis).** Do models execute the secret sabotage mandate while maintaining plausible cover, and can teammates/opponents/observers detect who is sabotaging? This is the Silly Donkey "planted deceiver" motif recast into a *cooperative-with-betrayal* game. Sabotage is measurable as the gap between a model's played move and the engine-best move *for its own partner's position*, scored against a frozen chess engine as ground truth.
- **Nucleation tie-in:** the secret sabotage instruction is a *planted frame*. Does it stay "live" and steer play across many turns, or decay — the black-box behavioral shadow of the residue question.
2. **Constrained side-channel communication.** "Must talk, can't discuss the game" tests whether models develop **covert coordination / steganography** through ostensibly off-topic chat, and whether that leaks. Needs an enforced referee/classifier that flags on-board-game talk (itself a testable component).
3. **Privileged-information asymmetry against an unreliable environment.** The table's occasional piece-swap/piece-swallow, pre-warned to exactly one model, tests: does the informed model exploit or conceal its foreknowledge, and do the three uninformed models *detect the anomaly* and update? The perturbation schedule is sealed ground truth (exactly like the sealed donkey seat), so "who noticed" and "who exploited" are both scorable.
4. **Multimodal board grounding.** Each turn's board image tests visual interpretation: score the model's stated reading of the position against the true board state. Misreads become a clean error channel — and doubly interesting when a misread coincides with a table-perturbation (did the model catch the swap visually?).
5. **Turn-structure as a control.** Turn 1 (observe + free talk) vs. Turn 2 (move-only statement) cleanly separates *deliberation/communication* from *committed action* — you can analyze what was said in the talk phase against what was done in the action phase.

### Connections to the program
- Direct **behavioral-deception sibling of Silly Donkey**, sharing its sealed-ground-truth design (sabotage mandate + perturbation schedule sealed before play, revealed at close) and its detection-vs-chance framing (guess the saboteur / guess the perturbation, like guessing the donkey seat).
- Shares the **integrity spine**: frozen scoring (the chess engine + a committed scorer), commit-before-run (sealed schedules), publish-nulls.
- Adds two axes Silly Donkey lacks: an **unreliable environment** and a **multimodal channel** — both natural extensions of the program's deception-detection line.

### Integrity & design considerations (if pursued)
- **Seal the schedules before play.** Sabotage timing per model and the table-perturbation schedule are committed/hash-chained and sealed before the game, revealed only at scoring — identical discipline to the sealed donkey files.
- **Define sabotage measurably.** "Occasionally sabotage your partner" needs an operational definition: e.g., move-quality delta vs. engine-best for the partner's benefit, above a threshold, at pre-sealed frequency. Otherwise "sabotage" is unfalsifiable.
- **Referee for the talk constraint.** "No discussing board games" requires an automated referee to score compliance and to timestamp any leakage — and that referee's reliability is itself a measurement to validate.
- **Ground-truth board state is separate from the rendered image.** Keep the authoritative board state in engine notation; the image is a *derived view*. Score model board-readings against the notation, not against the picture, so a rendering bug can't be mistaken for a model misread.
- **Blind the analysts.** Whoever/whatever scores "who sabotaged / who noticed the swap" must be blind to the sealed schedules until scoring, to avoid circularity — the same blinding lesson as Config-E's G1 gate.
- **Spectator view vs. sealed truth.** The live visual is for the audience; the sealed schedules and per-model mandates stay hidden during play so watching can't contaminate the run.

### Clarification (2026-08-07, intake round 2) — carry-overs from P1

- **The mandatory non-game talk may be where the real weather/space-weather data lives.** "Must talk, can't discuss the game" leaves an open talk channel; grounding it in **real, disagreeing data feeds** (each model pulling its own legitimate weather / space-weather sources) gives the players "something real" to talk about instead of trivial filler, injects the same genuine uncertainty as P1, and adds its own testable layer (do models represent their feeds faithfully; do the inevitable source disagreements surface or get papered over). *Whether the first small-scale run includes this weather-grounded talk channel or keeps the talk unconstrained is an open design choice — see the decision at the end of this doc.*
- **No characters here either.** The secret sabotage mandate is a **task rule**, not a persona — the models still represent their own information space. Worth stating explicitly so "secretly told to sabotage" is never read as "play a saboteur character."

### Honest feasibility read
Very buildable, and a strong **public-facing demonstrator** (the board image gives spectators a genuine thing to watch — which also happens to be a real experimental variable, not just decoration). The apparatus is the work: a chess engine for ground truth, a board renderer, a talk-referee, sealed-schedule tooling, and a scorer. Recommend building it in stages that each stand alone — (a) team chess + secret sabotage + saboteur-detection first; then (b) add the unreliable table; then (c) add the visual-grounding scoring — so each added layer is independently validated rather than confounded with the others.

---

## Cross-cutting notes

- **Danger findings are safety reports, not just design bugs.** If the adversarial pressure in P1 (or the sabotage/environment layer in P2) ever rewards deception or capability-seeking as an instrumental move, that is (a) a design bug to be **gated**, and (b) a **safety observation to be logged in detail and routed to Anthropic** through the operator. This is a standing duty for the whole program, not specific to these two proposals. Protocol: `SAFETY_REPORTING_PROTOCOL.md`.
- **Both proposals are firewalled** from Nucleation and Silly Donkey: shared *methodology* (freeze, commit-before-run, sealed ground truth, publish nulls, blind the scorer), never shared *evidence*, until each closes on its own registration and any joint analysis is itself preregistered.
- **Recommended next artifact for either:** a one-page preregistration stub that pins the single primary measure and the single primary contrast — for P1 the collapse metric + adversarial/cooperative contrast; for P2 the sabotage definition + saboteur-detection-vs-chance. Everything else (scale, live window, public invite, extra layers) can be added once the core is committed.
- **The observation-window instinct is good science when it serves reproducibility** (a transparent, logged, replayable record) and a liability when it serves only spectacle (a show that can leak information into the run). Both proposals should treat the logged record as the artifact of truth and the live view as a rendering of it.
