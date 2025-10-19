[← Back to Home](../README.md)

# 9E - CI/CD Pipelines

CI/CD (Continuous Integration / Continuous Deployment) automates testing and delivery.  
It ensures your app ships faster and safer.

---

### 1. CI/CD Overview

| Stage | Goal |
|--------|------|
| **CI (Integration)** | Automatically test code when pushed |
| **CD (Deployment)** | Automatically release new versions |

---

### 2. Example: GitHub Actions

Create `.github/workflows/deploy.yml`:

```yaml
name: CI Pipeline
on:
  push:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - name: Install dependencies
        run: pip install -r requirements.txt
      - name: Run tests
        run: pytest
```

---

### 3. Extending to Deployment

You can add a step to deploy to:
- Heroku (`git push heroku main`)
- Vercel (`vercel --prod`)
- DockerHub or cloud registry

---

### 4. Key Takeaways
- CI/CD automates quality control.  
- Add tests before deploying.  
- Start small — even one GitHub Action helps.
