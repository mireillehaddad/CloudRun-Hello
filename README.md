# Cloud Run Hello – Local Development Setup (Windows)

## Project Overview

This project documents the local development setup for a Python application that:

- Uses a virtual environment (`.venv`)
- Loads sensitive configuration from a `.env` file
- Authenticates locally with a Google Cloud service account
- Prepares for future Cloud Run deployment

This setup is for local development only.
Production deployment will use IAM service accounts instead of JSON keys.

---

## Environment

- OS: Windows  
- Terminal: PowerShell  
- Editor: VS Code  
- Python: Virtual Environment (`.venv`)  
- Package: `python-dotenv`

---

## 1️⃣ Create Virtual Environment

From the project root directory:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

After activation, the terminal should display:

```
(.venv) PS C:\Users\mirei\OneDrive\Desktop\cloudrun-hello>
```

---

## 2️⃣ Install Required Dependency

Install `python-dotenv` to manage environment variables:

```powershell
pip install python-dotenv
```

Verify installation:

```powershell
pip show python-dotenv
```

Expected:

```
Version: 1.2.1
Location: .venv\Lib\site-packages
```

---

## 3️⃣ Create `.env` File (Local Development Only)

Create a file named:

```
.env
```

Add the following content:

```
GOOGLE_APPLICATION_CREDENTIALS=C:\Users\mirei\OneDrive\Desktop\cloudrun-hello\calm-snowfall-485503-b4-fe8d076429fb.json
PROJECT_ID=calm-snowfall-485503-b4
REGION=northamerica-northeast1
```

⚠ This file contains sensitive data and must never be committed.

---

## ⚠ Issue Encountered

Initially, the `.env` file existed but had 0 bytes, which caused:

```
Project ID: None
Credentials Path: None
```

Verification command:

```powershell
dir -Force
```

It showed:

```
.env    Length: 0
```

---

## ✅ Fix Applied

Rewrote the `.env` file correctly using PowerShell:

```powershell
@"
GOOGLE_APPLICATION_CREDENTIALS=C:\Users\mirei\OneDrive\Desktop\cloudrun-hello\calm-snowfall-485503-b4-fe8d076429fb.json
PROJECT_ID=calm-snowfall-485503-b4
REGION=northamerica-northeast1
"@ | Set-Content -Encoding utf8 .env
```

Verify file content:

```powershell
Get-Content .\.env
```

---

## 4️⃣ Load Environment Variables in Python

`main.py`:

```python
import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path(__file__).with_name(".env")
loaded = load_dotenv(dotenv_path=env_path)

print("Loaded .env:", loaded)
print("Project ID:", os.getenv("PROJECT_ID"))
print("Credentials Path:", os.getenv("GOOGLE_APPLICATION_CREDENTIALS"))
print("Region:", os.getenv("REGION"))
```

---

## 5️⃣ Verify Local Execution

Run:

```powershell
python .\main.py
```

Expected output:

```
Loaded .env: True
Project ID: calm-snowfall-485503-b4
Credentials Path: C:\Users\mirei\OneDrive\Desktop\cloudrun-hello\calm-snowfall-485503-b4-fe8d076429fb.json
Region: northamerica-northeast1
```

This confirms:

- `.env` loads correctly
- Environment variables are accessible
- Local authentication configuration works

---

## 🔐 Security Configuration

Ensure `.gitignore` contains:

```
.venv/
.env
*.json
__pycache__/
```

This prevents committing:

- Service account JSON keys
- Environment variables
- Virtual environment files

---

## 📁 Current Project Structure

```
cloudrun-hello/
│
├── main.py
├── .env                          (local only)
├── calm-snowfall-485503-b4-fe8d076429fb.json  (local only)
├── .gitignore
├── README.md
└── .venv/
```

---

## Important Notes

- `.env` is used for local development only
- The service account JSON file must never be committed
- In production (Cloud Run), authentication should use IAM service accounts instead of JSON keys

---

Next steps will include:

- Creating `requirements.txt`
- Creating a `Dockerfile`
- Building the Docker image
- Deploying to Cloud Run Jobs

