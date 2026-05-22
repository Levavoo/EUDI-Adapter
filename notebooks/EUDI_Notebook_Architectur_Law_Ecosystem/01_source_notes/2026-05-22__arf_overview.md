# ARF Overview

Date: 2026-05-22
Status: Draft
Folder: 01_source_notes



---

## Source

Source title: Architecture and Reference Framework
Organization / author: European Commission / European Digital Identity Cooperation Group
Source type: Official architecture reference
Link:
Section / page:
Access date: 2026-05-22


| Date added | Source title | Source type | Link | Main topic | Used in note | Status |
|---|---|---|---|---|---|---|
| 2026-05-22 | EUDI Wallet Architecture and Reference Framework | Official architecture reference | https://eudi.dev/arf/ | Ecosystem, roles, PID, EAA/QEAA, relying parties, trust model, flows | 01_source_notes/2026-05-22__arf_overview.md | Reading |
---

## Meaning

What the ARF is in plain language.

---

## Relevance to my project

How the ARF helps define the relying-party-side prototype.

---

## Open questions

- [ ] What exact ARF role best matches my backend: relying party, verifier, or verifier endpoint?
- [ ] Which parts of the wallet response should my prototype simulate?
- [ ] What must be logged for auditability without storing unnecessary personal data?

---

## Next action

- [ ] Extract actor definitions into `wallet_roles.md`.
- [ ] Extract PID / EAA / QEAA definitions into `pid_eaa_qeaa.md`.
- [ ] Add ARF to `source_register.md`.

## Notes, question to answer
Who participates?
What does each actor do?
What is PID?
What are EAA and QEAA?
What does a relying party / verifier do?
How does wallet presentation roughly work?
Where does trust come from?
Which parts matter for your prototype?

# Reading order inside ARF

Do not read the full ARF from start to finish. Start only with:

Purpose / scope of the EUDI Wallet ecosystem
Roles and actors
PID, EAA, QEAA
Relying party / verifier role
Presentation / verification flow
Trust model
Privacy and selective disclosure