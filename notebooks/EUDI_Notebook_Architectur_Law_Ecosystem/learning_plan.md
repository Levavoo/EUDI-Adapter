# Learning Plan — Theory & Skills

**Created:** 2026-05-21  
**Notebook:** `Learning_Notebook_Theory_Skills`  
**Purpose:** Track learning progress for reusable technical knowledge needed for the EUDI Wallet relying party prototype and future professional development.

---

## 1. Notebook Purpose

This notebook is for technical learning that remains useful beyond one project.

Use it for:

- backend concepts
- API concepts
- validation concepts
- database concepts
- security and privacy basics
- process modeling
- audit logging
- EUDI-specific technical standards later
- professional/future engineering topics

Do not use it for:

- daily build logs
- final project decisions
- messy ideas
- source-only EUDI law notes

Those belong in the Project Notebook, Scratch Notebook, or EUDI Notebook.

---

## 2. Explanation Style Rule

Every topic should include two explanation styles.

### 2.1 Simple Explanation

Use this for first understanding.

Rules:

- minimal technical language
- short sentences
- explain like teaching a beginner
- use concrete examples
- avoid unnecessary terms

Purpose:

> Help me understand the idea without getting stuck in theory.

### 2.2 Industry Explanation

Use this for correct professional wording.

Rules:

- use accurate technical terms
- describe the concept the way a developer, analyst, architect, or compliance person would describe it
- include relevant constraints, risks, and tradeoffs
- connect to real backend or business system usage

Purpose:

> Help me learn how the concept is described in real professional work.

---

## 3. Strict Naming Format

All learning files and folders must respect the creation date.

### 3.1 Topic Folder Naming

Use this format:

```text
YYYY-MM-DD_level-[number]_[topic-slug]
```

Examples:

```text
2026-05-21_level-1_http-apis
2026-05-22_level-1_json-schemas
2026-05-23_level-1_fastapi
```

Rules:

- use lowercase letters
- use hyphens inside the topic slug
- do not use spaces
- include the level number
- keep folder names short

### 3.2 Note File Naming

Use this format:

```text
YYYY-MM-DD_[step-number]_[topic-slug].md
```

Examples:

```text
2026-05-21_01_what-is-an-api.md
2026-05-21_02_http-request-response.md
2026-05-21_03_api-methods.md
```

Rules:

- use the creation date
- use two-digit step numbers
- use lowercase letters
- use hyphens instead of spaces
- one file should cover one small concept

### 3.3 Recommended Folder Structure

```text
notebooks/
  Learning_Notebook_Theory_Skills/
    learning_plan.md
    2026-05-21_level-1_http-apis/
      2026-05-21_01_what-is-an-api.md
      2026-05-21_02_http-request-response.md
      2026-05-21_03_http-methods.md
```

Current repository file location:

```text
notebooks/learning_plan.md
```

If the notebook folder already exists, future topic notes should be saved inside:

```text
notebooks/Learning_Notebook_Theory_Skills/
```

---

## 4. Learning Levels

## Level 1 — Required Now

Goal:

Build the minimum knowledge needed to understand and design the first working prototype.

Topics:

| Order | Topic | Why It Matters Now | Status |
|---:|---|---|---|
| 1 | HTTP APIs | Needed to understand how systems send and receive requests | Not started |
| 2 | JSON schemas | Needed to define structured request and response data | Not started |
| 3 | Python FastAPI | Needed to understand the backend framework | Not started |
| 4 | Pydantic validation | Needed to validate input and output data | Not started |
| 5 | SQL basics | Needed to read and write structured database data | Not started |
| 6 | Basic database design | Needed to model templates, requests, responses, and logs | Not started |
| 7 | Process modeling | Needed to describe business flows before implementation | Not started |
| 8 | Audit logging | Needed to record what happened in each verification flow | Not started |
| 9 | Data minimization | Needed to keep verification requests privacy-preserving | Not started |

Completion target:

> I can explain each topic simply, describe it in industry language, and connect it to the prototype.

---

## Level 2 — Required After Prototype Works

Goal:

Make the prototype cleaner, easier to test, easier to run, and easier to present.

Topics:

| Order | Topic | Why It Matters Later | Status |
|---:|---|---|---|
| 1 | Docker | Needed to run the app consistently across environments | Not started |
| 2 | PostgreSQL | Needed for more realistic database work | Not started |
| 3 | Authentication basics | Needed to protect access to the prototype or dashboard | Not started |
| 4 | Logging | Needed to understand system behavior and errors | Not started |
| 5 | pytest | Needed to test backend behavior | Not started |
| 6 | API documentation | Needed to explain how the backend can be used | Not started |
| 7 | React or Streamlit dashboard | Needed to present results and audit logs visually | Not started |

Completion target:

> I can make the prototype easier to run, test, explain, and demonstrate.

---

## Level 3 — EUDI-Specific Later

Goal:

Understand the standards and ecosystem behind real EUDI Wallet integrations.

Topics:

| Order | Topic | Why It Matters Later | Status |
|---:|---|---|---|
| 1 | ARF | Architecture and Reference Framework for the EUDI Wallet ecosystem | Not started |
| 2 | OpenID4VP | Standard for wallet presentation flows | Not started |
| 3 | OpenID4VCI | Standard for credential issuance flows | Not started |
| 4 | SD-JWT VC | Format for selective disclosure verifiable credentials | Not started |
| 5 | Trust registries | Needed to understand trusted issuers and verifiers | Not started |
| 6 | Qualified attestations | Needed to understand higher-trust credential types | Not started |
| 7 | Verifier registration | Needed to understand how relying parties may be recognized | Not started |
| 8 | QTSP services | Needed to understand qualified trust service providers | Not started |

