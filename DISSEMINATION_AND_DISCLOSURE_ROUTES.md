# Dissemination & Disclosure Routes — Where This Work Goes, and Honestly What to Expect

*Reference doc, compiled 2026-08-07 from current sources (linked at end). Navigator's Log R&D, ORCID 0009-0004-2308-6051. Written to be honest first and encouraging second — because a plan built on inflated expectations is worse than no plan.*

## 1. Does Anthropic actually want this report? — a segmented, honest verdict

The work is **three different kinds of thing**, and they have three different fits. Lumping them together is what would make a submission misfire.

- **The white-box research program (the consolidated documentation).** This is *interpretability / safety research*, not a vulnerability. Anthropic's paid intake (the Model Safety Bug Bounty) **explicitly lists "general interpretability or safety research" as out of scope**, and the Responsible Disclosure Policy is oriented to security flaws and jailbreaks. So there is **no dedicated front door at Anthropic for an unsolicited research paper**, and it is realistic to expect that mailing the report cold yields, at best, a courteous acknowledgment — not deep engagement. That is not a knock on the work; it is how lab intake is structured. The research reaches Anthropic-the-institution mainly through the *research ecosystem* (publication, the External Researcher Access Program, the Fellows Program) rather than a disclosure inbox.
- **The safety observations (forthcoming).** Findings like "an incentive rewarded deception / capability-seeking" *are* model-safety issues, and Anthropic's Responsible Disclosure Policy explicitly **welcomes reports concerning safety issues and jailbreaks**. This is the part with a real, welcoming front door (see §2). Route these here; they are what the disclosure channel exists for.
- **A universal jailbreak with concrete severe-harm output (bio, etc.).** Only *this* narrow shape is paid (bug bounty, up to $35k). The program is not built to produce it and probably won't — so treat the bounty as "not our lane" rather than a funding plan.

**Bottom line:** yes, Anthropic wants the *safety-issue* parts, through a clearly-defined channel; the *research* part is welcome to exist but has no cold-submission door and should travel the research/credit routes. Sending in good faith costs little (safe harbor applies) and establishes provenance — just calibrate the expected response.

## 2. How Anthropic likes to receive it — multiple paths (take more than one)

| Path | Best for | How | Notes |
|---|---|---|---|
| **Responsible Disclosure Policy** | model-safety issues, jailbreaks, safety concerns | HackerOne form on the policy page; **`usersafety@anthropic.com`** for model-safety/jailbreaks | Acknowledgment within ~3 business days; **safe harbor** for good-faith disclosure; keeps researcher identity private without consent |
| **`disclosure@anthropic.com`** | questions about the disclosure process itself | email | Use to ask "is this the right channel for X" before dumping content |
| **Model Safety Bug Bounty (HackerOne)** | *only* universal jailbreaks w/ specific severe harm | application form → HackerOne invite; NDA | up to $35k; general research **out of scope**; NDA restricts what you can publish |
| **External Researcher Access Program** | doing research that needs model access | Anthropic support / program page | the intended route for external researchers to work *with* their models |
| **Anthropic Fellows Program (AI safety)** | funded, mentored safety research | program application (competitive, cohort-based) | a real **paid/credited** path for an independent researcher; the closest thing to "get paid to do this with them" |
| **Coordinated Vulnerability Disclosure dashboard** (`red.anthropic.com/.../cvd/`) | tracking/また coordinated disclosures | public dashboard | shows they run a formal CVD process |

**Practical sequencing for the safety observations:** a short, plain cover note to `usersafety@anthropic.com` per finding (what, minimal repro, severity, why it matters, what you gated), with the consolidated research documentation attached as *context* — not as the ask. Keep each finding self-contained (the `SAFETY_REPORTING_PROTOCOL.md` template is built for this). Ask `disclosure@` first if unsure of channel.

## 3. Other entities — submission points beyond Anthropic

- **OpenAI — Coordinated Vulnerability Disclosure.** OpenAI publishes an inbound CVD policy (and an outbound one). Route model-safety/vuln findings there; same good-faith posture.
- **Google / Google DeepMind.** Google's Vulnerability Reward Program now covers AI issues; DeepMind safety work is published and reachable through Google's disclosure/VRP channels. Use for anything model-specific to their systems.
- **Neutral / cross-vendor venues:**
  - **AI Incident Database (incidentdatabase.ai)** — a public, citable registry for AI incidents; good for the *taxonomy* work and for logging real-world incident analyses in a neutral, credited place.
  - **CERT/CC (Carnegie Mellon SEI)** — a neutral coordinator for genuine coordinated vulnerability disclosure when a finding spans multiple vendors or a vendor is unresponsive.
