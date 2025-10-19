[← Back to Home](../README.md)

# 7C - Client–Server Model

All modern apps follow the **client–server model** - one side requests, the other responds.

---

### 1. The Core Concept

| Role | Description |
|------|--------------|
| **Client** | The user-facing app (browser, phone, desktop) |
| **Server** | The machine that processes requests and sends data |

**Example:**
```
Browser → Request → API Server → Database → Response → Browser
```

---

### 2. Python Example - Simple Server

```python
from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Hello from server!")

server = HTTPServer(("localhost", 8080), Handler)
print("Server running on http://localhost:8080")
server.serve_forever()
```

Then open your browser to `http://localhost:8080`.

---

### 3. Python Example - Client

```python
import requests
res = requests.get("http://localhost:8080")
print(res.text)
```

---

### 4. Key Takeaways
- Clients ask, servers respond.  
- Local servers mimic how web servers work.  
- Understanding this model helps build APIs and web apps.
