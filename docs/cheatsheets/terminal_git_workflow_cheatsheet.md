# Terminal and Git Workflow Cheatsheet

## Project Context

| Field | Value |
|---|---|
| Project folder | `C:\Users\Developer\EUDI_Adapter\eudi-relying-party-integration-bus` |
| GitHub repository | `Levavoo/EUDI-Adapter` |
| Main working branch | `codex` |
| Python version | `Python 3.10.10` |
| Package manager | `uv` |
| Backend command | `uv run uvicorn backend.app.main:app --reload` |

## 1. Start a Work Session

Open PowerShell in the project folder or run:

```powershell
cd C:\Users\Developer\EUDI_Adapter\eudi-relying-party-integration-bus
```

Activate the virtual environment if it is not already active:

```powershell
.venv\Scripts\Activate.ps1
```

Confirm you are in the correct project:

```powershell
dir
```

Expected important files and folders:

```text
backend/
dashboard/
diagrams/
docs/
examples/
README.md
NorthStar.md
pyproject.toml
uv.lock
```

## 2. Check Current Git State

Always start with:

```powershell
git status
```

Useful meaning:

| Output | Meaning |
|---|---|
| `working tree clean` | No local uncommitted changes |
| `modified:` | Existing files changed locally |
| `untracked files:` | New files exist but are not tracked by Git |
| `branch is behind` | Remote branch has commits you do not have locally |
| `branch is ahead` | You have local commits not pushed yet |

## 3. Confirm Branch

Check current branch:

```powershell
git branch
```

Switch to the project working branch:

```powershell
git checkout codex
```

If the branch does not exist locally yet:

```powershell
git fetch origin
git checkout codex
```

## 4. Pull Latest Remote Changes

Before editing files, update your local branch:

```powershell
git pull origin codex
```

If you already have local commits and remote also changed, prefer:

```powershell
git pull --rebase origin codex
```

Use this after a non-fast-forward push rejection:

```powershell
git pull --rebase origin codex
git push origin codex
```

## 5. Run the Backend

Start FastAPI:

```powershell
uv run uvicorn backend.app.main:app --reload
```

Test in browser:

```text
http://127.0.0.1:8000/
http://127.0.0.1:8000/health
http://127.0.0.1:8000/docs
```

Stop the server:

```text
CTRL + C
```

Expected backend checks:

| URL | Expected result |
|---|---|
| `/` | Project status response if root endpoint exists |
| `/health` | `{"status":"ok"}` |
| `/docs` | FastAPI documentation page |

## 6. Python and uv Commands

Check Python:

```powershell
python --version
```

Check uv:

```powershell
uv --version
```

Install or sync dependencies from `pyproject.toml` and `uv.lock`:

```powershell
uv sync
```

Run a Python module or command inside the environment:

```powershell
uv run python --version
```

Run FastAPI:

```powershell
uv run uvicorn backend.app.main:app --reload
```

## 7. Add New Files Safely

When creating a new code file, also create a matching `.md` documentation file.

Example:

```text
backend/app/config.py
backend/app/config.md
```

Check what changed:

```powershell
git status
```

View changed content:

```powershell
git diff
```

## 8. Stage Files for Commit

Stage one file:

```powershell
git add backend/app/main.py
```

Stage several specific files:

```powershell
git add backend/app/main.py backend/app/main.md
```

Stage all changes:

```powershell
git add .
```

Use `git add .` carefully. It may include files you did not intend to commit.

Check staged files:

```powershell
git status
```

## 9. Remove a File from Staging

If a file was staged by mistake:

```powershell
git restore --staged path/to/file.md
```

Example:

```powershell
git restore --staged docs/protocol/2026-05-21_protocol.md
```

This does not delete the file. It only removes it from the next commit.

## 10. Discard Local File Changes

Discard changes in one file:

```powershell
git restore path/to/file
```

Example:

```powershell
git restore docs/protocol/2026-05-21_protocol.md
```

Warning: this removes your local edits to that file.

## 11. Commit Workflow

Recommended commit process:

```powershell
git status
git diff
git add path/to/changed-file
git status
git commit -m "Clear commit message"
```

Example:

```powershell
git add backend/app/main.py
git commit -m "Add root endpoint to FastAPI app"
```

Good commit messages:

```text
Add root endpoint to FastAPI app
Add development protocol for 2026-05-21
Create project Git cheatsheet
Add FastAPI health endpoint test
Update README project scope
```

Bad commit messages:

```text
update
fix
stuff
changes
work
```

## 12. Push Workflow

Push local commits to GitHub:

```powershell
git push origin codex
```

