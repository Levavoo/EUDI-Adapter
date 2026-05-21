# EUDI Wallet Relying Party Integration Bus

## 1. Project Overview

The **EUDI Wallet Relying Party Integration Bus** is a prototype backend system that explores how companies could connect their existing business processes to future EUDI Wallet-based verification flows.

The project focuses on the **relying party side** of the ecosystem.

A relying party is an organization that wants to verify information about a user, for example:

- whether the user is over 18
- whether the user lives in a specific country
- whether the user has a valid credential
- whether the user meets a business requirement for onboarding or access

This project does **not** build a wallet.

It builds a prototype service that helps a company define verification requests, simulate wallet responses, validate basic trust rules, and store privacy-preserving audit logs.

---

## 2. Simple Explanation

In the future, many users may hold digital identity credentials in an EUDI Wallet.

A company may not want to manually check passports, PDFs, screenshots, or uploaded documents anymore. Instead, the company may want to ask:

> Can the user prove this specific fact through a trusted wallet?

Example:

Instead of requesting a full identity document, a company may only request:

    age_over_18 = true

This project explores how such requests could be structured, processed, validated, and documented.

---

## 3. Core Idea

The central idea of this project is:

    Business process requirement
            ↓
    Minimal verification request
            ↓
    Simulated wallet presentation
            ↓
    Validation
            ↓
    Audit log
            ↓
    Dashboard / analysis

The project translates business needs into structured verification templates.

Example:

    Business need:
    The company needs to check whether the user is allowed to access an age-restricted service.

    Verification request:
    Request only "age_over_18", not the full date of birth or full identity document.

---

## 4. Project Goals

The project aims to create a clear prototype for:

- defining business verification templates
- mapping business processes to required identity claims
- simulating wallet-based verification responses
- validating whether required claims are present
- checking whether unnecessary data was received
- storing audit logs for transparency and analysis
- providing a simple dashboard for process visibility

---

## 5. What This Project Is

This project is:

- a learning project
- a backend prototype
- a data and process analysis project
- a relying party integration concept
- a foundation for future EUDI Wallet-related work
- a possible portfolio or IHK project foundation

It focuses on the question:

> How can an organization structure, process, and analyze wallet-based verification requests in a privacy-preserving way?

---

## 6. What This Project Is Not

This project is **not**:

- a certified EUDI Wallet
- an official EU implementation
- a replacement for the EUDI Wallet Reference Implementation
- a production-ready identity verification system
- a real QTSP service
- a real government PID integration
- a cryptographic proof validation engine
- a legally complete compliance solution

The first version uses mock data and simulated wallet responses.

Real EUDI Wallet protocols, cryptographic validation, OpenID4VP, SD-JWT VC, QTSP integrations, and certification processes may be studied later, but they are outside the first prototype scope.

---

## 7. Target Users

This prototype is designed from the perspective of organizations that may later act as relying parties.

Possible example users:

- banks
- insurance companies
- telecom providers
- universities
- employers
- public service portals
- age-restricted online services
- hotels or travel companies
- software vendors building compliance tools

The prototype is especially focused on people who need to understand:

- what data is requested
- why the data is requested
- whether the request is minimal
- whether the wallet response satisfies the business requirement
- whether the process is documented properly

---

## 8. Example Use Cases

### 8.1 Age Verification

A company wants to verify that a user is over 18.

Instead of requesting:

- full name
- date of birth
- address
- passport number

the system should request only:

    age_over_18

### 8.2 Residence Verification

A company wants to verify whether a user lives in Germany.

The system may request:

    country_of_residence

instead of a full address.

### 8.3 Employment Onboarding

An employer wants to verify basic identity information for onboarding.

The system may request:

- given_name
- family_name
- date_of_birth
- residence_country

### 8.4 Student Status Verification

A service wants to verify whether a user is currently enrolled as a student.

The system may request:

- student_status
- institution_name
- valid_until

---

## 9. Main System Components

The prototype is divided into several logical modules.

### 9.1 Verification Template Service

Stores reusable templates for common verification scenarios.

A template defines:

- business process
- purpose
- required claims
- optional claims
- accepted credential types
- trusted issuer categories
- retention policy
- risk level

Example template:

```json
{
  "template_id": "age_verification_v1",
  "business_process": "age_restricted_service_access",
  "purpose": "Verify that the user is at least 18 years old without collecting full birth date.",
  "required_claims": ["age_over_18"],
  "optional_claims": [],
  "accepted_credential_types": ["PID", "AgeAttestation"],
  "trusted_issuer_categories": ["government", "qualified_attribute_provider"],
  "retention_policy": "store_result_only_30_days",
  "risk_level": "low"
}
```

