# ARF Overview

Date: 2026-05-22
Status: Draft
Folder: 01_source_notes
Tags: [SOURCE] [ARCH] [TRUST] [PRIVACY] [PROJECT]

---

## Source

Source title: EUDI Wallet Architecture and Reference Framework
Organization / author: European Digital Identity Cooperation Group / European Commission context
Source type: Official architecture reference
Primary link: https://eudi.dev/arf/
Repository link: https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework
Official organization: https://github.com/eu-digital-identity-wallet
Section / page: Main ARF page, especially Introduction, Definitions, Use Cases, Ecosystem Roles, PID and (Q)EAA, Reference Architecture and Flows
Access date: 2026-05-22

---

## Source register entry

| Date added | Source title | Source type | Link | Main topic | Used in note | Status |
|---|---|---|---|---|---|---|
| 2026-05-22 | EUDI Wallet Architecture and Reference Framework | Official architecture reference | https://eudi.dev/arf/ | Ecosystem, roles, PID, EAA/QEAA, relying parties, trust model, flows | 01_source_notes/2026-05-22__arf_overview.md | Reading |

---

## Why this source matters

The Architecture and Reference Framework, shortened as ARF, is the best first source for this notebook because it connects legal, architectural, ecosystem, and implementation concepts.

For this project, the ARF is useful because it explains the EUDI Wallet ecosystem from the perspective of roles, responsibilities, data objects, trust relationships, and verification flows.

This is more useful as a first source than starting directly with legal text because the prototype needs to understand practical wallet verification scenarios before mapping them to requirements.

---

## Meaning

The ARF is the common architecture reference for the European Digital Identity Wallet ecosystem.

In plain language, it explains:

- what the EUDI Wallet is supposed to do
- which actors participate in the ecosystem
- how identity data and attribute attestations are issued and presented
- what PID, EAA, and QEAA mean
- how relying parties interact with wallet users
- how trust is established between ecosystem participants
- which flows and architecture components are expected
- how privacy and user control should shape wallet-based interactions

The ARF should be treated as an architecture and ecosystem guide, not as the final legal authority. Legal obligations must be checked against eIDAS 2.0, implementing acts, and other official legal sources.

---

## Important ARF areas for this project

### 1. Purpose and scope

The ARF describes the architecture and reference model for EUDI Wallet solutions and the surrounding ecosystem.

For this prototype, the important point is not to build a wallet. The important point is to understand how an organization should prepare, justify, execute, and document wallet-based verification requests.

### 2. Roles and actors

The ARF lists ecosystem roles such as:

- EUDI Wallet user
- EUDI Wallet provider
- PID provider
- EAA provider
- QEAA provider
- relying party
- trusted list provider
- authentic source
- trust service provider
- conformity assessment body
- supervisory body

For this prototype, the most important role is the relying party / verifier side.

The organization using the prototype is assumed to be the party that wants to request and rely on wallet-provided identity or attribute information.

### 3. PID, EAA, and QEAA

The ARF distinguishes between identity data and attribute attestations.

Working definitions for this project:

- PID means person identification data that can establish the identity of a natural or legal person.
- EAA means electronic attestation of attributes.
- QEAA means qualified electronic attestation of attributes, normally connected to a higher-trust qualified provider context.

For this prototype, these concepts help define what kind of claims a business process may request.

Example:

- age verification may need only an age-over-threshold result, not a full birth date
- residence verification may need country or address-related attributes
- employment onboarding may need stronger identity and qualification attributes

### 4. Relying party / verifier role

A relying party is the organization or service that relies on wallet-based identification or attested attributes.

For this project, the relying party perspective is central.

The prototype should help answer:

- What does the business process need to verify?
- Which attributes are necessary?
- Which attributes are excessive?
- What purpose should be declared?
- What wallet response should be accepted?
- What audit event should be recorded?

### 5. Presentation and verification flow

The ARF describes flows where wallet users present identity data or attestations to relying parties.

For this prototype, the flow can be simplified as:

```text
Business need
→ verification template
→ wallet request
→ user-controlled wallet response
→ validation result
→ audit log
```

This simplified flow is enough for the current prototype because the project uses simulated wallet responses instead of a real wallet integration.

### 6. Trust model

The ARF introduces a trust model around legitimate ecosystem actors, wallet components, providers, attestations, and trust lists.

For this prototype, the trust model is important as business logic, not as full cryptographic implementation.

The prototype should eventually be able to explain:

- which issuer or provider a credential claims to come from
- whether the credential type is accepted for the business process
- whether the response satisfies the requested claims
- whether the request was minimal and purpose-bound
- what was checked and recorded in the audit log

### 7. Privacy and selective disclosure

The ARF includes selective disclosure as an important wallet capability.

For this project, selective disclosure means the system should prefer minimal requests over collecting full identity data.

Business rule:

```text
Request only the claims needed for the business purpose.
```

Example:

```text
Bad request:
Request full name, birth date, address, nationality, and PID for simple age verification.

Better request:
Request proof that the user is over the required age threshold.
```

---

## Relevance to my project

This source is directly relevant because the prototype is a relying-party-side integration concept.

The ARF helps define what the prototype should represent:

- a business process has an identity-check requirement
- the requirement is translated into a wallet verification request
- the request should follow data minimization principles
- the wallet response should be checked against the original business requirement
- the result should be recorded in an audit log
- the system should make clear what was requested, why it was requested, and what was validated

