# Scratch Notes — 2026-05-26

> Purpose: Fast notes, messy thinking, questions, remarks, and possible future tasks.
> Rule: Do not polish here. Move useful notes later.

---

## Inbox

- [IDEA] The EUDI ecosystem diagram is highly relevant because it shows where the project sits: mainly around the Relying Party (9).
- [REMARK] The project should not be described as a wallet, issuer, or trusted list provider. It is a relying-party-side integration layer.
- [MOVE] This note should later be moved into the Project Notebook, probably under Project Scope, Architecture, or IHK project explanation.

---

## [REMARK] What the EUDI ecosystem diagram shows in simple terms

The diagram is an ecosystem view. It does not only describe one transaction. It shows the actors around the EUDI Wallet, how credentials are issued, how they are presented, and how trust/governance roles support the system.

Important center of the diagram:

```text
User (1) -> controls / activates -> EUDI Wallet Instance
```

Meaning:

- The user controls the wallet.
- The wallet should not act secretly in the background.
- The user activates the wallet and confirms important actions.
- The wallet can contain or manage digital credentials such as PID, QEAA, EAA, or qualified certificates.

Important credential terms:

```text
PID  = Person Identification Data
QEAA = Qualified Electronic Attestation of Attributes
EAA  = Electronic Attestation of Attributes
QC   = Qualified Certificate
```

Current understanding:

The EUDI Wallet is a trusted digital wallet application. It allows a user to store and present verified digital identity data or attestations. The user remains in control of what is shared.

---

## [REMARK] Phase A — Wallet is provided to the user

Relevant part of the diagram:

```text
EUDI Wallet Provider (2) -> offers services / provides wallet solution / provides support -> User (1)
```

Meaning:

- The EUDI Wallet Provider gives the wallet solution to the user.
- The provider supports the wallet service.
- The user receives, activates, and controls the wallet.

Simplified process:

```text
Wallet Provider gives user the wallet app.
User installs / activates wallet.
User controls wallet.
```

Project relevance:

This project is not mainly about this part. The prototype does not build the wallet app and does not act as the Wallet Provider.

---

## [REMARK] Phase B — Trusted data is issued into the wallet

Relevant part of the diagram:

```text
PID Provider (3)  -> issues PID  -> EUDI Wallet Instance
QEAA Provider (5) -> issues QEAA -> EUDI Wallet Instance
EAA Provider (6)  -> issues EAA  -> EUDI Wallet Instance
QES Provider (7)  -> provides QC -> EUDI Wallet Instance
```

Meaning:

Different trusted providers issue different types of credentials or certificates into the wallet.

Examples:

```text
PID Provider:
- name
- date of birth
- nationality
- personal identifier
- address, depending on implementation

QEAA Provider:
- driving licence
- residence certificate
- professional qualification
- official diploma

EAA Provider:
- employee badge
- gym membership
- ticket
- non-qualified certificate

QES Provider:
- qualified certificate
- signature-related capability
```

Simplified process:

```text
Issuer creates trusted digital credential.
Credential is stored in or made available through the user's wallet.
Later, the user can present it to a relying party.
```

Project relevance:

This project is not mainly an issuer-side system. It does not issue PID, QEAA, EAA, or qualified certificates. In the prototype, these credentials can be simulated as wallet response data.

---

## [REMARK] Phase C — Trust is registered and governed

Relevant part of the diagram:

```text
Trusted List Provider (4)
National Accreditation Body (14)
Conformity Assessment Body (10)
Supervisory Body (11)
(Q)EAA Schema Provider (13)
```

Meaning:

The ecosystem needs trust infrastructure and governance. Actors need to know who is trusted, who is registered, and who is allowed to issue or verify something.

The Trusted List Provider helps answer questions like:

```text
Who is trusted?
Who is registered?
Who is allowed to issue credentials?
Who is allowed to verify presentations?
Which wallet providers are valid?
Which relying parties are registered?
```

Governance roles define, supervise, accredit, or assess the ecosystem. They do not necessarily participate in every user transaction directly.

Simplified process:

```text
Governance bodies define and check the rules.
Trusted lists record trusted ecosystem actors.
Wallets and relying parties use trust information.
```

Project relevance:

The project may simulate trust checks, for example:

```text
issuer_trusted = true
relying_party_registered = true
credential_valid = true
```

But it does not build the official trusted list infrastructure or governance system.

---

## [IDEA] Phase D — User presents data to a relying party

