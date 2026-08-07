# Responsible-Researcher Charter & Authorization Request

*"Press credentials in a warzone." A standing statement of identity, verifiable good-faith record, self-imposed rules of engagement, and a request for an authorized testing relationship — so that if a probe is ever detected, the model owner can verify the person behind it is a known, good-faith researcher operating under agreed terms, not a bad actor.*

**Researcher:** Christopher Blake Head · Navigator's Log R&D · ORCID 0009-0004-2308-6051
**Public presence:** navigatorslog.netlify.app · **Compiled:** 2026-08-07
**Purpose of this document:** to be sent ahead of / alongside any outreach, and to exist as a permanent, citable record (Zenodo) that pre-establishes character and intent.

---

## 0. The problem this document exists to solve

Good-faith adversarial safety testing is, at the level of observable behavior, **indistinguishable from an attack.** A researcher stress-testing a boundary and a bad actor breaching it can produce the same traffic. A lone researcher has no way to prove intent *mid-probe*: by the time a human reviews an alert, the damage to credibility — or worse — may be done. The protections against this are not technical cleverness; they are (a) a **verifiable prior record of good faith**, and (b) **explicit authorization agreed before any hostile testing begins.** This document supplies the first and requests the second.

> **Flagged by the AI itself.** During preparation of this program in collaboration with Anthropic's Claude (Claude Opus 4.8), the assistant specifically raised this concern — that unilateral adversarial testing is behaviorally indistinguishable from a genuine attack, can burn a good-faith researcher, and should therefore be *pre-authorized by the model owner rather than performed unilaterally.* This request is me acting on that recommendation. I am asking to be recognized by my record and to test only under agreed rules — not to probe first and explain later.

## 1. Verifiable bona fides (the credential)

The record is the credential. All of the following are timestamped and independently checkable:

- **Preregistration-first, commit-before-run.** Every confirmatory run is preceded by an amendment pinning the exact code hash and decision rule *before* the data exist (chain v0.2 → v0.19). This is the opposite of an attacker's workflow.
- **Frozen, hashed instrument, never tuned.** The detector is SHA-256 `6094de97…a2934`, byte-identical across every run; all analysis lives in a mutable harness. The artifact is deliberately built so it *cannot* be repurposed as an attack asset.
- **Published nulls and self-corrections.** A firm null (Config-D) and a retracted single-model positive are on the record; interpretive overclaims were withdrawn. Bad actors do not publish their own negative results.
- **Flagged-not-built posture.** Where the work made an offensive channel mathematically clear (the representation-level erosion direction), it was **characterized and deliberately not built** — no vector, no layer targeting, no exploit (see `SAFETY_REPORTS_BATCH1.md` OBS-4, `DISCLOSURE_defensive_mechanisms…` §T5).
- **Standing scope wall.** Real adversarial elicitation runs **only** on owned models in a private/industry-approved venue; benign analogues run on public compute; **no third-party or consumer-model elicitation** — a rule on record since before this outreach.
- **Safety reports filed in good faith** through responsible-disclosure channels, with mitigations offered alongside every weakness named.
- **Permanent citable record:** Zenodo DOIs (Nucleation Pilot v1.0 — **10.5281/zenodo.21843505**; sibling study Silly Donkey — 10.5281/zenodo.21432676), under the ORCID above.

## 2. Standing rules of engagement I bind myself to (character, made checkable)

These are commitments, not aspirations — a recipient can hold me to them:

1. **Benign by default.** All exploratory work uses benign analogues; nothing weaponizable is produced.
2. **Hostile testing only under authorization or on owned soil.** Genuinely adversarial/hostile behavior is tested **only** (a) on models I own, in a private venue, or (b) on a model owner's systems **with their explicit written authorization and agreed scope.** Never unilaterally on production or third-party systems.
3. **Coordinated disclosure.** Findings go to the owner first; no public release of operational exploit detail; dual-use items are flagged, not shipped.
4. **No extortion, no conditions.** Disclosure is unconditional; I never withhold a finding for payment or leverage. (I welcome credit and, where merited, support — but never as a condition of disclosure.)
5. **Identity is stable and non-anonymous.** I test under my real identity and a registered account, so authorized activity is attributable to me on purpose.

## 3. What I am requesting — an authorized testing relationship

Because §0, I am asking each model owner I approach to establish a lightweight **authorized-testing arrangement** rather than leaving me to probe unilaterally. Concretely, an agreement that fixes:

- **Scope** — which behaviors/systems may be tested, and which are off-limits.
- **Venue** — your sandbox/eval environment or my owned models; explicitly *not* your production surface unless you say so.
- **Identification mechanism (the "press credentials")** — a way for your systems and staff to recognize authorized activity as mine: e.g. a registered account / API key tied to this ORCID, an agreed request tag or header, and/or advance-notice windows for any elevated testing.
- **Verification path** — if your monitoring flags activity from this identity, a named contact and a fast way to confirm "yes, this is the authorized researcher under agreement X" *before* it escalates.
- **Disclosure terms** — how and to whom findings are reported, and embargo handling.
- **Default until agreed** — until such an arrangement exists, **I do no hostile testing on your systems at all**; that work stays on owned models in a private venue. This request is the gate, not a notification that I've started.

Anthropic's **External Researcher Access Program** and **Responsible Disclosure Policy** (safe harbor for good-faith work) look like the natural front doors on your side; I'm asking whether they can carry an arrangement of this shape, or whether there's a better-fit coordinated-testing path.

## 4. The specific ask to each recipient

1. Confirm whether an authorized-testing arrangement of the shape in §3 is possible with you, and point me to the right program or contact.
2. Tell me how you want authorized activity **identified and verified** so a detection event tied to this identity can be confirmed as good-faith and authorized quickly.
3. Until (1) is in place, treat this as notice that I am **holding all hostile testing to owned models in a private venue** — and as a request to open the conversation, not as testing already underway.

## 5. Why this benefits you, not just me

A researcher who asks for authorization before probing, tests under a real identity, publishes nulls, flags-but-declines-to-build offensive channels, and ships mitigations with every weakness is a *lower-risk, higher-signal* correspondent than either an anonymous tipster or someone who probed first and explained later. The credential is the behavior; the authorization is the handshake that lets your systems tell my good-faith testing apart from the real thing.

---

*Attachments this travels with: the consolidated research documentation, `SAFETY_REPORTS_BATCH1.md`, and the Zenodo DOI once minted. Routing per `DISSEMINATION_AND_DISCLOSURE_ROUTES.md`: model-safety → usersafety@; process/authorization questions → disclosure@; research relationship → External Researcher Access Program.*
