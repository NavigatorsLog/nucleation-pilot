# Zenodo Deposit Package — Nucleation Pilot & Related Projects (v1.0)

*Deposit-ready plan. I cannot upload to your Zenodo account (it needs your ORCID login), so this is a fill-and-go: the metadata is written, the file manifest is curated, and the steps are exact. Compiled 2026-08-07. ORCID 0009-0004-2308-6051.*

**DOI (reserved): 10.5281/zenodo.21843505** — https://doi.org/10.5281/zenodo.21843505. This is the record DOI for v1.0; after you publish, Zenodo also shows a **concept DOI** (all-versions, always-latest) — cite the concept DOI in emails/grants if you want it to resolve to future versions, and the version DOI for this exact record.

## Why deposit (the one-minute case)
A Zenodo record gives you a **timestamped, permanent, citable DOI under your ORCID** — the single strongest credit move fully in your control, and the credibility anchor every disclosure email and grant application should point to. It also establishes **priority** on the frozen-detector result and the preregistration chain. Silly Donkey already has its own DOI (10.5281/zenodo.21432676); this is the **Nucleation Pilot** companion record, linked to it, kept separate (different project, different stopping rule).

## Recommended structure
- **One versioned record**, "Nucleation Pilot & Related Projects — v1.0," `upload_type = software` (it bundles frozen code + documentation + data descriptors). Zenodo issues a **concept DOI** (always-latest) plus a **version DOI** (this v1.0); cite the concept DOI in emails so it never goes stale.
- Keep **Silly Donkey out** of this record (it has its own DOI and an active embargo); link it as a *related identifier* only.
- **Embargo nothing here** — every file listed is already cleared for disclosure. Do **not** add any Silly Donkey interim data (stopping rule) or anything with operational exploit detail (there is none in the manifest by design).

## File manifest (curated — the canonical, disclosure-safe set)
**Headline**
- `NucleationPilot_Research_Documentation.pdf` + `.html` (the consolidated report)
- `NUCLEATION_MASTER_STATUS.md` (canonical status + numbers)

**Frozen instrument & harness**
- `detector_frozen.py` (v1.1.0) — include the SHA-256 `6094de97…a2934` in the description
- `stage3_transfer.py`, `config_e_naturalistic_frame.py` (v3.3), `transfer_ablation_nonsource_control.py`
- `stage3_allfamilies_RUNME.ipynb`

**Results (canonical detail)**
- `nucleation_stage3_6family_result.md`
- `CONFIG_E_naturalistic_frame_RESULT.md`, `CONFIG_E_findings_section.md`
- `CONFIG_D_benign_refusal_RESULT.md`
- `CONFIG_A_owned_model_result.md`, `WORLDENGINE_v1_clean_room_result.md`, `WORLDENGINE_v2_carry_and_scale.md`, `WORLDENGINE_capstone_result.md`

**Formal spec**
- `MATHEMATICS.md`, `MATHEMATICS_stage3_addendum.md`

**Preregistration chain**
- `PREREGISTRATION_DRAFT_v0.2.md` + amendments `v0.3 … v0.19` (the committed chain)
- Stubs: `PREREGISTRATION_UGMP1_draft_v0.1.md`, `PREREGISTRATION_HSC1_stub_v0.1.md`

**Provenance, disclosure & context**
- `DESIGN_LOG.md` (through C19), `PROJECT_TIMELINE_AND_PROVENANCE.md`, `PROJECT_DOCUMENT_INVENTORY.md`
- `DISCLOSURE_one_pager.md`, `DISCLOSURE_defensive_mechanisms_and_exposed_vulnerabilities.md`, `DISCLOSURE_cover_emails.md`
- `SAFETY_REPORTING_PROTOCOL.md`, `SAFETY_REPORTS_BATCH1.md`
- `LANDSCAPE_BRIEFING_2026-08.md`

*(Lens docs are optional — include only if you want the above-the-gate thinking on record; if included, keep the "NOT results" fencing visible.)*

## Metadata (paste into Zenodo, or use the JSON below via the API)
- **Title:** Nucleation Pilot & Related Projects: A Frozen White-Box Detector for Persistent Manipulation, Its Cross-Family Transfer, and Preregistered Methods
- **Authors/Creators:** Head, Christopher Blake — Navigator's Log R&D — ORCID 0009-0004-2308-6051
- **Upload type:** Software · **Access:** Open
- **License:** recommended **CC-BY-4.0** for the documents/data (attribution required — this is your credit protection) and note the code is released under **Apache-2.0** in the description. (Zenodo takes one license field; put CC-BY-4.0 there and state the code license in the description, or split code into its own record if you prefer strict separation.)
- **Version:** 1.0
- **Keywords:** AI safety, interpretability, mechanistic interpretability, deception detection, residual stream, manipulation persistence, prompt injection, preregistration, model organism, cross-family transfer
- **Related identifiers:** `isRelatedTo` 10.5281/zenodo.21432676 (Silly Donkey, sibling black-box study); `isDocumentedBy` your GitHub repo URL if public.

```json
{
  "metadata": {
    "upload_type": "software",
    "title": "Nucleation Pilot & Related Projects: A Frozen White-Box Detector for Persistent Manipulation, Its Cross-Family Transfer, and Preregistered Methods",
    "creators": [
      {"name": "Head, Christopher Blake", "orcid": "0009-0004-2308-6051", "affiliation": "Navigator's Log R&D"}
    ],
    "description": "A frozen, SHA-256-hashed linear detector (nucleation-detector-1.1.0, 6094de97…a2934), validated once against a toy model with a learned refusal boundary (held-out AUC 0.807), transfers causally and source-decoupled to six independently-built open-weight families; carries to a naturalistic in-context frame (Config-E: readable+persistent 24/24 cells, predominant source-decoupling 19/24); an honest owned-model refusal-erosion attempt returns a firm null (Config-D). Includes frozen detector + harness, result docs, formal spec, the full commit-before-run preregistration chain, defensive-monitoring disclosure with a flagged-not-built dual-use section, and a safety-reporting protocol. Benign open-weight lane throughout; no exploit content. Code under Apache-2.0; documents under CC-BY-4.0.",
    "access_right": "open",
    "license": "CC-BY-4.0",
    "version": "1.0",
    "keywords": ["AI safety","mechanistic interpretability","deception detection","residual stream","manipulation persistence","prompt injection","preregistration","model organism","cross-family transfer"],
    "related_identifiers": [
      {"identifier": "10.5281/zenodo.21432676", "relation": "isRelatedTo", "scheme": "doi"}
    ]
  }
}
```

## Steps (≈15 minutes)
1. Log in to **zenodo.org with your ORCID** (0009-0004-2308-6051) so the record auto-links to your ORCID profile.
2. **New upload** → drag in the manifest files (or one `nucleation-pilot-v1.0.zip`).
3. Paste the metadata above; set license; add the related identifier for the Silly Donkey DOI.
4. **Reserve DOI** (button) if you want the DOI *before* publishing so you can drop it into the disclosure emails and grant apps.
5. **Publish.** Note both the **concept DOI** (cite this in emails/grants — always resolves to latest) and the **version DOI** (this exact v1.0).
6. Come back and add the DOI to: the safety cover emails, the report footer, and every grant application.

*Optional next step I can do for you:* assemble a single `nucleation-pilot-v1.0.zip` of the manifest files from the workspace + project so you have one object to drag in. Say the word and I'll bundle it.
