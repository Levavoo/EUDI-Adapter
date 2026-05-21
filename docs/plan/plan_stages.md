# Project Plan — Stages

## Project Name

**EUDI Wallet Relying Party Integration Bus**

## Purpose of This Document

This document separates the project into clear development stages.

The goal is to avoid jumping between too many topics and to build the project step by step.

Each stage has:

- a goal
- required outputs
- files to create or update
- clear exit criteria

---

## Project North Star

> This project helps organizations translate business identity-check requirements into privacy-preserving wallet verification requests, process simulated wallet responses, and analyze the resulting audit logs.

---

## Stage 0 — Project Boundary and Foundation

### Goal

Define what the project is, what it is not, and what the first version should achieve.

This stage prevents scope creep.

### Main Questions

- What problem does this project solve?
- Who is the target user?
- What is included in version 1?
- What is excluded from version 1?
- What should be shown in a demo?

### Deliverables

- `README.md`
- `docs/project_scope.md`
- `docs/glossary.md`
- `docs/plan_stages.md`
- `docs/plan_weeks.md`

### Files to Work On

- `README.md`
- `docs/project_scope.md`
- `docs/glossary.md`

### Exit Criteria

This stage is complete when:

- the README explains the project clearly
- the project scope is written
- important terms are listed in the glossary
- version 1 boundaries are clear
- future topics are separated from current work

### Do Not Work On Yet

- real wallet integration
- cryptography
- QTSP integration
- OpenID4VP
- full legal compliance
- frontend design details

---

## Stage 1 — Use Cases and Business Process Modeling

### Goal

Define realistic company scenarios where a relying party wants to verify user information.

The project should start from business processes, not from technology.

### Main Questions

- What does the company need to verify?
- Why does the company need this information?
- What is the minimum data needed?
- Which data would be too much?
- How should the request be documented?

### First Use Cases

1. Age verification
2. Residence verification
3. Employment onboarding
4. Student status verification

### Deliverables

- `docs/use_cases.md`
- first use case descriptions
- business process list
- claim requirement list
- data minimization notes

### Files to Work On

- `docs/use_cases.md`
- `examples/verification_templates.json`

### Exit Criteria

This stage is complete when:

- at least three use cases are documented
- each use case has a business need
- each use case has required claims
- each use case has optional claims
- each use case has a privacy note
- each use case can become a verification template

---

## Stage 2 — Verification Template Design

### Goal

Create the first structured verification templates.

A verification template defines what a company wants to verify and which claims are needed.

### Template Fields

Each template should include:

- `template_id`
- `template_name`
- `business_process`
- `purpose`
- `required_claims`
- `optional_claims`
- `accepted_credential_types`
- `trusted_issuer_categories`
- `retention_policy`
- `risk_level`

### Deliverables

- `examples/verification_templates.json`
- documented template structure
- explanation of each field
- example templates

### Files to Work On

- `examples/verification_templates.json`
- `docs/data_model.md`
- `docs/privacy_model.md`

### Exit Criteria

This stage is complete when:

- at least three templates exist
- each template is valid JSON
- each template has required claims
- each template has a clear purpose
- each template has a retention policy
- each template avoids unnecessary personal data

---

## Stage 3 — Mock Data and Trust Model

### Goal

Create mock wallet responses and a simple trusted issuer list.

The first version does not connect to a real EUDI Wallet.

### Main Questions

- What does a simulated wallet response look like?
- What claims does the wallet return?
- Did the user consent?
- Which issuer issued the credential?
- Is the issuer trusted in the mock system?

### Deliverables

- `examples/mock_wallet_presentations.json`
- `examples/trusted_issuers.json`
- simple mock trust model
- positive and negative test examples

### Files to Work On

- `examples/mock_wallet_presentations.json`
- `examples/trusted_issuers.json`
- `docs/privacy_model.md`

### Exit Criteria

This stage is complete when:

- mock wallet responses exist
- trusted issuers are listed
- at least one valid response exists
- at least one invalid response exists
- at least one over-sharing response exists

---

## Stage 4 — Backend Skeleton

