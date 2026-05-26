# Learning Plan — EUDI Wallet Relying Party Integration Bus

## Purpose

This learning plan runs parallel to `plan/plan_stages.md`.

The development plan explains what to build. This learning plan explains what must be understood while building it.

The goal is to develop enough conceptual understanding to explain the project to technical staff, business stakeholders, legal/compliance staff, reviewers, and future contributors.

This plan focuses on:

- notions and vocabulary,
- concepts and mental models,
- business process understanding,
- privacy and compliance logic,
- architecture thinking,
- auditability,
- self-check questions.

---

## How to Use This File

For each development stage:

1. Read the matching learning stage.
2. Rewrite the topic in your own words.
3. Draw the meta scheme or create your own version.
4. Answer the check questions without looking at notes.
5. Add unclear points to the project notebook.
6. Connect each topic to real project files.

Recommended answer status:

```md
[ ] I can answer clearly
[ ] I can answer partly
[ ] I cannot answer yet
```

---

# Stage 0 — Project Orientation and Mental Model

## Parallel to Development Stage

Project setup, README, scope definition, documentation structure.

## Learning Goal

Understand what the project is, what problem it solves, and what it intentionally does not solve.

## Key Notions

- EUDI Wallet
- Relying Party
- Digital identity
- Attribute verification
- Business requirement
- Compliance requirement
- Verification request
- Wallet response
- Audit log
- Prototype scope
- Out-of-scope boundary

## Concepts to Understand

This project is not a full EUDI Wallet implementation.

It is a relying-party-side prototype. It helps an organization translate business identity-check requirements into structured verification requests, process simulated wallet responses, and create audit evidence.

Core project flow:

```text
Business Need
    ↓
Verification Requirement
    ↓
Structured Wallet Request
    ↓
Wallet Response
    ↓
Decision / Result
    ↓
Audit Log
```

The system should answer:

- What does the organization need to verify?
- Why is this verification needed?
- Which data is minimally required?
- What request should be sent to the wallet?
- What response was received?
- What decision was made?
- What evidence should be stored?

## Meta Scheme

```text
Organization asks:
"Do we need to know this person is allowed to access/use/do something?"

System translates that into:
"Which attributes or proofs must be verified?"

Wallet provides:
"Only the required attributes or proofs."

System records:
"What was requested, why, what was received, and what decision was made."
```

## Questions to Check Understanding

1. What is the main purpose of this project?
2. What is a relying party?
3. Why is this project not the same as building an EUDI Wallet?
4. What problem does the prototype solve for an organization?
5. What is the difference between identity verification and attribute verification?
6. Why is it important to define what the project does not do?
7. Which stakeholders would care about this system?
8. What does the system need to document for audit purposes?
9. Why should business requirements come before technical implementation?
10. How would you explain this project in two minutes to a non-technical person?

---

# Stage 1 — EUDI Wallet Basics

## Parallel to Development Stage

Basic documentation, glossary, first use cases.

## Learning Goal

Understand the basic EUDI Wallet ecosystem and the roles involved.

## Key Notions

- EUDI Wallet
- eIDAS
- Digital identity
- PID — Person Identification Data
- Electronic Attestation of Attributes
- Credential issuer
- Credential holder
- Relying party
- Trust framework
- Selective disclosure
- User consent
- Cross-border recognition

## Concepts to Understand

The EUDI Wallet allows users to store and present digital identity data and credentials.

Basic role model:

```text
Issuer
    gives credentials to
Holder / User
    presents credentials to
Relying Party
    verifies credentials
```

Example:

```text
Government authority
    issues identity data to
Citizen's wallet
    citizen presents proof to
Online service provider
```

A relying party should only request what is necessary. For example, instead of requesting a full birth date, a service may only need proof that the user is over 18.

## Meta Scheme

```text
Issuer = Source of trusted data
Holder = Person or organization controlling the wallet
Relying Party = Service requesting verification
Verifier = Technical component checking validity
Trust Framework = Rules that make the ecosystem reliable
```