Relevant part of the diagram:

```text
EUDI Wallet Instance -> presents PID / (Q)EAA -> Relying Party (9)
```

This is the most important part for the project.

The Relying Party is the company, authority, website, bank, university, hospital, employer, hotel, or platform that needs to verify something about the user.

Examples:

```text
Bank requests PID before opening an account.
Hotel requests PID for guest registration.
University requests education certificate.
Employer requests qualification proof.
Online shop requests proof that the user is over 18.
```

Simplified process:

```text
Relying Party has a business need.
Relying Party creates a request.
Wallet shows request to user.
User approves or rejects.
Wallet presents selected PID / QEAA / EAA.
Relying Party verifies the response.
Service continues, is denied, or goes to manual review.
```

Project relevance:

This is where the project is directly relevant. The prototype sits on the Relying Party side and helps structure, validate, and document this process.

---

## [IDEA] Actual simplified transaction flow

### Step 1 — Relying party has a business need

Example:

```text
A company wants to verify that a user is over 18.
```

Business wording:

```text
We need to check age eligibility.
```

This is not yet a wallet request.

Project relevance:

The project can capture the business requirement before it becomes a technical verification request.

---

### Step 2 — System creates a verification template

The project can translate business need into a structured verification template.

Example:

```json
{
  "purpose": "Age-restricted service access",
  "required_claims": ["age_over_18"],
  "credential_type": "PID",
  "data_minimisation": true,
  "retention_policy": "do_not_store_raw_birth_date",
  "risk_level": "low"
}
```

Meaning:

The relying party may not know how to ask the wallet correctly. The project helps it ask in a privacy-preserving and structured way.

Bad request:

```text
Give me full identity and full date of birth.
```

Better request:

```text
Prove that the user is over 18.
```

Project relevance:

This can become a central prototype feature: business requirement -> verification template -> privacy-minimal wallet request.

---

### Step 3 — Relying party sends request to wallet/user

The diagram shows the presentation result:

```text
EUDI Wallet Instance -> presents PID / (Q)EAA -> Relying Party
```

But before this presentation, there is normally a request.

Full simplified sequence:

```text
Relying Party creates request.
User opens wallet flow.
Wallet shows request.
User approves or rejects.
Wallet presents selected PID / QEAA / EAA.
Relying Party verifies response.
```

Project relevance:

The prototype can generate or simulate the request that would normally go to the wallet.

---

### Step 4 — Wallet shows the request to the user

Example wallet-facing request:

```text
Example Company requests:
- Proof that you are over 18

Purpose:
- Access age-restricted service

Data shared:
- age_over_18 = true

Not shared:
- full date of birth
- address
- nationality
```

Important idea:

The user should understand who is asking, what is requested, and why.

Project relevance:

The project does not build the wallet UI, but it can prepare the request content so that it is understandable, minimal, and traceable.

---

### Step 5 — Wallet presents proof/data to relying party

Example simulated wallet response:

```json
{
  "presentation_id": "vp_001",
  "credential_type": "PID",
  "claims": {
    "age_over_18": true
  },
  "issuer_trusted": true,
  "credential_valid": true,
  "user_consent": true
}
```

The response may contain actual data or minimal proof.

Examples:

```text
Actual data:
- name
- date of birth
- address

Minimal proof:
- age_over_18 = true
- has_valid_driving_licence = true
- diploma_is_valid = true
```

Project relevance:

The prototype can process simulated wallet responses. It does not need real cryptography in version 1.

Possible simulated cases:

```text
valid response
invalid response
missing claim
expired credential
untrusted issuer
over-requested data
privacy warning
user rejected request
```

---

### Step 6 — Relying party validates and decides

The relying party checks:

```text
Did the response contain the required claim?
Is the credential type acceptable?
Is the issuer trusted?
Is the credential valid?
Was the request privacy-minimal?
Should the service continue?
```

Possible outcomes:

```text
valid -> service continues
invalid -> service denied
unclear -> manual review
```

Project relevance:

This can become the core backend logic of the prototype:

```text
verification request created
wallet response received
response validated
privacy check performed
audit log created
business result returned
```

---

## [IDEA] Where exactly the project sits in the scheme

The project is not the whole EUDI ecosystem.

It does not build:

```text
PID Provider
QEAA Provider
EAA Provider
QES Provider
Wallet Provider
Device Manufacturer
Trusted List Provider
National Accreditation Body
Conformity Assessment Body
Supervisory Body
Schema Provider
```

