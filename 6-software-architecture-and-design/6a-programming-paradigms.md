[← Back to Home](../README.md)

# 6A - Programming Paradigms

Programming paradigms are the **styles of thinking and structuring code**.  
They shape how you organize logic, data, and behavior.

---

### 1. The Main Paradigms

| Paradigm | Core Idea | Example |
|-----------|------------|----------|
| **Procedural** | Step-by-step instructions using functions | Python scripts, C |
| **Object-Oriented (OOP)** | Bundle data + behavior into reusable objects | Python, Java, C# |
| **Functional** | Treat functions as data; avoid side effects | Haskell, Python (map, filter) |
| **Declarative** | Describe what you want, not how | SQL, HTML |

---

### 2. Procedural Example

```python
def greet(name):
    print("Hello,", name)

greet("Zach")
```

A simple sequence of commands and function calls.

---

### 3. Object-Oriented Example

```python
class Greeter:
    def __init__(self, name):
        self.name = name
    def greet(self):
        print(f"Hello, {self.name}")

g = Greeter("Zach")
g.greet()
```

Objects organize related data and behavior.

---

### 4. Functional Example

```python
names = ["Amy", "Liam", "Jade"]
greetings = list(map(lambda n: f"Hello, {n}", names))
print(greetings)
```

Here, functions act on data without changing it.

---

### 5. Key Takeaways
- Different paradigms offer different strengths.  
- Learn procedural first, then OOP, then functional.  
- Use the paradigm that fits your problem domain best.
