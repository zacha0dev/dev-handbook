[← Back to Home](../README.md)

# 5A - Time and Space Complexity

Understanding how efficiently your code runs is key to writing better programs.  
**Time complexity** measures *how fast* code runs.  
**Space complexity** measures *how much memory* it uses.

---

### ⏱1. What Is Big O Notation?

Big O notation describes how an algorithm scales as input size grows.  
It ignores exact timing and focuses on growth rate.

| Complexity | Example | Description |
|-------------|----------|-------------|
| **O(1)** | Accessing a list item | Constant time |
| **O(n)** | Looping through items | Linear growth |
| **O(log n)** | Binary search | Grows slowly |
| **O(n²)** | Nested loops | Quadratic growth |

---

### 2. Examples

**O(1) – Constant Time**
```python
nums = [1, 2, 3, 4]
print(nums[0])  # always 1 step
```

**O(n) - Linear**
```python
for n in nums:
    print(n)
```

**O(n²) - Quadratic**
```python
for i in nums:
    for j in nums:
        print(i, j)
```

---

### 3. Space Complexity

Memory usage also matters.  
Each variable and data structure consumes memory.

```python
numbers = [i for i in range(1000)]  # O(n) space
total = sum(numbers)                # O(1) space
```

---

### 4. Key Takeaways
- Big O describes scalability, not speed.  
- Focus on reducing unnecessary loops.  
- Balance readability with efficiency.
