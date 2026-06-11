# Project Scope — EUDI Wallet Relying Party Integration Bus

## 1. Project Summary

The **EUDI Wallet Relying Party Integration Bus** is a prototype service that helps an organisation act as a relying party in an EUDI Wallet verification process.

The project does **not** build a real EUDI Wallet. Instead, it focuses on the relying party side: defining verification requests, processing simulated wallet responses, validating whether the response fulfils the business requirement, and storing privacy-preserving audit logs.

The prototype demonstrates how a relying party could request only the minimum required information from a user’s wallet, evaluate the result, and document the verification event without storing unnecessary personal data.

The first version focuses on one simple use case: **age verification**.

---

## 2. Problem Statement

Organisations that want to use the EUDI Wallet need a clear way to translate business requirements into technical verification requests.

For example, an online service may need to know whether a user is over 18. However, from a privacy perspective, the service should not request or store the user’s full date of birth if a simple “over 18: yes/no” confirmation is enough.

This creates several challenges:

- The organisation must define what it actually needs to verify.
- The verification request should follow data minimisation principles.
- The wallet response must be checked against the original request.
- The result should be logged for audit purposes.
- Sensitive personal data should not be stored unnecessarily.
- The process should be understandable for both business and technical stakeholders.

This project addresses these challenges by creating a small prototype that models the relying party verification flow in a structured and explainable way.

---

## 3. Target Users

The project is intended for several types of users and stakeholders.

### Business or Process Analysts

They define what the organisation needs to verify and why. They are interested in the business purpose, the use case, the required attributes, and the process flow.

### Technical Staff and Developers

They need to understand how verification requests, wallet responses, validation logic, and audit logs are structured. They are interested in the API design, data model, backend structure, and simulator behaviour.

### Compliance and Privacy Stakeholders

They need to understand what data is requested, what data is stored, what is not stored, and how the prototype supports privacy-friendly verification.

### Project Reviewers or IHK Evaluators

They need a clear explanation of the project goal, scope, implementation boundaries, and final prototype result.

---

## 4. First Use Case

The first implemented use case is:

## UC-001 — Age Verification

A relying party wants to check whether a user is over 18 before granting access to an age-restricted service.

The relying party does not need the user’s full date of birth. It only needs a confirmation that the user fulfils the age requirement.

### Business Goal

Allow the relying party to verify that the user is over 18 while requesting and storing as little personal data as possible.

### Example Verification Requirement

```json
{
  "use_case": "age_verification",
  "required_attribute": "age_over_18",
  "purpose": "Access to age-restricted service",
  "data_minimisation": true
}
```

### Example Wallet Response

```json
{
  "request_id": "REQ-001",
  "age_over_18": true,
  "issuer_trusted": true,
  "presentation_valid": true
}
```

### Expected Result

If the wallet response confirms that the user is over 18, the issuer is trusted, and the presentation is valid, the verification result is approved.

If one of these checks fails, the verification result is rejected.

The audit log stores the result of the verification, but not the user’s full personal data.

---

## 5. In Scope

The following parts are included in the project scope:

### Project Documentation

- Project scope
- Glossary
- Use case description
- Architecture description
- Data model
- API design
- Privacy model
- Implementation stages
- Weekly project plan
- IHK or portfolio explanation

### Relying Party Verification Flow

- Define a verification request
- Generate a structured request object
- Simulate sending the request to a wallet
- Receive a simulated wallet response
- Validate the response against the original request
- Return an approved or rejected result
- Store a minimal audit log

### Wallet Simulator

The project may include a simple wallet simulator that returns predefined responses for testing.

The simulator is only used to test the relying party flow. It is not a real wallet implementation.

### Audit Logging

The project includes privacy-preserving audit logs that document:

- Request ID
- Timestamp
- Use case
- Relying party ID
- Verification result
- Validation status
- Reason for approval or rejection

The audit log should avoid storing raw personal data.

### Minimal Backend Prototype

A backend prototype may be implemented to expose the verification process through API endpoints.

Possible later endpoints include:

```text
POST /verification-requests
GET /verification-requests/{id}
POST /wallet-responses
GET /audit-logs
```

### Optional Dashboard

A simple dashboard may be added later to show:

- Created verification requests
- Simulated wallet responses
- Verification results
- Audit log overview

The dashboard is optional and should not be implemented before the core backend and documentation are clear.

---

## 6. Out of Scope

The following parts are explicitly outside the project scope:

- Building a real EUDI Wallet
- Issuing real digital identity credentials
- Connecting to real national identity systems
- Performing real cryptographic verification
- Implementing a production trust framework
- Connecting to real qualified trust service providers
- Handling real personal identity data
- Building a production-ready compliance system
- Creating a full enterprise integration platform
- Supporting all EUDI Wallet use cases in the first version
- Building a complex user management system
- Building a full frontend application before the backend flow is clear

