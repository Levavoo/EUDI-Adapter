# Requirements from EUDI Research

Date: 2026-06-11
Status: Draft
Folder: 03_project_relevance
Tags: [PROJECT] [REQUIREMENTS] [DECISION] [IHK]

---

## Purpose

This note turns EUDI research into prototype requirements.

The requirements are not final technical specifications. They are business and architecture requirements derived from ARF, eIDAS context, wallet roles, PID/EAA/QEAA concepts, selective disclosure, and relying-party relevance.

---

## Core requirement idea

The prototype should support this process:

```text
Relying Party defines a business verification purpose
→ system creates or uses a verification template
→ template requests minimal required claims
→ simulated wallet response is processed
→ claims and issuer metadata are checked
→ privacy warnings are generated if needed
→ audit log records the event
```

---

## Functional requirements

| ID | Requirement | Reason |
|---|---|---|
| FR-001 | The system shall allow a relying party to define a verification purpose. | Every data request needs a clear business reason. |
| FR-002 | The system shall define required claims and optional claims separately. | Supports data minimization and clearer validation. |
| FR-003 | The system shall support credential types `PID`, `EAA`, and `QEAA`. | These are central wallet data categories for the prototype. |
| FR-004 | The system shall process simulated wallet responses. | Version 1 does not use real wallets. |
| FR-005 | The system shall validate whether required claims are present. | Core verification result. |
| FR-006 | The system shall store issuer/provider metadata in simulated responses. | Relying parties need to know where data comes from. |
| FR-007 | The system shall simulate trust-check results. | Real trusted-list validation is out of scope, but trust logic must be visible. |
| FR-008 | The system shall generate privacy warnings for excessive or unclear requests. | Supports selective disclosure and data minimization. |
| FR-009 | The system shall create audit-log events for key verification steps. | Supports traceability and business review. |
| FR-010 | The system shall distinguish accepted, rejected, and missing-claims outcomes. | Needed for clear validation results. |

---

## Privacy requirements

| ID | Requirement | Reason |
|---|---|---|
| PR-001 | The system shall warn when full PID is requested for an age-only purpose. | Full identity may be excessive. |
| PR-002 | The system shall warn when purpose is missing. | Requests without purpose are hard to justify. |
| PR-003 | The system shall warn when retention policy is missing. | Storage rules should be clear. |
| PR-004 | The system shall warn when raw values are requested but threshold proof would be enough. | Example: birth date vs age-over-18. |
| PR-005 | The system shall avoid storing unnecessary raw personal data in audit logs. | Auditability should not create unnecessary data risk. |

---

## Scope requirements

| ID | Requirement | Reason |
|---|---|---|
| SR-001 | The system shall clearly state that wallet responses are simulated. | Avoids misleading production claims. |
| SR-002 | The system shall clearly state that trust checks are simulated. | Avoids claiming real legal/cryptographic validation. |
| SR-003 | The system shall not claim to be a wallet, issuer, QTSP, or official EUDI component. | Maintains correct project boundary. |
| SR-004 | Governance roles such as CAB, NAB, and supervisory bodies shall stay documentation-only in version 1. | Keeps prototype realistic. |

---

## Suggested data objects

| Object | Purpose |
|---|---|
| Verification Template | Stores purpose, required claims, accepted credential types, retention policy, and audit policy. |
| Simulated Wallet Response | Stores presented claims, credential type, issuer metadata, and presentation status. |
| Validation Result | Stores accepted/rejected/missing claims outcome. |
| Privacy Warning | Stores warning type, severity, message, and recommendation. |
| Audit Log Event | Stores important process events without unnecessary raw personal data. |

---

## Next action

- [ ] Use this note when designing the verification-template schema.
- [ ] Use this note when creating example wallet responses.
- [ ] Use this note when defining audit-log fields.
- [ ] Review whether all requirements are realistic for version 1.
