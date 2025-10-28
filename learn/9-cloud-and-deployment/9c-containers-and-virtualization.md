[← Back to Home](../README.md)

# 9C - Containers and Virtualization

Containers let you package your app and its dependencies into a **single portable unit**.  
They solve the classic problem: *“It works on my machine.”*

---

### 1. What Is a Container?

A container bundles:
- Code  
- Dependencies  
- Environment settings  

They run the same way on any system.

---

### 2. Docker Example

Create a file named `Dockerfile`:

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "main.py"]
```

Then build and run it:

```bash
docker build -t myapp .
docker run -p 8000:8000 myapp
```

---

### 3. Benefits
- Consistency between environments  
- Easy deployment to any cloud  
- Lightweight compared to full virtual machines

---

### 4. Key Takeaways
- Containers = portable environments.  
- Docker is the standard tool.  
- Learn the basics before moving to Kubernetes.
