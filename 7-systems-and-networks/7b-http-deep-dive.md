[← Back to Home](../README.md)

# 7B - HTTP Deep Dive

HTTP (HyperText Transfer Protocol) is the **language of the web**.  
Every website, API, and browser uses it to communicate.

---

### 1. The Request–Response Model

When your program asks for something online, it sends an HTTP **request**.  
The server replies with an HTTP **response**.

```
Client → Request → Server → Response → Client
```

---

### 2. Structure of a Request

| Part | Example | Description |
|------|----------|-------------|
| **Method** | `GET`, `POST`, `PUT`, `DELETE` | Action to perform |
| **URL** | `/users/123` | Resource location |
| **Headers** | `Authorization: Bearer TOKEN` | Metadata |
| **Body** | JSON or form data | Actual data being sent |

**Example (Python using `requests`)**
```python
import requests
res = requests.get("https://api.github.com/users/octocat")
print(res.status_code)
print(res.headers["content-type"])
print(res.json())
```

---

### 3. Common HTTP Methods

| Method | Use Case |
|---------|-----------|
| **GET** | Retrieve data |
| **POST** | Create data |
| **PUT** | Update data |
| **DELETE** | Remove data |
| **PATCH** | Partial update |

---

### 4. Status Codes

| Code | Meaning |
|------|----------|
| **200** | OK |
| **201** | Created |
| **400** | Bad Request |
| **401** | Unauthorized |
| **404** | Not Found |
| **500** | Server Error |

---

### 5. Key Takeaways
- HTTP runs on TCP ports 80 and 443.  
- Every web request is a **message**.  
- Mastering HTTP helps you debug and integrate APIs easily.
