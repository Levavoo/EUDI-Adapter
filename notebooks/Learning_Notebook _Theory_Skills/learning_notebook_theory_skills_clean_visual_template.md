# Learning Notebook — Theory & Skills  
Clean Visual Template

Use this template for reusable technical knowledge that remains useful beyond one project.

Examples:
- APIs
- HTTP methods
- JSON
- JSON Schema
- Pydantic
- FastAPI
- SQL
- database modeling
- audit logs
- authentication basics
- Docker basics
- testing

---

# Empty Note Template

Copy this section whenever you create a new theory note.

```markdown
# Topic: [Topic Name]

**Date:** YYYY-MM-DD  
**Tags:** `[LEARN]` `[BACKEND]` `[VALIDATION]`  
**Status:** Draft / Reviewed / Needs Practice

---

## 1. Core Concept

<div style="border-left: 5px solid #2563eb; padding: 10px; background-color: #eff6ff;">

<strong>Core Concept</strong><br>
Write the shortest clear definition here.

</div>

---

## 2. Why This Matters

Explain why this topic is important.

Focus on:
- what problem it solves
- why developers use it
- why it is important for backend/data/security work

<div style="border-left: 5px solid #16a34a; padding: 10px; background-color: #f0fdf4;">

<strong>Practical Use</strong><br>
Explain how this is used in real software development.

</div>

---

## 3. How It Works

Explain the topic step by step.

### Step-by-step logic

1. First step
2. Second step
3. Third step

### Process overview

```text
Input → Processing → Output
```

---

## 4. Key Terms

| Term | Meaning | Example |
|---|---|---|
| Term 1 | Explanation | Example |
| Term 2 | Explanation | Example |
| Term 3 | Explanation | Example |

---

## 5. Practical Example

Add one small example.

Use text, JSON, SQL, Python, or pseudocode depending on the topic.

```text
Example goes here.
```

For code:

```python
# Example code goes here
```

---

## 6. Common Mistakes and Risks

<div style="border-left: 5px solid #ea580c; padding: 10px; background-color: #fff7ed;">

<strong>Common Mistake</strong><br>
Write one common misunderstanding here.

</div>

List additional risks:

- Risk 1
- Risk 2
- Risk 3

---

## 7. Important Rules

<div style="border-left: 5px solid #dc2626; padding: 10px; background-color: #fef2f2;">

<strong>Important Rule</strong><br>
Write a rule that must not be forgotten.

</div>

---

## 8. Connection to My Project

<div style="border-left: 5px solid #7c3aed; padding: 10px; background-color: #f5f3ff;">

<strong>Connection to My Project</strong><br>
Explain how this topic connects to the EUDI relying party integration bus project.

</div>

This topic can help my project with:

- Use case 1
- Use case 2
- Use case 3

---

## 9. Cornell Questions

Use this section for active recall.

Write questions that help you test your understanding.

- What is this topic used for?
- What problem does it solve?
- How does it work internally?
- What can go wrong?
- How would I explain it to a beginner?
- How does it connect to my project?
- Where would I use this in code?

---

## 10. Summary in My Own Words

Write 3–5 sentences.

Rules:
- Do not copy theory directly.
- Use simple language.
- Explain the concept like you are teaching someone new.
- Mention one practical use.

---

## 11. Next Action

Choose one concrete next step.

Examples:
- Create a small code example.
- Add this to the project glossary.
- Build a test endpoint.
- Write a Pydantic model.
- Compare this with another concept.
- Review this note tomorrow.
```

---

# Quick Copy Template

Use this version when you want to write faster notes.

```markdown
# Topic:

**Date:** YYYY-MM-DD  
**Tags:**  
**Status:** Draft

---

## 1. Core Concept

<div style="border-left: 5px solid #2563eb; padding: 10px; background-color: #eff6ff;">

<strong>Core Concept</strong><br>


</div>

---

## 2. Why This Matters



---

## 3. How It Works

1. 
2. 
3. 

---

## 4. Key Terms

| Term | Meaning | Example |
|---|---|---|
|  |  |  |
|  |  |  |
|  |  |  |

---

## 5. Practical Example

```text

```

---

## 6. Common Mistakes and Risks

<div style="border-left: 5px solid #ea580c; padding: 10px; background-color: #fff7ed;">

<strong>Common Mistake</strong><br>


</div>

---

## 7. Important Rules

<div style="border-left: 5px solid #dc2626; padding: 10px; background-color: #fef2f2;">

<strong>Important Rule</strong><br>


</div>

---

## 8. Connection to My Project

<div style="border-left: 5px solid #7c3aed; padding: 10px; background-color: #f5f3ff;">

<strong>Connection to My Project</strong><br>


</div>

---

## 9. Cornell Questions

- 
- 
- 

---

## 10. Summary in My Own Words



---

## 11. Next Action


```