### Goal

Create the first FastAPI backend structure.

This stage creates the technical foundation without complex business logic.

### Planned Backend Structure

    backend/
    ├── app/
    │   ├── main.py
    │   ├── database.py
    │   ├── models/
    │   ├── schemas/
    │   ├── services/
    │   └── routers/
    ├── tests/
    └── requirements.txt

### First Endpoint

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/health` | Check whether the backend is running |

### Deliverables

- FastAPI app starts successfully
- `/health` endpoint works
- `requirements.txt` exists
- basic backend folder structure is ready

### Files to Work On

- `backend/requirements.txt`
- `backend/app/main.py`
- `backend/app/database.py`

### Exit Criteria

This stage is complete when:

- backend can be started locally
- `/health` returns a success response
- dependencies are documented
- the project can be opened by another developer

---

## Stage 5 — Schemas and Data Models

### Goal

Define the structure of the main project objects.

This includes Pydantic schemas first. Database models can be added later.

### Main Objects

- verification template
- verification request
- wallet presentation
- validation result
- audit log event

### Deliverables

- schema files
- documented schema fields
- example input/output structures

### Files to Create

- `backend/app/schemas/verification_template_schema.py`
- `backend/app/schemas/verification_template_schema.md`
- `backend/app/schemas/verification_request_schema.py`
- `backend/app/schemas/verification_request_schema.md`
- `backend/app/schemas/wallet_presentation_schema.py`
- `backend/app/schemas/wallet_presentation_schema.md`
- `backend/app/schemas/audit_log_schema.py`
- `backend/app/schemas/audit_log_schema.md`

### Exit Criteria

This stage is complete when:

- all main schemas exist
- required and optional fields are clear
- schemas match the example JSON files
- invalid data can be rejected by Pydantic

---

## Stage 6 — Template and Request API

### Goal

Allow the backend to manage verification templates and create verification requests.

### Planned Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| POST | `/templates` | Create a verification template |
| GET | `/templates` | List verification templates |
| GET | `/templates/{template_id}` | Get one verification template |
| POST | `/verification-requests` | Create a verification request |
| GET | `/verification-requests` | List verification requests |
| GET | `/verification-requests/{request_id}` | Get one verification request |

### Deliverables

- template router
- request router
- service logic
- simple in-memory or file-based storage first
- basic tests

### Files to Create

- `backend/app/routers/template_router.py`
- `backend/app/routers/template_router.md`
- `backend/app/routers/request_router.py`
- `backend/app/routers/request_router.md`
- `backend/app/services/template_service.py`
- `backend/app/services/template_service.md`
- `backend/app/services/request_service.py`
- `backend/app/services/request_service.md`

### Exit Criteria

This stage is complete when:

- templates can be created
- templates can be listed
- verification requests can be created from templates
- request status can be viewed
- basic tests pass

---

## Stage 7 — Mock Wallet Presentation and Validation

### Goal

Simulate wallet responses and validate them against verification requests.

### Validation Rules

The system should check:

- required claims are present
- credential type is accepted
- issuer is trusted
- user consent is true
- request is not expired
- response does not contain unnecessary claims

### Deliverables

- mock wallet endpoint
- validation service
- privacy warning logic
- validation result structure

### Planned Endpoint

| Method | Endpoint | Purpose |
|---|---|---|
| POST | `/mock-wallet/presentations` | Receive simulated wallet presentation |

### Files to Create

- `backend/app/routers/mock_wallet_router.py`
- `backend/app/routers/mock_wallet_router.md`
- `backend/app/services/validation_service.py`
- `backend/app/services/validation_service.md`

### Exit Criteria

This stage is complete when:

- mock wallet response can be submitted
- valid response passes validation
- missing required claim fails validation
- untrusted issuer fails validation
- unnecessary extra claims trigger privacy warning

---

## Stage 8 — Audit Logging

### Goal

Store important events from the verification process.

Audit logs should explain what happened without storing unnecessary personal data.

### Event Types

- `request_created`
- `presentation_received`
- `validation_completed`
- `privacy_warning_created`
- `request_failed`
- `request_expired`

### Deliverables

- audit log service
- audit log schema
- audit log endpoint
- privacy-preserving event records

### Planned Endpoint

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/audit-logs` | Return audit log events |

