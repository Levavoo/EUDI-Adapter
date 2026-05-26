# PID, EAA, and QEAA

Date: 2026-05-26
Status: Draft
Folder: 02_concept_notes
Tags: [CONCEPT] [ARCH] [LEGAL] [PRIVACY] [PROJECT]

---

## Source

Source title: EUDI Wallet Architecture and Reference Framework
Source section: Definitions and Roles in the Ecosystem
Source type: Official architecture reference
Primary link: https://eudi.dev/arf/
Related glossary: `../2026-05-26__glossary.md`
Related source note: `../01_source_notes/2026-05-22__arf_overview.md`

---

## Purpose of this note

This note explains the difference between:

- PID — Person Identification Data
- EAA — Electronic Attestation of Attributes
- QEAA — Qualified Electronic Attestation of Attributes

These three concepts are important because the prototype must help a relying party decide what kind of wallet data is actually needed for a business process.

The core question is:

```text
Does the business process need identity data, attribute proof, or a higher-trust qualified attribute proof?
```

---

## Short summary

| Concept | Simple meaning | Typical trust level | Example | Prototype use |
|---|---|---|---|---|
| PID | Core identity data about a person or legal entity. | High identity relevance. | Name, date of birth, personal identifier, nationality. | Used when the business process needs to know who the person or legal entity is. |
| EAA | Digital proof of an attribute. | Depends on issuer and context. | Student status, degree, membership, residence attribute. | Used when the process needs a fact about the user, not full identity. |
| QEAA | Qualified digital proof of an attribute. | Higher trust / qualified context. | Regulated professional licence, qualified company authority proof. | Used for high-assurance or regulated business cases. |

---

## PID — Person Identification Data

### Simple explanation

PID is core identity data. It helps establish who a natural person or legal person is.

In practical terms, PID is used when a relying party needs identity proof, not only a single attribute.

### Real-life example

A bank needs to identify a customer before opening an account.

The wallet may present identity-related data such as:

- legal name
- date of birth
- personal identifier
- nationality
- address or residence data, depending on the use case

### Prototype example

```json
{
  "credential_type": "PID",
  "claims": {
    "given_name": "Example",
    "family_name": "User",
    "date_of_birth": "1998-04-12",
    "age_over_18": true
  },
  "issuer": "Simulated National PID Provider",
  "issuer_trusted": true
}
```

### Relevance to the prototype

PID is relevant when the organization truly needs to identify the person.

Examples:

- employment onboarding
- account opening
- public service access
- regulated service registration

PID should not be requested when a smaller proof is enough.

Example:

```text
If the business only needs to know that the user is over 18,
it should not request full PID unless legally or operationally required.
```

---

## EAA — Electronic Attestation of Attributes

### Simple explanation

An EAA is a digital proof of one or more attributes.

It does not necessarily identify the whole person. It can prove a specific fact, status, qualification, or permission.

### Real-life example

A university issues a digital attestation that a person has completed a degree.

The wallet may present:

- degree title
- issuing university
- completion date
- study field

### Prototype example

```json
{
  "credential_type": "EAA",
  "claims": {
    "degree": "Bachelor of Science",
    "field": "Computer Science",
    "issuer_name": "Example University"
  },
  "issuer": "Simulated University",
  "issuer_trusted": true
}
```

### Relevance to the prototype

EAA is highly relevant because many business processes need only attributes, not full identity.

Examples:

- prove student status
- prove residence attribute
- prove membership
- prove qualification
- prove employment status

The prototype should encourage EAA-based requests when full PID is unnecessary.

---

## QEAA — Qualified Electronic Attestation of Attributes

### Simple explanation

A QEAA is a qualified version of an electronic attribute attestation.

It is connected to a higher-trust legal and governance context. In practice, it should be treated as stronger than a normal EAA.

### Real-life example

A qualified provider issues a professional licence attestation for a regulated profession.

Example:

- medical licence
- legal professional status
- regulated engineering qualification
- official company representation authority

### Prototype example

```json
{
  "credential_type": "QEAA",
  "claims": {
    "professional_role": "Licensed Veterinarian",
    "licence_status": "valid",
    "licence_country": "DE"
  },
  "issuer": "Simulated Qualified Attestation Provider",
  "issuer_trusted": true,
  "qualified": true
}
```

### Relevance to the prototype

QEAA is relevant for higher-assurance use cases.

Examples:

- regulated professional onboarding
- official company representation
- high-trust public-sector procedures
- cases where the relying party needs stronger assurance than a normal EAA

For version 1, QEAA can be simulated as a higher-trust credential type.

The prototype should clearly state that simulated QEAA is not a real qualified attestation.

---

## Comparison by business need

