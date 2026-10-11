# Raphael
R.A.P.H.A.E.L. : AI-Powered Community Moderation Assistant

> **Current status: Initial setup only.**
> No toxicity detection, spam detection, bot integration, or other
> moderation capabilities have been implemented yet.

---

## What R.A.P.H.A.E.L. is intended to become

**R.A.P.H.A.E.L.** (Rapid Analysis and Prevention of Harassment, Abuse, Exploitation, and Language toxicity) is a moderation assistant for online communities. It will:

- Score messages for potential toxicity using a trained classifier.
- Detect spam using transparent rule-based checks (with an optional classifier later).
- Apply rate-limit and burst heuristics for basic raid/flood defense.
- Route uncertain or suspicious messages to human moderators for review.
- Start in **review-only mode** — it will never automatically ban users based on an unvalidated model.

---

## Supported Python version

**Python 3.12.10** (64-bit). All packages have been selected for compatibility with this version.

---

## Optional - Virtual Environment setup (Windows, PowerShell)
A virtual environment isolates project dependencies from other Python projects. Using one is recommended.

If `.venv` already exists, skip Step 1.

```powershell
# 1. Create the virtual environment (skip if one already exists)
py -m venv .venv

# 2. Activate it (optional — see note below)
.\.venv\Scripts\Activate.ps1

# 3. Confirm you are using the venv interpreter
.\.venv\Scripts\python.exe -c "import sys; print(sys.executable)"
```

> **Note:** Activation is optional. All subsequent commands use `.venv\Scripts\python.exe` directly, so you do not need to activate the environment. If you choose not to use a virtual environment, replace that path with your chosen Python executable.


---

## Installing dependencies

These commands assume `.venv` already exists (see setup section above).

`requirements.txt` contains **pinned** package versions — the exact versions tested on Python 3.12.10. This helps reproduce the project's dependency environment on compatible systems.

```powershell
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Install the package itself in editable mode (required for `import raphael` to work):

```powershell
.\.venv\Scripts\python.exe -m pip install -e .
```

---

## Running the smoke test

```powershell
.\.venv\Scripts\python.exe -m pytest tests/test_smoke.py -v
```

Expected result: **9 tests passed** (1 package/version test + 1 per dependency × 8).

---

## Safety and secrets policy

- **Review-only:** The initial moderation policy will never automatically ban or mute users.
- **No secrets in code:** Never put bot tokens, API keys, or passwords in source files, notebooks, logs, or commit messages.
- **`.env` is private:** Copy `.env.example` to `.env` and fill in real values. `.env` is excluded from Git and must never be committed.
- **No private datasets:** Do not commit raw message dumps, private logs, or datasets that you do not have permission to share.

---

## Known limitations (Current Phase)

- No moderation logic exists yet.
- No bot integration exists yet.
- No model has been trained or evaluated.
- **Passing smoke tests does not mean moderation functionality exists.** The smoke tests only verify that the package is importable and the eight dependencies can be loaded. No message classification, spam detection, or moderation decision is performed.
