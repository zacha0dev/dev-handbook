[← Back to Home](../README.md)

# 8D - Package Management

Modern programming relies on **packages** - reusable code modules shared by others.  
Python uses `pip` and virtual environments to manage them cleanly.

---

### 1. Installing and Managing Packages

```bash
pip install requests
pip list
pip uninstall requests
```

To save your dependencies:
```bash
pip freeze > requirements.txt
pip install -r requirements.txt
```

---

### 2. Virtual Environments

Keep project dependencies separate.

```bash
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\activate   # Windows
```

Deactivate anytime:
```bash
deactivate
```

---

### 3. pyproject.toml

Modern Python packaging uses `pyproject.toml`:

```toml
[project]
name = "myapp"
version = "0.1.0"
dependencies = ["requests"]
```

---

### 4. Key Takeaways
- Always use a virtual environment.  
- Keep `requirements.txt` up to date.  
- Dependencies = reproducibility.
