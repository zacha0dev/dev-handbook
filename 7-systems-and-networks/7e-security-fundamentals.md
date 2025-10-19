[← Back to Home](../README.md)

# 7E - Security Fundamentals

Security is **non-optional** in modern software.  
Every program that handles data needs protection against misuse.

---

### 1. The Three Pillars

| Concept | Meaning |
|----------|----------|
| **Confidentiality** | Keep data secret (encryption) |
| **Integrity** | Prevent tampering |
| **Availability** | Ensure systems stay accessible |

---

### 2. Encryption Basics

Encryption turns readable data into unreadable text using a **key**.

```python
from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)

token = f.encrypt(b"secret message")
print(token)

print(f.decrypt(token))
```

---

### 3. Hashing

Hashes convert data into fixed-length codes.  
Used for passwords, file verification, etc.

```python
import hashlib

password = "mypassword".encode()
print(hashlib.sha256(password).hexdigest())
```

---

### 4. Authentication vs Authorization

| Term | Meaning |
|------|----------|
| **Authentication** | Who are you? |
| **Authorization** | What are you allowed to do? |

Example: logging in (authN) vs accessing admin panel (authZ).

---

### 5. Security in Practice
- Use HTTPS (encrypted HTTP).  
- Don’t store plain passwords.  
- Validate user input.  
- Keep API keys secret.  
- Update dependencies regularly.

---

### 6. Key Takeaways
- Security = trust.  
- Always validate, encrypt, and verify.  
- Small habits prevent big breaches.
