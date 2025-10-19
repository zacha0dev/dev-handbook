[← Back to Home](../README.md)

# 7D - Sockets and Real-Time Communication

Sockets are **direct communication channels** between two programs over a network.  
They enable live apps like chats, games, and IoT systems.

---

### 1. How Sockets Work

1. The **server** opens a port and waits.  
2. The **client** connects to that port.  
3. Both can send/receive data in real time.

---

### 2. Python Example - Echo Server

**Server**
```python
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("localhost", 9000))
server.listen(1)
print("Server listening...")

conn, addr = server.accept()
print("Connected by", addr)

while True:
    data = conn.recv(1024)
    if not data:
        break
    conn.sendall(data)

conn.close()
```

**Client**
```python
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 9000))
client.sendall(b"Hello Server!")
print(client.recv(1024))
client.close()
```

---

### 3. WebSockets

For browsers and modern apps, **WebSockets** extend this concept for real-time communication over HTTP.

Used in: chats, live dashboards, multiplayer games.

---

### 4. Key Takeaways
- Sockets = live two-way communication.  
- Great for chat apps, notifications, or sensors.  
- Python’s `socket` library makes testing easy.