The project sits mainly here:

```text
Relying Party (9)
```

More precisely, it is an internal integration layer for the relying party.

Visual positioning:

```text
Company / Organization
        |
        v
Relying Party Integration Bus
        |
        v
EUDI Wallet request / simulated wallet request
        |
        v
Wallet response / simulated wallet response
        |
        v
Validation + audit log + decision support
```

Alternative view:

```text
[Business Department]
       |
       | "We need to verify age / residence / diploma"
       v
[Project: Relying Party Integration Bus]
       |
       | creates minimal verification request
       v
[EUDI Wallet Instance]
       |
       | presents PID / QEAA / EAA
       v
[Project: validates response]
       |
       v
[Company Service Decision]
```

Core project positioning:

```text
The prototype sits on the Relying Party side and acts as a bridge between business requirements and EUDI Wallet verification requests.
```

---

## [IDEA] What the project does in business terms

The project helps a relying party answer:

```text
What do we need to verify?
Why do we need it?
Which credential type is acceptable?
Which exact claims are necessary?
Are we requesting too much data?
How do we process the wallet response?
What should be logged?
What should not be stored?
What decision follows?
```

Why this matters:

Organizations may not start with technical wallet knowledge. They start with business needs. The prototype translates business needs into wallet-compatible verification logic.

Example:

```text
Business says:
"We need to confirm the user can rent a car."

System translates:
Required:
- valid driving licence
- age_over_21, if needed
- licence category B

Do not request:
- full national ID number
- unnecessary address
- full driving history
```

---

## [IDEA] Project modules mapped to the scheme

### Module 1 — Business requirement intake

Relevant to:

```text
Relying Party (9)
```

Purpose:

```text
Capture why the organization wants data.
```

Example:

```text
Use case: Hotel check-in
Purpose: Legal guest registration
Required: identity + address
```

---

### Module 2 — Verification template builder

Relevant to:

```text
Relying Party (9) -> request to Wallet
```

Purpose:

```text
Convert business need into wallet-compatible request structure.
```

Example:

```text
Template: age_verification
Required claim: age_over_18
Credential type: PID
Retention: no raw birth date storage
```

---

### Module 3 — Privacy / data minimisation checker

Relevant to:

```text
Before Relying Party requests data
```

Purpose:

```text
Warn when the relying party requests too much.
```

Example:

```text
Problem:
Company asks for full date_of_birth.

Warning:
For age-restricted access, age_over_18 proof may be enough.
```

---

### Module 4 — Simulated wallet response processor

Relevant to:

```text
EUDI Wallet Instance -> presents PID / (Q)EAA -> Relying Party (9)
```

Purpose:

```text
Accept mock wallet presentations and evaluate them.
```

Example:

```text
Response:
age_over_18 = true
issuer_trusted = true
credential_valid = true

Decision:
approved
```

---

### Module 5 — Audit log

Relevant to:

```text
Relying Party internal governance
```

Purpose:

```text
Record what happened without storing unnecessary personal data.
```

Example events:

```text
request_created
privacy_check_completed
wallet_response_received
validation_completed
decision_returned
```

Important note:

The audit log is not shown as a separate box in the ecosystem diagram, but it belongs inside the relying party's internal system.

---

## [MOVE] Best sentence for README / IHK documentation

Long version:

```text
This project represents a relying-party-side integration layer for the EUDI Wallet ecosystem. It helps organizations translate business verification needs into privacy-preserving wallet requests, process simulated wallet responses, validate whether the required claims were fulfilled, and create audit logs for accountability.
```

Short version:

```text
The prototype sits on the Relying Party side and acts as a bridge between business requirements and EUDI Wallet verification requests.
```

Possible destination:

```text
Project Notebook -> Project Scope / README / IHK project outline
```

---

## Move Later

### Move to Project Notebook

- Project position in EUDI ecosystem
- Relying Party Integration Bus explanation
- Business requirement -> verification template -> wallet request -> wallet response -> validation -> audit log flow
- Project module mapping
- README/IHK positioning sentence

### Move to EUDI Notebook

- Ecosystem actor overview
- PID Provider, QEAA Provider, EAA Provider, QES Provider
- Trusted List Provider and governance roles

### Move to Theory Notebook

- Difference between business requirement, verification template, credential claim, and validation result

### Delete / Ignore

- None for now
