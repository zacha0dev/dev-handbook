[← Back to Home](../README.md)

# 9A - Deploying Web Apps

Deployment is how your app leaves your computer and runs for others to use online.  
It’s the final step in bringing software to life.

---

### 1. The Deployment Process

| Step | Description |
|------|--------------|
| **Build** | Package your code and assets |
| **Configure** | Set environment variables, ports, and secrets |
| **Deploy** | Upload to a hosting platform |
| **Run** | App starts serving users |

---

### 2. Common Deployment Options

| Platform | Best For | Example |
|-----------|-----------|----------|
| **Heroku** | Simplicity | `git push heroku main` |
| **Vercel** | Frontend / Serverless APIs | Next.js, React |
| **Render** | Python apps with databases | FastAPI, Flask |
| **Azure / AWS / GCP** | Full cloud control | Enterprise apps |

---

### 3. Example: Deploy a FastAPI App to Render

1. Create `requirements.txt` and `start.sh`  
2. Add a `render.yaml`:

```yaml
services:
  - type: web
    name: myapp
    env: python
    buildCommand: "pip install -r requirements.txt"
    startCommand: "uvicorn main:app --host 0.0.0.0 --port 8000"
```

3. Push to GitHub → connect repo to Render → deploy automatically.

---

### 4. Key Takeaways
- Deployment = build + configure + host.  
- Start small (Heroku, Render).  
- Automate later using CI/CD.
