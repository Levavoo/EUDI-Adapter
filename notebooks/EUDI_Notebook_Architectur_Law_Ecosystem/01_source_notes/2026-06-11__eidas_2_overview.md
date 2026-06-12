# eIDAS 2.0 Overview

Date: 2026-06-11
Status: Draft
Folder: 01_source_notes
Tags: [SOURCE] [LEGAL] [PROJECT] [PRIVACY]

---

## Source

Source title: Regulation (EU) 2024/1183
Source type: Official EU legal source
Link: https://eur-lex.europa.eu/eli/reg/2024/1183/oj
Context source: https://eudi.dev/arf/
Used sections: European Digital Identity Framework, EUDI Wallet context, relying-party relevance, privacy/data minimization context

---

## Meaning

eIDAS is the EU framework for electronic identification and trust services.

Regulation (EU) 2024/1183 updates the eIDAS context and establishes the European Digital Identity Framework around the EUDI Wallet.

For this notebook:

```text
eIDAS 2.0 = legal background
ARF = architecture and ecosystem explanation
Prototype = simulated relying-party-side support tool
```

---

## Relevance to my project

The prototype is not a legal compliance tool, but it works in a legal and trust context.

Relevant ideas:

| Idea | Meaning for the prototype |
|---|---|
| EUDI Wallet | The project models how organizations may request wallet-based proof. |
| User control | Simulated responses should show user-controlled presentation. |
| Relying party | The project focuses on the organization requesting and relying on data. |
| Trust services | The prototype must not claim to be a QTSP or trust service. |
| Data minimization | The prototype should warn about unnecessary data requests. |
| Legal boundary | Validation is simulated, not certified legal validation. |

---

## Practical project rule

The prototype may say:

```text
This verification request appears excessive for the stated business purpose.
```

The prototype should not say:

```text
This request is legally illegal or legally compliant.
```

Reason: legal conclusions require legal review and context.

---

## In scope

- Use eIDAS 2.0 as legal context.
- Explain why wallet verification exists.
- Explain why relying parties need purpose-bound requests.
- Support privacy warning logic.
- Keep audit logs focused on request, response, validation, and warnings.

---

## Out of scope

- Legal advice.
- Formal legal compliance assessment.
- Real EUDI Wallet certification.
- Real trust-service operation.
- Real QTSP role.
- Real trusted-list validation.

---

## Next action

- [ ] Use this note in `what_my_project_is_not.md`.
- [ ] Keep eIDAS legal claims cautious and source-based.
- [ ] Later review exact relying-party obligations if needed.
