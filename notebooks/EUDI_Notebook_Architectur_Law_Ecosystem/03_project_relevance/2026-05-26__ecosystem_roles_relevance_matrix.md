# Ecosystem Roles Relevance Matrix

Date: 2026-05-26
Status: Draft
Folder: 03_project_relevance
Tags: [PROJECT] [ARCH] [DECISION] [IHK]

---

## Source

Source title: EUDI Wallet Architecture and Reference Framework
Source section: 4.1. Roles in the Ecosystem
Source type: Official architecture reference
Primary link: https://eudi.dev/arf/#41-roles-in-the-ecosystem
Related glossary: `../2026-05-26__glossary.md`
Related concept notes:

- `../02_concept_notes/2026-05-26__wallet_roles.md`
- `../02_concept_notes/2026-05-26__pid_eaa_qeaa.md`
- `../02_concept_notes/2026-05-26__selective_disclosure_privacy_warnings.md`

---

## Purpose of this matrix

This matrix translates the EUDI Wallet ecosystem roles into project relevance.

The goal is to decide:

- which roles must be represented in the prototype
- which roles are useful as metadata or background
- which roles are out of scope for version 1
- which roles may become future features
- how each role affects verification templates, simulated wallet responses, privacy warnings, and audit logs

This file is project-facing. It should help with scope decisions, README explanations, IHK documentation, and future implementation planning.

---

## Project viewpoint

The prototype is a **relying-party-side support tool**.

It helps an organization:

```text
business identity-check requirement
→ verification template
→ simulated wallet request/response
→ validation result
→ privacy warning
→ audit log
```

The prototype is not a real EUDI Wallet and does not issue real PID, EAA, or QEAA.

---

## Relevance scale

| Relevance | Meaning |
|---|---|
| High | Must be represented in version 1 or strongly shapes the prototype. |
| Medium | Useful for modeling, documentation, or future extension. |
| Low | Background context only for version 1. |
| Out of scope | Should not be implemented in version 1. |

---

## Ecosystem roles relevance matrix

| No. | Ecosystem role | Relevance | Why it matters | Prototype representation | Version 1 decision |
|---:|---|---|---|---|---|
| 1 | End User of EUDI Wallet | High | The user controls wallet presentation and decides what to share. | Simulated actor behind wallet response; consent/presentation status. | Represent indirectly through simulated wallet response metadata. |
| 2 | EUDI Wallet Provider | Low | Explains who provides the wallet solution, but the project does not build wallets. | Boundary/documentation only. | Out of implementation scope. Mention in docs. |
| 3 | Person Identification Data Provider | High | PID provider is the source of identity data used in identity verification scenarios. | Simulated issuer/provider metadata for PID credentials. | Represent as issuer metadata. No real issuing. |
| 4 | Trusted List Provider | Medium/High | Supports trust decisions about providers and possibly relying parties. | Simulated trust-check field such as `issuer_trusted`. | Simulate only. Real trusted-list integration is future scope. |
| 5 | QEAA Provider | Medium | Important for high-assurance or regulated attribute proof scenarios. | Simulated issuer/provider metadata for QEAA. | Represent as credential type and issuer metadata. |
| 6 | EAA Provider | High | Many business use cases need attribute proof instead of full identity. | Simulated issuer/provider metadata for EAA. | Represent in verification templates and wallet responses. |
| 7 | Qualified/non-qualified certificate provider for electronic signature/seal | Low | Relevant for signing/sealing, but not central to current verification prototype. | None in version 1, possibly documentation note. | Out of implementation scope unless signing use case is added. |
| 8 | Authentic Source | Medium/High | Explains original authoritative source of data behind PID/EAA/QEAA. | Source metadata such as `source_type` or `authentic_source`. | Represent as optional metadata in simulated responses. |
| 9 | Relying Party | Highest | The prototype is built from this actor's perspective. | Main system user/organization; owner of verification templates and audit logs. | Core role of the prototype. |
| 10 | Conformity Assessment Body (CAB) | Low | Relevant for certification and conformity, not direct business verification flow. | Documentation only. | Out of implementation scope. |
| 11 | Supervisory Body | Low | Legal/governance supervision context. | Documentation only. | Out of implementation scope. |
| 12 | Device manufacturers and related subsystem providers | Low | Important for real wallet security, but unrelated to business-side prototype logic. | Documentation only. | Out of implementation scope. |
| 13 | (Q)EAA Schema Provider | Medium | Schemas define how attribute attestations are structured. Useful for future template alignment. | Future schema references; possible `credential_schema` metadata. | Mention in docs; implement later if needed. |
| 14 | National Accreditation Body | Low | Governance actor behind CAB accreditation. | Documentation only. | Out of implementation scope. |

