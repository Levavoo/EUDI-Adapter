# EUDI Notebook — Architecture, Law & Ecosystem

> Purpose: This notebook is for understanding the EUDI Wallet ecosystem, legal framework, architecture, actors, trust model, and official sources.
>
> This is **not** the main build log. Implementation tasks, coding decisions, and prototype progress belong in the Project Notebook.

---

## Notebook Index

| Area | Use this section for | Status |
|---|---|---|
| 1. Source Library | Official documents, GitHub repos, legal texts, pilots, architecture references | [ACTIVE] |
| 2. Core Concepts | EUDI Wallet terms and definitions | [ACTIVE] |
| 3. Roles & Actors | Issuer, holder, verifier, relying party, QTSP, trust providers | [ACTIVE] |
| 4. Legal Notes | eIDAS 2.0, implementing acts, privacy obligations, data minimization | [ACTIVE] |
| 5. Architecture Notes | ARF, protocols, trust model, reference implementation, data flows | [ACTIVE] |
| 6. German / EU Ecosystem | SPRIND, German pilots, national implementation notes, EU-wide initiatives | [ACTIVE] |
| 7. Project Relevance | What each source means for my relying-party integration prototype | [ACTIVE] |
| 8. Open Questions | Unclear legal, architectural, technical, or project-scope questions | [ACTIVE] |

---

# 1. Source Library

Use this section to collect important EUDI-related sources before turning them into detailed notes.

## Source Entry Template

```md
### [SOURCE] Source Title

**Date added:** YYYY-MM-DD  
**Source type:** Official / Legal / GitHub / Article / Pilot / Video / Other  
**Link or reference:**  
**Reliability level:** High / Medium / Low  
**Read status:** Not started / Skimmed / Read / Summarized  
**Connected topics:** ARF, eIDAS 2.0, PID, QEAA, Relying Party, QTSP, etc.

**Why this source matters:**
- 

**Key things to extract later:**
- 
```

## Source Entries

### [SOURCE] Example Source Title

**Date added:** 2026-05-21  
**Source type:** Official  
**Link or reference:**  
**Reliability level:** High  
**Read status:** Not started  
**Connected topics:** ARF, Relying Party, Wallet Architecture

**Why this source matters:**
- This source may define how relying parties interact with EUDI Wallets.

**Key things to extract later:**
- Roles and responsibilities
- Required data flow
- Trust and verification requirements

---

# 2. Core Concept Notes

Use this section for important EUDI terms. Keep each note short and practical.

## Concept Note Template

```md
### [CONCEPT] Topic Name

**Date:** YYYY-MM-DD  
**Source:**  
**Status:** Draft / Checked / Stable  
**Related terms:**  

#### Meaning

Explain the concept in simple words.

#### Official / technical definition

Write a more precise definition from the source. Keep it short.

#### Relevance to my project

Explain how this affects the relying-party integration bus prototype.

#### Example in my project

Describe how this concept appears in the project.

#### Questions

- [QUESTION] 

#### Next action

- [LEARN] 
```

## Concept Notes

### [CONCEPT] Relying Party

**Date:** 2026-05-21  
**Source:** ARF / eIDAS notes  
**Status:** Draft  
**Related terms:** Verifier, Wallet, Presentation Request

#### Meaning

A relying party is an organization or system that requests identity data or attestations from a wallet user.

#### Official / technical definition

To be completed after reading the official source.

#### Relevance to my project

The prototype represents a backend integration layer for relying parties. It should help define what data is requested, why it is requested, and how verification events are documented.

#### Example in my project

A company wants to verify that a user is over 18 without storing unnecessary personal data.

#### Questions

- [QUESTION] What exact obligations does a relying party have under eIDAS 2.0?
- [QUESTION] How must relying parties identify themselves to the wallet?

#### Next action

- [LEARN] Find the ARF section that explains relying parties and verifiers.

---

# 3. Roles & Actors

