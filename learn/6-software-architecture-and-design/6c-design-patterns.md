[← Back to Home](../README.md)

# 6C - Design Patterns

Design patterns are **reusable solutions to common software problems**.  
They aren’t code you copy-paste - they’re *templates for thinking.*

---

### 1. The Three Pattern Families

| Family | Examples | Use Case |
|---------|-----------|-----------|
| **Creational** | Singleton, Factory | Object creation |
| **Structural** | Adapter, Decorator, Facade | Combine or wrap objects |
| **Behavioral** | Observer, Strategy, Command | Control how objects interact |

---

### 2. Example: Singleton Pattern

Ensure only one instance exists.

```python
class Config:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

c1 = Config()
c2 = Config()
print(c1 is c2)  # True
```

---

### 3. Example: Observer Pattern

Notify listeners when something changes.

```python
class Event:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, fn):
        self.subscribers.append(fn)

    def notify(self, data):
        for fn in self.subscribers:
            fn(data)

def listener(msg):
    print("Received:", msg)

event = Event()
event.subscribe(listener)
event.notify("Hello!")
```

---

### 4. Key Takeaways
- Patterns make design consistent.  
- Learn to **recognize** them before implementing.  
- Use patterns to communicate intent clearly.
