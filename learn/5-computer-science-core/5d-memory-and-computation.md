[← Back to Home](../README.md)

# 5D - Memory and Computation

Understanding how memory works helps explain performance and debugging.

---

### 1. How Programs Use Memory

Python manages memory for you, but it still has rules.

| Area | Description |
|------|--------------|
| **Stack** | Stores local variables and function calls |
| **Heap** | Stores objects and dynamic data |
| **Code Area** | Where compiled bytecode lives |

---

### 2. Example of Stack vs Heap

```python
def add(a, b):
    total = a + b
    return total

x = 10
y = 20
result = add(x, y)
```

- `x`, `y`, and `total` live on the **stack**.  
- The function call creates a new stack frame.  
- The values (10, 20) live in the **heap**.

---

### 3. Garbage Collection

Python automatically frees unused memory using **reference counting**.

```python
a = [1, 2, 3]
b = a
del a  # object still exists (b points to it)
del b  # now it's removed from memory
```

---

### 4. Key Takeaways
- The stack handles function logic.  
- The heap stores dynamic data.  
- Memory leaks can still happen - know what’s being referenced.
