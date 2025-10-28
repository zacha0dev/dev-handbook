# my-system-design-hb/my-api/scripts/start_api_reload.py
from pathlib import Path
import os, sys, subprocess

if __name__ == "__main__":
    root = Path(__file__).resolve().parents[1]  # ...\my-api
    os.chdir(root)
    env = os.environ.copy()
    env["PYTHONPATH"] = str(root)
    print("🔁 Starting with reload at http://localhost:8000")
    subprocess.run([sys.executable, "-m", "uvicorn", "app.main:app", "--reload"], env=env, check=True)