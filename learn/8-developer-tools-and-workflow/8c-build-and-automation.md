[← Back to Home](../README.md)

# 8C - Build and Automation

Automation keeps developers productive and consistent.  
Instead of repeating manual steps, we let tools handle them.

---

### 1. Why Automate?

- Speed up repetitive tasks  
- Reduce human error  
- Keep projects reproducible  

---

### 2. Python Automation Basics

Use scripts to automate builds or cleanups.

```python
import os

def build():
    os.system("pytest")
    os.system("python setup.py sdist bdist_wheel")

if __name__ == "__main__":
    build()
```

---

### 3. Task Runners and Tools

| Tool | Use |
|------|------|
| **Makefile** | Define build steps (`make build`) |
| **invoke / fabric** | Python-based automation |
| **GitHub Actions** | Automate tests/deploys on push |
| **Shell Scripts** | Combine multiple CLI tasks |

---

### 4. Example Makefile

```
run:
	python main.py

test:
	pytest
```

Run with:
```bash
make run
make test
```

---

### 5. Key Takeaways
- Automate everything repeatable.  
- Use scripts to standardize work.  
- Automation scales your time and reliability.
