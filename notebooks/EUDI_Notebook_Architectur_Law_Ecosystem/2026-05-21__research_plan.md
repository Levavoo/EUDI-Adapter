# EUDI Research Plan

Date: 2026-05-21
Status: Initial research plan
Notebook: EUDI Notebook — Architecture, Law & Ecosystem

---

## Research goal

The goal of this research plan is to understand the EUDI Wallet ecosystem well enough to support a business-side prototype.

The prototype focuses on organizations that need to translate identity-check requirements into privacy-preserving wallet verification requests, process simulated wallet responses, and analyze audit logs.

This research should therefore focus on:

- business meaning
- actors and responsibilities
- trust relationships
- legal and compliance relevance
- verification flow concepts
- privacy and data minimization
- project scope boundaries

This research should not become a full legal commentary or implementation manual.

---

## Research principles

1. Official sources first.
2. Every source must be translated into plain meaning.
3. Every research note must explain relevance to the prototype.
4. Unclear topics must be recorded as open questions.
5. Research should produce project decisions, not only collected information.
6. The EUDI notebook explains context; the Project Build Log defines build work.

---

## Stage 1 — Orientation

Goal: understand the EUDI Wallet ecosystem at a high level.

Main questions:

- What is the EUDI Wallet?
- What problem does it solve?
- Which actors exist?
- What is the Architecture and Reference Framework?
- What does a relying party / verifier do?
- Which parts are relevant for this prototype?

Planned notes:

```text
01_source_notes/2026-05-21__arf_overview.md
02_concept_notes/2026-05-21__wallet_roles.md
03_project_relevance/2026-05-21__what_my_project_is.md
03_project_relevance/2026-05-21__what_my_project_is_not.md
```

Expected output:

- simple ecosystem overview
- first glossary entries
- first scope boundaries
- list of unclear terms

---

## Stage 2 — Legal foundation

Goal: understand eIDAS 2.0 only as much as needed for the project.

Main questions:

- What is the legal purpose of the European Digital Identity framework?
- What does the regulation mean for wallets?
- What does it mean for organizations that request wallet data?
- Which principles matter for business processes?
- What does the regulation imply about user control and data minimization?

Planned notes:

```text
01_source_notes/2026-05-21__eidas_2_overview.md
02_concept_notes/2026-05-21__selective_disclosure_privacy.md
03_project_relevance/2026-05-21__requirements_from_eudi_research.md
```

Expected output:

- legal context summary
- business obligations and risks
- privacy-related requirements
- initial compliance assumptions

---

## Stage 3 — Architecture and actors

Goal: understand the main actors and their responsibilities.

Main questions:

- What is an issuer?
- What is a wallet holder?
- What is a verifier?
- What is a relying party?
- What is the difference between verifier and relying party?
- What is a PID provider?
- What is an EAA provider?
- What is a QEAA provider?
- What is a QTSP?
- What trust relationships exist between these actors?

Planned notes:

```text
02_concept_notes/2026-05-21__issuer_holder_verifier_relying_party.md
02_concept_notes/2026-05-21__pid_eaa_qeaa.md
02_concept_notes/2026-05-21__trust_model.md
```

Expected output:

- role definitions
- actor responsibility table
- prototype actor mapping
- trust model summary

---

## Stage 4 — Credentials, claims, and privacy

Goal: understand what data is requested, disclosed, verified, and logged.

Main questions:

- What is PID?
- What are EAA and QEAA?
- What is a claim or attribute?
- What does selective disclosure mean?
- How can a business request only necessary data?
- What should be logged for auditability?
- What should not be stored?

Planned notes:

```text
02_concept_notes/2026-05-21__pid_eaa_qeaa.md
02_concept_notes/2026-05-21__selective_disclosure_privacy.md
03_project_relevance/2026-05-21__business_relevance_matrix.md
03_project_relevance/2026-05-21__requirements_from_eudi_research.md
```

Expected output:

- business data minimization rules
- example claim request categories
- audit-log relevance notes
- prototype requirements

---

## Stage 5 — Reference implementation overview

Goal: understand official implementation components without turning this notebook into a code notebook.

Main questions:

- Which official EUDI repositories exist?
- Which component is related to wallets?
- Which component is related to issuers?
- Which component is related to verifiers or relying parties?
- Which components are relevant for future technical comparison?
- Which components are out of scope for version 1?

Planned notes:

```text
01_source_notes/2026-05-21__eudi_reference_implementation.md
03_project_relevance/2026-05-21__what_my_project_is_not.md
```

Expected output:

- official component overview
- in-scope / out-of-scope list
- future research references

---

## Stage 6 — Business relevance mapping

Goal: translate EUDI research into project decisions.

Main questions:

- Which EUDI concepts directly affect the prototype?
- Which concepts are useful background only?
- Which concepts should become requirements?
- Which concepts should become future features?
- Which concepts are explicitly out of scope?

Planned notes:

```text
03_project_relevance/2026-05-21__business_relevance_matrix.md
03_project_relevance/2026-05-21__requirements_from_eudi_research.md
04_reviews/2026-05-21__weekly_review.md
```

Expected output:

- relevance matrix
- requirement candidates
- scope decisions
- next research tasks

---

## Research priority order

Use this order when working through the notebook:

1. ARF overview
2. EUDI roles and actors
3. eIDAS 2.0 overview
4. PID, EAA, QEAA
5. trust model
6. selective disclosure and privacy
7. reference implementation overview
8. business relevance matrix
9. requirements from EUDI research
10. weekly review

---

## Done criteria

A research note is done when it contains:

- source reference
- plain-language meaning
- relevance to this prototype
- open questions
- next action

A research stage is done when it produces at least one project-relevant decision or requirement candidate.

---

## Review rhythm

At the end of each week:

1. Review all notes created or changed that week.
2. Move unclear terms into the glossary or open questions file.
3. Add important sources to the source register.
4. Extract project-relevant requirements.
5. Write a short weekly review.
6. Decide the next research focus.
