[← Back to Home](../README.md)

# 6B - Design Principles

Design principles guide how we write **clean, maintainable, and scalable** code.

---

### 1. Core Principles

| Principle | Description |
|------------|--------------|
| **DRY** | Don’t Repeat Yourself - avoid duplicating logic |
| **KISS** | Keep It Simple, Stupid - clarity over cleverness |
| **YAGNI** | You Aren’t Gonna Need It - don’t over-engineer |
| **SOLID** | 5 principles for OOP design |

---

### 2. The SOLID Breakdown

| Letter | Meaning | Goal |
|---------|----------|------|
| **S** | Single Responsibility | One purpose per class |
| **O** | Open/Closed | Extend behavior without modifying code |
| **L** | Liskov Substitution | Derived classes should work anywhere base ones do |
| **I** | Interface Segregation | Avoid forcing unused functions |
| **D** | Dependency Inversion | Depend on abstractions, not specifics |

---

### 3. Example (Single Responsibility)

Bad:
```python
class User:
    def save_to_db(self): ...
    def send_email(self): ...
```

Better:
```python
class User: ...
class EmailService: ...
```

Each class handles one responsibility.

---

### 4. Key Takeaways
- Simplicity > cleverness.  
- Avoid repetition.  
- Keep modules focused and flexible.
