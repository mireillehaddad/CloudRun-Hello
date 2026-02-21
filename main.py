import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path(__file__).with_name(".env")
loaded = load_dotenv(dotenv_path=env_path)

print("Loaded .env:", loaded)
print("Project ID:", os.getenv("PROJECT_ID"))
print("Credentials Path:", os.getenv("GOOGLE_APPLICATION_CREDENTIALS"))
print("Region:", os.getenv("REGION"))