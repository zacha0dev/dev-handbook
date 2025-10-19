[← Back to Home](../README.md)

# 8B - IDEs and Debuggers

An **IDE (Integrated Development Environment)** is where code comes to life.  
It combines editing, debugging, and testing in one tool.

---

### 1. Common IDEs

| Tool | Strengths |
|------|------------|
| **VS Code** | Lightweight, extensions, cross-platform |
| **PyCharm** | Powerful for Python, refactoring tools |
| **Vim / Neovim** | Keyboard-based speed |
| **Jupyter Notebook** | Interactive data and research coding |

---

### 2. Debugging in VS Code

1. Set a **breakpoint** by clicking beside a line.  
2. Run with “Debug” (`F5`).  
3. Step through code (`F10`, `F11`).  
4. Inspect variable values in the side panel.

**Example**
```python
def add(a, b):
    return a + b

result = add(3, 4)
print(result)
```

You can step into `add()` to see how variables change.

---

### 3. The Debugging Mindset
- Never guess - inspect values.  
- Reproduce bugs consistently.  
- Add temporary prints or logs.  
- Fix one issue at a time.

---

### 4. Key Takeaways
- IDEs make development smoother.  
- Learn basic debugging shortcuts.  
- Debugging is **learning in action**.
