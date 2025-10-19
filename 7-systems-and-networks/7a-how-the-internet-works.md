[← Back to Home](../README.md)

# 7A - How the Internet Works

The Internet connects billions of computers so they can share information.  
To understand web apps and APIs, you need to know **how data travels**.

---

### 1. The Basic Flow

When you visit a website like `https://example.com`, this happens:

1. **DNS Lookup** - your computer asks a Domain Name Server for the IP address of `example.com`  
2. **Connection** - your browser connects to that IP using TCP or UDP  
3. **Request** - your browser sends an HTTP request (like “GET this page”)  
4. **Response** - the server sends back HTML, JSON, or files  
5. **Render** - your browser displays the result

```text
You → DNS → Server IP → Request → Response → Page
```

---

### 2. IP, TCP, and UDP

| Protocol | Purpose | Reliability |
|-----------|----------|-------------|
| **IP** | Address system for devices | Always used |
| **TCP** | Reliable, ordered delivery | Web pages, APIs |
| **UDP** | Fast, no delivery guarantee | Games, streaming |

---

### 3. Ports and Addresses

Every device has an **IP address**, and every app on that device listens on a **port**.  
For example:
- `80` → HTTP
- `443` → HTTPS
- `22` → SSH

```python
import socket
print(socket.gethostbyname("example.com"))  # Get server IP
```

---

### 4. Key Takeaways
- DNS converts names to IPs.  
- TCP ensures reliable communication.  
- Every web request uses IP + Port + Protocol.  
- The Internet = computers passing structured messages.
