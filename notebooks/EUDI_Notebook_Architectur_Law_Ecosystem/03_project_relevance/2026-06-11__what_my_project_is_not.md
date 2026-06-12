# What My Project Is Not

Date: 2026-06-11
Status: Draft
Folder: 03_project_relevance
Tags: [PROJECT] [DECISION] [SCOPE] [IHK]

---

## Purpose

This note defines the project boundaries.

Clear boundaries are important because the EUDI Wallet ecosystem is large. Without boundaries, the prototype could accidentally become too broad or misleading.

---

## The project is not a wallet

The project does not build an EUDI Wallet app.

It does not manage a user's real wallet, keys, credentials, lifecycle, recovery, or device security.

---

## The project is not an issuer

The project does not issue real PID, EAA, or QEAA.

Issuer roles are only simulated as metadata in wallet responses.

Example:

```json
{
  "issuer": "Simulated National PID Provider",
  "issuer_type": "PID_PROVIDER"
}
```

---

## The project is not a trust service provider

The project is not a QTSP, trust service provider, certificate provider, trusted-list provider, or legal trust infrastructure component.

Trust checks in version 1 are simulated.

---

## The project is not legal compliance software

The prototype may flag privacy risks or excessive requests.

It should not claim that a request is legally compliant or legally illegal.

Correct wording:

```text
This request may be excessive for the stated purpose.
```

Avoid wording:

```text
This request is legally illegal.
```

---

## The project is not production EUDI integration

Version 1 does not implement:

- real wallet integration
- real cryptographic proof validation
- real trusted-list lookup
- real PID/EAA/QEAA issuance
- certification
- conformity assessment
- production relying-party registration

---

## Why these boundaries matter

| Boundary | Reason |
|---|---|
| Not a wallet | Keeps focus on organization/relying-party side. |
| Not an issuer | Avoids claiming authority to create credentials. |
| Not a QTSP | Avoids regulated trust-service claims. |
| Not legal advice | Keeps prototype educational and analytical. |
| Not production integration | Keeps version 1 realistic for the current project stage. |

---

## Final scope statement

The project is a simulated relying-party-side support tool for understanding and documenting wallet verification processes.

It helps explain what an organization should request, why it should request it, how a simulated wallet response can be validated, and what should be recorded in an audit log.
