[← Back to Home](../README.md)

# 3E - Working With Files and Data

Up to this point, your programs have only lived in memory - everything disappears once they stop running.  
Now, it’s time to make them **remember** by learning how to work with **files and external data**.

This ability turns small scripts into real tools that store progress, preferences, and history.

---

### 1. Why Files Matter

Every real application needs a way to store information:
- A to-do app saves tasks between sessions.
- A music app stores playlists and history.
- A website saves user accounts or preferences.

In programming, we do this by **reading and writing files** - text, JSON, CSV, or more complex formats.

---

### 2. Reading and Writing Files

**Reading** a file means opening it, pulling its contents into memory, and using it.  
**Writing** means creating or updating a file on disk.

```python
# Writing text to a file
with open("notes.txt", "w") as file:
    file.write("Keep learning Python every day!")

# Reading it back
with open("notes.txt", "r") as file:
    content = file.read()
    print(content)
```

- `"w"` = write (overwrites existing file)  
- `"a"` = append (adds to existing file)  
- `"r"` = read  

Always close files or use the `with` keyword (which closes automatically).

---

### 3. Storing Structured Data with JSON

When data gets more complex, plain text isn’t enough.  
**JSON (JavaScript Object Notation)** is a universal format for storing and sharing structured data.

**Example**
```python
import json

tasks = [
    {"title": "Write handbook", "done": False},
    {"title": "Push repo", "done": True}
]

# Save to file
with open("tasks.json", "w") as f:
    json.dump(tasks, f, indent=2)

# Load it later
with open("tasks.json", "r") as f:
    loaded_tasks = json.load(f)

print(loaded_tasks)
```

JSON is lightweight, readable, and supported in every major programming language.  
It’s how most APIs communicate.

---

### 4. Working With CSV Files

CSV (Comma-Separated Values) is the simplest format for tabular data - like spreadsheets or reports.

```python
import csv

# Writing
with open("scores.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Score"])
    writer.writerow(["Zach", 95])
    writer.writerow(["Maya", 88])

# Reading
with open("scores.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
```

This format is great for exporting or analyzing data.

---

### 5. File Paths and Folders

When working with files, always know **where** your program is saving them.

```python
import os

print(os.getcwd())  # current working directory
os.makedirs("data", exist_ok=True)

with open("data/info.txt", "w") as f:
    f.write("This is stored in a subfolder.")
```

Using absolute paths (`/home/user/...`) vs relative paths (`./data/...`) matters - especially when deploying your code.

---

### 6. Real-World Example: Simple Log Writer

Let’s combine logic, functions, and file storage.

```python
from datetime import datetime

def log_event(message):
    with open("activity.log", "a") as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] {message}\n")

log_event("Program started")
log_event("User logged in")
```

Now your program keeps a permanent record of events - a simple foundation for analytics or debugging tools.

---

### 7. Key Takeaways
- Files give programs memory.  
- Use `open()` to read/write text.  
- JSON is perfect for structured data.  
- CSV is great for spreadsheets or lists.  
- Always manage file paths carefully.  
- Once you can save data, your programs can grow into full apps.


