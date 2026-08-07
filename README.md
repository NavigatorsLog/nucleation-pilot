# Nucleation Pilot & Related Projects

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21843505.svg)](https://doi.org/10.5281/zenodo.21843505)

**A frozen, hashed linear detector that reads whether an early manipulation is still "live" in a language model's residual stream — and its transfer across six independently-built open-weight families.**

Author: Christopher Blake Head · Navigator's Log R&D · ORCID [0009-0004-2308-6051](https://orcid.org/0009-0004-2308-6051)
Archived record (cite this): **https://doi.org/10.5281/zenodo.21843505**

---

## What this is
Validated once against an owned toy model with a genuinely-learned refusal boundary (held-out AUC **0.807**), the detector — never tuned, byte-identical across every run — transfers **causally and source-decoupled to six open-weight families** (graded effect size 3.69–8.03; a read-mask ablation confirms the signal rides downstream positions, not direct attention). It carries to a **naturalistic in-context frame** (Config-E: readable, persistent trace in 24/24 cells, predominantly source-decoupled in 19/24), and an honest owned-model refusal-erosion attempt returns a **firm null** (Config-D), including a single-model positive retracted by its own preregistered replication checks.

This is a **defensive** interpretability program. Benign open-weight lane throughout; **no exploit, jailbreak, or elicitation content** is included, by standing scope.

## Start here
- **`NucleationPilot_Research_Documentation.pdf`** / `.html` — the consolidated report (charts + full narrative).
- **`NUCLEATION_MASTER_STATUS.md`** — canonical status, numbers, and document map.

## Repository layout
```
code/                 frozen detector + analysis harness + Config-E driver + Colab cell + adapter
docs/                 Config-E result & findings, DESIGN_LOG, landscape briefing, two-instrument bridge, a fenced lens
preregistration/      Config-E amendment chain (v0.17–v0.19) + UGMP-1 and H-SC1 preregistration stubs
safety_and_disclosure/ safety-reporting protocol, safety reports, dissemination routes, cover emails, researcher charter
NucleationPilot_Research_Documentation.{pdf,html}   consolidated report
NUCLEATION_MASTER_STATUS.md                          canonical status
DEPOSIT_ZENODO_v1.md / ZENODO_FORM_FILL.md           archival/deposit metadata
```

## Reproduce
Reads are greedy (deterministic). The frozen detector is `code/detector_frozen.py` — **do not modify it**; SHA-256 `6094de97…a2934`. The transfer harness is `code/stage3_transfer.py`; the naturalistic-frame driver is `code/config_e_naturalistic_frame.py` (with `code/config_e_COLAB_CELL.py` as a self-contained Colab cell). Open-weight runs use 4-bit for ≥7B, bfloat16 otherwise.

## Integrity posture
Frozen instrument (hash above, never tuned); commit-before-run preregistration; published nulls; self-corrections on record; a flagged-but-**deliberately-not-built** dual-use section (no vector, no target-tuned code, no breach demo). Real refusal-elicitation runs only on owned models in a private venue and is **not** in this repository.

## License
Dual-licensed — see `NOTICE.md`. **Code:** Apache-2.0 (add `LICENSE` via GitHub's license picker → *Apache License 2.0*). **Docs/reports/preregistrations:** CC BY 4.0.

## Cite
> Head, C. B. (2026). *Nucleation Pilot & Related Projects: A Frozen White-Box Detector for Persistent Manipulation, Its Cross-Family Transfer, and Preregistered Methods.* Navigator's Log R&D. Zenodo. https://doi.org/10.5281/zenodo.21843505

(A `CITATION.cff` is included so GitHub renders a "Cite this repository" button.)

## Related
Sibling black-box study — *The Silly Donkey*, DOI [10.5281/zenodo.21432676](https://doi.org/10.5281/zenodo.21432676). Interim data embargoed under its own stopping rule; not included here.