The prototype should not claim to be a certified EUDI Wallet, PID provider, QEAA provider, QTSP, or official trust infrastructure.

---

## Project scope impact

### In scope for version 1

- model relying-party-side business requirements
- define verification templates
- simulate wallet requests
- simulate wallet responses
- check whether a simulated response satisfies the request
- record audit events
- show privacy warnings when requests are excessive
- explain project concepts using ARF terminology

### Out of scope for version 1

- building a real EUDI Wallet
- issuing real PID
- issuing real EAA or QEAA
- integrating with production trust lists
- implementing full cryptographic validation
- acting as a QTSP
- claiming legal certification or formal conformance
- connecting to real citizen identity data

---

## Questions answered from the first reading

### Who participates?

The ecosystem includes users, wallet providers, PID providers, EAA/QEAA providers, relying parties, trusted list providers, authentic sources, trust service providers, conformity assessment bodies, supervisory bodies, and related technical or governance actors.

### What does each actor do?

At a high level:

- the user controls and uses the wallet
- the wallet provider provides the wallet solution
- PID providers issue person identification data
- EAA/QEAA providers issue attribute attestations
- relying parties request and rely on wallet-presented data
- trusted list providers support trust decisions
- authentic sources are authoritative sources for attributes
- supervisory and conformity bodies support governance and certification

### What is PID?

PID is person identification data used to establish the identity of a person or legal entity.

### What are EAA and QEAA?

EAA are electronic attestations of attributes.

QEAA are qualified electronic attestations of attributes, connected to qualified trust and stronger assurance requirements.

### What does a relying party / verifier do?

A relying party requests and relies on identity or attribute information presented from the wallet. In this project, the relying party is the business-side actor whose requirements are converted into verification templates and wallet requests.

### How does wallet presentation roughly work?

A simplified wallet presentation flow is:

```text
Relying party requests specific claims
→ user reviews and consents through wallet
→ wallet presents selected PID or attributes
→ relying party verifies whether response satisfies the request
→ relying party records the outcome
```

### Where does trust come from?

Trust comes from a combination of legal rules, trusted ecosystem actors, trusted lists, issuer/provider status, wallet certification, technical validation, and governance rules.

For this prototype, trust will initially be simulated as business validation logic.

### Which parts matter for the prototype?

Most relevant:

- relying party role
- verification request purpose
- requested claims
- PID / EAA / QEAA terminology
- privacy and selective disclosure
- trust model basics
- auditability
- scope boundaries

Less relevant for version 1:

- real wallet certification
- real cryptographic trust validation
- real issuer onboarding
- production wallet lifecycle management
- QTSP operations

---

## Concepts to extract into other notes

| Concept | Target note | Priority |
|---|---|---|
| Ecosystem roles | `02_concept_notes/2026-05-22__wallet_roles.md` | High |
| Issuer / holder / verifier / relying party | `02_concept_notes/2026-05-22__issuer_holder_verifier_relying_party.md` | High |
| PID / EAA / QEAA | `02_concept_notes/2026-05-22__pid_eaa_qeaa.md` | High |
| Trust model | `02_concept_notes/2026-05-22__trust_model.md` | Medium |
| Selective disclosure and privacy | `02_concept_notes/2026-05-22__selective_disclosure_privacy.md` | High |
| What my project is | `03_project_relevance/2026-05-22__what_my_project_is.md` | High |
| What my project is not | `03_project_relevance/2026-05-22__what_my_project_is_not.md` | High |
| Requirements from EUDI research | `03_project_relevance/2026-05-22__requirements_from_eudi_research.md` | High |

---

## Open questions

- [ ] What exact ARF role best matches my backend: relying party, verifier, verifier endpoint, or relying-party integration layer?
- [ ] Which ARF sections define relying party obligations most clearly?
- [ ] Which parts of the wallet response should the prototype simulate first?
- [ ] What should be logged for auditability without storing unnecessary personal data?
- [ ] Which privacy warnings should the prototype show when a request asks for too much data?
- [ ] How should the prototype distinguish PID, EAA, and QEAA in a business-friendly way?
- [ ] Which trust checks can be simulated in version 1 without misleading users into thinking this is real legal/technical validation?

---

## Next action

- [ ] Add this source to `2026-05-21__source_register.md`.
- [ ] Create `02_concept_notes/2026-05-22__wallet_roles.md`.
- [ ] Create `02_concept_notes/2026-05-22__pid_eaa_qeaa.md`.
- [ ] Create `03_project_relevance/2026-05-22__what_my_project_is.md`.
- [ ] Create `03_project_relevance/2026-05-22__what_my_project_is_not.md`.
- [ ] Review ARF sections about relying parties and presentation flows in more detail.

---

## Reading order inside ARF

Do not read the full ARF from start to finish in one pass.

Use this order:

1. Purpose / scope of the EUDI Wallet ecosystem
2. Roles and actors
3. PID, EAA, QEAA
4. Relying party / verifier role
5. Presentation / verification flow
6. Trust model
7. Privacy and selective disclosure
8. Requirements that affect relying parties
9. Reference architecture and flows

---

## Current conclusion

The ARF confirms that this prototype should be positioned as a relying-party-side support tool.

The prototype should help organizations define privacy-preserving verification requests, process simulated wallet responses, and document what happened in an audit-friendly way.

The prototype should clearly state that it is not a real wallet, issuer, QTSP, PID provider, QEAA provider, trust list service, or certified EUDI component.