## Questions to Check Understanding

1. What is the EUDI Wallet?
2. What is eIDAS?
3. What is the difference between issuer, holder, and relying party?
4. What kind of data can be stored in a wallet?
5. What is a digital credential?
6. What does a relying party want from a wallet?
7. Why should a relying party avoid requesting unnecessary data?
8. What does selective disclosure mean?
9. Why is user consent important?
10. How does the wallet model differ from uploading a PDF copy of an ID card?

---

# Stage 2 — Business Use Cases and Service Blueprints

## Parallel to Development Stage

Use case documentation and business process modeling.

## Learning Goal

Understand how EUDI Wallet use cases are described from a business and service perspective.

## Key Notions

- Use case
- Service blueprint
- User journey
- Frontstage process
- Backstage process
- Business process
- Stakeholder
- Touchpoint
- Preconditions
- Trigger
- Outcome
- Optional step
- Alternative flow

## Concepts to Understand

A use case describes a real-world situation where the wallet provides value.

A service blueprint describes how the service works from multiple perspectives:

```text
User Actions
    ↓
Visible Service Interaction
    ↓
Internal Business Process
    ↓
Technical Support Process
    ↓
Evidence / Logs / Data
```

In this project, service blueprints help identify what the relying party needs to request, why it needs the data, and what should happen after the wallet response is received.

## Meta Scheme

```text
Use Case:
"User wants to access a service."

Business Requirement:
"Organization must verify condition X."

Wallet Interaction:
"Request proof of X."

Result:
"Access granted, denied, or manual review required."

Audit:
"Record why and how the decision was made."
```

## Questions to Check Understanding

1. What is a use case?
2. What is a service blueprint?
3. Why are service blueprints useful before implementation?
4. What is the difference between a user journey and a business process?
5. What is a frontstage process?
6. What is a backstage process?
7. Why should optional and alternative steps be documented?
8. How can a use case produce system requirements?
9. What is a stakeholder in this project?
10. How does a service blueprint help define wallet verification requests?

---

# Stage 3 — Requirements Thinking

## Parallel to Development Stage

Requirement files, business rules, verification rule definitions.

## Learning Goal

Learn how to translate business needs into structured requirements.

## Key Notions

- Business requirement
- Functional requirement
- Non-functional requirement
- Compliance requirement
- Verification rule
- Decision rule
- Acceptance criterion
- Input
- Output
- Constraint
- Traceability

## Concepts to Understand

A business requirement explains what the organization needs.

A functional requirement explains what the system must do.

A non-functional requirement explains how the system must behave.

Example:

```text
Business Requirement:
The organization must verify that a user is at least 18 years old.

Functional Requirement:
The system shall create a wallet request asking for proof of age-over-18.

Non-Functional Requirement:
The system shall not request the user's full birth date if age-over-18 proof is sufficient.

Compliance Requirement:
The system shall store an audit record explaining the purpose of the verification.
```

## Meta Scheme

```text
Business Need
    ↓
Requirement
    ↓
Rule
    ↓
System Behavior
    ↓
Test Question
    ↓
Audit Evidence
```

## Questions to Check Understanding

1. What is a business requirement?
2. What is a functional requirement?
3. What is a non-functional requirement?
4. What is a compliance requirement?
5. What is the difference between a requirement and a rule?
6. Why should requirements be traceable?
7. How can one business requirement create multiple technical requirements?
8. What makes a requirement testable?
9. Why should privacy requirements be included early?
10. How would you convert “verify customer eligibility” into clearer requirements?

---

# Stage 4 — Data and Attribute Modeling

## Parallel to Development Stage

Data model documentation and schema design.

## Learning Goal

Understand how identity-related data should be modeled without over-collecting personal information.

## Key Notions

- Attribute
- Credential
- Claim
- Schema
- Data minimization
- Required attribute
- Optional attribute
- Derived attribute
- Verification result
- Data category
- Personal data
- Sensitive data
- Pseudonymization

## Concepts to Understand

