# Project Plan — Weekly Roadmap

## Project Name

**EUDI Wallet Relying Party Integration Bus**

## Purpose of This Document

This document breaks the project into weekly work packages.

The goal is to make progress without getting lost in too many topics.

Each week contains:

- a weekly goal
- concrete tasks
- files to create or update
- learning focus
- completion checklist

---

## Weekly Working Rule

Each week should produce something visible.

A week is successful if it creates at least one of these:

- a document
- a schema
- an example JSON file
- a working API endpoint
- a test
- a dashboard view
- a diagram

---

## Week 1 — Project Foundation

### Goal

Create the project foundation and define the project clearly.

### Main Tasks

- create project folder structure
- create README
- define project scope
- create glossary
- write the project north star
- separate version 1 from future ideas

### Files to Create or Update

- `README.md`
- `docs/project_scope.md`
- `docs/glossary.md`
- `docs/plan_stages.md`
- `docs/plan_weeks.md`

### Learning Focus

- EUDI ecosystem basics
- relying party concept
- issuer, wallet, verifier
- project scope writing

### Completion Checklist

- [ ] README explains the project to a new person
- [ ] scope document explains what is included
- [ ] scope document explains what is excluded
- [ ] glossary has first key terms
- [ ] future topics are not mixed into version 1

### Result

A clear project foundation exists.

---

## Week 2 — Use Cases and Business Processes

### Goal

Define the first realistic business use cases.

### Main Tasks

- write age verification use case
- write residence verification use case
- write employment onboarding use case
- optionally write student status use case
- identify required and optional claims
- write data minimization notes for each use case

### Files to Create or Update

- `docs/use_cases.md`
- `docs/privacy_model.md`
- `examples/verification_templates.json`

### Learning Focus

- business process modeling
- data minimization
- required vs optional claims
- purpose limitation

### Completion Checklist

- [ ] at least three use cases are documented
- [ ] each use case has a business goal
- [ ] each use case has required claims
- [ ] each use case has optional claims
- [ ] each use case has a privacy note
- [ ] each use case can become a template

### Result

The project has realistic business scenarios.

---

## Week 3 — Verification Template Schema

### Goal

Design the first verification template structure.

### Main Tasks

- define required template fields
- create example templates
- check if each template follows data minimization
- document the meaning of each field
- keep JSON examples valid

### Files to Create or Update

- `examples/verification_templates.json`
- `docs/data_model.md`
- `docs/privacy_model.md`

### Learning Focus

- JSON
- JSON structure
- schema thinking
- process-to-data mapping

### Completion Checklist

- [ ] `verification_templates.json` exists
- [ ] age verification template exists
- [ ] residence verification template exists
- [ ] employment onboarding template exists
- [ ] each template has a purpose
- [ ] each template has required claims
- [ ] each template has retention policy
- [ ] JSON is valid

### Result

The project has the first structured verification templates.

---

## Week 4 — Mock Wallet Presentations and Trusted Issuers

### Goal

Create mock wallet responses and a simple trust list.

### Main Tasks

- create valid wallet presentation example
- create invalid wallet presentation example
- create over-sharing wallet presentation example
- create trusted issuer list
- document the mock trust model

### Files to Create or Update

- `examples/mock_wallet_presentations.json`
- `examples/trusted_issuers.json`
- `docs/privacy_model.md`
- `docs/data_model.md`

### Learning Focus

- mock data design
- issuer trust concept
- positive and negative test cases
- privacy warning scenarios

### Completion Checklist

- [ ] valid presentation example exists
- [ ] missing claim example exists
- [ ] untrusted issuer example exists
- [ ] over-sharing example exists
- [ ] trusted issuers JSON exists
- [ ] mock trust model is documented

### Result

The project can simulate wallet responses without real wallet integration.

---

## Week 5 — Backend Skeleton

### Goal

Create the first running FastAPI backend.

### Main Tasks

- add backend dependencies
- create FastAPI app
- create `/health` endpoint
- start the backend locally
- document how to run it

### Files to Create or Update

- `backend/requirements.txt`
- `backend/app/main.py`
- `backend/app/main.md`
- `docs/api_design.md`

### Learning Focus

- FastAPI basics
- Python project structure
- HTTP endpoints
- local development

### Completion Checklist

- [ ] requirements file exists
- [ ] FastAPI app starts
- [ ] `/health` endpoint works
- [ ] run instructions are documented
- [ ] first backend commit is made

### Result

A running backend exists.

---

## Week 6 — Pydantic Schemas

### Goal

Create Pydantic schemas for the main data objects.