If push is rejected with non-fast-forward:

```powershell
git pull --rebase origin codex
git push origin codex
```

## 13. Standard Daily Git Workflow

Use this flow most of the time:

```powershell
cd C:\Users\Developer\EUDI_Adapter\eudi-relying-party-integration-bus
.venv\Scripts\Activate.ps1
git checkout codex
git pull origin codex
git status
```

Work on files.

Then:

```powershell
git status
git diff
git add path/to/file
git commit -m "Describe the change"
git pull --rebase origin codex
git push origin codex
git status
```

## 14. If Git Says Local Changes Would Be Overwritten

Example error:

```text
error: Your local changes to the following files would be overwritten by merge
```

Option A: keep your changes temporarily:

```powershell
git stash
git pull origin codex
git stash pop
```

Option B: discard your local change to one file:

```powershell
git restore path/to/file
git pull origin codex
```

Option C: commit your local changes first:

```powershell
git add path/to/file
git commit -m "Save local change"
git pull --rebase origin codex
```

## 15. If Git Says Non-Fast-Forward

Example error:

```text
! [rejected] codex -> codex (non-fast-forward)
```

Fix:

```powershell
git pull --rebase origin codex
git push origin codex
```

Meaning:

The remote branch has commits that your local branch does not have yet.

## 16. If There Is a Merge Conflict

Git may show files with conflicts.

Check:

```powershell
git status
```

Open the conflicted files in VS Code and look for:

```text
<<<<<<< HEAD
local version
=======
remote version
>>>>>>> branch-name
```

Edit the file so only the correct final content remains.

Then:

```powershell
git add path/to/conflicted-file
git rebase --continue
```

If you want to cancel the rebase:

```powershell
git rebase --abort
```

## 17. Check Commit History

Show recent commits:

```powershell
git log --oneline --decorate -10
```

Show branch history graph:

```powershell
git log --oneline --graph --decorate --all -20
```

## 18. Check Remote Setup

Show remotes:

```powershell
git remote -v
```

Expected remote:

```text
origin  https://github.com/Levavoo/EUDI-Adapter.git (fetch)
origin  https://github.com/Levavoo/EUDI-Adapter.git (push)
```

Add remote if missing:

```powershell
git remote add origin https://github.com/Levavoo/EUDI-Adapter.git
```

Change remote URL if wrong:

```powershell
git remote set-url origin https://github.com/Levavoo/EUDI-Adapter.git
```

## 19. Files That Should Not Be Committed

These should stay ignored:

```text
.venv/
.env
__pycache__/
*.sqlite
*.sqlite3
*.db
.pytest_cache/
.ruff_cache/
.mypy_cache/
```

Check ignored files:

```powershell
git status --ignored
```

## 20. Protocol Workflow

Protocol files go here:

```text
docs/protocol/
```

Naming convention:

```text
YYYY-MM-DD_protocol.md
```

Example:

```text
docs/protocol/2026-05-21_protocol.md
```

After creating or updating a protocol file:

```powershell
git add docs/protocol/YYYY-MM-DD_protocol.md
git commit -m "Add development protocol for YYYY-MM-DD"
git push origin codex
```

## 21. FastAPI File Workflow

For every new Python code file, create a matching Markdown documentation file.

Example for a new config module:

```text
backend/app/config.py
backend/app/config.md
```

Commit both together:

```powershell
git add backend/app/config.py backend/app/config.md
git commit -m "Add application configuration module"
git push origin codex
```

## 22. Safe Command Checklist Before Pushing

Run this before every push:

```powershell
git status
git diff --staged
```

Then push:

```powershell
git push origin codex
```

## 23. Common Recovery Commands

Unstage a file:

```powershell
git restore --staged path/to/file
```

Discard local edits to a file:

```powershell
git restore path/to/file
```

Save temporary changes:

```powershell
git stash
```

Restore temporary changes:

```powershell
git stash pop
```

Abort a rebase:

```powershell
git rebase --abort
```

Check what branch you are on:

```powershell
git branch
```

Check what changed:

```powershell
git diff
```

Check what is staged:

```powershell
git diff --staged
```

## 24. Minimal Command Flow to Memorize

Start:

```powershell
cd C:\Users\Developer\EUDI_Adapter\eudi-relying-party-integration-bus
.venv\Scripts\Activate.ps1
git checkout codex
git pull origin codex
git status
```

Run backend:

```powershell
uv run uvicorn backend.app.main:app --reload
```

Commit:

```powershell
git status
git add path/to/file
git commit -m "Message"
git pull --rebase origin codex
git push origin codex
git status
```
