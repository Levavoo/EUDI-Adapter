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
- current status

---

## Project North Star

> This project helps organizations translate business identity-check requirements into privacy-preserving wallet verification requests, process simulated wallet responses, and analyze the resulting audit logs.

---

## Current Project Status

| Item | Status |
|---|---|
| Current phase | Stage 1 — Use Cases and Business Process Modeling |
| Stage 0 | Complete |
| Active branch | `codex` |
| Planning files location | `docs/plan/` |
| Protocol files location | `docs/protocol/` |

Stage 0 is complete. The project now moves fully into Stage 1.

---

## Stage 0 — Project Boundary and Foundation

**Status:** Complete

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

| Deliverable | Path | Status |
|---|---|---|
| Main project overview | `README.md` | Available |
| Project scope | `docs/project_scope.md` | Complete |
| Glossary | `docs/glossary.md` | Complete |
| Stage plan | `docs/plan/plan_stages.md` | Updated |
| Week plan | `docs/plan/plan_weeks.md` | Available / to keep updated |
| Terminal and Git workflow cheatsheet | `docs/cheatsheets/terminal_git_workflow_cheatsheet.md` | Complete |
| Mentored development workflow | `docs/process/mentored_development_workflow.md` | Complete |
| Daily protocol folder | `docs/protocol/` | Created |

### Files Worked On

- `README.md`
- `docs/project_scope.md`
- `docs/glossary.md`
- `docs/plan/plan_stages.md`
- `docs/plan/plan_weeks.md`
- `docs/process/mentored_development_workflow.md`
- `docs/cheatsheets/terminal_git_workflow_cheatsheet.md`
- `docs/protocol/2026-05-21_protocol.md`

### Exit Criteria

This stage is complete because:

- the README explains the project at a high level
- the project scope is written
- important terms are listed in the glossary
- version 1 boundaries are clear
- future topics are separated from current work
- GitHub and local Git workflow are working on the `codex` branch
- the protocol workflow is established
- the mentored development workflow is documented

### Do Not Work On Yet

- real wallet integration
- cryptography
- QTSP integration
- OpenID4VP
- full legal compliance
- frontend design details

### Stage 0 Closure Note

Stage 0 is now closed. New work should not expand the foundation indefinitely. If a missing foundation topic appears, document it briefly and continue Stage 1 unless it blocks the current work.

---

## Stage 1 — Use Cases and Business Process Modeling

**Status:** Active

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

| Deliverable | Path | Status |
|---|---|---|
| Use case documentation | `docs/use_cases.md` | To do |
| Business process model notes | `docs/business_processes.md` or section inside `docs/use_cases.md` | To decide |
| Verification template examples | `examples/verification_templates.json` | To do |
| Data minimization notes | Section inside `docs/use_cases.md` | To do |

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

### Immediate Next Work

Start with `docs/use_cases.md`.

Recommended first use case structure:

```text
Use case name
Business context
Actor / relying party
User / holder
Business need
Minimum required claims
Optional claims
Claims that should not be requested
Privacy note
Possible verification template mapping
Open questions
```

---

## Stage 2 — Verification Template Design

**Status:** Planned

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

**Status:** Planned

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

**Status:** In early preparation / planned technical stage

### Goal

Create the first FastAPI backend structure.

This stage creates the technical foundation without complex business logic.

### Planned Backend Structure

```text
backend/
├── app/
│   ├── main.py
│   ├── main.md
│   ├── database.py
│   ├── models/
│   ├── schemas/
│   ├── services/
│   └── routers/
├── tests/
└── pyproject-managed dependencies
```

### First Endpoint

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | Basic project/service overview |
| GET | `/health` | Check whether the backend is running |

### Deliverables

- FastAPI app starts successfully
- `/` endpoint works
- `/health` endpoint works
- root-level `pyproject.toml` and `uv.lock` manage dependencies
- basic backend folder structure is ready
- `backend/app/main.md` explains the entry point

### Files to Work On

- `pyproject.toml`
- `backend/app/main.py`
- `backend/app/main.md`
- `backend/app/database.py` later, when storage becomes necessary

### Exit Criteria

This stage is complete when:

- backend can be started locally
- `/` returns a service overview
- `/health` returns a success response
- dependencies are documented
- the project can be opened by another developer
- `main.py` contains no business logic

---

## Stage 5 — Schemas and Data Models

**Status:** Planned

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

**Status:** Planned

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

**Status:** Planned

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

**Status:** Planned

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

**Status:** Planned

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

**Status:** Planned

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

**Status:** Backlog

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

| Stage | Name | Status | Main Result |
|---|---|---|---|
| 0 | Project Boundary | Complete | Clear scope |
| 1 | Use Cases | Active | Business scenarios |
| 2 | Templates | Planned | Structured verification templates |
| 3 | Mock Data | Planned | Wallet responses and trusted issuers |
| 4 | Backend Skeleton | Planned / early preparation | Running FastAPI app |
| 5 | Schemas | Planned | Pydantic data structures |
| 6 | Template and Request API | Planned | Create/list templates and requests |
| 7 | Validation | Planned | Mock wallet response validation |
| 8 | Audit Logging | Planned | Privacy-preserving event history |
| 9 | Dashboard | Planned | Process visibility |
| 10 | Testing and Documentation | Planned | Portfolio-ready foundation |
| 11 | Future Expansion | Backlog | Controlled backlog |

---

## Anti-Distraction Rule

Every new idea must go into one of these categories:

### Build Now

Needed for the current prototype.

Examples:

- Stage 1 use cases
- business process descriptions
- data minimization notes
- verification template ideas

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
