# Wallet Ecosystem Roles

Date: 2026-05-26
Status: Draft
Folder: 02_concept_notes
Tags: [CONCEPT] [ARCH] [PROJECT] [TRUST]

---

## Source

Source title: EUDI Wallet Architecture and Reference Framework
Source section: 4.1. Roles in the Ecosystem
Source type: Official architecture reference
Primary link: https://eudi.dev/arf/#41-roles-in-the-ecosystem
Related glossary: `../2026-05-26__glossary.md`
Related source note: `../01_source_notes/2026-05-22__arf_overview.md`
Related concept notes:

- `2026-05-26__pid_eaa_qeaa.md`
- `2026-05-26__selective_disclosure_privacy_warnings.md`

---

## Purpose of this note

This note explains the main roles in the EUDI Wallet ecosystem from an application-oriented perspective.

The goal is not to memorize the diagram. The goal is to understand:

- who participates in the ecosystem
- what each actor does
- how actors relate to each other
- which actors matter for the prototype
- which actors are background or out of scope for version 1

For this project, the most important viewpoint is the **Relying Party** side.

The prototype supports an organization that wants to create privacy-aware verification requests, process simulated wallet responses, validate claims, and record audit events.

---

## Short summary

The EUDI Wallet ecosystem can be understood as a chain:

```text
Authentic Sources
→ PID / EAA / QEAA Providers
→ EUDI Wallet Instance controlled by the User
→ Relying Party receives presented data
→ Trust and governance actors support the ecosystem
```

The project focuses mainly on:

```text
Relying Party
→ verification template
→ simulated wallet response
→ validation result
→ audit log
```

---

## Main role categories

| Category | Roles | Meaning |
|---|---|---|
| User side | End User, EUDI Wallet Instance, Device Manufacturer | The person/legal entity uses a wallet on a device. |
| Provider side | Wallet Provider, PID Provider, EAA Provider, QEAA Provider, Certificate Provider | Actors that provide wallet solutions, identity data, attributes, or certificates. |
| Relying-party side | Relying Party | Organization that requests and relies on wallet-presented information. |
| Trust infrastructure | Trusted List Provider, Authentic Source, Schema Provider | Actors that support trust, source quality, and structure of data. |
| Governance side | CAB, Supervisory Body, National Accreditation Body | Actors that support assessment, supervision, and accreditation. |

---

## Ecosystem roles table

| No. | Role | Simple explanation | Real-life example | Relationship in the ecosystem | Relevance to my project |
|---:|---|---|---|---|---|
| 1 | End User of EUDI Wallet | The natural or legal person using the wallet. | A citizen proving age, or a company representative proving authority to act. | Controls and activates the EUDI Wallet Instance. Receives services from a Relying Party. | High. The user controls what is presented, so the prototype should respect consent and selective disclosure. |
| 2 | EUDI Wallet Provider | Actor responsible for providing the wallet solution. | A Member State or approved provider offering a wallet app. | Provides wallet solution and support to the user. Registers with trust infrastructure. | Low for version 1. The project is not a wallet provider. |
| 3 | Person Identification Data Provider | Actor that provides PID to the wallet/user. | A national identity authority issuing identity data. | Issues PID to the EUDI Wallet Instance. May rely on authentic sources. Registers with Trusted List Provider. | High. PID appears in simulated wallet responses and must be minimized where possible. |
| 4 | Trusted List Provider | Actor maintaining trusted lists of ecosystem actors/status. | A national/EU trust list showing recognized providers. | Receives registrations from providers and potentially relying parties. Supports trust checking. | Medium/high. Version 1 can simulate trusted-list checks with simple trust flags. |
| 5 | QEAA Provider | Actor issuing Qualified Electronic Attestations of Attributes. | Provider issuing an official professional licence attestation. | Issues QEAA to the Wallet Instance. May use authentic source data. Registers with Trusted List Provider. | Medium. Important for future high-trust use cases; simulated in version 1. |
| 6 | EAA Provider | Actor issuing non-qualified Electronic Attestations of Attributes. | University issuing a degree attestation; membership body issuing status proof. | Issues EAA to the Wallet Instance. May use authentic source data. Registers with Trusted List Provider. | High. Many business checks need attributes instead of full identity. |
| 7 | Qualified/non-qualified certificate provider for electronic signature/seal | Actor providing certificates for signing or sealing. | Provider issuing an electronic signature certificate to a person or seal certificate to a company. | Provides certificates or related trust material to the Wallet Instance. Registers with Trusted List Provider. | Low for version 1 unless signing/sealing is added later. |
| 8 | Authentic Source | Authoritative source of data. | Population register, company register, professional register, education register. | Provides authoritative or qualified data to PID/EAA/QEAA providers. | High conceptually. Helps explain where reliable data originates. |
| 9 | Relying Party | Organization or service that requests and relies on wallet-presented data. | Employer, bank, public office, online platform, car rental company, age-restricted service. | Receives presented PID/(Q)EAA from the Wallet Instance. Offers services to the User. May register with trust infrastructure. | Highest. This is the main project perspective. |
| 10 | Conformity Assessment Body (CAB) | Actor assessing whether wallet solutions/providers meet required standards. | Independent body checking wallet conformity. | Governance/certification role rather than direct verification-flow actor. | Low for version 1. Useful for certification context only. |
| 11 | Supervisory Body | Authority supervising relevant actors and trust services. | National authority supervising trust service providers. | Governance role outside the direct wallet-presentation flow. | Low for version 1. Useful legal/governance context. |
| 12 | Device manufacturers and related subsystem providers | Actors providing devices, operating systems, secure subsystems, tools, or libraries. | Smartphone manufacturer, mobile OS provider, secure element provider, SDK provider. | Provides device to User and support/tools/libraries to wallet-related actors. | Low/medium. Important real-world dependency, but not implemented by the prototype. |
| 13 | (Q)EAA Schema Provider | Actor defining schemas for attribute attestations. | Schema provider defining structure of a university degree attestation. | Supports standardized structure of EAA/QEAA. | Medium. Future verification templates should align with known schemas. |
| 14 | National Accreditation Body | National body accrediting conformity assessment bodies. | National accreditation authority authorizing CABs. | Governance role supporting trust in CABs. | Low for version 1. Background for certification ecosystem. |

