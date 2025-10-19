[← Back to Home](../README.md)

# 3C - Functions and Structures: Organizing Your Code

Once you understand variables and logic, the next step is **structure** - how to keep your code organized, readable, and reusable.  
This is where **functions** come in. They let you group logic into meaningful chunks, just like chapters in a book or steps in a recipe.

---

### 1. What Is a Function?

A **function** is a reusable block of code that performs a specific task.  
It takes **input**, does something with it, and often gives **output** back.

**Example**
```python
def greet(name):
    print("Hello,", name)

greet("Zach")
greet("Maya")
```

Here’s what happens:
1. The function is *defined* with `def` and a name.  
2. It runs the code inside its block whenever you *call* it.  
3. You can reuse it as many times as you want — just change the input.

Functions make your code cleaner and prevent repetition.

---

### 2. Input and Output (Parameters and Return Values)

Functions can take data in and send results back.

**Example**
```python
def add(x, y):
    total = x + y
    return total

result = add(5, 3)
print("The sum is:", result)
```

- `x` and `y` are **parameters** (inputs).  
- `return` sends a value back to the caller.  
- The result is stored in a variable and can be used elsewhere.

You can think of it like a vending machine:  
you put in coins (inputs), it processes them (logic), and gives back a drink (output).

---

### 3. Why Functions Matter

Without functions, your code grows messy and repetitive.  
With them, you can break your program into smaller, logical parts:

| Without Functions | With Functions |
|--------------------|----------------|
| Repeating the same code many times | Reuse one function call |
| Hard to debug | Easier to test each part separately |
| No clear flow | Code reads like a story |

This structure is called **modular programming** - building with pieces that can fit together.

---

### 4. Scope and Lifetime

Each variable inside a function lives only while that function runs.  
This is called **scope**.

```python
def show_message():
    msg = "Hello!"
    print(msg)

show_message()
# print(msg)  # Error: variable doesn't exist outside the function
```

Variables inside a function are **local**, and ones outside are **global**.  
This keeps your code safe from accidental changes.

---

### 5. Nested Functions and Organization

You can define one function inside another or organize related functions into modules or files.

**Example**
```python
def main():
    def greet(name):
        return "Hello " + name
    print(greet("Zach"))

main()
```

Later, you’ll split code into multiple files (like `helpers.py` or `math_utils.py`) and import them into your main program.

```python
# helpers.py
def greet(name):
    return f"Hello, {name}"

# main.py
from helpers import greet
print(greet("Maya"))
```

This is how real projects stay structured and maintainable.

---

### 6. Combining Functions with Logic

Now you can mix everything you’ve learned - variables, flow, and functions - into a working program.

**Example**
```python
def check_age(name, age):
    if age >= 18:
        return f"Welcome, {name}, you're an adult."
    else:
        return f"Hi, {name}, you're still growing!"

user = input("Enter your name: ")
years = int(input("Enter your age: "))
print(check_age(user, years))
```

**Flow:**  
1. User input →  
2. Function call →  
3. Conditional logic →  
4. Output message

---

### 7. Key Takeaways
- Functions group logic into reusable parts.  
- Parameters are inputs, and return values are outputs.  
- Scope keeps data organized and isolated.  
- Functions make your code modular, clear, and maintainable.  

