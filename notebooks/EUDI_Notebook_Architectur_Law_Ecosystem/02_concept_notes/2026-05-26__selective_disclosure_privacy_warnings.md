# Selective Disclosure and Privacy Warnings

Date: 2026-05-26
Status: Draft
Folder: 02_concept_notes
Tags: [CONCEPT] [PRIVACY] [PROJECT] [ARCH]

---

## Source

Source title: EUDI Wallet Architecture and Reference Framework
Source section: Definitions, ecosystem roles, privacy-related wallet concepts
Source type: Official architecture reference
Primary link: https://eudi.dev/arf/
Related glossary: `../2026-05-26__glossary.md`
Related source note: `../01_source_notes/2026-05-22__arf_overview.md`
Related concept note: `2026-05-26__pid_eaa_qeaa.md`

---

## Purpose of this note

This note explains **Selective Disclosure** and how it should become practical business logic in the prototype.

The key idea is:

```text
A relying party should request only the data needed for a specific business purpose.
```

For the prototype, selective disclosure should not stay only as a theoretical privacy principle. It should become visible through:

- verification-template design
- requested-claim review
- excessive-data warnings
- simulated wallet responses
- validation results
- audit-log events

---

## Short summary

| Concept | Simple meaning | Prototype meaning |
|---|---|---|
| Selective Disclosure | The user shares only selected data instead of all available wallet data. | The verification request should ask only for necessary claims. |
| Data Minimization | The relying party should collect as little personal data as possible. | The system should warn when a request asks for unnecessary attributes. |
| Privacy Warning | A system warning that the request may be excessive or poorly justified. | The dashboard/API can flag risky templates before they are used. |
| Purpose Binding | Data should be requested for a clear reason. | Every verification template should include a business purpose. |
| Auditability | The system records what was requested, why, and what result was produced. | Audit logs should show the request and result without storing unnecessary personal data. |

---

## Simple explanation

Selective disclosure means that a wallet user does not have to reveal every available identity attribute.

Instead, the user can present only what is needed for the transaction.

Example:

```text
The relying party needs to know whether the user is over 18.
The user should be able to share only "age_over_18 = true" instead of full date of birth, name, address, and PID.
```

This is important because the wallet ecosystem should support privacy-preserving verification, not unnecessary data collection.

---

## Why this matters for the relying party

A relying party may be tempted to request more data than necessary because more data feels safer.

However, from a privacy and compliance perspective, excessive requests create risk.

For this prototype, the relying party should be guided from:

```text
"What data can I request?"
```

toward:

```text
"What is the minimum data needed for this business purpose?"
```

---

## Real-life examples

| Business scenario | Bad request | Better selective request | Why better |
|---|---|---|---|
| Age verification | Full PID, full name, birth date, address | `age_over_18 = true` | Confirms eligibility without exposing full identity. |
| Residence eligibility | Full address and full PID | `country_of_residence = DE` or `region = BW` | Shares only the residence level needed by the service. |
| Student discount | Full PID and full education history | `student_status = active` | Confirms discount eligibility without exposing unrelated education data. |
| Employment onboarding | Full wallet dump | Required identity claims + required qualification claims | Limits data to onboarding purpose. |
| Professional licence check | Full identity profile and personal history | `licence_status = valid`, `profession = veterinarian` | Confirms professional eligibility without irrelevant personal data. |
| Company representative check | Full company records and full personal PID | `authorized_representative = true`, `company_id`, `role` | Confirms authority without exposing unnecessary company/person data. |

---

## Relationship to PID, EAA, and QEAA

Selective disclosure is closely connected to the choice between PID, EAA, and QEAA.

| Situation | Preferred approach | Reason |
|---|---|---|
| A simple fact is needed | EAA or limited disclosed attribute | Avoids full identity disclosure. |
| Identity must be established | PID with only necessary claims | PID may be valid, but still should be limited. |
| A high-trust attribute is needed | QEAA with specific required claims | Stronger trust, but still not a reason to request everything. |
| Only eligibility is needed | Boolean or threshold proof | Avoids exposing raw personal data. |

Example:

```text
Need: user is allowed to access an age-restricted service.
Poor design: request full PID.
Better design: request an age-over-threshold attribute.
```

---

## Relationship to ecosystem roles