The system should focus on what needs to be verified, not on collecting as much data as possible.

Example:

```text
Bad request:
Give me your full ID document.

Better request:
Prove that you are over 18.

Even better:
Prove that you are over 18 using a trusted credential.
```

Important distinction:

```text
Raw Attribute:
Date of birth = 1998-04-12

Derived Attribute:
Age over 18 = true
```

The second option is usually better for privacy because it reveals less information.

## Meta Scheme

```text
Credential contains claims.
Claims contain attributes.
Attributes answer business questions.
Business questions should be minimal.
Minimal questions reduce privacy risk.
```

## Questions to Check Understanding

1. What is an attribute?
2. What is a claim?
3. What is a credential?
4. What is the difference between raw and derived attributes?
5. Why is “age over 18” often better than requesting date of birth?
6. What is data minimization?
7. What kind of data should not be stored if it is not needed?
8. What should be included in a verification result?
9. What is the difference between requested data and received data?
10. How can a data model support privacy?

---

# Stage 5 — Verification Request Logic

## Parallel to Development Stage

Request builder, rule-to-request translation.

## Learning Goal

Understand how business rules become structured wallet verification requests.

## Key Notions

- Verification request
- Presentation request
- Attribute request
- Purpose binding
- Consent prompt
- Request template
- Rule engine
- Request generation
- Required proof
- Trust requirement

## Concepts to Understand

The relying party should not manually invent a wallet request each time.

Instead, the system should use structured business rules.

Example:

```text
Rule:
User must prove they are over 18.

Generated Request:
Request proof of age_over_18 from a trusted issuer.

Purpose:
Access to age-restricted service.
```

A good verification request should answer:

```text
What is requested?
Why is it requested?
Who requests it?
Which credential type is acceptable?
Which issuer or trust level is acceptable?
What should happen if verification fails?
```

## Meta Scheme

```text
Business Rule
    ↓
Request Template
    ↓
Wallet Verification Request
    ↓
User Consent
    ↓
Wallet Response
```

## Questions to Check Understanding

1. What is a verification request?
2. What information should a verification request contain?
3. Why should the purpose of the request be clear?
4. What is a request template?
5. Why should requests be generated from rules instead of written manually each time?
6. What does trusted issuer mean?
7. What should happen if a required attribute is missing?
8. What should happen if the wallet response is invalid?
9. Why does the user need to understand what is being requested?
10. How does request logic connect business needs to technical implementation?

---

# Stage 6 — Wallet Response and Decision Logic

## Parallel to Development Stage

Simulated wallet responses, response processing, decision results.

## Learning Goal

Understand how the relying party processes a wallet response and reaches a business decision.

## Key Notions

- Wallet response
- Verification result
- Valid response
- Invalid response
- Missing attribute
- Expired credential
- Revoked credential
- Trust validation
- Decision logic
- Access granted
- Access denied
- Manual review

## Concepts to Understand

A wallet response should not automatically mean “yes”.

The system must check whether the response satisfies the rule.

Example:

```text
Requirement:
User must prove age_over_18 = true.

Wallet Response:
age_over_18 = true
issuer = trusted authority
credential_status = valid

Decision:
Approved
```

Alternative:

```text
Wallet Response:
age_over_18 = true
issuer = unknown source

Decision:
Rejected or manual review
```

## Meta Scheme

```text
Wallet Response
    ↓
Technical Validation
    ↓
Business Rule Check
    ↓
Decision
    ↓
Audit Record
```

## Questions to Check Understanding

1. What is a wallet response?
2. What makes a wallet response valid?
3. What is the difference between technical validation and business validation?
4. What could make a response unacceptable?
5. What is an expired credential?
6. What is a revoked credential?
7. Why might a response require manual review?
8. What decision states should the prototype support?
9. Why should the system record both successful and failed checks?
10. How does the system know whether a wallet response satisfies a business rule?

---

# Stage 7 — Audit, Logging, and Compliance Evidence

## Parallel to Development Stage

