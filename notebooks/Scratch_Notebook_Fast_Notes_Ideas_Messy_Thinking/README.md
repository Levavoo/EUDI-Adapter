# Scratch Notebook — Fast Notes / Ideas / Messy Thinking

This notebook is for fast capture, messy thinking, rough ideas, questions, remarks, possible tasks, and links that should not interrupt current work.

It is not the source of truth for final project decisions. Useful notes should later be moved into the Project Notebook, EUDI Notebook, or Theory Notebook.

---

## Folder Structure

```text
Scratch_Notebook_Fast_Notes_Ideas_Messy_Thinking/
├── README.md
├── templates/
│   ├── README.md
│   ├── YYYY-MM-DD_scratch_notes_template.md
│   ├── YYYY-W##_scratch_review_template.md
│   ├── type_idea_template.md
│   ├── type_question_template.md
│   ├── type_remark_template.md
│   ├── type_problem_template.md
│   ├── type_possible_task_template.md
│   ├── type_link_template.md
│   ├── type_decision_candidate_template.md
│   └── type_move_later_template.md
├── 2026/
│   └── 05/
│       └── YYYY-MM-DD_scratch_notes.md
└── weekly_reviews/
    └── YYYY-W##_scratch_review.md
```

---

## Naming Convention

Daily scratch files:

```text
YYYY-MM-DD_scratch_notes.md
```

Example:

```text
2026-05-21_scratch_notes.md
```

Weekly review files:

```text
YYYY-W##_scratch_review.md
```

Example:

```text
2026-W21_scratch_review.md
```

Type templates:

```text
type_<note_type>_template.md
```

Example:

```text
type_idea_template.md
```

---

## Core Tags

```text
[IDEA]       Possible feature, concept, process idea, or future direction
[QUESTION]   Something unclear that needs later research
[REMARK]     Observation, reminder, or small thought
[PROBLEM]    Confusion, blocker, risk, or unresolved issue
[NEXT]       Possible action, not yet a confirmed task
[LINK]       Source, repository, article, video, or documentation to check later
[DECISION?]  Possible decision, not final yet
[MOVE]       Note that should be transferred into another notebook
```

---

## Workflow

During the week:

1. Capture fast notes in the daily scratch file.
2. Use tags instead of heavy structure.
3. Do not polish unfinished thoughts.
4. Add possible destinations only when obvious.

At the end of the week:

1. Create one weekly review file.
2. Move useful notes into the correct notebook.
3. Convert concrete actions into project tasks.
4. Delete or ignore low-value notes.

---

## Destination Rules

Move to Project Notebook when the note affects:

- scope
- requirements
- user stories
- business process modeling
- audit logic
- dashboard behavior
- IHK documentation
- confirmed next tasks

Move to EUDI Notebook when the note concerns:

- EUDI Wallet architecture
- ARF
- eIDAS 2.0
- relying parties / verifiers
- PID / attestations
- trust model
- official ecosystem sources

Move to Theory Notebook when the note concerns reusable technical knowledge:

- APIs
- JSON / JSON Schema
- Pydantic
- database modeling
- audit logs
- testing
- Docker

Keep here when the note is:

- unclear
- speculative
- incomplete
- low priority
- not yet connected to the project

---

## Rule

Scratch notes are allowed to be messy.

The weekly review is where useful material becomes structured.