---

## Core roles for version 1

These roles should actively shape the first prototype:

| Role | Prototype responsibility |
|---|---|
| Relying Party | Defines business purpose, required claims, accepted credential types, and audit needs. |
| End User | Controls whether wallet data is presented. Represented by consent/presentation status. |
| EUDI Wallet Instance | Produces the simulated wallet response. |
| PID Provider | Simulated source of identity credentials. |
| EAA Provider | Simulated source of attribute attestations. |
| QEAA Provider | Simulated source of higher-trust qualified attribute attestations. |
| Authentic Source | Optional metadata explaining where data originates. |
| Trusted List Provider | Simulated trust decision source. |

---

## Version 1 prototype mapping

| Project object | Ecosystem role connection | Required in version 1? | Notes |
|---|---|---|---|
| Verification Template | Relying Party | Yes | Central object. Defines purpose and required claims. |
| Requested Claim | Attribute / PID / EAA / QEAA | Yes | Defines what the relying party wants to verify. |
| Simulated Wallet Response | End User + EUDI Wallet Instance | Yes | Represents what the user presents. |
| Credential Type | PID Provider / EAA Provider / QEAA Provider | Yes | Values: `PID`, `EAA`, `QEAA`. |
| Issuer Metadata | PID/EAA/QEAA Provider | Yes | Needed to explain who issued the simulated proof. |
| Trust Check Result | Trusted List Provider / Trust Model | Yes, simulated | Use simple fields first, not real trust-list integration. |
| Source Metadata | Authentic Source | Optional | Useful for explanation and future trust modeling. |
| Privacy Warning | Relying Party + Selective Disclosure | Yes | Flags excessive or unclear requests. |
| Audit Log Event | Relying Party | Yes | Records request, response, validation, and warning events. |
| Credential Schema Reference | (Q)EAA Schema Provider | Later | Useful when templates become more formal. |
| Wallet Provider Metadata | EUDI Wallet Provider | No | Out of scope for version 1. |
| Device Metadata | Device Manufacturer | No | Out of scope for version 1. |
| Certification Metadata | CAB / NAB / Supervisory Body | No | Out of scope for version 1. |

---

## Recommended version 1 fields

These fields follow from the ecosystem role analysis.

### Verification template fields

| Field | Reason |
|---|---|
| `template_id` | Identify the verification template. |
| `business_purpose` | Explain why the relying party requests data. |
| `use_case` | Connect request to a business scenario. |
| `required_claims` | Define minimum data needed. |
| `optional_claims` | Separate useful but non-required data. |
| `accepted_credential_types` | Define whether PID, EAA, or QEAA are accepted. |
| `retention_policy` | Explain what is stored and for how long. |
| `audit_policy` | Define what should be logged. |
| `privacy_review_required` | Mark whether request needs review. |

### Simulated wallet response fields

| Field | Related role | Reason |
|---|---|---|
| `response_id` | Wallet Instance | Identify simulated response. |
| `presentation_status` | User | Show whether user presented/approved data. |
| `credential_type` | PID/EAA/QEAA Provider | Show kind of credential or attestation. |
| `claims` | Attribute | Store presented claims. |
| `issuer` | PID/EAA/QEAA Provider | Show who issued data. |
| `issuer_type` | PID/EAA/QEAA Provider | Distinguish provider type. |
| `issuer_trusted` | Trusted List Provider | Simulated trust result. |
| `authentic_source` | Authentic Source | Optional source metadata. |
| `extra_claims_present` | Selective Disclosure | Detect over-disclosure. |

### Audit log fields

| Field | Reason |
|---|---|
| `event_type` | Identifies what happened. |
| `template_id` | Links event to request. |
| `response_id` | Links event to wallet response. |
| `actor_role` | Shows whether event came from relying party/system/wallet simulation. |
| `requested_claims_count` | Helps evaluate minimization. |
| `received_claims_count` | Helps detect over-disclosure. |
| `validation_result` | Shows accepted/rejected/missing claims. |
| `privacy_warning_count` | Records warnings. |
| `raw_personal_data_stored` | Important privacy/audit flag. |
| `created_at` | Timestamp for traceability. |

---

## Business-process relevance

| Business process | Most relevant roles | Why |
|---|---|---|
| Age verification | Relying Party, User, Wallet Instance, EAA/PID Provider | Needs minimal eligibility proof, not full identity. |
| Residence verification | Relying Party, User, Wallet Instance, PID/EAA Provider, Authentic Source | Needs residence-related claim from trusted source. |
| Employment onboarding | Relying Party, User, PID Provider, EAA/QEAA Provider, Authentic Source | May need identity and qualification proof. |
| Professional licence check | Relying Party, User, QEAA Provider, Authentic Source, Trusted List Provider | Higher-trust attribute verification may be needed. |
| Company representative check | Relying Party, User, QEAA/EAA Provider, Authentic Source | Needs proof that a user may act for an organization. |

