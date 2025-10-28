[← Back to Home](../README.md)

# 5B - Algorithms and Patterns

Algorithms are **step-by-step methods** for solving problems.  
They’re the logic behind every app - sorting, searching, routing, encryption, and more.

---

### 1. Common Algorithm Types

| Type | What It Does | Example |
|------|---------------|----------|
| **Sorting** | Arrange data | Bubble, Merge, Quick sort |
| **Searching** | Find something | Linear, Binary search |
| **Recursion** | Function calls itself | Factorials, Tree traversal |
| **Greedy** | Pick best immediate option | Coin change |
| **Dynamic Programming** | Store results of subproblems | Fibonacci optimization |

---

### 2. Example: Binary Search

Search a sorted list efficiently.

```python
def binary_search(arr, target):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
```

**O(log n)** efficiency - much faster than linear search.

---

### 3. Recursion Example

```python
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)
```

Every recursive call adds to the call stack until it resolves.

---

### 4. Key Takeaways
- Algorithms are reusable logic blueprints.  
- Choose the right one for the problem.  
- Optimize when performance matters.