---

# Example Note

```markdown
# Topic: JSON Schema

**Date:** 2026-05-21  
**Tags:** `[LEARN]` `[JSON]` `[BACKEND]` `[VALIDATION]`  
**Status:** Draft

---

## 1. Core Concept

<div style="border-left: 5px solid #2563eb; padding: 10px; background-color: #eff6ff;">

<strong>Core Concept</strong><br>
JSON Schema defines the expected structure, required fields, and allowed data types of JSON data.

</div>

---

## 2. Why This Matters

JSON is commonly used for communication between frontend apps, backend services, APIs, and external systems.

Without validation, a backend might accept incomplete, wrong, or unsafe data.

<div style="border-left: 5px solid #16a34a; padding: 10px; background-color: #f0fdf4;">

<strong>Practical Use</strong><br>
A backend can use JSON Schema to check whether incoming request data has the correct structure before processing it.

</div>

---

## 3. How It Works

1. A developer defines the expected JSON structure.
2. The system receives JSON data.
3. The validator checks the data against the schema.
4. Valid data is accepted.
5. Invalid data is rejected or returned with an error message.

### Process overview

```text
Incoming JSON → Schema validation → Accept or reject
```

---

## 4. Key Terms

| Term | Meaning | Example |
|---|---|---|
| Schema | A definition of expected data structure | A template for valid JSON |
| Required field | A field that must exist | `purpose` |
| Type | The kind of value expected | `string`, `number`, `array` |
| Validation | Checking data against rules | Rejecting missing fields |

---

## 5. Practical Example

```json
{
  "type": "object",
  "required": ["purpose", "required_claims"],
  "properties": {
    "purpose": {
      "type": "string"
    },
    "required_claims": {
      "type": "array",
      "items": {
        "type": "string"
      }
    }
  }
}
```

---

## 6. Common Mistakes and Risks

<div style="border-left: 5px solid #ea580c; padding: 10px; background-color: #fff7ed;">

<strong>Common Mistake</strong><br>
Do not confuse JSON Schema with JSON data. JSON Schema describes the structure of data; it is not the business data itself.

</div>

Additional risks:

- Making schemas too vague.
- Forgetting required fields.
- Accepting data without validation.
- Using inconsistent field names.

---

## 7. Important Rules

<div style="border-left: 5px solid #dc2626; padding: 10px; background-color: #fef2f2;">

<strong>Important Rule</strong><br>
Never trust incoming API data without validation.

</div>

---

## 8. Connection to My Project

<div style="border-left: 5px solid #7c3aed; padding: 10px; background-color: #f5f3ff;">

<strong>Connection to My Project</strong><br>
JSON Schema can help define and validate verification templates in the EUDI relying party integration bus.

</div>

This topic can help my project with:

- age verification templates
- residence verification templates
- employment onboarding templates
- validation of backend configuration files

---

## 9. Cornell Questions

- What is JSON Schema used for?
- What happens if a required field is missing?
- How is JSON Schema different from normal JSON?
- How does JSON Schema connect to Pydantic?
- How could JSON Schema help define verification templates?

---

## 10. Summary in My Own Words

JSON Schema is a way to describe what valid JSON data should look like.  
It defines required fields, allowed data types, and structure.  
It is useful because systems should validate incoming data before using it.  
In my project, it can help make verification templates clear and safe.

---

## 11. Next Action

Create one JSON Schema for an age verification template.
```

---

# Recommended Tags

Use tags to keep notes searchable.

```text
[LEARN]        General learning topic
[API]          API-related topic
[BACKEND]      Backend development
[DATABASE]     SQL, tables, modeling, storage
[SECURITY]     Authentication, authorization, privacy
[VALIDATION]   Data validation, schemas, Pydantic
[TESTING]      Tests, pytest, test strategy
[DOCKER]       Docker, containers, deployment
[EUDI-LINK]    Useful for the EUDI project, but not only EUDI-specific
[QUESTION]     Something unclear
[EXAMPLE]      Practical example
```

---

# Formatting Rules and Explanation

## Purpose of the formatting system

The goal of this format is to make heavy theory easier to process.

Each section has one clear job:

| Section | Purpose |
|---|---|
| Core Concept | Understand the topic in one simple definition |
| Why This Matters | Understand why the topic is useful |
| How It Works | Understand the process or internal logic |
| Key Terms | Learn vocabulary and definitions |
| Practical Example | Connect theory to real usage |
| Common Mistakes and Risks | Avoid misunderstandings |
| Important Rules | Remember critical principles |
| Connection to My Project | Connect general learning to practical work |
| Cornell Questions | Test understanding through active recall |
| Summary in My Own Words | Prove that you understood the concept |
| Next Action | Turn learning into practice |

---

## Color Code

Use colors by meaning, not decoration.

| Color | Label | Meaning | Use For |
|---|---|---|---|
| Blue | Core Concept | Main definition | What is this? |
| Green | Practical Use | Real development use | Where is this used? |
| Purple | Connection to My Project | EUDI/backend relevance | How does this help my project? |
| Orange | Common Mistake | Warning or misunderstanding | What should I avoid? |
| Red | Important Rule | Critical principle | What must I remember? |
| Gray | Extra Note | Optional context | What is useful but not central? |

---

## Callout Blocks

Use HTML callout blocks inside Markdown when you want color-coded sections.

### Blue callout

```html
<div style="border-left: 5px solid #2563eb; padding: 10px; background-color: #eff6ff;">

<strong>Core Concept</strong><br>
Write the main definition here.

</div>
```

### Green callout

```html
<div style="border-left: 5px solid #16a34a; padding: 10px; background-color: #f0fdf4;">

<strong>Practical Use</strong><br>
Write the practical use here.

</div>
```

### Purple callout

```html
<div style="border-left: 5px solid #7c3aed; padding: 10px; background-color: #f5f3ff;">

<strong>Connection to My Project</strong><br>
Write the project connection here.

</div>
```

### Orange callout

```html
<div style="border-left: 5px solid #ea580c; padding: 10px; background-color: #fff7ed;">

<strong>Common Mistake</strong><br>
Write the warning here.

</div>
```

### Red callout

```html
<div style="border-left: 5px solid #dc2626; padding: 10px; background-color: #fef2f2;">

<strong>Important Rule</strong><br>
Write the critical rule here.

</div>
```

### Gray callout

```html
<div style="border-left: 5px solid #6b7280; padding: 10px; background-color: #f9fafb;">

<strong>Extra Note</strong><br>
Write optional context here.

</div>
```

---

## Font and Text Formatting Rules

Markdown does not fully control fonts unless your editor supports custom styling.  
Use Markdown hierarchy to create readable structure.

| Information Type | Format |
|---|---|
| Main topic | `# Heading 1` |
| Major section | `## Heading 2` |
| Subsection | `### Heading 3` |
| Important term | `**bold**` |
| Code term or field name | `` `inline code` `` |
| Code example | fenced code block |
| Data structure | table |
| Warning | orange callout |
| Critical rule | red callout |
| Project relevance | purple callout |
| Optional context | gray callout |

---

## Study Workflow

Use this order when learning heavy theory:

1. Write the Core Concept first.
2. Add Why This Matters in simple language.
3. Explain How It Works step by step.
4. Define the Key Terms.
5. Add one small Practical Example.
6. Add Common Mistakes and Risks.
7. Add one Important Rule.
8. Connect the topic to your project.
9. Write Cornell Questions.
10. Write the Summary in your own words.
11. Choose one Next Action.

---

## Quality Checklist

Before marking a note as reviewed, check:

```text
[ ] I can explain the topic in one simple sentence.
[ ] I know why the topic matters.
[ ] I understand the most important terms.
[ ] I added at least one practical example.
[ ] I added at least three Cornell questions.
[ ] I connected the topic to my project or wrote why it is not project-related.
[ ] I wrote the summary in my own words.
[ ] I chose one next action.
```

---

## Rules for This Notebook

1. Keep explanations simple.
2. Use examples whenever possible.
3. Do not mix project decisions into this notebook.
4. If a note becomes project-specific, copy the relevant part into the Project Build Log.
5. Every serious note should end with a summary and one next action.
6. Prefer small notes over huge notes.
7. Write in your own words first, then improve later.
8. Use color blocks only when they help understanding.
9. Do not color every paragraph.
10. Keep the same structure for every serious note.

---

## Difference Between Notebooks

| Notebook | Purpose |
|---|---|
| Learning Notebook — Theory & Skills | Reusable technical knowledge |
| Scratch Notebook | Fast ideas and messy thinking |
| Project Notebook | Actual build progress and decisions |
| EUDI Notebook | EUDI-specific law, architecture, and ecosystem notes |

The Learning Notebook should answer:

> What technical concept did I learn, and how can I reuse it later?