### 9.2 Verification Request Service

Creates an individual verification request from a template.

A request represents one actual verification attempt.

Example:

    Company creates request:
    "Verify user X for age-restricted access using template age_verification_v1."

### 9.3 Mock Wallet Service

Simulates a wallet response.

In the first prototype, there is no real wallet connection. Instead, the system accepts predefined mock presentations.

Example mock response:

```json
{
  "request_id": "req_001",
  "credential_type": "AgeAttestation",
  "issuer": "Mock Government Issuer",
  "claims": {
    "age_over_18": true
  },
  "user_consent": true
}
```

### 9.4 Validation Service

Checks whether the wallet response satisfies the verification request.

The validation service checks:

- Are all required claims present?
- Is the credential type accepted?
- Is the issuer trusted in the mock trust list?
- Has the user consented?
- Has the request expired?
- Did the wallet return more data than necessary?

The last point is important for privacy.

Example privacy warning:

    Requested claim:
    age_over_18

    Received claims:
    age_over_18, full_name, date_of_birth, address

    Result:
    Privacy warning: unnecessary claims received.

### 9.5 Audit Log Service

Stores events that happen during the verification process.

Example events:

- request_created
- presentation_received
- validation_completed
- privacy_warning_created
- request_failed
- request_expired

Audit logs help explain what happened and why.

### 9.6 Dashboard

The dashboard provides a simple visual overview of:

- verification requests
- request status
- audit events
- privacy warnings
- most requested claims
- successful and failed verifications

The first version may use Streamlit for fast development.

---

## 10. Planned Project Structure

    eudi-relying-party-integration-bus/
    │
    ├── README.md
    │
    ├── docs/
    │   ├── project_scope.md
    │   ├── glossary.md
    │   ├── use_cases.md
    │   ├── architecture.md
    │   ├── data_model.md
    │   ├── api_design.md
    │   ├── privacy_model.md
    │   └── ihk_project_outline.md
    │
    ├── backend/
    │   ├── app/
    │   │   ├── main.py
    │   │   ├── models/
    │   │   ├── schemas/
    │   │   ├── services/
    │   │   ├── routers/
    │   │   └── database.py
    │   │
    │   ├── tests/
    │   └── requirements.txt
    │
    ├── dashboard/
    │   ├── app.py
    │   └── README.md
    │
    ├── examples/
    │   ├── verification_templates.json
    │   ├── mock_wallet_presentations.json
    │   └── trusted_issuers.json
    │
    └── diagrams/
        ├── process_flow.drawio
        └── architecture.drawio

---

## 11. Folder Explanation

### `docs/`

Contains project documentation.

Important files:

- `project_scope.md` — defines what is included and excluded
- `glossary.md` — explains important terms
- `use_cases.md` — describes business scenarios
- `architecture.md` — explains the system design
- `data_model.md` — explains entities and relationships
- `api_design.md` — documents planned API endpoints
- `privacy_model.md` — explains data minimization and audit logic
- `ihk_project_outline.md` — stores possible IHK project framing

### `backend/`

Contains the FastAPI backend.

The backend is responsible for:

- managing verification templates
- creating verification requests
- receiving mock wallet presentations
- validating responses
- writing audit logs
- exposing API endpoints

### `backend/app/models/`

Contains database models.

Example future files:

- `verification_template_model.py`
- `verification_request_model.py`
- `wallet_presentation_model.py`
- `audit_log_model.py`

### `backend/app/schemas/`

Contains Pydantic schemas.

Schemas define the structure of incoming and outgoing API data.

Example future files:

- `verification_template_schema.py`
- `verification_request_schema.py`
- `wallet_presentation_schema.py`
- `audit_log_schema.py`

### `backend/app/services/`

Contains business logic.

Example future files:

- `template_service.py`
- `request_service.py`
- `validation_service.py`
- `audit_log_service.py`

### `backend/app/routers/`

Contains API route definitions.

Example future files:

- `template_router.py`
- `request_router.py`
- `mock_wallet_router.py`
- `audit_log_router.py`
- `analytics_router.py`

### `backend/tests/`

Contains automated tests.

The tests should check:

- template creation
- request creation
- validation logic
- privacy warning logic
- audit log creation

### `dashboard/`

Contains the dashboard application.

The dashboard shows the current state of the system and supports analysis.