These exclusions are important because the purpose of the project is to demonstrate the relying party verification process, not to recreate the entire EUDI Wallet ecosystem.

---

## 7. Simulated Components

Several components are simulated in the prototype.

### Wallet

The wallet is simulated. It returns predefined responses such as:

- Approved age verification
- Rejected age verification
- Invalid presentation
- Untrusted issuer

### Credential Issuer

The credential issuer is not implemented as a real external service. Issuer trust is represented through a simplified field such as:

```json
{
  "issuer_trusted": true
}
```

### Cryptographic Validation

Real cryptographic validation is not implemented in the first prototype.

Instead, the prototype uses simplified validation fields such as:

```json
{
  "presentation_valid": true
}
```

This allows the project to focus on business logic, request handling, validation flow, and audit logging.

### Trust Framework

The real EUDI trust framework is not implemented.

The prototype may use a simplified internal list or boolean value to represent whether an issuer is trusted.

### User Interaction

The user’s real wallet interaction is not implemented. The prototype only simulates the result that a wallet could return to the relying party service.

---

## 8. Data Handling and Privacy Boundaries

The prototype follows the principle of data minimisation.

For the first use case, the relying party should not request or store the user’s full date of birth if the only required fact is whether the user is over 18.

### Data That May Be Processed

For the age verification use case, the prototype may process:

- Request ID
- Use case name
- Required attribute
- Verification purpose
- Result of `age_over_18`
- Issuer trust status
- Presentation validity status
- Final verification result
- Timestamp

### Data That Should Not Be Stored

The prototype should not store:

- Full name
- Full date of birth
- Address
- National identity number
- Raw credential contents
- Unnecessary personal attributes
- Real wallet identifiers
- Sensitive personal data that is not required for the use case

### Audit Log Boundary

The audit log should store proof that a verification decision happened, but not more personal data than necessary.

A good audit log entry should answer:

- What was requested?
- Why was it requested?
- When did the verification happen?
- Was the verification approved or rejected?
- What validation checks were passed or failed?

It should not become a hidden storage place for raw identity data.

---

## 9. Expected Prototype Result

At the end of the first project version, the prototype should show a complete simplified relying party verification flow.

The expected result is:

1. A relying party creates an age verification request.
2. The system generates a structured request.
3. A simulated wallet response is received.
4. The response is validated.
5. The system returns an approved or rejected result.
6. A privacy-preserving audit log entry is created.
7. The process is documented clearly enough for business and technical readers.

### Minimum Successful Result

The minimum successful prototype should include:

- Clear project documentation
- One implemented use case: age verification
- Example request and response JSON files
- A basic data model
- A basic API design
- A simplified backend flow
- Audit log concept
- Privacy boundaries

### Stronger Result

A stronger version may also include:

- A working FastAPI backend
- Test cases for approved and rejected responses
- A simple dashboard or Streamlit view
- Example diagrams
- A short IHK or portfolio presentation section

---

## 10. Future Extensions

The project can be extended after the first use case is stable.

Possible future use cases include:

### Residence Verification

Verify whether a user lives in a specific country, federal state, or city without storing the full address.

### Student Status Verification

Verify whether a user is currently a student without storing full university records.

### Driving Licence Verification

Verify whether a user has a valid driving licence for a required vehicle category.

### Professional Qualification Verification

Verify whether a user has a required professional qualification or certification.

### Multi-Use-Case Request Templates

Create reusable verification request templates for different relying party scenarios.

### Advanced Trust Logic

Replace the simplified trust flag with a more realistic trust registry or issuer validation model.

### Improved Audit Dashboard

Add a dashboard for reviewing verification events, filtering audit logs, and showing privacy-relevant statistics.

### Compliance Mapping

Map the prototype flow to legal and organisational requirements such as data minimisation, consent, purpose limitation, and auditability.

---

## Quality Check

This project scope is suitable for the current stage because it:

- Defines the project goal clearly.
- Separates the relying party service from the real EUDI Wallet.
- Keeps the first implementation focused on one use case.
- Makes privacy boundaries explicit.
- Explains what is simulated.
- Prevents scope creep.
- Gives both business and technical readers a clear understanding of the project.
- Creates a stable basis for the next documents: `use_cases.md`, `data_model.md`, `api_design.md`, and `privacy_model.md`.

The next logical document after this file is:

```text
docs/use_cases.md
```

The next implementation-related file after that is:

```text
examples/age_verification_request.json
```
