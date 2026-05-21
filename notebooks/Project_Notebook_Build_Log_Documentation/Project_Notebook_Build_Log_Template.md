# Project Notebook — Build Log & Documentation

> Main purpose: This notebook documents what is actually being built, why decisions were made, what changed, what problems appeared, and what should be done next.
>
> Use this notebook as the source for your README, GitHub documentation, IHK project report, and presentation notes.

---

## Project Index

| Section | Purpose | Status |
|---|---|---|
| 1. Project Scope | Define what the project is and is not | Draft |
| 2. User Stories | Describe who uses the system and why | Draft |
| 3. Requirements | Functional and non-functional requirements | Draft |
| 4. Data Model | Database tables, entities, fields, relationships | Draft |
| 5. API Design | Endpoints, request/response formats, validation rules | Draft |
| 6. Build Log | Weekly and daily implementation progress | Active |
| 7. Testing Notes | Manual tests, automated tests, bugs, results | Draft |
| 8. Problems & Decisions | Important technical or project decisions | Active |
| 9. Presentation / IHK Notes | Material useful for report, demo, and final explanation | Draft |

---

# 1. Project Scope

## 1.1 Project Summary

**Project name:**  
EUDI Relying Party Integration Bus

**Short description:**  
A backend prototype that helps organizations define, manage, and process digital credential verification requests in a structured and privacy-aware way.

**Main goal:**  
Build a prototype that demonstrates how a relying party could request only the necessary identity data from an EUDI Wallet flow.

**Target users:**  
- Companies
- Public institutions
- Relying parties
- Developers integrating verification flows
- Technical evaluators / IHK examiners

---

## 1.2 What This Project Includes

```text
[BUILD]
The project includes:
- Verification template management
- Mock wallet response handling
- Minimal data request modeling
- Audit logging
- API endpoints
- Basic dashboard or demo interface
- Documentation for technical and IHK explanation
```

---

## 1.3 What This Project Does Not Include

```text
[OUT OF SCOPE]
The project does not include:
- Building a real EUDI Wallet
- Acting as an issuer
- Acting as a QTSP
- Full production security certification
- Real personal identity document processing
- Full legal compliance implementation
```

---

## 1.4 Scope Decisions

| Date | Decision | Reason | Impact |
|---|---|---|---|
| YYYY-MM-DD | Use mock wallet responses first | Real wallet integration is too large for version 1 | Faster prototype development |
| YYYY-MM-DD | Focus on relying party backend | Clearer project boundary | Avoids wallet/issuer complexity |

---

# 2. User Stories

## 2.1 User Story Template

```text
[USER STORY]
As a [type of user],
I want to [perform an action],
so that [benefit or reason].
```

---

## 2.2 User Stories

### User Story 1 — Create Verification Template

**Tag:** [BUILD]  
**Priority:** High  
**Status:** Draft

```text
As a relying party administrator,
I want to create a verification template,
so that my organization can define which identity claims are required for a specific business process.
```

**Acceptance criteria:**
- Template has a name
- Template has a purpose
- Template defines required claims
- Template defines optional claims
- Template defines accepted credential types
- Template defines retention policy
- Template defines risk level

---

### User Story 2 — Process Mock Wallet Response

**Tag:** [BUILD]  
**Priority:** High  
**Status:** Draft

```text
As a backend system,
I want to receive a mock wallet response,
so that I can validate whether the response satisfies the verification template.
```

**Acceptance criteria:**
- Response can be received through an API endpoint
- Response is checked against required claims
- Missing claims are detected
- Result is stored or returned
- Audit log event is created

---

# 3. Requirements

## 3.1 Functional Requirements

| ID | Requirement | Priority | Status | Related Section |
|---|---|---|---|---|
| FR-001 | System can create verification templates | High | Draft | API Design |
| FR-002 | System can list existing templates | High | Draft | API Design |
| FR-003 | System can process mock wallet responses | High | Draft | API Design |
| FR-004 | System can create audit log events | High | Draft | Data Model |
| FR-005 | System can detect missing required claims | High | Draft | Testing Notes |

---

## 3.2 Non-Functional Requirements

| ID | Requirement | Priority | Status | Reason |
|---|---|---|---|---|
| NFR-001 | API should use clear JSON request and response formats | High | Draft | Easier integration and testing |
| NFR-002 | System should minimize stored personal data | High | Draft | Privacy-aware design |
| NFR-003 | Code should be modular and documented | High | Draft | Easier maintenance |
| NFR-004 | Each important decision should be documented | Medium | Active | Useful for IHK report |
| NFR-005 | Prototype should be easy to run locally | Medium | Draft | Easier demo and review |

---

# 4. Data Model

## 4.1 Entity Overview

```text
[DATA MODEL]
Main entities:
- VerificationTemplate
- VerificationRequest
- WalletResponse
- AuditLog
- PrivacyWarning
```

---

## 4.2 Entity Template

### Entity: VerificationTemplate

**Purpose:**  
Defines what identity information is requested for a specific verification process.