### `examples/`

Contains example JSON files.

These files are used for learning, testing, and demo flows.

### `diagrams/`

Contains architecture and process diagrams.

---

## 12. First Prototype Scope

The first prototype should support the following flow:

1. Load or create verification templates.
2. Create a verification request from a selected template.
3. Simulate a wallet response with mock data.
4. Validate the response.
5. Store audit log events.
6. Show the result in a dashboard.

This is the minimum useful version.

---

## 13. Planned API Endpoints

Possible first API endpoints:

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/health` | Checks whether the backend is running |
| POST | `/templates` | Creates a new verification template |
| GET | `/templates` | Returns all verification templates |
| GET | `/templates/{template_id}` | Returns one verification template |
| POST | `/verification-requests` | Creates a new verification request from a template |
| GET | `/verification-requests` | Returns all verification requests |
| GET | `/verification-requests/{request_id}` | Returns one verification request |
| POST | `/mock-wallet/presentations` | Receives a simulated wallet presentation |
| GET | `/audit-logs` | Returns audit log entries |
| GET | `/analytics/summary` | Returns basic process statistics |

---

## 14. Example Process Flow

    Company system
        ↓
    Creates verification request
        ↓
    Relying Party Integration Bus
        ↓
    Generates structured request
        ↓
    Mock wallet responds
        ↓
    Validation service checks response
        ↓
    Audit log service stores events
        ↓
    Dashboard displays status and privacy warnings

---

## 15. Data Minimization Principle

A central principle of this project is data minimization.

The system should help answer:

> What is the smallest amount of information needed to satisfy the business process?

Example:

Bad request:

    Request full identity document to check age.

Better request:

    Request only whether the user is over 18.

The system should detect when more data was received than necessary.

---

## 16. Audit Log Principle

The audit log should document the process without storing unnecessary personal data.

The audit log should answer:

- What request was created?
- Which template was used?
- What claims were required?
- Was the response valid?
- Was there a privacy warning?
- When did each event happen?
- Which system component created the event?

The audit log should avoid storing full personal identity data unless clearly necessary.

---

## 17. Technical Stack

Planned first version:

| Layer | Technology |
|---|---|
| Backend API | Python + FastAPI |
| Validation | Pydantic |
| Database | SQLite first, PostgreSQL later |
| Dashboard | Streamlit first, React later possible |
| Testing | pytest |
| Documentation | Markdown |
| Diagrams | draw.io |
| Deployment | Docker later |

---

## 18. Development Strategy

The project will be developed in small, modular steps.

Each important code file should have a matching documentation file later.

Example:

    validation_service.py
    validation_service.md

This helps keep the project understandable for:

- the developer
- future collaborators
- IHK documentation
- portfolio reviewers
- technical interviewers

---

## 19. First Milestones

### Milestone 1 — Project Foundation

Create:

- project folder structure
- README.md
- project scope document
- glossary
- first use cases

### Milestone 2 — Example Data

Create:

- verification template examples
- mock wallet presentation examples
- trusted issuer examples

### Milestone 3 — Backend Skeleton

Create:

- FastAPI application
- health endpoint
- basic routers
- basic schemas

### Milestone 4 — Template and Request Logic

Create:

- template schema
- request schema
- template endpoints
- request endpoints

### Milestone 5 — Mock Wallet and Validation

Create:

- mock wallet presentation endpoint
- validation service
- basic trust checks
- privacy warning logic

### Milestone 6 — Audit Logging

Create:

- audit log model
- audit log service
- audit log endpoints

### Milestone 7 — Dashboard

Create:

- request overview
- audit log table
- privacy warning view
- summary metrics

---

## 20. Current Status

Project status:

    Planning / Foundation Phase

Current focus:

    Define the project clearly before implementing the backend.

Next planned step:

    Create the first verification template examples:
    1. Age verification
    2. Residence verification
    3. Employment onboarding

---

## 21. Long-Term Vision

In the future, this prototype could grow into a more advanced system that supports:

- real wallet protocol integration
- OpenID4VP-based presentation flows
- SD-JWT VC support
- trust registry lookup
- verifier registration workflows
- QTSP service integration
- company compliance dashboards
- sector-specific verification templates
- enterprise API gateway integration

These topics are intentionally outside the first version.

---

## 22. Project North Star

The project should always stay focused on this sentence:

> This project helps organizations translate business identity-check requirements into privacy-preserving wallet verification requests, process simulated wallet responses, and analyze the resulting audit logs.