### Main Tasks

- create verification template schema
- create verification request schema
- create wallet presentation schema
- create audit log schema
- document every schema file

### Files to Create

- `backend/app/schemas/verification_template_schema.py`
- `backend/app/schemas/verification_template_schema.md`
- `backend/app/schemas/verification_request_schema.py`
- `backend/app/schemas/verification_request_schema.md`
- `backend/app/schemas/wallet_presentation_schema.py`
- `backend/app/schemas/wallet_presentation_schema.md`
- `backend/app/schemas/audit_log_schema.py`
- `backend/app/schemas/audit_log_schema.md`

### Learning Focus

- Pydantic
- type hints
- validation
- required and optional fields

### Completion Checklist

- [ ] template schema exists
- [ ] request schema exists
- [ ] wallet presentation schema exists
- [ ] audit log schema exists
- [ ] schemas match example JSON files
- [ ] each schema has matching `.md` documentation

### Result

The backend has clear data structures.

---

## Week 7 — Template API

### Goal

Create API endpoints for verification templates.

### Main Tasks

- create template router
- create template service
- load templates from JSON or memory
- create endpoint to list templates
- create endpoint to get one template
- optionally create endpoint to add template

### Files to Create

- `backend/app/routers/template_router.py`
- `backend/app/routers/template_router.md`
- `backend/app/services/template_service.py`
- `backend/app/services/template_service.md`
- `backend/tests/test_templates.py`

### Planned Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/templates` | List templates |
| GET | `/templates/{template_id}` | Get one template |
| POST | `/templates` | Create template |

### Learning Focus

- API routers
- service layer
- separation of responsibilities
- basic tests

### Completion Checklist

- [ ] `/templates` returns template list
- [ ] `/templates/{template_id}` returns one template
- [ ] missing template returns error
- [ ] service logic is separated from router
- [ ] tests exist

### Result

The backend can work with verification templates.

---

## Week 8 — Verification Request API

### Goal

Create verification requests from templates.

### Main Tasks

- create request router
- create request service
- create request object from selected template
- assign request status
- store request in memory or file
- document request lifecycle

### Files to Create

- `backend/app/routers/request_router.py`
- `backend/app/routers/request_router.md`
- `backend/app/services/request_service.py`
- `backend/app/services/request_service.md`
- `backend/tests/test_requests.py`

### Planned Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| POST | `/verification-requests` | Create request |
| GET | `/verification-requests` | List requests |
| GET | `/verification-requests/{request_id}` | Get one request |

### Learning Focus

- request lifecycle
- status handling
- ID generation
- API input/output design

### Completion Checklist

- [ ] request can be created from template
- [ ] request has unique ID
- [ ] request has status
- [ ] requests can be listed
- [ ] one request can be retrieved
- [ ] tests exist

### Result

The backend can create and track verification requests.

---

## Week 9 — Mock Wallet Endpoint and Validation Logic

### Goal

Accept mock wallet presentations and validate them.

### Main Tasks

- create mock wallet router
- create validation service
- check required claims
- check credential type
- check issuer trust
- check user consent
- detect over-sharing
- return validation result

### Files to Create

- `backend/app/routers/mock_wallet_router.py`
- `backend/app/routers/mock_wallet_router.md`
- `backend/app/services/validation_service.py`
- `backend/app/services/validation_service.md`
- `backend/tests/test_validation.py`

### Planned Endpoint

| Method | Endpoint | Purpose |
|---|---|---|
| POST | `/mock-wallet/presentations` | Submit simulated wallet response |

### Learning Focus

- business rule validation
- clean function design
- error cases
- privacy warning logic

### Completion Checklist

- [ ] valid response passes
- [ ] missing required claim fails
- [ ] untrusted issuer fails
- [ ] missing consent fails
- [ ] extra unnecessary claims create privacy warning
- [ ] tests exist

### Result

The project has its first real business logic.

---

## Week 10 — Audit Logging

### Goal

Record events during the verification process.

### Main Tasks

- create audit log service
- create audit log router
- log request creation
- log presentation received
- log validation result
- log privacy warnings
- expose audit logs through API

### Files to Create

- `backend/app/services/audit_log_service.py`
- `backend/app/services/audit_log_service.md`
- `backend/app/routers/audit_log_router.py`
- `backend/app/routers/audit_log_router.md`
- `backend/tests/test_audit_logs.py`