| Role | Relationship to selective disclosure |
|---|---|
| User | Controls what is presented from the wallet. |
| EUDI Wallet Instance | Presents selected PID, EAA, or QEAA claims. |
| Relying Party | Defines what claims are requested and why. |
| PID Provider | May issue identity data, but the relying party should not always request all PID claims. |
| EAA Provider | Can issue specific attribute attestations that reduce need for full PID. |
| QEAA Provider | Can issue high-trust attributes for regulated scenarios. |
| Trusted List Provider | Future trust checks may confirm whether issuers/providers are trusted. |
| Authentic Source | Helps explain why a claim is reliable, but does not justify excessive disclosure. |

Simplified relation:

```text
Relying Party defines purpose and claims
→ User reviews request
→ Wallet presents only selected data
→ System validates response
→ Audit log records result and warnings
```

---

## Privacy warning concept

A privacy warning is a signal that a verification request may ask for too much data, lacks a clear purpose, or uses the wrong credential type.

In this prototype, privacy warnings should help the relying party correct the request before it becomes a real wallet request.

A warning does not always mean the request is illegal or forbidden.

It means:

```text
Review this request because it may be excessive, unclear, or risky.
```

---

## Privacy warning categories

| Warning category | Meaning | Example warning text |
|---|---|---|
| Excessive PID request | Full identity is requested where a smaller proof may be enough. | `Full PID requested for age-only purpose. Consider age_over_18 instead.` |
| Missing purpose | The request does not explain why the data is needed. | `Verification template has no clear business purpose.` |
| Too many required claims | The template requests more claims than the purpose suggests. | `Request contains 8 required claims for simple eligibility check.` |
| Sensitive claim requested | The request includes a claim that may be sensitive or high-risk. | `Sensitive attribute requested. Confirm legal/business necessity.` |
| Raw value requested instead of proof | The request asks for raw data when a boolean/threshold proof would be enough. | `Date of birth requested. Consider age_over_18 proof.` |
| Credential type mismatch | The requested credential type is stronger or broader than needed. | `PID requested, but EAA may satisfy this business purpose.` |
| Unclear retention | The template does not define what will be stored or for how long. | `Retention policy missing for requested claims.` |
| No audit purpose | The system cannot explain what should be recorded. | `Audit reason is missing. Add validation purpose.` |
| Untrusted simulated issuer | The response comes from an issuer not accepted by the template. | `Issuer is not marked as trusted for this verification template.` |
| Missing user consent indicator | The simulated response does not show user-controlled presentation. | `Wallet response does not include consent/presentation status.` |

---

## Example warning rules for version 1

These are not final legal rules. They are practical prototype rules.

| Rule ID | Condition | Warning | Severity |
|---|---|---|---|
| PW-001 | `purpose = age_verification` and `PID` is requested | Full PID may be excessive for age verification. | High |
| PW-002 | `date_of_birth` is requested and `age_over_18` would satisfy the template | Raw birth date may be unnecessary. | Medium |
| PW-003 | Required claims count is greater than expected for the use case | Too many required claims for stated purpose. | Medium |
| PW-004 | `purpose` is empty or generic | Missing or unclear business purpose. | High |
| PW-005 | `retention_policy` is missing | Retention policy should be defined. | Medium |
| PW-006 | `credential_type = QEAA` but use case is low-assurance | Qualified attestation may be unnecessary for this purpose. | Low |
| PW-007 | `issuer_trusted = false` | Issuer is not accepted/trusted in this simulated check. | High |
| PW-008 | wallet response includes extra claims not requested | Response contains unnecessary additional data. | Medium |
| PW-009 | template requests address when only country/region is needed | Full address may be excessive. | Medium |
| PW-010 | no audit event is configured | Verification cannot be properly documented. | Medium |

---

## Severity levels

| Severity | Meaning | Prototype behavior |
|---|---|---|
| Low | Request may be improvable but not obviously risky. | Show suggestion. |
| Medium | Request may be excessive or incomplete. | Show warning and require review. |
| High | Request conflicts strongly with minimization or trust assumptions. | Mark template as risky before use. |

---

## Prototype object: privacy warning

A privacy warning can be modeled like this:

```json
{
  "warning_id": "PW-001",
  "severity": "high",
  "category": "excessive_pid_request",
  "message": "Full PID requested for age-only purpose. Consider age_over_18 instead.",
  "affected_claims": ["given_name", "family_name", "date_of_birth", "address"],
  "recommendation": "Replace full PID with an age-over-threshold claim.",
  "created_at": "2026-05-26T10:00:00Z"
}
```

---

## Prototype object: verification template with minimization review

Example: bad age-verification template

```json
{
  "template_id": "age_check_bad_example",
  "purpose": "age_verification",
  "required_credential_type": "PID",
  "required_claims": [
    "given_name",
    "family_name",
    "date_of_birth",
    "address"
  ],
  "retention_policy": "not_defined"
}
```

