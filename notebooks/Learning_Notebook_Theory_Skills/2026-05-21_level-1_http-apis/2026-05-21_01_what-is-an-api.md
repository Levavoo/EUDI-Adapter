# Topic: What Is an API?

**Created:** 2026-05-21  
**Level:** Level 1 — Required Now  
**Step:** 01  
**Status:** Draft  
**Tags:** `[LEARN]` `[API]` `[BACKEND]` `[EUDI-LINK]`

---

## 1. Simple Explanation

An **API** is a way for two systems to talk to each other.

Think of it like a menu in a restaurant.

You do not go into the kitchen yourself. You choose something from the menu, send your request, and the kitchen gives you a result.

In software, one program sends a request to another program. The other program processes the request and sends back a response.

Simple example:

```text
Frontend asks backend: "Show me verification templates."
Backend answers: "Here is the list of templates."
```

An API defines:

- what requests are allowed
- what data must be sent
- what response comes back
- what errors can happen

---

## 2. Industry Explanation

An **Application Programming Interface** is a defined contract that allows software components, services, or systems to communicate.

In web backend development, an API usually exposes endpoints that clients can call over HTTP. Each endpoint defines an operation, expected input, output structure, and possible error responses.

An API is not only the code that handles a request. It is also the agreement between systems about how communication works.

An HTTP API normally includes:

- endpoint paths
- HTTP methods
- request parameters
- request body schemas
- response schemas
- status codes
- authentication and authorization rules
- error handling conventions

A well-designed API separates the internal implementation from the external contract. This means the backend can change internally while the client can continue using the same API contract.

---

## 3. Why This Matters

APIs are important because modern software systems are usually made of separate parts.

For example:

- a frontend needs to talk to a backend
- a backend may talk to a database
- a backend may talk to external services
- a dashboard may request audit log data
- a simulated wallet response may be sent to the backend

Without an API, these parts would not have a clear way to exchange information.

For this project, APIs matter because the prototype needs to translate business identity-check requirements into structured verification requests.

---

## 4. Key Terms

| Term | Simple Meaning | Industry Meaning |
|---|---|---|
| API | A way for systems to talk | A defined interface or contract for software communication |
| Client | The system asking for something | The caller or consumer of the API |
| Server | The system answering | The provider that exposes the API |
| Request | A question or instruction | A structured message sent from client to server |
| Response | The answer | A structured message returned by the server |
| Endpoint | A specific API address | A URL path that exposes one operation or resource |
| Contract | The rules of communication | The defined request and response behavior of the API |

---

## 5. Practical Example

Example API idea for the EUDI prototype:

```text
POST /verification-templates
```

Possible request:

```json
{
  "name": "Age Verification",
  "purpose": "Check whether a user is over 18",
  "required_claims": ["age_over_18"],
  "data_minimization_level": "high"
}
```

Possible response:

```json
{
  "template_id": "tpl_age_001",
  "status": "created"
}
```

Simple meaning:

```text
The client asks the backend to create a new verification template.
The backend creates it and returns an ID.
```

---

## 6. Connection to My Project

The EUDI Wallet prototype needs APIs because the backend must expose clear operations for business identity-check flows.

Possible API operations in the prototype:

- create a verification template
- list available verification templates
- simulate a wallet response
- validate the simulated response
- create an audit log event
- show audit log history
- detect privacy or data minimization warnings

In this project, the backend acts like a relying party integration layer. It does not build the wallet itself. It receives business requirements, turns them into structured verification requests, processes simulated wallet responses, and records what happened.

APIs are the communication layer that make those actions possible.

---

## 7. Common Mistakes

- Thinking an API is only a URL.
- Thinking an API is the same as a database.
- Designing endpoints before understanding the business process.
- Returning too much data in API responses.
- Forgetting error responses.
- Not validating input data.
- Mixing internal database structure with public API structure.

---

## 8. Cornell Questions

- What problem does an API solve?
- How is an API like a contract between systems?
- What is the difference between a client and a server?
- What is an endpoint?
- Why should an API not expose unnecessary data?
- How does an API connect to the EUDI relying party prototype?
- What API operations might this project need?

---

## 9. Summary in My Own Words

An API is a structured way for software systems to communicate. It defines what a client can ask for and what the server will return. In backend development, APIs usually use endpoints, requests, responses, and status codes. In my EUDI prototype, APIs are needed so the system can create verification templates, process simulated wallet responses, and expose audit log data in a controlled way.

---

## 10. Next Action

Create the next note:

```text
2026-05-21_02_http-request-response.md
```

Focus:

```text
How HTTP clients and servers communicate through request and response messages.
```
