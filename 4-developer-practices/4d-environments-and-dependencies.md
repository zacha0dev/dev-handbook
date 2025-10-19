[← Back to Home](../README.md)

# 4D - Environments and Dependencies

Every project you build depends on certain Python versions and packages.  
Managing them properly keeps your setup clean and reproducible.

---

### 1. Virtual Environments

A **virtual environment** isolates dependencies for each project.

```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux
```

Then install packages locally:

```bash
pip install requests
pip freeze > requirements.txt
```

Deactivate when done:
```bash
deactivate
```

---

### 2. Environment Variables

Keep secrets (like API keys) safe.

```python
import os
API_KEY = os.getenv("OPENAI_KEY")
```

Use a `.env` file (with `python-dotenv`) and never commit secrets to GitHub.

---

### 3. Key Takeaways
- Use virtual environments for isolation.  
- Manage dependencies with `requirements.txt`.  
- Store secrets safely using environment variables.
