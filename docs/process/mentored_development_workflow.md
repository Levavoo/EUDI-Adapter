# Mentored Development Workflow

## Purpose

This document defines how development will be handled for the EUDI Adapter project from this point forward.

The goal is to keep the project educational, review-driven, and professionally documented while allowing the developer to write the implementation code directly.

## Core Agreement

The assistant will act as a mentor and reviewer, not as the primary code author.

The developer writes the code.

The assistant may generate full Markdown documentation files, project plans, review notes, checklists, and protocol files.

The assistant should not generate complete implementation code files unless explicitly requested as an exception.

## What the Assistant Should Do

### Planning

- Break work into clear stages.
- Keep the project aligned with the existing stage plans.
- Adjust the plan when the project needs change.
- Explain what should be done now, next, and later.
- Keep tasks small enough to implement and review safely.

### Mentoring

- Explain concepts before implementation.
- Give small code examples or patterns when useful.
- Provide hints instead of full file replacements.
- Point out design risks before they become large problems.
- Help the developer understand why a change is needed.

### Code Review

When the developer pushes changes to the `codex` branch or opens a pull request, the assistant should review the changes and provide feedback.

Review should include:

- Problematic parts of the implementation.
- Missing docstrings.
- Missing type hints.
- Formatting or naming problems.
- Missing tests.
- Missing documentation.
- Files that are too large or should be split.
- Logic that belongs in a different layer.
- Security, privacy, or maintainability concerns.
- Suggestions for what to add, remove, or change.

### GitHub Review Style

The assistant may comment on GitHub pull requests or summarize review findings in chat.

Review comments should be practical and specific.

Use this structure when possible:

```text
Problem:
Why it matters:
Suggested change:
Small example:
```

### Documentation

The assistant may generate full Markdown files, including:

- Stage plans.
- Protocol files.
- Architecture notes.
- Review checklists.
- Cheatsheets.
- Module documentation templates.
- Design decision records.
- Learning notes.

## What the Assistant Should Not Do

The assistant should not:

- Generate complete implementation code files by default.
- Replace entire `.py` files unless explicitly requested.
- Hide design decisions inside generated code.
- Push large code changes without the developer writing or approving them.
- Skip documentation when new modules are introduced.

## Allowed Code Help

The assistant may provide small code snippets for illustration.

Good examples:

```python
class ExampleSchema(BaseModel):
    """Short example of a Pydantic schema style."""

    name: str
```

```python
def parse_requirement(raw_text: str) -> ParsedRequirement:
    """Convert raw business text into a structured requirement object."""
```

These examples are guidance only. The developer should adapt and write the actual project code.

## Branch Workflow

Main working branch:

```text
codex
```

Recommended local workflow:

```powershell
git checkout codex
git pull --rebase origin codex
```

After implementing a small change:

```powershell
git status
git diff
git add path/to/changed-file
git commit -m "Describe the change"
git pull --rebase origin codex
git push origin codex
```

## Review Workflow

### 1. Developer Implements a Small Change

The developer writes the code locally and tests it.

### 2. Developer Pushes to `codex`

The developer pushes changes to GitHub.

### 3. Assistant Reviews

The assistant reviews pushed commits, changed files, or a pull request.

### 4. Assistant Gives Review Notes

Review notes should identify:

- What is good.
- What is risky.
- What must be changed.
- What can wait.
- What documentation or tests are missing.

### 5. Developer Applies Changes

The developer updates the code based on review comments.

### 6. Repeat

The process repeats in small steps.

## Stage-Based Development

Development should stay close to existing stage plans, while remaining flexible.

Recommended current stage order:

| Stage | Focus |
|---|---|
| Stage 0 | Environment, Git workflow, project documentation |
| Stage 1 | Minimal FastAPI backend structure |
| Stage 2 | Business requirement input model |
| Stage 3 | Verification request model |
| Stage 4 | Requirement-to-request translation service |
| Stage 5 | Simulated wallet response handling |
| Stage 6 | Audit log model and storage |
| Stage 7 | Dashboard prototype |
| Stage 8 | Tests, documentation, and IHK-ready explanation |

## Current Working Rules

### One Module at a Time

Work on one focused module or feature at a time.

Avoid mixing unrelated changes in one commit.

### One Code File, One Documentation File

When adding a new code file, add a matching Markdown explanation file.

Example:

```text
backend/app/config.py
backend/app/config.md
```

### Small Commits

Each commit should describe one meaningful change.

Good examples:

```text
Add root endpoint to FastAPI app
Add configuration module documentation
Create requirement schema draft
Add health endpoint test
```

Avoid vague messages:

```text
update
fix
stuff
changes
```

## Definition of Done for a Small Feature

A small feature is done when:

- The code runs locally.
- The changed files are committed.
- The change is pushed to `codex`.
- Basic tests exist where reasonable.
- Documentation exists for new modules.
- The assistant has reviewed the change.
- Review comments are either fixed or intentionally deferred.

## Current Next Step

Continue with Stage 1: minimal FastAPI backend structure.

### Stage 1 Goal

Create a small, understandable backend entry point that proves the project can run locally and gives future modules a clean place to attach routers, configuration, and services.

At the end of this stage, a new developer should be able to:

- Start the backend with one command.
- Open `/` and understand what the service is.
- Open `/health` and verify the service is alive.
- Open `/docs` and see the generated FastAPI documentation.
- Read `backend/app/main.md` and understand what `main.py` is responsible for.
- Understand that business logic does not belong in `main.py`.

### Current Task

Improve the FastAPI application entry point and document it.

Files involved:

```text
backend/app/main.py
backend/app/main.md
```

### What Should Be Done in `backend/app/main.py`

Do not add business logic yet.

The file should only handle:

- Creating the FastAPI `app` object.
- Defining application metadata such as title, version, and description.
- Providing a simple root endpoint `/` that introduces the service.
- Providing a simple health endpoint `/health`.

Expected endpoints:

| Endpoint | Purpose |
|---|---|
| `GET /` | Human-readable service overview for developers/testers |
| `GET /health` | Minimal health check for confirming the backend is running |
| `GET /docs` | FastAPI-generated API documentation |

### What Should Be Done in `backend/app/main.md`

The documentation file should explain:

- What `main.py` is for.
- What it should contain.
- What it should not contain.
- Which endpoints currently exist.
- How to run the backend.
- How to manually test `/`, `/health`, and `/docs`.
- What future modules should be moved into routers or services.

### Acceptance Criteria

This task is done when:

- `uv run uvicorn backend.app.main:app --reload` starts without errors.
- `/` returns a simple project/service status response.
- `/health` returns a simple alive/ok response.
- `/docs` opens successfully.
- `main.py` is small and readable.
- `main.py` has appropriate docstrings or comments where helpful.
- `main.md` exists and explains the file clearly.
- The change is committed and pushed to `codex`.
- The assistant reviews the pushed changes.

### Not Part of This Task

Do not implement these yet:

- Database connection logic.
- Business requirement parsing.
- EUDI verification request generation.
- Wallet response simulation.
- Audit log storage.
- Dashboard logic.
- Authentication or authorization.

These belong to later stages.

## Review Request Template

When asking for review, use this format:

```md
## Review Request

Branch: codex

Changed area:
- backend/app/main.py
- backend/app/main.md

What I tried to do:
- Add or refine root endpoint
- Keep health endpoint working
- Document the role of `main.py`

What I want reviewed:
- Structure
- Naming
- Docstrings
- Missing tests
- Professional formatting
- Whether the file stays inside the Stage 1 scope
```
