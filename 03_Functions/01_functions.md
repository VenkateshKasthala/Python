# Functions in Python — Concepts and Basics

---

## What is a Function?

A function is a **named block of code** that performs a specific task.

Instead of writing the same logic again and again, we place it inside a function and reuse it whenever needed.

Conceptually, a function:

* groups related steps together
* can take input (parameters)
* can produce output (return value)

---

## Why Functions Matter (Very Important)

Without functions, programs tend to become:

* long
* repetitive
* hard to read
* difficult to maintain

Functions solve these problems.

### Functions help by:

1. **Avoiding repetition**
   Write logic once, reuse it many times.

2. **Improving readability**
   A well-named function explains *what* the code does.

3. **Making code testable**
   Small functions can be tested independently.

4. **Enabling clean design**
   Industry-level Python code is structured around functions.

Almost all real-world Python logic lives inside functions.

---

## Function Syntax

```python
def function_name(parameters):
    # function body
    return value  # optional
```

Key points:

* `def` keyword defines a function
* parameters are optional
* `return` is optional
* indentation defines the function body

---

## Calling a Function

A function does **nothing** until it is called.

```python
def multiply(a, b):
    return a * b

result = multiply(4, 5)
print(result)
```

---

## Parameters vs Arguments

* **Parameters**: variables listed in the function definition
* **Arguments**: actual values passed during the function call

```python
def add(a, b):   # a, b are parameters
    return a + b

result = add(3, 5)  # 3, 5 are arguments
```

---

## `print()` vs `return()` (CRITICAL SECTION)

This is one of the most important concepts in Python functions.

---

### What `print()` does

* Displays a value to the console
* Intended for **humans**
* Does NOT send data back to the caller

Example:

```python
def add(a, b):
    print(a + b)

result = add(2, 3)
print(result)
```

Output:

```
5
None
```

Explanation:

* `print(a + b)` prints `5`
* the function has **no return statement**
* Python automatically returns `None`
* `result` becomes `None`

---

### What `return` does

* Sends a value back to the caller
* Used by the **program**, not just for display
* Stops function execution immediately

Example:

```python
def add(a, b):
    return a + b

result = add(2, 3)
print(result)
```

Output:

```
5
```

Explanation:

* `return a + b` sends `5` back
* `result` receives the value
* the value can be reused or combined

---

### Key Differences (Side-by-Side)

| `print()`        | `return`             |
| ---------------- | -------------------- |
| Displays output  | Sends value back     |
| For humans       | For program logic    |
| Returns `None`   | Returns actual value |
| Cannot be reused | Can be reused        |

---

### `return` ends function execution

```python
def example():
    print("A")
    return
    print("B")

example()
```

Output:

```
A
```

Anything after `return` is never executed.

---

### Multiple `return` statements

```python
def check_number(n):
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    return "Zero"
```

Only one `return` runs per function call.

---

## When to use `print`

Use `print` when:

* debugging
* learning
* showing final output to the user

Avoid `print` inside core logic.

---

## When to use `return`

Use `return` when:

* a value is needed later
* logic must be reusable
* writing industry-level code
* building functions used by other functions

---

## Common Beginner Mistake

```python
def calculate_total(price):
    print(price * 1.1)
```

This function cannot be reused.

Correct version:

```python
def calculate_total(price):
    return price * 1.1
```

---

##

* Prefer `return` over `print` inside functions
* Functions that only print are usually incomplete
* `print` is for visibility, `return` is for logic
* Clean functions return values

---
