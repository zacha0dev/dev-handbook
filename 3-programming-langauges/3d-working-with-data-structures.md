[← Back to Home](../README.md)

# 3D - Working With Data Structures

Now that you can write and organize code with functions, it’s time to learn how programs actually **store and manage large amounts of data**.  
Real programs rarely work with just one variable - they handle lists of items, sets of options, and key-value data that describe real things.

These collections of data are called **data structures**.

---

### 1. What Are Data Structures?

A **data structure** is a way of organizing information so it can be used efficiently.  
Think of it like drawers in a toolbox - each drawer has a purpose and stores things in a specific way.

Different structures solve different problems:

| Type | Purpose | Example |
|------|----------|----------|
| **List / Array** | Store items in order | shopping list, tasks |
| **Dictionary / Object / Map** | Store labeled data | contact info, settings |
| **Tuple** | Store fixed, ordered data | coordinates, RGB color |
| **Set** | Store unique items only | unique tags, categories |

Each type affects how you access, add, or modify the data.

---

### 2. Lists - Ordered Collections

A **list** (in Python) or **array** (in other languages) stores multiple items in sequence.

```python
tasks = ["Email client", "Write report", "Walk dog"]
print(tasks[0])        # first item
tasks.append("Read book")
print(tasks)
```

You can loop through lists to process all items:

```python
for task in tasks:
    print("Task:", task)
```

Lists are flexible - you can change, sort, and slice them easily.

```python
tasks.remove("Write report")
tasks.sort()
print(tasks[0:2])  # show first two items
```

---

### 3. Dictionaries - Key–Value Storage

A **dictionary** (also called a map or object) lets you store data in pairs: a **key** (the label) and a **value** (the content).

```python
user = {
    "name": "Zach",
    "age": 27,
    "email": "zach@example.com"
}

print(user["name"])
user["age"] = 28
```

Dictionaries are powerful for storing real-world information where you want to **look things up by name** instead of index.

---

### 4. Tuples - Fixed Collections

Tuples are like lists, but **immutable** - you can’t change them after creation.

```python
location = (27.9475, -82.4584)  # coordinates
print("Latitude:", location[0])
```

They’re useful for data that shouldn’t be modified, like coordinates, color codes, or database records.

---

### 5. Sets - Unique Items Only

A **set** stores only unique values - duplicates are automatically removed.

```python
tags = {"python", "learning", "python", "coding"}
print(tags)  # {'python', 'learning', 'coding'}
```

Sets are perfect for filtering duplicates or checking membership quickly.

```python
if "coding" in tags:
    print("You're a coder!")
```

---

### 6. Combining Data Structures

Most programs combine these structures together.  
For example, a to-do app might use:

```python
tasks = [
    {"title": "Write handbook", "done": False},
    {"title": "Push repo", "done": True},
    {"title": "Go for a run", "done": False}
]

for task in tasks:
    status = "✅" if task["done"] else "🕓"
    print(status, task["title"])
```

This is the beginning of **data modeling** - thinking about how information connects and interacts.

---

### 7. Key Takeaways

- Data structures are how you organize information inside your program.  
- Lists are ordered collections.  
- Dictionaries store named data.  
- Tuples hold fixed data.  
- Sets store unique values.  
- Real-world apps combine these in creative ways to solve problems.

