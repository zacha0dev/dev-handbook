[← Back to Home](../README.md)

# 4A - Error Handling and Debugging

Every programmer - from beginner to expert - runs into errors.  
They aren’t failures; they’re feedback.  
Learning how to *read*, *understand*, and *fix* those errors is one of the most valuable skills you can develop.

---

### 1. Why Errors Happen

Computers follow instructions exactly.  
If something doesn’t match the rules - a missing file, a typo, or a wrong data type - Python stops and shows an error.

**Example**
```python
print("Hello"
```
This will cause:
```
SyntaxError: unexpected EOF while parsing
```
Errors are clues - not punishments.

---

### 2. Common Error Types

| Error Type | Meaning | Example |
|-------------|----------|----------|
| **SyntaxError** | Code is written incorrectly | Missing `)` or `:` |
| **NameError** | Using a variable that doesn’t exist | `print(total)` before defining it |
| **TypeError** | Doing something invalid with a data type | `"5" + 2` |
| **ValueError** | The right type, but the wrong value | `int("abc")` |
| **KeyError** | Missing key in a dictionary | `user["age"]` when `"age"` isn’t there |
| **IndexError** | Missing index in a list | `names[5]` when only 3 exist |
| **FileNotFoundError** | File doesn’t exist | `open("missing.txt")` |

---

### 3. Try / Except

```python
try:
    num = int(input("Enter a number: "))
    print(10 / num)
except ZeroDivisionError:
    print("You can’t divide by zero!")
except ValueError:
    print("That wasn’t a number.")
```

---

### 4. Debugging Tips

1. Read the full error message.  
2. Add `print()` statements to see what’s happening.  
3. Isolate problem code.  
4. Check variable values and types.

---

### Key Takeaways
- Errors are feedback, not failure.  
- `try` / `except` keeps code safe.  
- Debugging builds understanding.  
- Logging helps track program behavior.
