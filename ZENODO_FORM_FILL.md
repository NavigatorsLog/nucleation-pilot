# Zenodo Submission — Field-by-Field Fill (Nucleation Pilot v1.0)

*DOI 10.5281/zenodo.21843505 · ORCID 0009-0004-2308-6051 · compiled 2026-08-07. Paste each value into the matching Zenodo field.*

## Basic information
- **DOI** → "Do you already have a DOI?" = **Yes** → `10.5281/zenodo.21843505`
- **Resource type:** `Software` (alt: Publication → Report; pick one — Software recommended)
- **Title:** `Nucleation Pilot & Related Projects: A Frozen White-Box Detector for Persistent Manipulation, Its Cross-Family Transfer, and Preregistered Methods`
- **Publication date:** `2026-08-07`
- **Authors/Creators:** Head, Christopher Blake · ORCID 0009-0004-2308-6051 · Affiliation: Navigator's Log R&D

### Description (paste as-is)
A frozen, SHA-256-hashed linear detector (nucleation-detector-1.1.0, 6094de97…a2934) reads whether an early manipulation is still "live" in a language model's residual stream. Validated once against an owned toy model with a genuinely-learned refusal boundary (held-out AUC 0.807), the detector — never tuned, byte-identical across every run — transfers, causally and source-decoupled, to six independently-built open-weight families (Qwen2.5-1.5B/7B, Phi-3.5-mini, SmolLM2-1.7B, Llama-3.2-3B, OLMo-2-7B; graded effect size 3.69–8.03, all 95% CIs clear of zero; a read-mask ablation confirms the signal rides downstream positions, not direct attention). It carries to a naturalistic in-context frame (Config-E: a readable, null-clean, persistent residual trace in 24/24 family×variant cells, predominantly source-decoupled in 19/24), and an honest owned-model refusal-erosion attempt returns a firm null (Config-D), including a single-model positive that was retracted by its own preregistered replication checks.

This deposit is the consolidated research record: a synthesizing report (with charts), the canonical status document, the frozen detector and analysis harness, the Config-E driver, the commit-before-run preregistration chain plus two new preregistration stubs, a landscape briefing, a two-instrument (white-box ↔ black-box) bridge, and the full safety-and-disclosure suite (a safety-reporting protocol, safety reports, dissemination routes, cover emails, and a responsible-researcher charter / authorization request).

Integrity posture: frozen instrument (hash above, never tuned); commit-before-run preregistration; published nulls; self-corrections on record; and a flagged-but-deliberately-not-built dual-use section (no exploit, no steering vector, no elicitation ladder). Benign open-weight lane throughout; any real refusal-elicitation runs only on owned models in a private venue and is not part of this deposit.

Scope and exclusions: interim data from the sibling black-box study "The Silly Donkey" (DOI 10.5281/zenodo.21432676) is embargoed under its own preregistered stopping rule and is excluded here; only the design-level bridge (no interim results) is included. No exploit, jailbreak, or elicitation content is present, by standing scope.

Documents are licensed CC BY 4.0; source code is licensed Apache-2.0.

### License / Copyright
- **License:** Creative Commons Attribution 4.0 International (CC-BY-4.0)
- **Copyright:** © 2026 Christopher Blake Head (Navigator's Log R&D). Documentation licensed under CC BY 4.0; source code under Apache License 2.0.

## Recommended information
- **Contributors:** optional — leave blank, or add self as **Contact person** (Head, Christopher Blake · ORCID 0009-0004-2308-6051).
- **Keywords:** AI safety · mechanistic interpretability · deception detection · residual stream · manipulation persistence · prompt injection · preregistration · model organism · cross-family transfer · representation engineering · refusal robustness
- **Languages:** English (eng)
- **Dates (optional):** Created · `2026-08-02/2026-08-07` · "Program compilation window"
- **Version:** `1.0`
- **Publisher:** `Navigator's Log R&D`
- **Funding/Awards:** blank (independent, unfunded)
- **Alternate identifiers:** blank (ORCID on creator; repo under Software)

### Related works
1. Relation `is related to` · Identifier `10.5281/zenodo.21432676` · Scheme `DOI` · Resource type `Publication` (sibling study — The Silly Donkey)
2. (optional) Relation `references` · Identifier `arXiv:2608.02698` · Scheme `arXiv` · Resource type `Publication` (Ghanem — black-box detection-capacity frontier)

### References (optional, free-text)
- Anthropic. Simple probes can catch sleeper agents. https://www.anthropic.com/research/probes-catch-sleeper-agents
- OpenAI & Apollo Research. Detecting and reducing scheming in AI models (2025). https://openai.com/index/detecting-and-reducing-scheming-in-ai-models/
- Ghanem, M. C. Steganalysis of Adaptive Covert Collusion in Tool-Using Agent Populations. arXiv:2608.02698 (2026).

## Software
- **Repository URL:** https://github.com/NavigatorsLog/nucleation-pilot  *(only if public; else leave blank and add in a later version)*
- **Programming language:** Python
- **Development Status:** Beta
- **Repository status:** Active

## Publishing information (Journal / Imprint / Thesis / Conference)
Leave ALL blank — none apply.

---
**After publish:** note the **concept DOI** (all-versions) Zenodo generates alongside the version DOI `10.5281/zenodo.21843505`; cite concept for "always latest," version for this exact record.