| Business need | Best fit | Reason |
|---|---|---|
| Prove user is over 18 | EAA or selective disclosure from PID | Full identity may be unnecessary. |
| Open a regulated bank account | PID | The organization likely needs identity proof. |
| Prove university degree | EAA | The business needs a qualification attribute, not full identity. |
| Prove regulated professional licence | QEAA | Higher trust may be required. |
| Prove country of residence | EAA or limited PID-derived attribute | Full address may be excessive if only country is needed. |
| Prove company representation authority | QEAA or high-trust EAA | The relying party may need strong assurance that the user can act for the company. |

---

## Relationship to ecosystem roles

| Concept | Issued by | Presented by | Received by | Related role |
|---|---|---|---|---|
| PID | PID Provider | EUDI Wallet Instance / User | Relying Party | Person Identification Data Provider |
| EAA | EAA Provider | EUDI Wallet Instance / User | Relying Party | Non-qualified Electronic Attestation Provider |
| QEAA | QEAA Provider | EUDI Wallet Instance / User | Relying Party | Qualified Electronic Attestation Provider |

Simplified relation:

```text
Provider issues PID/EAA/QEAA
→ Wallet stores or accesses it
→ User controls presentation
→ Relying Party receives and validates it
→ Audit log records the result
```

---

## Relationship to selective disclosure

PID, EAA, and QEAA should not automatically mean that all available data is shared.

The relying party should request only what is necessary.

Examples:

| Situation | Excessive request | Better request |
|---|---|---|
| Age verification | Full PID with name, date of birth, address | Proof of age over threshold |
| Residence eligibility | Full address and full PID | Country or region of residence only |
| Degree check | Full education history | Specific degree or qualification claim |
| Professional licence check | Full personal profile | Licence status and profession claim |

---

## Prototype design implications

The prototype should model these fields in verification templates and simulated responses:

| Field | Meaning | Example |
|---|---|---|
| `credential_type` | Whether the response is PID, EAA, or QEAA. | `PID`, `EAA`, `QEAA` |
| `required_claims` | Claims the relying party needs. | `age_over_18`, `residence_country` |
| `optional_claims` | Claims that may help but are not mandatory. | `preferred_name` |
| `issuer` | Who issued the credential or attestation. | `Simulated National PID Provider` |
| `issuer_trusted` | Simulated trust result. | `true` |
| `qualified` | Whether the attestation is treated as qualified. | `true` for simulated QEAA |
| `privacy_warning` | Warning if the request asks for too much data. | `Full PID requested for age-only purpose.` |
| `validation_result` | Whether the wallet response satisfies the template. | `accepted`, `rejected`, `missing_claims` |

---

## Rules for version 1

### Rule 1 — Prefer attributes over full identity

If the business process needs only a fact, request an attribute proof instead of full PID.

Example:

```text
Need: user is over 18
Prefer: age_over_18 claim
Avoid: full date of birth, full name, full address
```

### Rule 2 — Use PID only when identity is actually required

PID should be used for processes where knowing the person's identity is necessary.

Example:

```text
Employment onboarding may require identity proof.
Simple age verification usually does not.
```

### Rule 3 — Treat QEAA as high-trust but simulated

Version 1 may represent QEAA in data models, but must not claim real qualification or legal validation.

Example:

```text
The prototype may show: credential_type = QEAA.
It must not claim: this is a real qualified attestation.
```

### Rule 4 — Record the reason for the requested data

Every verification template should include a business purpose.

Example:

```text
Purpose: verify eligibility for employment onboarding.
Required claims: identity confirmation, work authorization, professional licence status.
```

---

## In scope for version 1

- Model PID, EAA, and QEAA as credential types.
- Create example verification templates using these types.
- Simulate wallet responses containing claims.
- Check whether required claims are present.
- Simulate issuer trust status.
- Generate privacy warnings for excessive requests.
- Log validation results.

---

## Out of scope for version 1

- Real PID issuance.
- Real EAA issuance.
- Real QEAA issuance.
- Real cryptographic proof validation.
- Real trusted-list integration.
- Legal certification.
- Acting as a PID, EAA, QEAA, QTSP, or wallet provider.

---

## Open questions

- [ ] Which credential types should be supported in the first verification-template schema?
- [ ] Should `PID`, `EAA`, and `QEAA` be stored as simple strings or modeled as separate objects?
- [ ] Which example use cases should use PID and which should use EAA?
- [ ] Should the dashboard show a privacy warning when PID is requested but EAA would be enough?
- [ ] Which simulated trust fields are enough for version 1?

---

## Next action

- [ ] Create example verification templates for age verification, residence verification, and employment onboarding.
- [ ] Add privacy-warning rules based on excessive PID requests.
- [ ] Connect this note to the future selective disclosure concept note.
- [ ] Reuse the comparison table in project documentation.