---

## Priority decisions

### Decision 1 — Relying Party is the core actor

The prototype should be described as a relying-party-side support tool.

It should not be described as:

- an EUDI Wallet
- a wallet provider
- a PID provider
- an EAA/QEAA provider
- a QTSP
- a trusted-list service

### Decision 2 — Providers are simulated as metadata

PID, EAA, and QEAA providers should be represented through metadata in simulated wallet responses.

Example:

```json
{
  "issuer": "Simulated National PID Provider",
  "issuer_type": "PID_PROVIDER",
  "issuer_trusted": true
}
```

### Decision 3 — Trust is simulated, not implemented

Trusted-list behavior should be represented as a simulated result.

Example:

```json
{
  "trust_check": {
    "issuer_trusted": true,
    "method": "simulated_trusted_list_check"
  }
}
```

The system must not imply real legal or cryptographic trust validation in version 1.

### Decision 4 — Authentic source is useful but optional

Authentic source metadata is useful for explanation, but it should not block version 1.

Example:

```json
{
  "authentic_source": {
    "source_type": "population_register",
    "simulated": true
  }
}
```

### Decision 5 — Governance roles stay documentation-only

CABs, supervisory bodies, national accreditation bodies, and device manufacturers should stay in research/documentation for version 1.

They should not become implementation objects until there is a concrete use case.

---

## Scope table

| Role / concept | Version 1 scope | Future scope |
|---|---|---|
| Relying Party | Core | More detailed registration/authorization logic. |
| User | Simulated consent/presentation status | More detailed consent flow. |
| Wallet Instance | Simulated response source | Real wallet integration. |
| PID Provider | Simulated issuer metadata | Real issuer validation. |
| EAA Provider | Simulated issuer metadata | Real attestation validation. |
| QEAA Provider | Simulated issuer metadata | Qualified trust validation. |
| Trusted List Provider | Simulated trust flag | Real trusted-list lookup. |
| Authentic Source | Optional metadata | Source verification or registry mapping. |
| Schema Provider | Documentation only | Credential schema validation. |
| Wallet Provider | Documentation only | Real wallet compatibility notes. |
| Device Manufacturer | Out of scope | Only relevant if wallet/device security is studied. |
| CAB / NAB / Supervisory Body | Documentation only | Certification/compliance documentation. |

---

## Risks if roles are misunderstood

| Misunderstanding | Risk | Correction |
|---|---|---|
| Treating the prototype as a wallet | Scope becomes too large and misleading. | State clearly: relying-party-side prototype only. |
| Treating simulated trust as real trust | Users may believe the system performs legal/cryptographic validation. | Label all trust checks as simulated in version 1. |
| Requesting PID for every use case | Privacy risk and poor data minimization. | Prefer EAA or selective disclosure where possible. |
| Ignoring issuer/provider metadata | Validation becomes unrealistic. | Include issuer and issuer type in simulated responses. |
| Ignoring audit logs | Business process is hard to justify or review. | Log request, validation result, and privacy warnings. |
| Treating governance roles as implementation tasks | Project becomes too broad. | Keep governance roles as documentation-only for v1. |

---

## IHK / presentation relevance

This matrix can be used to explain the project scope:

```text
The project focuses on the relying-party side of the EUDI Wallet ecosystem.
It does not build a wallet or issue real credentials.
Instead, it models how an organization can translate a business verification need into a privacy-aware wallet request, evaluate a simulated wallet response, and create an audit trail.
```

This gives the project a clear business and architecture boundary.

---

## Open questions

- [ ] Should the first prototype store `issuer_type` as `PID_PROVIDER`, `EAA_PROVIDER`, or `QEAA_PROVIDER`?
- [ ] Should `issuer_trusted` be a boolean or a more detailed object?
- [ ] Should `authentic_source` be included in version 1 examples?
- [ ] Should relying-party registration be modeled now or left for future scope?
- [ ] Which roles should be shown in the first dashboard diagram?
- [ ] Should the audit log store claim names only, or also claim values in demo mode?

---

## Next action

- [ ] Use this matrix to update project scope documentation.
- [ ] Use the recommended fields when designing verification-template schema.
- [ ] Use the recommended fields when designing simulated wallet response examples.
- [ ] Create example use cases for age verification, residence verification, and employment onboarding.
- [ ] Keep governance roles in documentation only for version 1.