Audit log model, logging documentation, compliance process.

## Learning Goal

Understand why auditability is central to the project.

## Key Notions

- Audit log
- Compliance evidence
- Decision record
- Timestamp
- Request purpose
- Data access record
- Accountability
- Traceability
- Retention
- Integrity
- Non-repudiation
- Review process

## Concepts to Understand

The system should be able to explain what happened after the fact.

An audit log should answer:

```text
Who requested verification?
What was requested?
Why was it requested?
When was it requested?
What response was received?
What decision was made?
Which rule caused that decision?
Was unnecessary data avoided?
```

The audit log does not need to store all personal data.

In many cases, it should store proof that a check was completed, not the full data itself.

## Meta Scheme

```text
Event
    ↓
Context
    ↓
Rule Applied
    ↓
Result
    ↓
Evidence
    ↓
Reviewability
```

## Questions to Check Understanding

1. What is an audit log?
2. Why does this project need audit logs?
3. What should be recorded in an audit log?
4. What should not be recorded if it is unnecessary?
5. Why is a timestamp important?
6. Why should the applied rule be stored?
7. How does audit logging support compliance?
8. What is traceability?
9. How can audit logs create privacy risks?
10. How can the system prove that it followed its own rules?

---

# Stage 8 — Privacy and Data Protection Logic

## Parallel to Development Stage

Privacy model, minimization rules, purpose documentation.

## Learning Goal

Understand the privacy principles behind wallet-based identity verification.

## Key Notions

- Privacy by design
- Privacy by default
- Data minimization
- Purpose limitation
- Consent
- User control
- Selective disclosure
- Unlinkability
- Personal data
- Legal basis
- Retention limitation

## Concepts to Understand

A wallet-based verification system should reduce unnecessary personal data sharing.

The relying party should ask:

```text
What do we need to know?
```

Not:

```text
What data can we collect?
```

Example:

```text
Need:
Confirm user may access service.

Possible proof:
User is over 18.

Unnecessary:
Full name, address, birth date, ID number.
```

Privacy should be designed into the system rules, not added at the end.

## Meta Scheme

```text
Purpose
    ↓
Minimum Required Attribute
    ↓
Selective Disclosure
    ↓
Limited Storage
    ↓
Audit Without Over-Collection
```

## Questions to Check Understanding

1. What is privacy by design?
2. What is privacy by default?
3. What is data minimization?
4. What is purpose limitation?
5. Why is selective disclosure important?
6. What is the risk of storing full wallet responses?
7. Why should the system separate verification from data collection?
8. How can audit logs respect privacy?
9. What does user control mean in the wallet context?
10. How can privacy become a business advantage?

---

# Stage 9 — Architecture and Component Thinking

## Parallel to Development Stage

Architecture documentation, module overview, component responsibilities.

## Learning Goal

Understand how the system should be structured conceptually.

## Key Notions

- Component
- Module
- Boundary
- Interface
- API
- Backend
- Dashboard
- Database
- Request builder
- Response processor
- Audit service
- Rule repository
- Simulation layer

## Concepts to Understand

Each part of the system should have a clear responsibility.

Possible conceptual components:

```text
Dashboard
    allows users to define or trigger verification cases

Backend API
    receives requests and coordinates processing

Rule Service
    stores business verification rules

Request Builder
    converts rules into wallet requests

Wallet Simulator
    returns simulated wallet responses

Response Processor
    validates responses against rules

Audit Service
    records what happened

Database
    stores rules, requests, responses, and audit records
```

## Meta Scheme

```text
User Interface
    ↓
Business Logic
    ↓
Verification Logic
    ↓
Persistence
    ↓
Audit and Review
```

## Questions to Check Understanding

1. What are the main components of the prototype?
2. What should the dashboard do?
3. What should the backend API do?
4. What is the responsibility of the request builder?
5. What is the responsibility of the response processor?
6. Why should audit logic be separated from request logic?
7. What data should the database store?
8. What is a system boundary?
9. Why is modular architecture useful?
10. How would you explain the system architecture with a simple diagram?