Completion target:

> I can explain how the prototype maps to real EUDI Wallet architecture without claiming it is a production wallet integration.

---

## Level 4 — Professional / Future

Goal:

Build knowledge for production-grade systems, professional roles, and future specialization.

Topics:

| Order | Topic | Why It Matters Professionally | Status |
|---:|---|---|---|
| 1 | Cryptographic proof validation | Needed for real credential verification systems | Not started |
| 2 | Production security | Needed for safe deployment and access control | Not started |
| 3 | Certification processes | Needed for regulated identity and trust systems | Not started |
| 4 | Sector-specific compliance | Needed for healthcare, finance, public sector, and enterprise use cases | Not started |
| 5 | Enterprise integrations | Needed to connect wallet verification to existing business systems | Not started |
| 6 | Cloud deployment | Needed to deploy systems professionally | Not started |
| 7 | Monitoring | Needed to observe system health and incidents | Not started |

Completion target:

> I can discuss how a prototype could evolve toward a professional, secure, and compliant product.

---

## 5. Recommended Additions

The current plan is strong. Recommended additions are listed below.

### 5.1 Add Privacy by Design

Suggested level:

- Level 1 or Level 3

Reason:

The project is about privacy-preserving verification requests. Data minimization is one part of this, but privacy by design is the broader principle.

### 5.2 Add Requirements Modeling

Suggested level:

- Level 1

Reason:

The prototype translates business identity-check requirements into wallet verification requests. Requirements modeling helps connect business needs to technical templates.

### 5.3 Add Threat Modeling Basics

Suggested level:

- Level 2 or Level 4

Reason:

Even a prototype benefits from understanding what could go wrong, especially around identity, logs, personal data, and access control.

### 5.4 Add Data Retention

Suggested level:

- Level 1 or Level 2

Reason:

Audit logs are useful, but logs must not store more personal data than necessary. Retention rules are important for privacy and compliance.

### 5.5 Add Sequence Diagrams

Suggested level:

- Level 1

Reason:

Sequence diagrams help explain the interaction between business user, backend, simulated wallet, and audit log.

---

## 6. First Topic Plan — HTTP APIs

Recommended folder:

```text
notebooks/Learning_Notebook_Theory_Skills/2026-05-21_level-1_http-apis/
```

Recommended smaller steps:

| Step | File Name | Focus |
|---:|---|---|
| 1 | `2026-05-21_01_what-is-an-api.md` | Simple and industry explanation of APIs |
| 2 | `2026-05-21_02_http-request-response.md` | How clients and servers communicate |
| 3 | `2026-05-21_03_http-methods.md` | GET, POST, PUT, PATCH, DELETE |
| 4 | `2026-05-21_04_status-codes.md` | 200, 201, 400, 401, 403, 404, 422, 500 |
| 5 | `2026-05-21_05_headers-and-body.md` | Headers, body, content type, authorization |
| 6 | `2026-05-21_06_api-endpoints.md` | Endpoint design and naming |
| 7 | `2026-05-21_07_api-example-for-eudi-project.md` | Example API flow for verification templates |

Recommended first note:

```text
2026-05-21_01_what-is-an-api.md
```

---

## 7. Standard Topic Note Structure

Each topic note should use this structure.

```markdown
# Topic: [Topic Name]

**Created:** YYYY-MM-DD  
**Level:** Level [number]  
**Step:** [step number]  
**Status:** Draft / Reviewed / Needs Practice  
**Tags:** `[LEARN]` `[BACKEND]`

---

## 1. Simple Explanation

Explain the topic with minimal technical language.

---

## 2. Industry Explanation

Explain the topic with correct professional terminology.

---

## 3. Why This Matters

Explain why the topic matters for software systems and the EUDI prototype.

---

## 4. Key Terms

| Term | Simple Meaning | Industry Meaning |
|---|---|---|
|  |  |  |

---

## 5. Practical Example

Add one small example.

---

## 6. Connection to My Project

Explain how this topic connects to the EUDI relying party integration bus.

---

## 7. Common Mistakes

List typical misunderstandings.

---

## 8. Cornell Questions

- Question 1
- Question 2
- Question 3

---

## 9. Summary in My Own Words

Write 3–5 sentences.

---

## 10. Next Action

Choose one concrete next step.
```

---

## 8. Progress Tracking

Use this table to track progress.

| Date | Level | Topic | Step | File | Status | Notes |
|---|---:|---|---:|---|---|---|
| 2026-05-21 | 1 | HTTP APIs | 1 | `2026-05-21_01_what-is-an-api.md` | Planned | First topic |

Status values:

```text
Planned
Draft
Reviewed
Needs Practice
Done
```

---

## 9. Main Remark

The plan should stay flexible.

The order is good, but topics can overlap. For example:

- HTTP APIs and JSON schemas connect directly.
- FastAPI and Pydantic should be learned close together.
- SQL and database design should be learned together.
- Audit logging and data minimization should be learned together.
- Process modeling should happen before or during backend design, not after.

Recommended Level 1 learning path:

```text
HTTP APIs
→ JSON schemas
→ Pydantic validation
→ Python FastAPI
→ SQL basics
→ Basic database design
→ Process modeling
→ Audit logging
→ Data minimization
```

Reason:

This order moves from communication, to data structure, to validation, to backend implementation, to storage, to business process and privacy logic.
