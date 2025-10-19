[← Back to Home](../README.md)

# 9B - Databases and Hosting

Databases store structured data so your app can remember things between runs.  
Hosting connects that database to your deployed code.

---

### 1. Common Database Types

| Type | Description | Examples |
|------|--------------|-----------|
| **Relational** | Tables, rows, columns | SQLite, PostgreSQL, MySQL |
| **NoSQL** | Flexible, key-value or document-based | MongoDB, Firebase |
| **In-Memory** | Temporary, fast lookups | Redis |

---

### 2. Local Database Example (SQLite)

```python
import sqlite3

conn = sqlite3.connect("app.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER, name TEXT)")
cursor.execute("INSERT INTO users VALUES (1, 'Zach')")
conn.commit()

for row in cursor.execute("SELECT * FROM users"):
    print(row)

conn.close()
```

---

### 3. Cloud Databases

You can host your DB on:
- **Supabase / Firebase** → simple and managed  
- **PostgreSQL / MySQL** → standard for most production apps  
- **MongoDB Atlas** → flexible JSON-style data

---

### 4. Connecting From Deployed Apps

```python
import os, psycopg2

conn = psycopg2.connect(os.getenv("DATABASE_URL"))
```

Use environment variables for credentials.

---

### 5. Key Takeaways
- Start with SQLite, then move to hosted DBs.  
- Always separate logic from credentials.  
- Back up regularly.