---

## Relationship map

This section translates the ecosystem diagram into practical relationships.

| Relationship | Plain meaning | Example | Prototype interpretation |
|---|---|---|---|
| User controls / activates Wallet Instance | The user decides to use the wallet and present data. | User opens wallet and approves an age proof. | Simulated response should include presentation/consent status. |
| PID Provider issues PID to Wallet Instance | Identity data is issued into the wallet context. | National authority issues identity data. | Simulate PID credential and issuer metadata. |
| EAA Provider issues EAA to Wallet Instance | Attribute proof is issued into the wallet context. | University issues degree attestation. | Simulate EAA response for qualification/status use cases. |
| QEAA Provider issues QEAA to Wallet Instance | Qualified attribute proof is issued. | Qualified provider issues professional licence proof. | Simulate high-trust attribute response for regulated scenarios. |
| Certificate provider provides certificate to Wallet Instance | Certificates support electronic signature/seal use cases. | User receives certificate for signing. | Out of scope unless signing is later added. |
| Wallet Instance presents PID/(Q)EAA to Relying Party | Wallet presents selected data to the organization. | User shares age-over-18 proof with online service. | Core prototype flow: request → response → validation. |
| Relying Party offers service to User | The organization provides the service requiring verification. | Bank opens account after verification. | Business process is the starting point for the verification template. |
| Wallet Provider provides wallet solution/support to User | User receives wallet app and support. | State-provided wallet app. | Out of scope, but useful for boundary explanation. |
| Device/subsystem providers support wallet use | Devices/OS/security libraries enable wallet operation. | Smartphone secure element supports wallet key storage. | Out of scope for business prototype. |
| Authentic Source provides data to providers | Providers rely on authoritative records. | Population register supports PID provider. | Used in metadata/source explanation. |
| Providers register with Trusted List Provider | Actors are registered as recognized/trusted. | QEAA provider appears on trusted list. | Simulate as `issuer_trusted = true/false`. |
| Relying Party registers with Trusted List Provider | Relying parties may need recognition/registration. | Service provider is recognized as legitimate verifier. | Future feature: validate requester registration/status. |

---

## Central flow for the prototype

The practical flow for this project is:

```text
1. Relying Party has a business need.
2. Relying Party creates a verification template.
3. Template defines purpose and required claims.
4. User controls wallet presentation.
5. Wallet Instance presents selected PID/EAA/QEAA claims.
6. Prototype validates simulated response against the template.
7. Prototype generates privacy warnings if request is excessive.
8. Prototype records audit events.
```

This means the prototype represents the organizational layer around wallet verification, not the wallet itself.

---

## Role priority for version 1

| Priority | Role | Reason |
|---:|---|---|
| 1 | Relying Party | Main perspective of the prototype. |
| 2 | End User | Controls wallet presentation and consent. |
| 3 | EUDI Wallet Instance | Source of simulated wallet response. |
| 4 | PID Provider | Provides identity data used in PID use cases. |
| 5 | EAA Provider | Provides attribute proofs for many business checks. |
| 6 | QEAA Provider | Needed for higher-trust or regulated examples. |
| 7 | Authentic Source | Explains source quality and reliability. |
| 8 | Trusted List Provider | Supports simulated trust checks and future real validation. |
| 9 | (Q)EAA Schema Provider | Relevant for future template/schema alignment. |

---

## Low-priority roles for version 1

| Role | Why lower priority |
|---|---|
| EUDI Wallet Provider | The project does not build or operate a wallet. |
| Certificate provider for electronic signature/seal | Signing/sealing is not part of the first prototype. |
| Device manufacturer and subsystem providers | Real device security is outside the business prototype. |
| Conformity Assessment Body | Certification assessment is not implemented. |
| Supervisory Body | Legal supervision context only. |
| National Accreditation Body | Accreditation chain is background context. |

