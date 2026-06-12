# EUDI Source Register

Date: 2026-05-21
Last updated: 2026-06-11
Status: Active register

---

## Purpose

This file tracks the sources used in the EUDI Notebook.

For each source, record source title, link, source type, specific sections used, related notebook notes, and status.

---

## Status values

| Status | Meaning |
|---|---|
| Open | Source identified but not yet processed. |
| Reading | Source currently being reviewed. |
| Processed | Source has been used in at least one note. |
| Reference | Source supports context but is not yet deeply processed. |

---

## Main sources used

| Date added | Source title | Source type | Link | Specific sections used | Related notes | Status |
|---|---|---|---|---|---|---|
| 2026-05-22 | EUDI Wallet Architecture and Reference Framework | Official architecture reference | https://eudi.dev/arf/ | General overview; 2. Definitions; 4.1 Roles in the Ecosystem; PID/EAA/QEAA concepts; wallet basics; selective disclosure/privacy; trust concepts | `01_source_notes/2026-05-22__arf_overview.md`; `01_source_notes/2026-05-26__eudi_wallet_basics.md`; `02_concept_notes/2026-05-26__wallet_roles.md`; `02_concept_notes/2026-05-26__pid_eaa_qeaa.md`; `02_concept_notes/2026-05-26__selective_disclosure_privacy_warnings.md`; `03_project_relevance/2026-05-26__ecosystem_roles_relevance_matrix.md`; `2026-05-26__glossary.md` | Processed |
| 2026-05-22 | ARF GitHub Repository | Official source repository | https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/tree/main | Repository version of the ARF; source control, change tracking, and official document structure | Same ARF-based notes as above | Processed |
| 2026-06-11 | Regulation (EU) 2024/1183 / eIDAS 2.0 | Official EU legal source | https://eur-lex.europa.eu/eli/reg/2024/1183/oj | Legal background for the European Digital Identity Framework and EUDI Wallet context | `01_source_notes/2026-06-11__eidas_2_overview.md` | Processed |
| 2026-06-11 | European Commission EUDI Wallet implementation page | Official European Commission information page | https://digital-strategy.ec.europa.eu/en/policies/eudi-wallet-implementation | EUDI Wallet implementation, pilots, reference implementation context | `01_source_notes/2026-06-11__eudi_reference_implementation.md` | Processed |
| 2026-06-11 | Official European Digital Identity Wallet GitHub organization | Official GitHub organization | https://github.com/eu-digital-identity-wallet | Reference implementation repositories and official project source code/documentation context | `01_source_notes/2026-06-11__eudi_reference_implementation.md` | Processed |

---

## Current source priority

1. ARF and ARF GitHub repository for architecture, roles, definitions, wallet concepts, and project mapping.
2. Regulation (EU) 2024/1183 / eIDAS 2.0 for legal and business context.
3. European Commission implementation page and official GitHub organization for implementation ecosystem overview.

---

## Notes

Most current notebook content is based on the ARF website and ARF GitHub repository.

The next research step is to deepen the eIDAS 2.0 note only if specific relying-party obligations become important for the prototype.