Use this section to map the ecosystem around the wallet.

## Actor Map

| Actor | Simple meaning | Main responsibility | Relevance to my project |
|---|---|---|---|
| Holder / User | Person using the wallet | Controls and presents credentials | User approves or rejects data sharing |
| Issuer | Entity that issues credentials | Provides trusted data | Prototype may use mock issued credentials |
| Verifier | Entity checking a presentation | Verifies wallet response | Similar to relying party in prototype context |
| Relying Party | Organization relying on verified data | Defines business reason for verification | Main target user of the integration bus |
| QTSP | Qualified Trust Service Provider | Provides qualified trust services | Important for trust and legal assurance |
| Trust Registry | List or mechanism for trusted entities | Helps determine who is trusted | May affect future production architecture |

## Actor Note Template

```md
### [ACTOR] Actor Name

**Date:** YYYY-MM-DD  
**Source:**  
**Status:** Draft / Checked / Stable  

#### Role in the EUDI ecosystem


#### Responsibilities

- 

#### Data handled

- 

#### Trust / legal obligations

- 

#### Relevance to my project


#### Risk or uncertainty

- [QUESTION] 

#### Next action

- [LEARN] 
```

---

# 4. Legal Notes

Use this section for legal and regulatory understanding. Keep notes practical and connected to project decisions.

## Legal Note Template

```md
### [LEGAL] Legal Topic

**Date:** YYYY-MM-DD  
**Source:**  
**Legal area:** eIDAS 2.0 / GDPR / Implementing Act / National Law / Other  
**Status:** Draft / Checked / Stable  

#### What the source says

Summarize the legal point in simple words.

#### Meaning for EUDI Wallets

Explain what this changes or requires in the wallet ecosystem.

#### Meaning for relying parties

Explain what a relying party must consider.

#### Meaning for my project

Explain whether this creates a requirement, limitation, risk, or documentation need.

#### Practical project rule

- [DECISION] 

#### Questions

- [QUESTION] 

#### Next action

- [LEARN] 
```

## Legal Notes

### [LEGAL] Data Minimization

**Date:** 2026-05-21  
**Source:** GDPR / EUDI privacy notes  
**Legal area:** GDPR / eIDAS 2.0  
**Status:** Draft

#### What the source says

Only data that is necessary for a specific purpose should be requested or processed.

#### Meaning for EUDI Wallets

Wallet presentations should avoid unnecessary identity data sharing.

#### Meaning for relying parties

A relying party should define why each requested claim is necessary.

#### Meaning for my project

Verification templates should include purpose, required claims, optional claims, retention policy, and risk level.

#### Practical project rule

- [DECISION] Every verification template should include a short reason for each requested claim.

#### Questions

- [QUESTION] How detailed must the purpose explanation be for a real relying party?

#### Next action

- [BUILD] Add `purpose` and `claim_reason` fields to verification template examples.

---

# 5. Architecture Notes

Use this section for technical architecture of the EUDI ecosystem, not for your implementation details.

## Architecture Note Template

```md
### [ARCHITECTURE] Topic Name

**Date:** YYYY-MM-DD  
**Source:**  
**Architecture area:** ARF / Protocol / Trust Model / Reference Implementation / Data Flow / Other  
**Status:** Draft / Checked / Stable  

#### Problem this architecture solves


#### Main idea


#### Components involved

- 

#### Data flow

1. 
2. 
3. 

#### Trust assumptions

- 

#### Relevance to my project


#### What I will not build in version 1

- [OUT-OF-SCOPE] 

#### Questions

- [QUESTION] 

#### Next action

- [LEARN] 
```

## Architecture Notes

### [ARCHITECTURE] Wallet Presentation Flow

**Date:** 2026-05-21  
**Source:** ARF / reference implementation notes  
**Architecture area:** Data Flow  
**Status:** Draft

#### Problem this architecture solves

It allows a user to present selected identity claims to a verifier without manually uploading documents.