| Field | Type | Required | Description |
|---|---|---|---|
| id | UUID | Yes | Unique template identifier |
| name | string | Yes | Human-readable template name |
| purpose | string | Yes | Reason for requesting claims |
| required_claims | list/string JSON | Yes | Claims that must be provided |
| optional_claims | list/string JSON | No | Claims that may be provided |
| accepted_credential_types | list/string JSON | Yes | Allowed credential types |
| retention_policy | string | Yes | How long data is kept |
| risk_level | string | Yes | Low, medium, or high |
| created_at | datetime | Yes | Creation timestamp |
| updated_at | datetime | No | Last update timestamp |

**Open questions:**
- Should claims be stored as JSON or normalized into a separate table?
- Should retention policy be an enum?
- Should risk level affect validation behavior?

---

## 4.3 Relationship Notes

```text
[QUESTION]
A VerificationRequest probably references one VerificationTemplate.
A WalletResponse probably references one VerificationRequest.
An AuditLog event probably references one VerificationRequest.
```

---

# 5. API Design

## 5.1 API Overview

| Method | Endpoint | Purpose | Status |
|---|---|---|---|
| POST | /templates | Create verification template | Draft |
| GET | /templates | List verification templates | Draft |
| GET | /templates/{template_id} | Read one verification template | Draft |
| POST | /verification-requests | Create verification request | Draft |
| POST | /wallet-responses/mock | Submit mock wallet response | Draft |
| GET | /audit-logs | List audit log events | Draft |

---

## 5.2 Endpoint Template

### Endpoint: POST /templates

**Tag:** [BUILD]  
**Status:** Draft

**Purpose:**  
Create a new verification template.

**Request body:**

```json
{
  "name": "Age Verification",
  "purpose": "Check whether a user is over 18",
  "required_claims": ["age_over_18"],
  "optional_claims": [],
  "accepted_credential_types": ["PID"],
  "retention_policy": "do_not_store_claim_values",
  "risk_level": "low"
}
```

**Success response:**

```json
{
  "id": "template-uuid",
  "name": "Age Verification",
  "status": "created"
}
```

**Validation rules:**
- `name` must not be empty
- `purpose` must not be empty
- `required_claims` must contain at least one claim
- `risk_level` must be `low`, `medium`, or `high`

**Open questions:**
- Should template names be unique?
- Should accepted credential types be predefined?

---

# 6. Build Log

## 6.1 Weekly Summary Template

## Week: YYYY-MM-DD to YYYY-MM-DD

**Main goal for this week:**  
Write the main goal here.

**Completed:**
- [x] Completed task 1
- [x] Completed task 2

**In progress:**
- [ ] Current task 1
- [ ] Current task 2

**Blocked:**
- Blocker 1
- Blocker 2

**Important decisions:**
- [DECISION] Decision summary

**Next 3 tasks:**
1. Task 1
2. Task 2
3. Task 3

---

## 6.2 Daily Build Entry Template

### Date: YYYY-MM-DD

**Tag:** [BUILD]  
**Focus:** Write the main focus of the work session.

#### Goal

Write what should be achieved today.

#### Work Done

- Work item 1
- Work item 2
- Work item 3

#### Result

Write what changed in the project.

#### Problems Found

- Problem 1
- Problem 2

#### Decision Made

```text
[DECISION]
Write the decision here.

Reason:
Write why this decision was made.

Impact:
Write what this changes in the project.
```

#### Next Action

- [ ] Next action 1
- [ ] Next action 2

---

# 7. Testing Notes

## 7.1 Test Case Template

### Test Case: TC-001 — Create Verification Template

**Tag:** [TEST]  
**Status:** Draft  
**Related requirement:** FR-001

**Goal:**  
Check whether a verification template can be created successfully.

**Preconditions:**
- Backend is running
- Database is available
- API endpoint exists

**Test steps:**
1. Send POST request to `/templates`
2. Include valid JSON body
3. Check response status
4. Check response body
5. Check database entry

**Expected result:**
- API returns success response
- Template is stored correctly
- Audit log event is created if required

**Actual result:**  
Write result here.

**Pass / Fail:**  
Pending

---

## 7.2 Bug Report Template

### Bug: Short Bug Title

**Tag:** [BUG]  
**Date:** YYYY-MM-DD  
**Status:** Open  
**Severity:** Low / Medium / High

**What happened:**  
Describe the bug.

**Expected behavior:**  
Describe what should have happened.

**Steps to reproduce:**
1. Step 1
2. Step 2
3. Step 3

**Possible cause:**  
Write current guess.

**Fix:**  
Write fix after solved.

**Retest result:**  
Pending

---

# 8. Problems & Decisions

## 8.1 Decision Record Template

### Decision: Short Decision Title

**Tag:** [DECISION]  
**Date:** YYYY-MM-DD  
**Status:** Accepted / Rejected / Revisit Later

**Context:**  
Explain the situation or problem.

**Options considered:**

| Option | Benefit | Problem |
|---|---|---|
| Option A | Benefit | Problem |
| Option B | Benefit | Problem |

**Decision:**  
Write the final decision.

**Reason:**  
Explain why this option was chosen.

**Impact:**  
Explain what this changes in code, scope, documentation, or testing.

