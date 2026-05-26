# EUDI Wallet Basics

Date: 2026-05-26
Status: Draft
Folder: 01_source_notes
Tags: [SOURCE] [CONCEPT] [ARCH] [PRIVACY] [PROJECT] [IHK]

---

## Source

Source title: EUDI Wallet Architecture and Reference Framework
Source sections: General ARF overview, definitions, ecosystem roles, wallet concepts, privacy concepts
Source type: Official architecture reference
Primary link: https://eudi.dev/arf/
Related sources:

- Regulation (EU) 2024/1183 / eIDAS 2.0: https://eur-lex.europa.eu/eli/reg/2024/1183/oj
- European Commission EUDI Wallet information: https://digital-strategy.ec.europa.eu/en/policies/eudi-wallet-implementation

Related project notes:

- `2026-05-22__arf_overview.md`
- `../2026-05-26__glossary.md`
- `../02_concept_notes/2026-05-26__wallet_roles.md`
- `../02_concept_notes/2026-05-26__pid_eaa_qeaa.md`
- `../02_concept_notes/2026-05-26__selective_disclosure_privacy_warnings.md`

---

## Purpose of this note

This note answers the first basic questions needed to understand the EUDI Wallet from a business and relying-party perspective.

The goal is not to explain the full regulation or full technical architecture.

The goal is to create a simple foundation for the prototype:

```text
Business needs identity or attribute proof
→ relying party creates a wallet verification request
→ user presents selected wallet data
→ system validates the response
→ audit log records what happened
```

---

## 1. What is the EUDI Wallet?

The EUDI Wallet is a digital wallet model for the European Digital Identity ecosystem.

In simple terms, it allows a person or legal entity to store, manage, and present identity data and digital credentials in a controlled way.

A wallet user can use it to prove things about themselves without always sharing full documents or unnecessary personal data.

### Simple example

A person wants to access an age-restricted online service.

Instead of uploading an ID card scan, the wallet can present only:

```text
age_over_18 = true
```

The service receives the proof it needs without receiving the full ID card copy.

### Relevance to my project

The prototype does not build the wallet.

It models the organization side:

```text
What does the relying party need to verify?
Which claims are necessary?
What wallet response should be accepted?
What should be logged?
```

---

## 2. What is eIDAS?

eIDAS is the EU legal framework for electronic identification and trust services.

The newer European Digital Identity framework builds on eIDAS and introduces the EUDI Wallet ecosystem.

In simple terms:

```text
eIDAS = legal framework
EUDI Wallet = wallet ecosystem enabled by that framework
ARF = architecture/reference model explaining how the ecosystem should work
```

### Simple example

A business wants to rely on a digital proof from a user's wallet.

eIDAS provides the legal background for digital identity and trust services, while the ARF explains the roles, flows, and architecture concepts.

### Relevance to my project

eIDAS matters because the prototype operates in a regulated identity/trust context.

However, the prototype must not claim legal certification or real production compliance.

Version 1 should say:

```text
This is a simulated relying-party-side prototype inspired by EUDI Wallet concepts.
```

---

## 3. What is the difference between issuer, holder, and relying party?

These three roles are central to digital credential flows.

| Role | Simple explanation | Real-life example | Prototype equivalent |
|---|---|---|---|
| Issuer | Actor that creates or issues a credential/attestation. | A university issues a degree credential. A state authority issues PID. | Simulated issuer metadata in the wallet response. |
| Holder | The user or wallet that holds and presents the credential. | A citizen has identity data or degree proof in their wallet. | Simulated wallet user / wallet response. |
| Relying Party | Actor that requests and relies on the presented data. | Employer, bank, online service, public office. | Main project perspective: organization creating verification templates. |

### Simple flow

```text
Issuer gives credential to Holder
→ Holder presents selected proof
→ Relying Party checks and relies on it
```

### Example

```text
University issues degree proof
→ Candidate stores/presents it through wallet
→ Employer verifies degree during onboarding
```

### Relevance to my project

The prototype represents the relying-party side.

It does not issue credentials and it does not act as the user's wallet.

---

## 4. What kind of data can be stored in a wallet?

A wallet can hold or access different kinds of identity and attribute data, depending on implementation and regulation.

Important categories for this project:

| Data type | Simple meaning | Example | Project relevance |
|---|---|---|---|
| PID | Person Identification Data. Core identity data. | Name, date of birth, personal identifier, nationality. | Used when identity proof is truly needed. |
| EAA | Electronic Attestation of Attributes. Digital proof of an attribute. | Student status, degree, residence attribute, membership. | Useful when a business needs a fact, not full identity. |
| QEAA | Qualified Electronic Attestation of Attributes. Higher-trust attribute proof. | Regulated professional licence, qualified company authority proof. | Useful for higher-assurance scenarios. |
| Certificates | Data related to electronic signatures/seals. | Signing certificate, seal certificate. | Mostly out of scope for version 1. |
| Presentation proofs | Selected data or proof presented to a relying party. | `age_over_18 = true`. | Core for simulated wallet responses. |

### Important note

The wallet model does not mean every relying party should receive all wallet data.

The relying party should request only the necessary claims.

---

## 5. What is a digital credential?

A digital credential is a digital proof or attestation that contains claims about a person, legal entity, or thing.

A credential is not just a normal file. It should have structured data and trust information, such as issuer information and proof that it was issued by the right actor.

### Simple example

A university degree credential may contain:

```json
{
  "credential_type": "EAA",
  "issuer": "Example University",
  "claims": {
    "degree": "Bachelor of Science",
    "field": "Computer Science",
    "graduation_year": 2025
  }
}
```

### Relevance to my project

The prototype can simulate credentials as structured wallet responses.

This helps the relying party check:

- who issued the credential
- what claims it contains
- whether required claims are present
- whether the issuer is trusted in the simulated scenario
- whether unnecessary data was included

---

## 6. What does a relying party want from a wallet?

A relying party wants trustworthy proof that satisfies a business need.

It usually does not want the wallet itself. It wants answers to specific verification questions.

### Examples

| Business question | Wallet proof needed |
|---|---|
| Is the user over 18? | `age_over_18 = true` |
| Does the user live in Germany? | `country_of_residence = DE` |
| Is the user a student? | `student_status = active` |
| Does the user have a required qualification? | Degree or licence attestation. |
| Is this person allowed to represent a company? | Company representation authority proof. |

### Relevance to my project

The prototype should start from business questions, not from data collection.

Good design:

```text
Business need → required claims → accepted credential type → validation rule
```

Bad design:

```text
Ask for everything and decide later.
```

---

## 7. Why should a relying party avoid requesting unnecessary data?

A relying party should avoid unnecessary data because excessive requests create privacy, compliance, security, and trust risks.

### Main reasons

| Reason | Simple explanation | Example |
|---|---|---|
| Privacy | Users should not reveal more than needed. | Age check should not require full address. |
| Data minimization | Collect only what is necessary for the purpose. | Ask for `country_of_residence`, not full address, if country is enough. |
| Lower security risk | Less collected data means less data to protect. | If no full ID copy is stored, there is less damage in a breach. |
| Better user trust | Users are more likely to trust a request that is clear and minimal. | Wallet request clearly says: only age-over-18 proof requested. |
| Easier audit | A minimal request is easier to justify later. | Audit log shows purpose and required claim only. |

### Relevance to my project

The prototype should create privacy warnings when a request asks for too much data.

Example warning:

```text
Full PID requested for age-only purpose. Consider requesting age_over_18 instead.
```

---

## 8. What does selective disclosure mean?

Selective disclosure means that the user can share only selected claims instead of a full document or full identity profile.

It supports the principle:

```text
Share only what is needed for the purpose.
```

### Simple examples

| Scenario | Instead of sharing | Selectively disclose |
|---|---|---|
| Age check | Full ID card | `age_over_18 = true` |
| Residence check | Full address | `country_of_residence = DE` |
| Student discount | Full identity + full education history | `student_status = active` |
| Licence check | Full personal profile | `licence_status = valid` |

### Relevance to my project

Selective disclosure should become practical logic in the prototype.

The system should help the relying party choose minimal claims and should warn when the request is excessive.

---

## 9. Why is user consent important?

User consent is important because the wallet model is user-controlled.

The user should understand what is being requested, why it is requested, and which data will be presented.

### Simple example

A service requests:

```text
age_over_18
```

The wallet shows the user what will be shared.

The user approves the presentation.

The relying party receives only the selected proof.

### Relevance to my project

The prototype should represent consent/presentation status in simulated responses.

Example:

```json
{
  "presentation_status": "approved_by_user",
  "claims_presented": ["age_over_18"]
}
```