### Files to Create

- `backend/app/services/audit_log_service.py`
- `backend/app/services/audit_log_service.md`
- `backend/app/routers/audit_log_router.py`
- `backend/app/routers/audit_log_router.md`

### Exit Criteria

This stage is complete when:

- request creation writes an audit event
- wallet presentation writes an audit event
- validation writes an audit event
- privacy warnings are recorded
- audit logs can be viewed through the API

---

## Stage 9 — Analytics and Dashboard

### Goal

Create a simple dashboard that shows verification activity and privacy warnings.

### First Dashboard Views

- verification request overview
- audit log table
- privacy warning list
- summary metrics

### Useful Metrics

- total verification requests
- successful validations
- failed validations
- privacy warnings
- most requested claims
- requests by business process

### Deliverables

- Streamlit dashboard
- analytics endpoint
- dashboard README

### Planned Endpoint

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/analytics/summary` | Return basic process statistics |

### Files to Work On

- `dashboard/app.py`
- `dashboard/README.md`
- `backend/app/routers/analytics_router.py`
- `backend/app/routers/analytics_router.md`

### Exit Criteria

This stage is complete when:

- dashboard starts locally
- dashboard shows request status
- dashboard shows audit logs
- dashboard shows privacy warnings
- dashboard shows basic metrics

---

## Stage 10 — Testing and Documentation

### Goal

Make the project understandable and testable.

This stage prepares the project for portfolio, presentation, or IHK discussion.

### Deliverables

- test cases
- API documentation
- architecture documentation
- data model documentation
- demo script
- known limitations

### Files to Work On

- `backend/tests/`
- `docs/api_design.md`
- `docs/architecture.md`
- `docs/data_model.md`
- `docs/ihk_project_outline.md`

### Exit Criteria

This stage is complete when:

- main validation logic has tests
- README is up to date
- documentation explains the system clearly
- project can be demonstrated from start to finish
- limitations are documented honestly

---

## Stage 11 — Future Expansion

### Goal

Collect advanced topics for later versions without mixing them into the first prototype.

### Future Topics

- real OpenID4VP flow
- SD-JWT VC support
- trust registry lookup
- QTSP integration
- verifier registration workflow
- PostgreSQL migration
- Docker deployment
- authentication and authorization
- React dashboard
- enterprise API gateway design

### Deliverables

- future roadmap
- research notes
- issue backlog

### Files to Work On

- `docs/architecture.md`
- `docs/ihk_project_outline.md`
- GitHub Issues, later if used

### Exit Criteria

This stage is never fully complete.

It is a controlled backlog for future development.

---

## Stage Summary

| Stage | Name | Main Result |
|---|---|---|
| 0 | Project Boundary | Clear scope |
| 1 | Use Cases | Business scenarios |
| 2 | Templates | Structured verification templates |
| 3 | Mock Data | Wallet responses and trusted issuers |
| 4 | Backend Skeleton | Running FastAPI app |
| 5 | Schemas | Pydantic data structures |
| 6 | Template and Request API | Create/list templates and requests |
| 7 | Validation | Mock wallet response validation |
| 8 | Audit Logging | Privacy-preserving event history |
| 9 | Dashboard | Process visibility |
| 10 | Testing and Documentation | Portfolio-ready foundation |
| 11 | Future Expansion | Controlled backlog |

---

## Anti-Distraction Rule

Every new idea must go into one of these categories:

### Build Now

Needed for the current prototype.

Examples:

- templates
- mock wallet responses
- validation
- audit logs
- dashboard

### Learn Later

Important, but not needed yet.

Examples:

- OpenID4VP
- SD-JWT VC
- QTSP
- trust registries
- cryptographic proof validation

### Ignore for Now

Too large for version 1.

Examples:

- full wallet implementation
- legal certification
- production security approval
- real government PID integration