### Planned Endpoint

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/audit-logs` | Return audit events |

### Learning Focus

- audit trails
- event design
- privacy-preserving logging
- traceability

### Completion Checklist

- [ ] request creation creates audit event
- [ ] wallet presentation creates audit event
- [ ] validation creates audit event
- [ ] privacy warning creates audit event
- [ ] audit logs can be listed
- [ ] tests exist

### Result

The project can explain what happened during a verification process.

---

## Week 11 — Analytics Summary and Dashboard

### Goal

Create a simple dashboard and summary endpoint.

### Main Tasks

- create analytics summary endpoint
- calculate total requests
- calculate successful and failed validations
- calculate privacy warning count
- show audit log table
- show request overview
- build first Streamlit dashboard

### Files to Create or Update

- `backend/app/routers/analytics_router.py`
- `backend/app/routers/analytics_router.md`
- `dashboard/app.py`
- `dashboard/README.md`
- `docs/api_design.md`

### Planned Endpoint

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/analytics/summary` | Return process statistics |

### Learning Focus

- simple analytics
- dashboard structure
- Streamlit basics
- process visibility

### Completion Checklist

- [ ] analytics endpoint works
- [ ] dashboard starts
- [ ] dashboard shows request overview
- [ ] dashboard shows audit log table
- [ ] dashboard shows privacy warnings
- [ ] dashboard shows summary metrics

### Result

The project becomes visually understandable.

---

## Week 12 — Documentation, Testing, and Demo Preparation

### Goal

Prepare the project for presentation, portfolio, or IHK discussion.

### Main Tasks

- update README
- update architecture documentation
- update API documentation
- update data model documentation
- write demo script
- document limitations
- clean project structure
- run tests

### Files to Create or Update

- `README.md`
- `docs/architecture.md`
- `docs/api_design.md`
- `docs/data_model.md`
- `docs/ihk_project_outline.md`
- `docs/project_scope.md`

### Learning Focus

- documentation quality
- presentation structure
- project explanation
- honest limitation handling

### Completion Checklist

- [ ] README matches current project state
- [ ] architecture is documented
- [ ] API endpoints are documented
- [ ] data model is documented
- [ ] tests run
- [ ] demo script exists
- [ ] limitations are documented
- [ ] next steps are documented

### Result

The project is ready to show.

---

## Optional Week 13 — Database Upgrade

### Goal

Move from memory or JSON storage to SQLite or PostgreSQL.

### Main Tasks

- decide SQLite or PostgreSQL
- create database models
- connect FastAPI to database
- store templates
- store requests
- store audit logs

### Files to Create or Update

- `backend/app/database.py`
- `backend/app/models/verification_template_model.py`
- `backend/app/models/verification_request_model.py`
- `backend/app/models/wallet_presentation_model.py`
- `backend/app/models/audit_log_model.py`
- `docs/data_model.md`

### Learning Focus

- SQL
- database design
- persistence
- SQLAlchemy basics

### Completion Checklist

- [ ] database connection works
- [ ] templates are stored
- [ ] requests are stored
- [ ] audit logs are stored
- [ ] tests still work

### Result

The project becomes more professional and persistent.

---

## Optional Week 14 — Docker and Developer Setup

### Goal

Make the project easier to run on another machine.

### Main Tasks

- create Dockerfile
- optionally create docker-compose file
- document setup process
- document environment variables

### Files to Create or Update

- `Dockerfile`
- `docker-compose.yml`
- `.env.example`
- `README.md`
- `docs/architecture.md`

### Learning Focus

- Docker basics
- environment configuration
- reproducible setup

### Completion Checklist

- [ ] backend can run with Docker
- [ ] setup is documented
- [ ] environment variables are documented
- [ ] project can be started by another developer

### Result

The project becomes easier to share.

---

## Weekly Review Template

Use this at the end of every week.

    ## Weekly Review — Week X

    ### What I completed

    - 

    ### What I learned

    - 

    ### Problems I had

    - 

    ### Decisions made

    - 

    ### What I will do next

    - 

    ### Files changed

    - 

    ### Open questions

    - 

---

## Focus Rules

### Rule 1 — One Main Goal Per Week

Do not work on five different parts at the same time.

### Rule 2 — Documentation Comes With Code

Every important code file should later have a matching `.md` explanation file.

Example:

    validation_service.py
    validation_service.md

### Rule 3 — Mock First, Real Integration Later

The first version uses mock wallet responses.

Real EUDI Wallet integration comes later.

### Rule 4 — Privacy Is a Feature

The project should not only verify data.

It should also detect when too much data was requested or received.

### Rule 5 — Keep the Project Explainable

At every stage, the project should be explainable to:

- a beginner
- a technical reviewer
- an IHK examiner
- a future employer