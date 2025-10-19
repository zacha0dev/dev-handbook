[← Back to Home](../README.md)

# 3B - Programming Basics: Variables, Data, and Logic

Once you understand what a programming language is, the next step is learning the *building blocks* that every language uses.  
These are the small, repeatable tools that let you describe logic, store information, and make your program react.

Programming is like writing a recipe:  
- **Variables** are the ingredients you keep track of.  
- **Data types** are the kinds of ingredients (numbers, text, lists).  
- **Logic and control flow** are the steps and choices in the recipe.  

Let’s walk through them.

---

### 1. Variables - Storing Information

A **variable** is a name that holds a piece of data in memory.  
You can think of it as a labeled box that stores something the program can use later.

**Example (Python)**
```python
name = "Zach"
age = 27
print("Hello,", name, "- you are", age)
```

Here:
- `name` and `age` are variables.  
- The equals sign `=` means “store this value.”  
- You can change a variable at any time - it always keeps the most recent value.

```python
age = age + 1
print("Next year, you'll be", age)
```

---

### 2. Data Types - The Nature of Data

Not all data is the same.  
Some represent text, some represent numbers, and others store collections of things.

| Type | Description | Example |
|------|--------------|----------|
| **Integer** | Whole number | `score = 95` |
| **Float** | Decimal number | `temperature = 72.5` |
| **String** | Text | `name = "Zach"` |
| **Boolean** | True/False | `is_online = True` |
| **List / Array** | Ordered collection | `friends = ["Amy", "Liam", "Jade"]` |
| **Dictionary / Object** | Key–value pairs | `user = {"name": "Zach", "age": 27}` |

Each type supports different actions.  
You can add numbers, join text, or check if a value exists in a list.

```python
print("2 + 3 =", 2 + 3)
print("Hello " + "World")
print("Liam" in friends)
```

---

### 3. Operators - Doing Something With Data

Operators perform actions.  
They let you compare, calculate, and combine information.

| Category | Example | Description |
|-----------|----------|-------------|
| **Arithmetic** | `x + y`, `x - y`, `x * y`, `x / y` | math operations |
| **Comparison** | `x > y`, `x == y`, `x != y` | check relationships |
| **Logical** | `and`, `or`, `not` | combine multiple conditions |

**Example**
```python
temp = 30
if temp > 25 and temp < 35:
    print("The weather is nice!")
```

---

### 4. Control Flow - Guiding Decisions

By default, programs run top to bottom.  
But with **control flow**, you can tell the computer *when* and *how* to do things differently.

#### If / Else
```python
temp = 30
if temp > 25:
    print("It's warm!")
else:
    print("It's cool.")
```

#### Loops
Loops repeat an action until a condition changes.

**For loop**
```python
for i in range(3):
    print("Hello", i)
```

**While loop**
```python
count = 0
while count < 3:
    print("Count is", count)
    count += 1
```

---

### 5. Combining Logic

You can mix variables, input, and decisions to make interactive programs.

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age >= 18:
    print("Welcome,", name, "you're an adult.")
else:
    print("Hi,", name, "you're still growing!")
```

This demonstrates **input → process → output** again - now with real logic.

---

### 6. Key Takeaways
- Programming is about describing *data* and *actions*.
- **Variables** store information.  
- **Control flow** makes decisions.  
- **Loops** repeat actions.  
- **Functions** (next topic) organize and reuse code.

**Next up:** we’ll explore how to group logic into **functions and structures**, turning small tasks into organized, reusable code.
