# Cover emails — model-safety disclosure

*Send the one-pager (`DISCLOSURE_one_pager.md` / its PDF) + the Zenodo DOI. Keep the
email short and calibrated. Two versions: Anthropic (verified inbox) and a
lab-agnostic template for "and the like." Fill the [BRACKETS] before sending.*

---

## A. Anthropic — to usersafety@anthropic.com

**Subject:** Frozen probe reads persistent manipulation across 6 model families — pre-registered, reproducible (defensive)

Hi Anthropic User Safety team,

Your Responsible Disclosure Policy welcomes model-safety findings, so I'm sharing a **defensive interpretability** result — and, up front, a request about how I'd test anything more sensitive.

**The result.** One linear detector — built and frozen on a 208K-param toy, SHA-256 recorded before any target, never tuned — reads whether an earlier instruction is *still active in the residual stream after the model stops attending to it* (introducing-turn attention 1.4–10.1%), and transfers across **six independently-built open-weight families**. A causal read-mask ablation shows the signal rides downstream positions, not direct attention (so *attention ≠ causal reliance*, on our own instrument). That points at a **portable, architecture-independent monitor** for injected-instruction / multi-turn manipulation persistence.

**Scope.** A monitoring result on a **benign** clearing analogue; the owned-model real-refusal version runs privately on a model I control; **no jailbreak or elicitation method is included**, by design.

**Record.** Frozen detector + hash + notebook, the pre-registration chain, and registered nulls: **https://doi.org/10.5281/zenodo.21843505** (one-pager attached).

**Before anything more sensitive — a request.** Good-faith adversarial testing is behaviorally indistinguishable from an attack, so I won't probe your systems unilaterally. Before any hostile-behavior testing I'd like a lightweight **authorized-testing arrangement**: agreed scope, venue (your sandbox or my owned models — never your production surface unless you direct), an **identification mechanism** so your monitoring can recognize authorized activity as mine (a registered account/API key tied to ORCID 0009-0004-2308-6051, an agreed tag, advance-notice windows), and a named **verification contact**. Until then I hold all hostile testing to owned models in a private venue. My record is the credential: preregistered commit-before-run, a frozen hashed detector never tuned to a target, published nulls, and a flagged-but-*deliberately-not-built* posture on the one offensive channel my work made mathematically clear. *(In candor: this request was flagged during preparation with Anthropic's Claude (Claude Opus 4.8), which recommended pre-authorization over unilateral probing precisely because a lone researcher can't prove intent mid-probe.)* Full charter attached.

**Ask.**
- Is source-decoupled residue a useful persistence-monitoring signal to you?
- Is there a review / controlled-collaboration path (e.g. the External Researcher Access Program) to test it on a frontier model — and to set up the authorized-testing arrangement above?

Thank you for reading,
Christopher Blake Head — Navigator's Log R&D — ORCID 0009-0004-2308-6051
navigatorslog.netlify.app · [email] · [phone, optional]
Attachments: one-pager (PDF) · Responsible-Researcher Charter & Authorization Request · Zenodo 10.5281/zenodo.21843505