Expected warnings:

```json
[
  {
    "warning_id": "PW-001",
    "severity": "high",
    "message": "Full PID requested for age-only purpose. Consider age_over_18 instead."
  },
  {
    "warning_id": "PW-005",
    "severity": "medium",
    "message": "Retention policy should be defined."
  }
]
```

Example: better age-verification template

```json
{
  "template_id": "age_check_minimized_example",
  "purpose": "age_verification",
  "required_credential_type": "EAA",
  "required_claims": [
    "age_over_18"
  ],
  "retention_policy": "store_result_only",
  "audit_policy": "record_request_result_no_raw_personal_data"
}
```

Expected result:

```text
No high privacy warning. Request is more aligned with selective disclosure.
```

---

## Audit-log connection

Privacy warnings should be connected to audit logs.

The audit log should record:

- which template was used
- which claims were requested
- which claims were received
- whether extra claims were received
- whether privacy warnings were generated
- whether the request was accepted, rejected, or reviewed
- what validation result was produced

The audit log should avoid storing unnecessary raw personal data.

Better audit event:

```json
{
  "event_type": "privacy_warning_created",
  "template_id": "age_check_bad_example",
  "warning_id": "PW-001",
  "severity": "high",
  "reason": "PID requested for age-only purpose",
  "raw_personal_data_stored": false
}
```

---

## Use-case examples

### Age verification

| Item | Poor design | Better design |
|---|---|---|
| Requested data | Full PID | `age_over_18` |
| Risk | Collects unnecessary identity data | Minimal data disclosed |
| Warning | High | None or low |
| Audit log | Should not store full PID | Store result only |

### Residence verification

| Item | Poor design | Better design |
|---|---|---|
| Requested data | Full address | Country or region only, if sufficient |
| Risk | More precise location data than needed | Matches purpose more closely |
| Warning | Medium/high depending on purpose | Lower risk |
| Audit log | Record purpose and result | Store only required residence level |

### Employment onboarding

| Item | Poor design | Better design |
|---|---|---|
| Requested data | Full wallet dump | Required PID subset + required qualification claims |
| Risk | Broad unnecessary data collection | Purpose-bound onboarding data |
| Warning | High | Lower if justified and documented |
| Audit log | Hard to justify | Clear purpose and claim list |

---

## Design implications for version 1

The prototype should include privacy review logic before a verification template is used.

Minimum fields needed:

| Field | Purpose |
|---|---|
| `purpose` | Explains why data is requested. |
| `required_claims` | Defines necessary claims. |
| `optional_claims` | Separates useful-but-not-required claims. |
| `credential_type` | Shows whether PID, EAA, or QEAA is requested. |
| `retention_policy` | Explains what is stored and for how long. |
| `audit_policy` | Explains what gets logged. |
| `privacy_warnings` | Stores generated warnings. |
| `validation_result` | Shows whether response satisfies request. |

---

## In scope for version 1

- Detect excessive PID requests in simple use cases.
- Warn when required claims exceed the stated purpose.
- Warn when purpose is missing.
- Warn when retention policy is missing.
- Warn when raw values are requested but boolean/threshold proof would be enough.
- Log privacy warnings as audit events.
- Show privacy warnings in the dashboard/API output.

---

## Out of scope for version 1

- Final legal determination of whether a request is lawful.
- Real wallet consent UX.
- Real cryptographic selective-disclosure proofs.
- Real trusted-list validation.
- Automatic legal compliance certification.
- Real deletion/retention enforcement across external systems.

---

## Important project boundary

The prototype can say:

```text
This verification request may be excessive based on the stated purpose.
```

The prototype should not say:

```text
This verification request is legally illegal.
```

Reason:

The system can support privacy-aware business logic, but legal conclusions require legal review and context.

---

## Open questions

- [ ] Which warning rules are required for the first demo?
- [ ] Should privacy warnings block a template or only mark it for review?
- [ ] Should severity be calculated from purpose, claim count, and credential type?
- [ ] Which use cases should be used to test privacy warnings first?
- [ ] Should extra claims in wallet responses be rejected or only ignored and logged?
- [ ] How should retention policy be represented in the template schema?

---

## Next action

- [ ] Connect warning rules to the future verification-template schema.
- [ ] Create example templates for age verification, residence verification, and employment onboarding.
- [ ] Add privacy warning event types to the audit-log concept.
- [ ] Reuse warning categories in the project relevance matrix.