---

# Stage 10 — Stakeholders and Organizational Value

## Parallel to Development Stage

Business documentation, stakeholder mapping, project explanation.

## Learning Goal

Understand who benefits from the system and how to explain its value.

## Key Notions

- Stakeholder
- Business value
- Compliance value
- Operational efficiency
- Risk reduction
- User trust
- Legal department
- IT department
- Process owner
- Service provider
- End user
- Auditor

## Concepts to Understand

Different stakeholders care about different things.

```text
End User:
Wants simple, safe, privacy-friendly verification.

Business Department:
Wants a clear process and fewer manual checks.

Legal / Compliance:
Wants lawful, documented, minimal data handling.

IT Department:
Wants a structured, maintainable integration.

Auditor:
Wants evidence that rules were followed.

Management:
Wants risk reduction and future readiness.
```

## Meta Scheme

```text
Stakeholder
    ↓
Problem
    ↓
Expected Value
    ↓
System Feature
    ↓
Evidence of Success
```

## Questions to Check Understanding

1. Who are the main stakeholders of this project?
2. What does the end user gain from wallet-based verification?
3. What does the organization gain?
4. What does the legal department care about?
5. What does the IT department care about?
6. Why would an auditor care about this system?
7. How does the system reduce manual work?
8. How can the system reduce compliance risk?
9. How can the system increase user trust?
10. How would you explain the business value of the prototype?

---

# Stage 11 — Testing Understanding Through Scenarios

## Parallel to Development Stage

Example cases, test cases, prototype validation.

## Learning Goal

Learn to validate the system through realistic scenarios.

## Key Notions

- Test scenario
- Positive case
- Negative case
- Edge case
- Expected result
- Actual result
- Acceptance test
- Validation
- Business rule test
- Compliance test

## Concepts to Understand

A scenario checks whether the system behaves correctly.

Example positive scenario:

```text
User has valid proof of age over 18.
System approves access.
Audit log records the request, purpose, result, and applied rule.
```

Example negative scenario:

```text
User does not provide required proof.
System denies access or sends case to manual review.
Audit log records the failure reason.
```

Example privacy scenario:

```text
System only needs age-over-18 proof.
System must not request full birth date.
```

## Meta Scheme

```text
Scenario
    ↓
Input
    ↓
Expected Rule
    ↓
Expected Decision
    ↓
Expected Audit Evidence
```

## Questions to Check Understanding

1. What is a test scenario?
2. What is a positive test case?
3. What is a negative test case?
4. What is an edge case?
5. Why should business rules be tested?
6. Why should privacy rules be tested?
7. What should happen when a required attribute is missing?
8. What should happen when a credential is expired?
9. What should an audit log contain after a failed verification?
10. How do test cases prove that the prototype works?

---

# Stage 12 — Final Project Explanation and Review

## Parallel to Development Stage

Final documentation, presentation, review, improvement notes.

## Learning Goal

Be able to explain the project clearly from business, technical, privacy, and compliance perspectives.

## Key Notions

- Final project narrative
- Problem statement
- Solution overview
- Scope
- Architecture
- Business process
- Requirement traceability
- Privacy model
- Audit model
- Limitations
- Future work

## Concepts to Understand

At the end, you should be able to explain:

```text
Problem:
Organizations need a structured way to request and process EUDI Wallet-based identity or attribute verification.

Solution:
This prototype translates business requirements into wallet verification requests, processes simulated responses, and records audit evidence.

Value:
It helps organizations prepare for wallet-based digital identity while improving privacy, compliance, and process clarity.

Limitations:
It is a prototype and does not implement a production wallet, cryptographic verification, or full legal compliance automation.
```

## Meta Scheme

```text
Problem
    ↓
Context
    ↓
Proposed Solution
    ↓
How It Works
    ↓
Why It Matters
    ↓
Limitations
    ↓
Future Improvements
```

## Questions to Check Understanding

