# Scratch Notebook — Fast Notes / Ideas / Messy Thinking

> Purpose: Capture thoughts quickly before they disappear.  
> Rule: This notebook does **not** need to be clean, complete, or well-organized.

---

## Inbox

Use this section for anything that appears suddenly and should not interrupt current work.

```text
[IDEA] 
[QUESTION] 
[BUILD] 
[LEARN] 
[LINK] 
[PROBLEM] 
[DECISION?] 
[NEXT] 
```

---

## Fast Capture

### Date: YYYY-MM-DD

#### Raw Note

Write the thought here without editing too much.

```text
Example:
[IDEA] Maybe the relying party integration bus could generate reusable verification request templates.
```

#### Why It Appeared

Write the trigger, context, or reason for the thought.

```text
Example:
I was thinking about how companies would avoid asking for too much user data.
```

#### Possible Value

Mark whether this might become useful later.

```text
Value:
- Low
- Medium
- High
- Unknown
```

#### Related Area

```text
Related to:
- EUDI / Architecture
- Backend
- API
- Data model
- Privacy
- Dashboard
- IHK documentation
- Future feature
- General learning
- Unknown
```

#### Next Action

```text
Next:
- Ignore for now
- Research later
- Move to Project Notebook
- Move to EUDI Notebook
- Move to Theory Notebook
- Turn into task
```

---

## Messy Thinking Space

Use this section when the idea is not ready for structure.

```text
Thought:

Questions:

Possible solution:

Problems:

What I do not understand yet:

Maybe useful later because:
```

---

## Quick Questions

Use this when you do not want to stop your current work but want to remember a question.

```text
[QUESTION] 

Context:

Where to check later:

Possible notebook destination:
```

---

## Feature Ideas

Use this for possible features that are not approved project scope yet.

```text
[IDEA] 

Feature:

Who would use it:

Why it might be useful:

Risk / complexity:

Keep, reject, or review later:
```

---

## Problem Sketches

Use this when something feels unclear, broken, or too large.

```text
[PROBLEM] 

What is confusing:

What I already know:

What is missing:

Smallest next step:
```

---

## Links To Check Later

Use this section for links, resources, GitHub repositories, articles, videos, or documentation.

```text
[LINK] 

URL:

Why I saved it:

Related topic:

Check by:
```

---

## Weekly Review

Review this notebook once per week. Move only useful notes into the correct notebook.

### Week: YYYY-MM-DD to YYYY-MM-DD

#### Keep

```text
Notes worth keeping:
-
-
-
```

#### Move

```text
Move to Project Notebook:
-

Move to EUDI Notebook:
-

Move to Theory Notebook:
-
```

#### Delete / Ignore

```text
Notes no longer useful:
-
-
-
```

#### Convert Into Tasks

```text
[NEXT]
1.
2.
3.
```

---

# Formatting Rules

## 1. Use Tags First

Tags make messy notes easier to scan later.

```text
[IDEA]       Possible feature, concept, or direction
[QUESTION]   Something unclear
[BUILD]      Something that may become implementation work
[LEARN]      Something to study later
[LINK]       Resource to check later
[PROBLEM]    Confusion, blocker, or open issue
[DECISION?]  Possible decision, not final yet
[NEXT]       Possible next action
```

## 2. Do Not Over-Clean

This notebook is allowed to contain:
- unfinished thoughts
- broken sentences
- repeated ideas
- unclear questions
- sketches
- temporary assumptions

The goal is speed, not quality.

## 3. Use Question Marks for Unconfirmed Ideas

Use `?` when something is not yet certain.

```text
[DECISION?] Use mock wallet responses in version 1?
[IDEA?] Dashboard could show privacy risk score?
```

Only remove the question mark after the idea becomes a real decision in the Project Notebook.

## 4. Use Short Blocks

Prefer short sections over long paragraphs.

Good:

```text
Problem:
Companies may not know which identity claims they are allowed to request.

Possible solution:
Create reusable verification templates.
```

Avoid turning scratch notes into full documentation too early.

## 5. Move Notes, Do Not Perfect Them Here

At the end of the week:
- useful build notes go to the Project Notebook
- EUDI-specific notes go to the EUDI Notebook
- reusable technical knowledge goes to the Theory Notebook
- unclear or low-value notes stay here or are deleted

## 6. Color / Visual Convention

If your Markdown editor supports colors or callouts, use this convention:

```text
Blue    = Questions / unclear topics
Green   = Build ideas / next actions
Yellow  = Warnings / risks / problems
Purple  = EUDI / legal / architecture references
Gray    = raw messy thinking
```

If your editor does not support colors, use tags only.

## 7. Weekly Rule

This notebook should stay messy during the week.

Once per week, review it and ask:

```text
Is this useful?
Where should it go?
Is there a next action?
Can I delete it?
```

The Scratch Notebook is not the source of truth.  
The Project Notebook is the source of truth for what you actually build.
