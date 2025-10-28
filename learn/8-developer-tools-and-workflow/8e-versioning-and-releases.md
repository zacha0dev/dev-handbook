[← Back to Home](../README.md)

# 8E - Versioning and Releases

Versioning lets you **track progress and maintain compatibility** over time.  
It’s how software evolves in a predictable way.

---

### 1. Semantic Versioning (SemVer)

Format: **MAJOR.MINOR.PATCH**

| Example | Meaning |
|----------|----------|
| **1.0.0** | First stable release |
| **1.1.0** | Adds features, no breaking changes |
| **1.1.1** | Bug fix only |
| **2.0.0** | Breaking change |

---

### 2. Git Tags

Tagging versions helps track releases in Git.

```bash
git tag v1.0.0
git push origin v1.0.0
```

---

### 3. Creating a Release Package

Example: building and publishing a Python package.

```bash
python setup.py sdist bdist_wheel
twine upload dist/*
```

---

### 4. Changelogs

Document what changed and why.

```
## [1.2.0] - 2025-10-10
### Added
- User authentication feature

### Fixed
- Minor UI bug on dashboard
```

---

### 5. Key Takeaways
- Follow SemVer for clear versioning.  
- Tag releases in Git.  
- Keep changelogs transparent and simple.
