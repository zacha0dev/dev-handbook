[← Back to Home](../README.md)

# 4F - Basic Testing

Testing ensures your code works as expected and stays stable when changed.

---

### 1. Why Test?

Bugs happen - testing catches them early.

---

### 2. Simple Tests with Assert

```python
def add(x, y):
    return x + y

assert add(2, 3) == 5
assert add(-1, 1) == 0
```

If nothing prints, all tests passed.

---

### 3. Unit Tests with `unittest`

```python
import unittest

from math import sqrt

class MathTests(unittest.TestCase):
    def test_square_root(self):
        self.assertEqual(sqrt(9), 3)

if __name__ == "__main__":
    unittest.main()
```

Run it:
```bash
python -m unittest
```

---

### 4. Key Takeaways
- Tests prove your logic works.  
- Use `assert` or `unittest`.  
- Run tests before pushing to GitHub.