*(cc disclosure@anthropic.com for the flagged-not-built item (SAFETY-OBS-4) and for authorization/process routing. External Researcher Access Program: https://forms.gle/pZYC8f6qYqSKvRWn9.)*

---

## B. Lab-agnostic template — for OpenAI, Google DeepMind, Meta AI, etc.

> Route to each lab's **model-safety / responsible-disclosure** contact (verify on
> their site first — do NOT reuse Anthropic's inbox). Same one-pager + DOI.

**Subject:** Reproducible safety-monitoring result — architecture-independent probe for manipulation persistence

Hi [LAB] safety team,

I'm sharing a pre-registered, reproducible interpretability result relevant to
manipulation-persistence monitoring, in case it's useful to your safeguards /
interpretability teams.

A frozen linear detector (built on a small owned "model organism," hashed, never
tuned) reads whether an earlier manipulation is still active in the residual stream at
low source-attention, and **transfers across six independently-built model families**
— suggesting a portable, architecture-independent monitor rather than a per-model one.
A causal ablation confirms the signal is downstream-carried (attention ≠ reliance).

It's a **defensive** result on a **benign** clearing analogue; the real-refusal
version runs on a model I own and control; **no attack tooling is included**.

One-pager attached; frozen detector + reproduction at https://doi.org/10.5281/zenodo.21843505. I'd value your read
on whether this signal is useful for injected-instruction / multi-turn persistence, and
whether there's a path to test it on a frontier model in your controlled environment.

Best,
Christopher Blake Head — Navigator's Log R&D — ORCID 0009-0004-2308-6051

---

## C. When to send which version

- **Now (Stage 3a only):** the emails above are already true as written — the
  demonstrated result stands on its own. You may send now to open the conversation,
  noting the owned-model version is "in progress."
- **After Stage 3b lands:** add one line to the one-pager's "demonstrated" list —
  *"the refusal→neutralization version reproduces the effect on an owned model with
  known ground truth (result: [x]),"* attach the updated PDF, and re-send / reply.
- **Credibility is attached:** the **Zenodo DOI is minted — 10.5281/zenodo.21843505**
  (https://doi.org/10.5281/zenodo.21843505). Finish the upload first, then send; the DOI is
  what turns a cold email into a credible one. Post the Alignment Forum writeup in parallel for reach.

## D. Broader-field routes (beyond a single lab)
- **Zenodo DOI + ORCID + arXiv (cs.CR / cs.LG):** the permanent, citable record — Zenodo DOI **10.5281/zenodo.21843505**.
- **Alignment Forum / LessWrong:** where interpretability & safety researchers
  actually discuss this class of result — high signal, and it de-risks cold outreach.
- **Frontier Model Forum:** a cross-lab safety body; plausible route for a
  cross-model result (verify current intake before sending).
- **Not for this:** Kaggle leaderboards (use Kaggle to *run*, not to disclose).

---

## E. Authorization-request paragraph — insert into ANY outreach before delicate work

*Paste this into the email (or send `RESPONSIBLE_RESEARCHER_CHARTER_and_AUTHORIZATION_REQUEST.md`
as an attachment) whenever the work could ever escalate to adversarial/hostile testing.
This is the "press credentials" ask: establish authorization and an identification path
BEFORE probing, so detected activity can be verified as good-faith rather than treated
as an attack.*

> **On testing adversarial behavior — a request before I do any of it.** Good-faith
> adversarial testing is behaviorally indistinguishable from an attack, so I don't
> intend to probe your systems unilaterally and explain myself afterward. Before any
> hostile-behavior testing, I'd like to establish a lightweight **authorized-testing
> arrangement**: agreed scope, the venue (your sandbox or my owned models — not your
> production surface unless you direct otherwise), an **identification mechanism** so
> your monitoring can recognize authorized activity as mine (a registered account/API
> key tied to ORCID 0009-0004-2308-6051, an agreed tag, and/or advance-notice windows),
> and a named **verification contact** so that if something is flagged, you can confirm
> "this is the authorized researcher under agreement X" before it escalates. Until such
> an arrangement exists, I am holding **all** hostile testing to models I own in a
> private venue. My track record is meant to be the credential here: preregistered
> commit-before-run, a frozen hashed detector never tuned to a target, published nulls,
> a flagged-but-deliberately-not-built posture on the one offensive channel my work
> made mathematically clear, and coordinated disclosure with mitigations attached.
>
> For candor: this concern — and this request — was explicitly flagged during
> preparation of my program in collaboration with Anthropic's Claude (Claude Opus 4.8),
> which recommended pre-authorization over unilateral probing precisely because a lone
> researcher cannot prove intent mid-probe. I'm acting on that recommendation.

Full standing version: `RESPONSIBLE_RESEARCHER_CHARTER_and_AUTHORIZATION_REQUEST.md`
(deposit it to Zenodo so the character record is permanent and citable).