#### Main idea

The verifier requests specific claims, the wallet user approves the request, and the relying party receives a verifiable response.

#### Components involved

- User wallet
- Relying party / verifier backend
- Credential issuer
- Trust infrastructure
- Audit or transaction logs

#### Data flow

1. Relying party creates a verification request.
2. User receives or opens the request in the wallet.
3. Wallet prepares a presentation.
4. User approves or rejects sharing.
5. Relying party receives and validates the response.
6. System records the verification event.

#### Trust assumptions

- Credentials must come from trusted issuers.
- The relying party must be identifiable.
- The wallet response must be verifiable.

#### Relevance to my project

The prototype can model this flow with mock wallet responses and focus on request templates, validation logic, audit logs, and privacy warnings.

#### What I will not build in version 1

- [OUT-OF-SCOPE] Real wallet app
- [OUT-OF-SCOPE] Real credential issuing
- [OUT-OF-SCOPE] Full EU trust infrastructure integration

#### Questions

- [QUESTION] Which protocol should be studied first for verifier-to-wallet communication?

#### Next action

- [LEARN] Read the ARF section on presentation exchange.

---

# 6. German / EU Ecosystem Notes

Use this section for organizations, pilots, national implementation details, and real-world EUDI projects.

## Ecosystem Note Template

```md
### [ECOSYSTEM] Organization / Pilot / Initiative Name

**Date:** YYYY-MM-DD  
**Country / region:** Germany / EU / Other  
**Source:**  
**Status:** Draft / Checked / Stable  

#### What it is


#### What they are building or researching

- 

#### Why it matters


#### Relevance to my project


#### Useful links or repos

- 

#### Questions

- [QUESTION] 

#### Next action

- [LEARN] 
```

---

# 7. Project Relevance Notes

Use this section to convert EUDI knowledge into project meaning without turning this notebook into the build log.

## Project Relevance Template

```md
### [PROJECT-LINK] Topic Name

**Date:** YYYY-MM-DD  
**Related source / concept:**  
**Project area affected:** Scope / API / Data Model / Privacy / Audit Log / Dashboard / IHK Documentation  

#### What I learned


#### What this means for my prototype


#### Possible project decision

- [DECISION-CANDIDATE] 

#### Move to Project Notebook?

Yes / No / Later

#### Next action

- [BUILD] 
```

## Project Relevance Entries

### [PROJECT-LINK] Mock Wallet Responses for Version 1

**Date:** 2026-05-21  
**Related source / concept:** Wallet presentation flow  
**Project area affected:** Scope / API / Testing

#### What I learned

A full wallet integration requires protocols, trust infrastructure, and production-grade verification rules.

#### What this means for my prototype

Version 1 should focus on the relying-party integration layer, using mock wallet responses to prove the business and technical concept.

#### Possible project decision

- [DECISION-CANDIDATE] Version 1 uses mock wallet responses instead of real wallet integration.

#### Move to Project Notebook?

Yes

#### Next action

- [BUILD] Document this as a version 1 scope decision in the Project Notebook.

---

# 8. Open Questions

Use this section to prevent unclear points from blocking progress.

## Question Tracker

| ID | Question | Area | Status | Next step | Answer source |
|---|---|---|---|---|---|
| Q-001 | What are the exact obligations of a relying party? | Legal / Architecture | Open | Check ARF and eIDAS 2.0 |  |
| Q-002 | Which protocol should a verifier study first? | Architecture | Open | Search official architecture sources |  |
| Q-003 | How should trust registries affect relying-party onboarding? | Trust Model | Open | Research trust model |  |

## Question Entry Template

```md
### [QUESTION] Q-000 — Question title

**Date opened:** YYYY-MM-DD  
**Area:** Legal / Architecture / Ecosystem / Project Scope / Other  
**Status:** Open / In progress / Answered / Not relevant  
**Priority:** High / Medium / Low  

#### Question


#### Why this matters


#### Current understanding


#### Possible answer


#### Source needed


#### Final answer


#### Next action

- [LEARN] 
```

