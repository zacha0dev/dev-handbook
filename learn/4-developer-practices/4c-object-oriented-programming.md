[← Back to Home](../README.md)

# 4C - Object-Oriented Programming (OOP)

**Object-Oriented Programming** helps model real-world ideas using **classes** and **objects**.  
It’s one of the most powerful ways to structure code.

---

### 1. Classes and Objects

A **class** defines what an object is and what it can do.

```python
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says woof!")

my_dog = Dog("Leia", "Husky")
my_dog.bark()
```

---

### 2. Why Use Classes?

| Concept | Example |
|----------|----------|
| **Encapsulation** | Keep related data + behavior together |
| **Reusability** | One class → many instances |
| **Organization** | Cleaner than long procedural code |

---

### 3. Inheritance

You can extend classes to build specialized versions.

```python
class Animal:
    def speak(self):
        print("Some sound")

class Dog(Animal):
    def speak(self):
        print("Woof!")

Dog().speak()
```

---

### 4. Key Takeaways
- Classes define templates for objects.  
- Objects combine data and functions.  
- Inheritance allows code reuse.  
- OOP makes large systems cleaner.
