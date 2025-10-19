[← Back to Home](../README.md)

# 6D - Code Architecture

Architecture is about **organizing code so it’s clear, scalable, and maintainable**.

---

### 1. The Layered Approach

| Layer | Role |
|--------|------|
| **Presentation/UI** | Interfaces with users |
| **Business Logic** | Core app rules and processing |
| **Data Access** | Reads/writes data (DB, files, APIs) |
| **Infrastructure** | Connects services, configurations |

---

### 2. Example Structure

```
project/
├── app/
│   ├── main.py
│   ├── models/
│   ├── services/
│   ├── utils/
│   └── tests/
├── requirements.txt
└── README.md
```

Each folder has one responsibility.

---

### 3. Separation of Concerns

Don’t mix logic across layers.  
Keep functions focused and files modular.

---

### 4. Example (Good vs. Bad)

Bad:
```python
def save_user(name):
    db.insert(name)
    print("User saved!")  # UI + Data + Logic mixed
```

Better:
```python
def save_user(name):
    db.insert(name)

def notify_user(name):
    print(f"{name} saved!")
```

---

### 5. Key Takeaways
- Organize by responsibility, not type.  
- Keep each layer independent.  
- Clean architecture makes testing and scaling easier.
