# CloudRun-Hello  
## Windows Local Setup + Git Workflow (Full Chronological Steps)

This document records **exactly what happened step-by-step** while setting up a local Python project for future Cloud Run deployment.

Environment:
- OS: Windows
- Terminal: PowerShell
- Editor: VS Code
- Python Virtual Environment: `.venv`
- GitHub repository: CloudRun-Hello

---

# STEP 1 — Create Python Virtual Environment

From project folder:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

After activation:

```
(.venv) PS C:\Users\mirei\OneDrive\Desktop\cloudrun-hello>
```

---

# STEP 2 — Install python-dotenv

```powershell
pip install python-dotenv
```

Verification:

```powershell
pip show python-dotenv
```

Package successfully installed inside:

```
.venv\Lib\site-packages
```

---

# STEP 3 — First Execution Attempt

```powershell
python .\main.py
```

Output:

```
Project ID: None
Credentials Path: None
```

### Problem Identified

`.env` file existed but had 0 bytes.

Verification:

```powershell
dir -Force
```

Output showed:

```
.env    Length: 0
```

---

# STEP 4 — Fix Empty .env File

Recreated `.env` using PowerShell:

```powershell
@"
GOOGLE_APPLICATION_CREDENTIALS=C:\Users\mirei\OneDrive\Desktop\cloudrun-hello\calm-snowfall-485503-b4-fe8d076429fb.json
PROJECT_ID=calm-snowfall-485503-b4
REGION=northamerica-northeast1
"@ | Set-Content -Encoding utf8 .env
```

Verification:

```powershell
Get-Content .\.env
```

---

# STEP 5 — Successful Execution

```powershell
python .\main.py
```

Output:

```
Loaded .env: True
Project ID: calm-snowfall-485503-b4
Credentials Path: C:\Users\mirei\OneDrive\Desktop\cloudrun-hello\calm-snowfall-485503-b4-fe8d076429fb.json
Region: northamerica-northeast1
```

Environment variables correctly loaded.

---

# STEP 6 — Generate requirements.txt

```powershell
pip freeze > requirements.txt
```

---

# STEP 7 — Initialize Git

```powershell
git init
git status
```

Untracked files detected:
- .dockerignore
- .gitignore
- README.md
- main.py
- requirements.txt

---

# STEP 8 — First Commit Attempt (Error)

Attempted:

```powershell
git commit -m "Local setup: venv + dotenv + README + requirements"
```

Error:

```
nothing added to commit but untracked files present
```

### Fix

```powershell
git add .
git commit -m "Initial local setup: venv + dotenv + README + requirements"
```

Commit successful.

---

# STEP 9 — Add Remote Repository

```powershell
git remote add origin git@github.com:mireillehaddad/CloudRun-Hello.git
git branch -M main
```

---

# STEP 10 — First Push Error

```powershell
git push -u origin main
```

Error:

```
src refspec main does not match any
```

Then after proper commit:

```
rejected (fetch first)
```

Reason:
Remote repository already had commits.

---

# STEP 11 — Pull with Rebase

```powershell
git pull --rebase origin main
```

Conflict occurred in:

```
README.md
```

---

# STEP 12 — Resolve Merge Conflict

1. Open README in VS Code:
   ```powershell
   code README.md
   ```

2. Remove conflict markers:
   ```
   <<<<<<<
   =======
   >>>>>>>
   ```

3. Save file

4. Stage resolved file:
   ```powershell
   git add README.md
   ```

5. Continue rebase:
   ```powershell
   git rebase --continue
   ```

Output:

```
Successfully rebased and updated refs/heads/main.
```

---

# STEP 13 — Final Push (Success)

```powershell
git push -u origin main
```

Output:

```
branch 'main' set up to track 'origin/main'.
```

Repository successfully pushed to GitHub.

---

# Security Configuration

Ensure `.gitignore` contains:

```
.venv/
.env
*.json
__pycache__/
```

Never commit:
- Service account JSON
- .env file
- Virtual environment

---

# Final Project Structure

```
cloudrun-hello/
│
├── main.py
├── requirements.txt
├── README.md
├── .gitignore
├── .dockerignore
├── .env                         (local only)
├── calm-snowfall-...json         (local only)
└── .venv/                        (local only)
```

---

# Key Lessons Learned

- Always run `git add` before `git commit`
- A remote repository may already contain commits
- `git pull --rebase` keeps commit history clean
- Merge conflicts must be manually resolved
- `.env` files can exist but be empty — always verify file size
- Never push secrets to GitHub

---

# Next Steps

- Create Dockerfile
- Build Docker image
- Install and configure gcloud CLI
- Create Artifact Registry
- Push Docker image
- Deploy to Cloud Run