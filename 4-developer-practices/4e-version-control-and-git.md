[← Back to Home](../README.md)

# 4E - Version Control and Git

**Version control** lets you save progress, experiment safely, and collaborate.  
Git is the most widely used tool for this.

---

### 1. Initialize and Commit

```bash
git init
git add .
git commit -m "Initial commit"
```

---

### 2. Push to GitHub

```bash
git remote add origin https://github.com/username/repo.git
git branch -M main
git push -u origin main
```

---

### 3. Branching

```bash
git checkout -b feature-login
# make edits
git commit -am "Add login feature"
git checkout main
git merge feature-login
```

---

### 4. Best Practices
- Commit often with clear messages.  
- Use `.gitignore` to exclude `venv/`, `.env`, and cache files.  
- Always pull before pushing.
