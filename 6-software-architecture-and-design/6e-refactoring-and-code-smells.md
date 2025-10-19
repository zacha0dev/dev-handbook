[← Back to Home](../README.md)

# 6E - Refactoring and Code Smells

**Refactoring** means improving code *without changing behavior.*  
It’s how developers keep code healthy over time.

---

### 1. What Are Code Smells?

A "code smell" is a hint that something could be structured better.

| Smell | Description | Fix |
|--------|--------------|------|
| **Long Function** | Too many lines | Split into smaller functions |
| **Duplicated Code** | Repeated logic | Extract shared function |
| **Magic Numbers** | Unclear constants | Use named variables |
| **Large Class** | Too many responsibilities | Split into smaller classes |
| **Deep Nesting** | Too many if/else | Early returns or guard clauses |

---

### 2. Example Refactor

Before:
```python
def process_user(data):
    if data["role"] == "admin":
        print("Admin access")
    else:
        print("User access")
```

After:
```python
def process_user(data):
    print(f"{data['role'].title()} access")
```

---

### 3. The Refactoring Process

1. Identify code smell.  
2. Write tests.  
3. Refactor step-by-step.  
4. Verify tests still pass.

---

### 4. Key Takeaways
- Clean code improves long-term maintainability.  
- Refactor often, not just when broken.  
- Code should read like clear thought.