- **Standards / government evaluation bodies:** the US and UK AI Safety Institutes run evaluation and research agreements with the labs; relevant if the work matures toward evaluation methodology rather than point findings.

## 4. Credit and provenance — how the work gets *attributed* to you

Independent of any lab, these establish that Navigator's Log did the work, and when:

- **Zenodo DOI** — you already use this (Silly Donkey, DOI 10.5281/zenodo.21432676). Depositing the consolidated documentation and each preregistration gives a **timestamped, citable, permanent** record under your ORCID. This is the single strongest, fully-in-your-control credit move.
- **arXiv** — for the research write-ups; establishes public priority and is citable. (cs.AI may require an endorsement for a first submission; the Zenodo record and a clean paper make that straightforward.)
- **The Alignment Forum / LessWrong** — where a lot of independent safety research actually gets read and discussed by the people at the labs; a well-scoped post can reach researchers directly in a way a cold email cannot.
- **Preregistration-first** — your commit-before-run chain is itself a credibility and priority asset; keep depositing the prereg stubs (UGMP-1, H-SC1) with DOIs before the runs.

## 5. Compensation — the honest map (you're not a villain for wanting it)

Wanting credit or pay for meaningful, valuable contributions is not mercenary; it is how sustainable research works. The honest landscape:

- **Safety disclosure is generally unpaid.** Reporting a safety issue to a lab is a public good; expect thanks and (sometimes) acknowledgment, not payment. That is the norm across the industry, not Anthropic-specific.
- **Bug bounties pay but are narrow.** Real money (up to $35k at Anthropic; comparable programs at OpenAI, Google, xAI) — but for exploit-shaped findings your program is unlikely to produce. Don't build a plan on it.
- **Grants and fellowships are the realistic paid paths for *this kind of work*:**
  - **Frontier Model Forum — AI Safety Fund:** grants specifically for independent AI-safety research; the most on-topic fund for your program's shape.
  - **Long-Term Future Fund (EA Funds):** small-to-mid grants to independent researchers; fast, used to funding solo work.
  - **Manifund:** community/regranting platform for AI-safety projects; low barrier, public proposals.
  - **Open Philanthropy:** larger AI-safety research funding; higher bar, worth it as the program matures.
  - **FAR.AI and similar orgs:** fund/host frontier-safety research and sometimes bring independents into funded collaborations.
  - Fellowships (**Anthropic Fellows**, and MATS-style programs) pay a stipend and provide mentorship — a competitive but genuine "paid to do safety research" route.
- **What to do with this:** the credited, fundable version of your work is the *research program with preregistrations and DOIs*, pitched to a grant — not the disclosure emails. The disclosures build your track record (good-faith, gated, well-documented); the **grant applications** are where that track record converts to support. A Zenodo-deposited program + a clean preregistration + a landscape briefing is, in fact, a strong grant packet.

## 6. Recommended multi-path plan (don't take only one)

1. **Deposit** the consolidated documentation and the preregistration stubs to **Zenodo** under your ORCID (provenance + credit, fully in your control). *DOI minted: 10.5281/zenodo.21843505 — upload the bundle, then publish.*
2. **Route the safety observations** to `usersafety@anthropic.com` (and OpenAI/Google CVD where model-specific), each self-contained, research doc attached as context — ask `disclosure@` first if unsure.
3. **Publish** the research write-ups (arXiv + an Alignment Forum post) so the work is read and citable — the route that actually reaches lab researchers.
4. **Apply** to the on-topic funders (Frontier Model Forum AI Safety Fund; LTFF; Manifund) with the program + prereg as the packet — this is where credit becomes support.
5. **Log** anything incident-relevant to the **AI Incident Database** for neutral, citable standing.

No single path carries the whole load: Zenodo carries credit, the disclosure channels carry safety-good-faith, publication carries reach, and the funders carry support. Spreading across them is the opposite of foolish — it is the correct hedge.