---

# 9. Weekly EUDI Review

Use this once per week to summarize what changed in your understanding.

## Weekly Review Template

```md
## Weekly Review — YYYY-MM-DD

### Sources reviewed

- [SOURCE] 

### Concepts learned

- [CONCEPT] 

### Legal points clarified

- [LEGAL] 

### Architecture points clarified

- [ARCHITECTURE] 

### Project implications

- [PROJECT-LINK] 

### Decisions to move into Project Notebook

- [DECISION-CANDIDATE] 

### Open questions for next week

- [QUESTION] 

### Next 3 research tasks

1. [LEARN] 
2. [LEARN] 
3. [LEARN] 
```

---

# Formatting Rules

## 1. Use clear tags

Use tags at the start of important lines so notes are easy to scan.

| Tag | Meaning | Use for |
|---|---|---|
| [SOURCE] | Source or reference | Official documents, GitHub repos, legal texts, pilots |
| [CONCEPT] | EUDI term | PID, QEAA, EAA, QTSP, relying party, issuer |
| [ACTOR] | Ecosystem role | Holder, issuer, verifier, relying party, trust provider |
| [LEGAL] | Legal note | eIDAS 2.0, GDPR, implementing acts |
| [ARCHITECTURE] | Technical architecture | ARF, protocols, trust model, data flow |
| [ECOSYSTEM] | Organization or initiative | SPRIND, pilots, Animo, EU projects |
| [PROJECT-LINK] | Project relevance | How EUDI knowledge affects the prototype |
| [QUESTION] | Unclear point | Anything that needs research |
| [DECISION-CANDIDATE] | Possible project decision | Items that may move to the Project Notebook |
| [OUT-OF-SCOPE] | Not part of version 1 | Wallet app, issuer system, full production trust infrastructure |
| [LEARN] | Research task | Something to read or understand |
| [BUILD] | Implementation task | Something to move into the Project Notebook |
| [IHK] | Exam/project documentation relevance | Points useful for final explanation or presentation |

## 2. Use status labels

Use one of these status values in every serious note:

- **Draft** — written from first understanding, not fully checked yet.
- **Checked** — verified against a reliable source.
- **Stable** — clear enough to reuse in documentation.
- **Open** — still unclear.
- **Not relevant** — researched but not useful for this project.

## 3. Keep source notes separate from project decisions

This notebook explains EUDI architecture, law, and ecosystem.

Project decisions should only be marked as:

```md
[DECISION-CANDIDATE]
```

Then move the actual final decision into the **Project Notebook — Build Log & Documentation**.

## 4. Use this note structure for serious notes

Every serious note should answer:

```md
Topic:
Date:
Source:
Meaning:
Relevance to my project:
Questions:
Next action:
```

This keeps the notebook useful instead of becoming a collection of copied links.

## 5. Use tables for overview, headings for detail

Use tables when comparing actors, sources, questions, or responsibilities.
Use headings when explaining one concept deeply.

Good use of a table:

```md
| Actor | Responsibility | Relevance |
|---|---|---|
| Issuer | Issues credentials | Provides trusted data |
```

Good use of headings:

```md
### [CONCEPT] PID

#### Meaning

#### Relevance to my project
```

## 6. Do not overfill this notebook

Do not paste long legal texts into this notebook.
Instead, summarize them using:

```md
Source → Meaning → Relevance to my project → Next action
```

## 7. Weekly cleanup rule

At the end of each week:

1. Mark weak notes as **Draft**.
2. Mark verified notes as **Checked**.
3. Move project decisions into the Project Notebook.
4. Keep unresolved issues in the Question Tracker.
5. Choose three research tasks for next week.

## 8. Main rule

This notebook supports the project, but it does not control the project.

The **Project Notebook — Build Log & Documentation** decides what gets built next.