1. What problem does the project solve?
2. Why is EUDI Wallet relevant for relying parties?
3. How does the system translate business rules into wallet requests?
4. How does the system process wallet responses?
5. How does the system support auditability?
6. How does the system support privacy?
7. What are the main components of the prototype?
8. What are the project limitations?
9. What would be needed for a production-ready system?
10. How would you present the project in five minutes?

---

# General Weekly Learning Routine

Use this routine for each development week.

## Step 1 — Read

Read the relevant documentation, notes, and source material for the stage.

Focus on understanding the terms before implementation.

## Step 2 — Rewrite

Rewrite the topic in your own words.

Use this format:

```text
This topic is about ...

It matters because ...

In this project, it is used for ...

One example is ...
```

## Step 3 — Draw

Create a small diagram or flow.

Example:

```text
Business Rule → Wallet Request → Wallet Response → Decision → Audit Log
```

## Step 4 — Explain

Explain the topic as if speaking to:

1. a technical person,
2. a business person,
3. a legal/compliance person,
4. a complete beginner.

## Step 5 — Answer Questions

Answer the stage questions without looking at the notes.

Mark each answer:

```text
[ ] I can answer clearly
[ ] I can answer partly
[ ] I cannot answer yet
```

## Step 6 — Connect to Project Files

For each topic, connect it to one or more project files.

Example:

```text
Topic: Audit Logging

Related files:
- docs/privacy_model.md
- docs/data_model.md
- docs/architecture.md
- backend/app/models/audit_log.py
```

## Step 7 — Write Learning Notes

Add short notes to the project notebook.

Recommended format:

```md
## Topic

### My Explanation

### Important Terms

### Project Connection

### Example

### Open Questions
```

---

# Learning Progress Checklist

Use this checklist to track progress.

```md
| Stage | Topic | Can Explain | Can Apply | Can Answer Questions | Notes |
|---|---|---:|---:|---:|---|
| 0 | Project Orientation | [ ] | [ ] | [ ] | |
| 1 | EUDI Wallet Basics | [ ] | [ ] | [ ] | |
| 2 | Use Cases and Service Blueprints | [ ] | [ ] | [ ] | |
| 3 | Requirements Thinking | [ ] | [ ] | [ ] | |
| 4 | Data and Attribute Modeling | [ ] | [ ] | [ ] | |
| 5 | Verification Request Logic | [ ] | [ ] | [ ] | |
| 6 | Wallet Response and Decision Logic | [ ] | [ ] | [ ] | |
| 7 | Audit and Compliance Evidence | [ ] | [ ] | [ ] | |
| 8 | Privacy and Data Protection Logic | [ ] | [ ] | [ ] | |
| 9 | Architecture and Component Thinking | [ ] | [ ] | [ ] | |
| 10 | Stakeholders and Organizational Value | [ ] | [ ] | [ ] | |
| 11 | Scenario Testing | [ ] | [ ] | [ ] | |
| 12 | Final Project Explanation | [ ] | [ ] | [ ] | |
```

---

# Final Self-Assessment Questions

At the end of the project, answer these without notes.

## Project Understanding

1. What is this project?
2. What is it not?
3. Who is it for?
4. What problem does it solve?
5. Why is EUDI Wallet relevant?

## Business Understanding

1. What business process does the prototype support?
2. What are the main stakeholder needs?
3. How are use cases converted into requirements?
4. What value does the system provide?
5. What risks does the system reduce?

## Technical Understanding

1. What are the main system components?
2. How does a verification request get created?
3. How is a wallet response processed?
4. What data is stored?
5. What should be modularized?

## Privacy and Compliance Understanding

1. How does the system support data minimization?
2. What is purpose limitation?
3. Why is selective disclosure useful?
4. What should be included in audit logs?
5. What should not be stored unnecessarily?

## Presentation Readiness

1. Can I explain the project in two minutes?
2. Can I explain the architecture with one diagram?
3. Can I explain the business value?
4. Can I explain the privacy value?
5. Can I explain the project limitations honestly?