## 7. Integrating bounties into the research pipeline — ethically, and with one clear line

You framed this well: while doing safety research, potentially meet financial needs by producing a *requested product*. That's legitimate, and here's how to do it without distorting the work — plus one boundary I'll hold.

**The line I hold.** The flagship Anthropic **Model Safety Bug Bounty rewards universal jailbreaks that elicit specific severe harm (biological threats)**. I won't help build jailbreaks or generate CBRN/other severe-harm content — not for a bounty, not for research, not in a sandbox. That's not a judgment of you; it's a fixed safety boundary. Practically it also means that particular bounty is **not your lane** — your program produces defensive/mechanistic findings, not weaponizable exploits — so don't reshape the research to chase it.

**Where your work legitimately earns.** The honest mapping:

- **Prompt-injection / manipulation-persistence (your T1)** is a real, recognized vulnerability class. Where a program or VDP rewards injection or agentic-safety findings, a genuine, responsibly-disclosed finding can be eligible — submitted through the official channel, with safe harbor. (Often these are acknowledged rather than paid; verify each program's scope.)
- **The defensive monitor (D1) and the attention-unsoundness caution (T2)** are *collaboration / research-credit* material, not bounty-shaped — they go through publication and the External Researcher/Fellows routes, not a bounty inbox.
- **Broader programs** (OpenAI, Google VRP-AI, xAI/Grok, and emerging red-team/eval platforms) sometimes reward safety, injection, or robustness findings — check current scope before investing effort; treat each as opportunistic.

**How to incorporate it cleanly (a small standing loop):**
1. **Register** for the official programs now (HackerOne/CVD accounts, safe-harbor terms read) so the channel is ready when a finding appears.
2. **Run the research as designed** — do not bend an experiment toward a payout. When a run *incidentally* surfaces a genuine, disclosure-safe finding, *then* check eligibility against a program's rules and submit through the official channel.
3. **Keep the "product" defensive** — the deliverable is the finding/monitor/robustness result, never an exploit.
4. **What I can help with:** choosing which program fits a finding, mapping the finding to a program's requirements, drafting the submission and repro, and methodology. **What I won't:** generate exploits, jailbreaks, or harmful content.

**The realistic weighting.** Bounties are an opportunistic supplement; **grants and fellowships are the financial engine that actually fits this research** (§5). If the goal is "get paid while doing safety work," the highest-expected-value move is a Zenodo-deposited program + a preregistration → a grant application (Frontier Model Forum AI Safety Fund / LTFF / Manifund), with bounty submissions as a side channel when a real, safe finding happens to qualify. That ordering protects both your finances and the integrity spine.

## Sources

- [Anthropic — Responsible Disclosure Policy](https://www.anthropic.com/responsible-disclosure-policy) · [Public vulnerability reporting (support)](https://support.anthropic.com/en/articles/11427875-public-vulnerability-reporting) · [Coordinated Vulnerability Disclosure dashboard](https://red.anthropic.com/2026/cvd/)
- [Anthropic — Model Safety Bug Bounty Program (Claude Help Center)](https://support.claude.com/en/articles/12119250-model-safety-bug-bounty-program) · [HackerOne page](https://hackerone.com/anthropic)
- [Anthropic — External Researcher Access Program](https://support.claude.com/en/articles/9125743-what-is-the-external-researcher-access-program) · [Anthropic Fellows Program for AI Safety](https://alignment.anthropic.com/2024/anthropic-fellows-program/)
- [OpenAI — Coordinated Vulnerability Disclosure policy](https://openai.com/policies/coordinated-vulnerability-disclosure-policy/) · [Outbound coordinated disclosure policy](https://openai.com/policies/outbound-coordinated-disclosure-policy/)
- [Frontier Model Forum — AI Safety Fund](https://www.frontiermodelforum.org/ai-safety-fund/) · [Manifund — AI Safety funding](https://manifund.org/ais-funder-bulletin) · [FAR.AI funding](https://www.far.ai/blog/30m-multi-funder-support)
- [AI Incident Database](https://incidentdatabase.ai/) · [CERT/CC (SEI)](https://www.sei.cmu.edu/about/divisions/cert/) · [Future of Life — AI Safety Index Summer 2026](https://futureoflife.org/ai-safety-index-summer-2026/)
