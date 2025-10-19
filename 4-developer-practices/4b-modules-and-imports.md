[← Back to Home](../README.md)

# 4B - Modules and Imports

As programs grow, you’ll need to **organize your code** into multiple files.  
Python uses **modules** and **imports** to keep everything tidy.

---

### 1. What Is a Module?

A **module** is any `.py` file that contains code.  
You can import one module into another to reuse its functions or variables.

**Example:**
```python
# utils.py
def greet(name):
    return f"Hello, {name}!"
```
```python
# main.py
import utils
print(utils.greet("Zach"))
```

---

### 2. Import Variations

```python
from utils import greet
print(greet("Maya"))

import math
print(math.sqrt(16))
```

---

### 3. Standard Library Modules

Python includes hundreds of built-ins you can import anytime.

| Module | Purpose |
|---------|----------|
| `math` | math functions |
| `os` | file and system ops |
| `random` | random numbers |
| `datetime` | time and date |
| `json` | handle structured data |

---

### Key Takeaways
- Split logic into modules for clarity.  
- Use `import` or `from ... import ...`.  
- Explore the standard library.  
- Keeps large projects maintainable.
