# EUDI Reference Implementation Overview

Date: 2026-06-11
Status: Draft
Folder: 01_source_notes
Tags: [SOURCE] [ARCH] [PROJECT]

---

## Sources

| Source | Link | Used for |
|---|---|---|
| European Commission EUDI Wallet implementation page | https://digital-strategy.ec.europa.eu/en/policies/eudi-wallet-implementation | Implementation and pilot context. |
| Official EUDI Wallet GitHub organization | https://github.com/eu-digital-identity-wallet | Official repositories and implementation components. |
| ARF GitHub repository | https://github.com/eu-digital-identity-wallet/eudi-doc-architecture-and-reference-framework/tree/main | Architecture reference behind implementation context. |

---

## Meaning

The EUDI reference implementation ecosystem contains official repositories and components that demonstrate parts of the wallet ecosystem.

For this project, the important point is not to copy or implement the official stack.

The important point is to understand which official components exist and where this prototype fits.

---

## Relevance to my project

The prototype is a relying-party-side support tool.

It should be positioned near the verifier / relying-party side of the ecosystem, but it is not a certified official verifier component.

The project uses simulated wallet responses and simulated trust checks to explain business logic.

---

## Component relevance

| Component area | Meaning | Relevance to prototype |
|---|---|---|
| Wallet components | User-facing wallet software and related services. | Out of scope. The project does not build a wallet. |
| Issuer components | Components for issuing PID or attestations. | Out of scope. Issuers are simulated as metadata. |
| Verifier / relying-party components | Components related to requesting and receiving wallet presentations. | Most relevant comparison area. |
| Trust validation components | Components supporting trust checks. | Future reference. Version 1 simulates trust checks. |
| ARF documentation | Architecture and role definitions. | Main architecture source for this notebook. |

---

## Project boundary

This prototype may use the reference implementation as inspiration for terminology and ecosystem mapping.

It should not claim to be:

- an official EUDI Wallet component
- a certified verifier endpoint
- a PID issuer
- an EAA/QEAA issuer
- a QTSP
- a trust-list service
- a production-ready EUDI integration

---

## Future use

Later, this note can be extended by reviewing concrete repositories from the official GitHub organization.

Possible future research:

- verifier endpoint repository
- trust validator repository
- PID issuer repository
- wallet web/mobile reference components
- official API or protocol examples

---

## Next action

- [ ] Identify which official repository is closest to a verifier/relying-party endpoint.
- [ ] Compare official verifier concepts with this prototype's verification-template idea.
- [ ] Keep implementation details out of this notebook unless they affect architecture or scope.
