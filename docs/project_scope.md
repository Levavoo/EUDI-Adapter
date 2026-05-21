# Project Scope

## Project Name

**EUDI Wallet Relying Party Integration Bus**

## Project Summary

This project is a prototype for organizations that need to request and verify identity-related information from a future EUDI Wallet flow.

The system helps a relying party translate business identity-check requirements into structured, privacy-preserving verification request definitions. It then processes simulated wallet responses and records audit events that explain what happened during the verification process.

The prototype focuses on the relying-party side of the workflow. It does not implement a real wallet, real cryptographic validation, or production-grade trust infrastructure.

## Problem Statement

Organizations often know their business requirement, such as "verify that a person is over 18" or "confirm that a person lives in a specific country", but they may not know how to translate that requirement into a minimal, privacy-preserving digital credential request.

This project addresses that gap by providing a structured process for:

- describing the business need,
- identifying the minimum necessary claims,
- generating a verification request definition,
- simulating a wallet presentation response,
- validating the response against the request,
- recording an audit trail without storing unnecessary personal data.

## Target Users

| User Group | Need |
|---|---|
| Business analysts | Describe identity-check requirements in business language |
| Compliance staff | Check whether requested data is necessary and proportionate |
| Technical architects | Understand how business requirements become verification requests |
| Backend developers | Implement and test relying-party verification workflows |
| Auditors | Review verification events and privacy-relevant decisions |
| Portfolio / IHK reviewers | Understand the project purpose, boundaries, and implementation logic |

## Version 1 Goal

Version 1 should demonstrate the complete prototype flow with simulated data:

```text
Business requirement
-> Verification template
-> Verification request
-> Simulated wallet response
-> Validation result
-> Audit log
-> Basic analytics / dashboard view
```

The goal is not to create a certified production EUDI Wallet verifier. The goal is to create a clear, testable, and explainable prototype of the relying-party process.

## In Scope for Version 1

### Business and Documentation Scope

- Clear project scope and glossary.
- Use case descriptions for common relying-party scenarios.
- Business process modeling for identity-check situations.
- Data minimization notes for each use case.
- Explanation of what the system verifies and why.
- Documentation suitable for technical and non-technical readers.

### Prototype Functional Scope

- Verification templates based on business needs.
- Structured verification request definitions.
- Simulated wallet presentation responses.
- Mock trusted issuer list.
- Validation logic for simulated responses.
- Privacy warning logic for unnecessary claims.
- Audit log entries for important verification events.
- Basic API endpoints for templates, requests, validation, and audit logs.
- Basic dashboard or analytics view.

### Technical Scope

- FastAPI backend.
- Pydantic schemas for structured data.
- Simple local development setup with `uv`.
- Mock data files in `examples/`.
- Simple in-memory, file-based, or lightweight local storage during prototype stage.
- Tests for important validation behavior.

## Out of Scope for Version 1

The following topics are intentionally excluded from the first prototype:

| Topic | Reason |
|---|---|
| Real EUDI Wallet integration | Too complex for the first prototype and requires ecosystem-specific setup |
| Real OpenID4VP protocol flow | Important later, but not required to prove the business workflow |
| Real cryptographic proof validation | Requires production-grade standards and libraries |
| QTSP integration | Out of scope for the initial relying-party prototype |
| Government PID integration | Not available or appropriate for local prototype work |
| Production security certification | The project is a prototype, not a certified production system |
| Full legal compliance assessment | The project can document privacy logic, but does not replace legal review |
| Production authentication and authorization | Can be added later after core workflow is stable |
| Enterprise deployment | Docker, cloud hosting, monitoring, and scaling are future topics |
| Full wallet implementation | The project is a relying-party adapter, not a wallet |

## First Use Case Candidates

The first version should focus on simple, realistic relying-party use cases:

| Use Case | Example Business Need |
|---|---|
| Age verification | Verify that a person is over a required age without requesting full date of birth |
| Residence verification | Confirm country or region of residence without collecting a full address unless required |
| Employment onboarding | Confirm identity or work-related eligibility for onboarding |
| Student status verification | Confirm student status for access to discounts or services |

## Privacy Principles

The prototype should follow these privacy principles:

- Request only claims needed for the stated business purpose.
- Prefer derived claims over raw personal data where possible.
- Avoid storing personal claims in audit logs unless strictly necessary.
- Record verification decisions and metadata rather than full credential contents.
- Detect and flag over-sharing in simulated wallet responses.
- Keep business purpose visible in each verification template.

## Expected Demo Flow

A successful demo should show:

1. A business use case is selected.
2. A verification template defines required and optional claims.
3. A verification request is created from the template.
4. A simulated wallet response is submitted.
5. The backend validates the response.
6. The system shows whether validation passed or failed.
7. The audit log records the event.
8. Privacy warnings are shown if unnecessary data was shared.

## Main Project Boundaries

### The Project Is

- A relying-party prototype.
- A business-to-technical translation tool.
- A simulation environment for verification workflows.
- A documentation-heavy portfolio project.
- A foundation for later EUDI Wallet research.

### The Project Is Not

- A real EUDI Wallet.
- A government identity provider.
- A certified verifier product.
- A full OpenID4VP implementation.
- A legal compliance tool.
- A production security system.

## Success Criteria

The project is successful when another person can:

- understand the project purpose from the README and documentation,
- see clear boundaries between prototype and production topics,
- run the backend locally,
- inspect documented use cases,
- understand how a business requirement becomes a verification request,
- test simulated wallet responses,
- see validation results and audit logs,
- understand the privacy reasoning behind required and optional claims.

## Current Stage Status

Stage 0 is complete after this scope document, the glossary, and the plan documents are available.

The project should now move into Stage 1: use cases and business process modeling.