**Follow-up task:**
- [ ] Write next action here

---

## 8.2 Problem Record Template

### Problem: Short Problem Title

**Tag:** [QUESTION]  
**Date:** YYYY-MM-DD  
**Status:** Open / Solved / Revisit Later

**Problem:**  
Describe the problem clearly.

**Why it matters:**  
Explain how it affects the project.

**Current understanding:**  
Write what is already known.

**Possible solutions:**
- Solution 1
- Solution 2
- Solution 3

**Chosen solution:**  
Write solution after decision.

**Next action:**
- [ ] Write next action here

---

# 9. Presentation / IHK Notes

## 9.1 IHK-Relevant Summary

**Project problem:**  
Organizations need a structured way to request and process digital identity data without requesting more data than necessary.

**Project solution:**  
The prototype provides a relying party integration layer for defining verification templates, processing mock wallet responses, and documenting verification events.

**Technical focus:**
- Backend API
- Data modeling
- Validation logic
- Audit logging
- Privacy-aware request design
- Documentation

**Demo idea:**
1. Show verification template creation
2. Show mock wallet response submission
3. Show validation result
4. Show audit log event
5. Explain privacy and scope decisions

---

## 9.2 Presentation Notes Template

### Slide / Topic: Short Title

**Purpose of this slide:**  
Write what this slide should explain.

**Main points:**
- Point 1
- Point 2
- Point 3

**Demo connection:**  
Write how this connects to the working prototype.

**IHK relevance:**  
Write why this is relevant for evaluation.

---

# Tag System

Use tags to make notes easier to scan.

| Tag | Meaning | Use When |
|---|---|---|
| [BUILD] | Implementation work | You create or change code, files, APIs, database models, or dashboard parts |
| [DECISION] | Final project decision | You choose one approach and continue with it |
| [QUESTION] | Open question | Something is unclear and needs research or testing |
| [TEST] | Testing note | You test an endpoint, model, function, or user flow |
| [BUG] | Problem in implementation | Something does not work as expected |
| [IHK] | Exam/report relevant | Something should be reused in documentation, presentation, or final report |
| [OUT OF SCOPE] | Not part of prototype | Something is intentionally excluded |
| [DATA MODEL] | Database or entity note | You define fields, relationships, or storage decisions |
| [API] | Endpoint or request/response note | You design or update API behavior |

---

# Formatting Rules

## 1. Use headings to show structure

Use large headings for notebook sections:

```md
# Main Section
## Subsection
### Entry or Record
```

Example:

```md
# 6. Build Log
## Week: 2026-05-21 to 2026-05-28
### Date: 2026-05-21
```

---

## 2. Use bold text for important labels

Use bold text for fields that should be easy to scan.

```md
**Goal:**
**Decision:**
**Reason:**
**Next action:**
```

---

## 3. Use tables for structured comparison

Use tables when comparing requirements, endpoints, decisions, or statuses.

Good for:
- requirements
- API endpoints
- database fields
- options considered
- test results

Example:

```md
| ID | Requirement | Priority | Status |
|---|---|---|---|
| FR-001 | Create verification template | High | Draft |
```

---

## 4. Use code blocks for exact technical examples

Use code blocks for JSON, terminal commands, schemas, pseudo-logic, or fixed decision text.

```json
{
  "name": "Age Verification",
  "required_claims": ["age_over_18"]
}
```

Use plain text blocks for decisions or scope notes:

```text
[DECISION]
The first prototype uses mock wallet responses.

Reason:
Real wallet integration is too large for version 1.
```

---

## 5. Use checkboxes for tasks

Use checkboxes only for actions that can be completed.

```md
- [ ] Create template model
- [ ] Add POST /templates endpoint
- [ ] Write first test case
- [x] Create project README draft
```

---

## 6. Keep project notes separate from theory notes

This notebook is for build progress and project documentation.

Use this notebook for:
- project scope
- implementation progress
- API design
- database decisions
- testing
- bugs
- IHK notes

Do not use this notebook for general learning notes unless they directly affect the project.

Examples:

| Topic | Correct Notebook |
|---|---|
| What is JSON Schema? | Theory & Skills |
| Why this project uses JSON Schema | Project Notebook |
| ARF legal background | EUDI Architecture & Law |
| How ARF affects relying party scope | Project Notebook |

---

## 7. Every serious entry should end with a next action

A project notebook should lead to progress.

Use this ending:

```md
**Next action:**
- [ ] Write the next concrete task here
```

---

## 8. Keep decision records short but clear

A good decision record answers:

1. What problem existed?
2. What options were considered?
3. What was chosen?
4. Why was it chosen?
5. What changes because of it?

---

## 9. Use status words consistently

Recommended status values:

```text
Draft
Active
Blocked
Done
Open
Solved
Revisit Later
Accepted
Rejected
Pending
Pass
Fail
```

---

## 10. Avoid decorative formatting

Use visual structure, not decoration.

Recommended:
- headings
- tables
- tags
- bold labels
- code blocks
- checkboxes
- horizontal separators

Avoid:
- emojis
- too many colors
- unclear symbols
- long unstructured paragraphs

