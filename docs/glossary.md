# Glossary

## Purpose

This glossary defines the main terms used in the EUDI Wallet Relying Party Integration Bus project.

The goal is to keep business, technical, and privacy-related language consistent across documentation, examples, backend schemas, and later presentation material.

## Core Project Terms

| Term | Meaning in This Project |
|---|---|
| EUDI Wallet | A European Digital Identity Wallet concept that allows users to store and present digital identity credentials. In this prototype, it is simulated, not implemented directly. |
| Relying Party | The organization or service that requests identity information from a user. This project focuses on the relying-party side. |
| Integration Bus | A coordinating backend layer that translates business verification needs into structured verification requests, processes responses, and records audit logs. |
| Prototype | A simplified system used to demonstrate logic, workflows, and architecture without production-grade security or real ecosystem integration. |
| Verifier | A system or organization that checks presented claims or credentials. In this project, the verifier role is represented by the backend prototype. |
| Holder | The person who controls the wallet and chooses whether to present requested information. |
| Issuer | An organization that issues a credential, such as a government body, university, employer, or trusted authority. |
| Credential | A digital statement issued by an issuer and held by a user, containing one or more claims. |
| Claim | A single piece of information about a user, such as age-over-18, country of residence, or student status. |
| Presentation | The data a wallet sends to a relying party in response to a verification request. |
| Wallet Response | The simulated response from a wallet. In this project, it is mock data used for testing validation logic. |

## Business and Process Terms

| Term | Meaning in This Project |
|---|---|
| Business Requirement | A real-world need described in business language, such as verifying age or residence. |
| Business Process | The operational context in which verification happens, such as onboarding, access control, or eligibility checking. |
| Use Case | A documented scenario explaining who needs verification, why, and which data is required. |
| Verification Purpose | The reason a relying party requests identity information. This should be clear and specific. |
| Required Claim | A claim that must be present for the verification to succeed. |
| Optional Claim | A claim that may be useful but is not required for the main decision. |
| Over-Sharing | A situation where the wallet response contains more personal data than the business purpose requires. |
| Data Minimization | The principle of requesting and storing only the data that is necessary for the stated purpose. |
| Retention Policy | A rule describing how long verification-related data should be kept. |
| Risk Level | A simple classification of how sensitive or business-critical a verification process is. |

## Prototype Data Terms

| Term | Meaning in This Project |
|---|---|
| Verification Template | A reusable definition of what a relying party wants to verify for a specific business process. |
| Verification Request | A concrete request created from a template, usually representing one verification attempt. |
| Accepted Credential Type | A credential type that the relying party accepts for a specific template or request. |
| Trusted Issuer Category | A category of issuers considered acceptable for a specific verification scenario. |
| Mock Wallet Presentation | A test object representing what a wallet might send back. |
| Mock Trusted Issuer | A simulated issuer used to test trust decisions in the prototype. |
| Validation Result | The system's decision after checking a wallet response against a request. |
| Privacy Warning | A warning generated when the response contains unnecessary or unexpected claims. |
| Audit Log Event | A record of something important that happened during the verification process. |

## API and Backend Terms

| Term | Meaning in This Project |
|---|---|
| FastAPI | The Python web framework used for the backend prototype. |
| Endpoint | An API route such as `/health` or `/verification-requests`. |
| Router | A FastAPI module that groups related endpoints. |
| Service | A module that contains business logic, such as validation or request creation. |
| Schema | A Pydantic model that defines the structure of input and output data. |
| Model | A data representation. In this project, database models may be added later after schemas are stable. |
| Health Check | A simple endpoint used to confirm that the backend is running. |
| Dashboard | A simple user interface or analytics view for inspecting requests, logs, and warnings. |
| Local Development | Running the prototype on the developer's machine, not in production. |

## Privacy and Compliance Terms

| Term | Meaning in This Project |
|---|---|
| Personal Data | Information that relates to an identified or identifiable person. |
| Derived Claim | A claim that answers a question without exposing raw data, such as `age_over_18` instead of full date of birth. |
| Purpose Limitation | The principle that data should only be used for the stated purpose. |
| Consent | The holder's agreement to present information. In this prototype, consent is simulated. |
| Auditability | The ability to review what happened in the verification process. |
| Traceability | The ability to follow how a request, response, validation result, and audit event are connected. |
| Privacy-Preserving | Designed to reduce unnecessary exposure, storage, or processing of personal data. |
| Compliance Review | A later human review of whether a process meets legal or organizational rules. This project can support review but does not replace it. |

## EUDI and Ecosystem Terms

| Term | Meaning in This Project |
|---|---|
| OpenID4VP | OpenID for Verifiable Presentations. A protocol for requesting and presenting credentials. It is a future research topic, not part of the first prototype. |
| SD-JWT VC | Selective Disclosure JWT Verifiable Credential. A credential format that can support selective disclosure. Future topic. |
| PID | Person Identification Data. A core identity data concept in the EUDI ecosystem. Future topic for this project. |
| QTSP | Qualified Trust Service Provider. Relevant to trust and qualified services, but not implemented in version 1. |
| Trust Registry | A source or system for checking trusted issuers or verifiers. This project uses only mock trusted issuer data in version 1. |
| Selective Disclosure | Revealing only selected pieces of information instead of a full credential. The prototype models the idea conceptually. |

## Terms That Need Careful Use

| Term | Use Carefully Because |
|---|---|
| Verification | In this prototype, verification means mock validation of structured data, not real cryptographic proof verification. |
| Trusted | In version 1, trusted means listed in mock trusted issuer data, not legally or cryptographically trusted. |
| Compliance | The project can support compliance reasoning but does not provide legal compliance certification. |
| Wallet | The wallet is simulated through mock responses. The project does not build a real wallet. |
| Production | The project is not production-ready unless future security, legal, and infrastructure work is completed. |

## Naming Conventions

Use these terms consistently in files and documentation:

| Preferred Term | Avoid |
|---|---|
| Verification template | Random request form, identity form |
| Verification request | Wallet query, data ask |
| Wallet presentation | Wallet answer, user data package |
| Validation result | Check result, verification output |
| Audit log event | Log row, history item |
| Privacy warning | Data warning, over-share flag |
| Relying party | Company, service provider, requester, unless context requires those terms |

## Glossary Maintenance Rules

- Add new terms when they appear repeatedly in documentation or code.
- Keep definitions short and project-specific.
- Avoid legal claims unless they are clearly marked as conceptual or future research.
- Prefer business-readable wording before technical detail.
- Update this glossary when naming changes in schemas, routers, or documentation.