This reminds the project that wallet verification is not the same as a hidden backend data lookup.

The user is part of the flow.

---

## 10. How does the wallet model differ from uploading a PDF copy of an ID card?

Uploading a PDF copy of an ID card is document-based and often over-discloses personal data.

The wallet model is structured, claim-based, user-controlled, and better suited to selective disclosure.

| Aspect | PDF copy of ID card | Wallet model |
|---|---|---|
| Data format | Static image/PDF document | Structured digital claims/credentials |
| Data amount | Often reveals everything on the document | Can reveal only selected claims |
| User control | User uploads a copy, often hard to control later | User approves a specific presentation |
| Verification | Manual or document-processing based | Claim/credential-based validation possible |
| Privacy | High risk of over-disclosure | Supports data minimization |
| Storage risk | Copy may be stored by the relying party | Result or proof can be logged without storing full document |
| Auditability | Harder to prove exactly what was checked | Request, claims, result, and warnings can be logged |
| Reuse risk | Copies can be reused or leaked | Presentation can be purpose-specific |

### Simple example

PDF approach:

```text
User uploads ID card scan.
Relying party sees name, birth date, address, document number, photo, and more.
```

Wallet approach:

```text
Relying party requests age_over_18.
User presents only age_over_18 = true.
Relying party stores verification result, not a full ID copy.
```

### Relevance to my project

This difference is central to the prototype.

The prototype should show that wallet-based verification is not just digital document upload.

It is a structured process:

```text
purpose → minimal claims → user-controlled presentation → validation → audit log
```

---

## Combined real-life example: age verification

| Step | PDF copy model | Wallet model | Prototype model |
|---:|---|---|---|
| 1 | Service asks user to upload ID scan. | Service requests age proof. | Relying party creates age verification template. |
| 2 | User uploads full ID document. | User approves sharing age-over-threshold proof. | Simulated wallet response includes `age_over_18 = true`. |
| 3 | Service manually or automatically checks date of birth. | Service checks structured claim. | Prototype validates required claim. |
| 4 | Service may store ID copy. | Service can store only result/audit event. | Audit log records result without raw personal data. |
| 5 | High over-disclosure risk. | Lower data exposure. | Privacy warning appears if full PID is requested. |

---

## Project design rules derived from this note

| Rule | Meaning | Prototype effect |
|---|---|---|
| Start from purpose | Define why data is needed before requesting claims. | Verification template requires `business_purpose`. |
| Request minimal claims | Ask only for what satisfies the purpose. | Privacy-warning rules check excessive data. |
| Prefer attributes over full identity where possible | Use EAA/selective claim instead of PID when identity is not required. | Age check should use `age_over_18`, not full PID. |
| Record issuer/provider metadata | Relying party needs to know where data came from. | Simulated wallet response includes `issuer` and `issuer_type`. |
| Represent user-controlled presentation | Wallet flow includes user approval/presentation. | Simulated response includes `presentation_status`. |
| Avoid storing raw personal data when result is enough | Store validation outcome rather than full claim values where possible. | Audit log can use `raw_personal_data_stored = false`. |

---

## In scope for version 1

- Explain the EUDI Wallet in simple business terms.
- Model the relying-party perspective.
- Simulate wallet responses as structured credentials/claims.
- Use PID, EAA, and QEAA as credential categories.
- Add privacy warnings for excessive requests.
- Show how wallet verification differs from PDF upload.
- Record validation results in an audit log.

---

## Out of scope for version 1

- Real wallet integration.
- Real credential issuing.
- Real eIDAS compliance assessment.
- Real cryptographic credential validation.
- Real trusted-list lookup.
- Legal certification.
- Replacing legal advice.

---

## Open questions

- [ ] Should the first demo use age verification as the main example because it best shows selective disclosure?
- [ ] Should PDF upload comparison be included in the README or only in the notebook?
- [ ] Which claims should be stored as values and which should be stored only as validation results?
- [ ] Should user consent be simulated as `approved`, `declined`, and `expired` statuses?
- [ ] Should every template require a `business_purpose` before it can be validated?

---

## Next action

- [ ] Use this note to create beginner-friendly README explanation.
- [ ] Add PDF-vs-wallet comparison to project presentation material.
- [ ] Reuse the design rules in verification-template documentation.
- [ ] Create age-verification example template using minimal claims.
- [ ] Connect `presentation_status` to simulated wallet response examples.