---

## Applied example 1 — age verification

| Step | Actor | What happens | Prototype equivalent |
|---:|---|---|---|
| 1 | Relying Party | Online service needs to check age. | Create template: `age_verification`. |
| 2 | End User | User wants access to service. | Simulated user starts wallet flow. |
| 3 | Wallet Instance | Presents selected proof. | Response contains `age_over_18 = true`. |
| 4 | EAA/PID Provider | Underlying data was issued by provider. | Response contains simulated issuer metadata. |
| 5 | Trusted List Provider | Provider trust may be checked. | Simulated trust result: `issuer_trusted = true`. |
| 6 | Relying Party | Accepts/rejects proof. | Validation result: `accepted`. |
| 7 | Audit Log | Event is recorded. | Store result without raw unnecessary personal data. |

Privacy note:

```text
Age verification should prefer an age-over-threshold proof instead of full PID.
```

---

## Applied example 2 — employment onboarding

| Step | Actor | What happens | Prototype equivalent |
|---:|---|---|---|
| 1 | Relying Party | Employer needs identity and qualification proof. | Create onboarding verification template. |
| 2 | End User | Candidate presents wallet proofs. | Simulated wallet response includes PID subset and qualification EAA/QEAA. |
| 3 | PID Provider | Provides identity data. | Simulated PID issuer. |
| 4 | EAA/QEAA Provider | Provides degree, licence, or professional-status proof. | Simulated attribute attestation. |
| 5 | Authentic Source | Original data comes from register/university/professional body. | Metadata records source type. |
| 6 | Trusted List Provider | Trust status may be checked. | Simulated trusted issuer flag. |
| 7 | Relying Party | Employer validates requirements. | Result: accepted, rejected, or missing claims. |
| 8 | Audit Log | Verification event is recorded. | Store purpose, requested claims, result, warnings. |

Privacy note:

```text
Employment onboarding may justify more data than age verification, but still should not request a full wallet dump.
```

---

## Applied example 3 — residence verification

| Step | Actor | What happens | Prototype equivalent |
|---:|---|---|---|
| 1 | Relying Party | Service needs proof of residence. | Create residence verification template. |
| 2 | End User | User agrees to present residence proof. | Simulated consent/presentation status. |
| 3 | Authentic Source | Residence data originates from a register. | Metadata: `source_type = population_register`. |
| 4 | PID/EAA Provider | Issues residence-related data. | Credential type: PID or EAA depending on use case. |
| 5 | Wallet Instance | Presents selected residence attribute. | Response contains `country_of_residence` or `region`. |
| 6 | Relying Party | Checks if proof satisfies requirement. | Validation result generated. |
| 7 | Audit Log | Event is recorded. | Log purpose, result, and privacy warnings. |

Privacy note:

```text
If only country is needed, full address may be excessive.
```

---

## Prototype object mapping

| Prototype object | Ecosystem role connection | Purpose |
|---|---|---|
| Verification Template | Relying Party | Defines business purpose and requested claims. |
| Requested Claim | Attribute / PID / EAA / QEAA | Defines what data is needed. |
| Simulated Wallet Response | End User + Wallet Instance | Represents what the user presents. |
| Issuer Metadata | PID Provider / EAA Provider / QEAA Provider | Shows who issued the credential or attestation. |
| Source Metadata | Authentic Source | Shows where data originally comes from. |
| Trust Check Result | Trusted List Provider / Trust Model | Simulates whether issuer/provider is accepted. |
| Privacy Warning | Selective Disclosure / Data Minimization | Flags excessive or unclear requests. |
| Audit Log Event | Relying Party | Records request, validation, warnings, and result. |

---

## Version 1 boundaries

### In scope

- Explain ecosystem roles in project documentation.
- Model Relying Party, User, Wallet Instance, and Providers in simplified form.
- Simulate PID/EAA/QEAA providers as issuer metadata.
- Simulate trusted-list result using flags.
- Connect roles to verification templates, wallet responses, privacy warnings, and audit logs.

### Out of scope

- Real wallet provider implementation.
- Real PID/EAA/QEAA issuance.
- Real trusted-list integration.
- Real device/OS subsystem logic.
- Real conformity assessment.
- Real supervision or accreditation workflows.
- Legal certification.

---

## Open questions

- [ ] Should the prototype explicitly store `actor_type` for Relying Party, Provider, and User?
- [ ] Should issuer metadata distinguish PID Provider, EAA Provider, and QEAA Provider?
- [ ] Should trusted-list status be represented as simple boolean or detailed simulated object?
- [ ] Should the Relying Party registration concept appear in version 1?
- [ ] Which roles should appear in dashboard diagrams for the demo?

---

## Next action

- [ ] Create `03_project_relevance/2026-05-26__ecosystem_roles_relevance_matrix.md`.
- [ ] Reuse the role-priority table in project scope documentation.
- [ ] Use role mapping when designing verification-template fields.
- [ ] Connect role concepts to audit-log event design.
