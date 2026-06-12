# What My Project Is

Date: 2026-06-11
Status: Draft
Folder: 03_project_relevance
Tags: [PROJECT] [DECISION] [IHK]

---

## Short definition

This project is a relying-party-side prototype for EUDI Wallet verification processes.

It helps an organization translate a business identity-check requirement into a privacy-aware wallet verification request, process a simulated wallet response, validate whether required claims are present, generate privacy warnings, and record audit-log events.

---

## Project flow

```text
Business need
→ verification template
→ simulated wallet request
→ simulated wallet response
→ validation result
→ privacy warning
→ audit log
```

---

## Main user perspective

The main perspective is the **Relying Party**.

A relying party is an organization or service that wants to rely on identity or attribute information presented from a wallet.

Examples:

- employer
- bank
- public office
- online service
- age-restricted service
- professional onboarding process

---

## Core purpose

The prototype should show how a relying party can:

| Goal | Meaning |
|---|---|
| Define purpose | Explain why data is needed. |
| Request minimal claims | Avoid unnecessary data collection. |
| Accept specific credential types | PID, EAA, or QEAA depending on the use case. |
| Process wallet response | Check whether required claims are present. |
| Simulate trust checks | Show whether issuer/provider is accepted in the scenario. |
| Generate privacy warnings | Flag excessive or unclear requests. |
| Record audit events | Document what happened without storing unnecessary raw data. |

---

## Example use cases

| Use case | Minimal idea |
|---|---|
| Age verification | Request `age_over_18`, not full PID. |
| Residence verification | Request country/region if full address is not needed. |
| Employment onboarding | Request required identity and qualification claims only. |
| Professional licence check | Request licence status, possibly as QEAA. |

---

## Why this project is useful

The project demonstrates that wallet integration is not only a technical API problem.

It also requires business decisions:

- What must be verified?
- Why is this data needed?
- Which claims are enough?
- Is full identity really required?
- Which issuer/provider is acceptable?
- What must be logged?
- What should not be stored?

---

## Version 1 position

Version 1 is a simulation and documentation prototype.

It is useful for learning, business-process modeling, IHK-style documentation, and demonstrating privacy-aware relying-party logic.

It is not a production EUDI integration.
