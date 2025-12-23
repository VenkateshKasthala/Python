# Recursion in Python

---

## What is Recursion?

Recursion is a technique where a **function calls itself** to solve a problem.

Instead of solving the entire problem at once, recursion breaks the problem into **smaller sub-problems of the same type**.

A recursive solution always has:

1. A **base case** (when to stop)
2. A **recursive case** (the function calling itself)

Without a base case, recursion will never stop.

---

## Why Recursion Exists

Recursion is useful when:

* the problem is naturally hierarchical
* the solution can be expressed in terms of smaller versions of itself
* clarity is more important than raw performance

Common recursive problem domains:

* mathematical definitions (factorial, Fibonacci)
* tree and graph traversal
* divide-and-conquer algorithms

---

## Basic Structure of a Recursive Function

```python
def recursive_function(problem):
    if base_condition:
        return base_result
    return recursive_function(smaller_problem)
```

Think of recursion as:

> "Solve a simpler version of the same problem, until it becomes trivial."

---

## Example 1: Factorial (Classic Example)

Mathematical definition:

```
factorial(n) = n * factorial(n - 1)
factorial(0) = 1
```

Python implementation:

```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
```

Explanation:

* Base case: `n == 0`
* Recursive case: `n * factorial(n - 1)`

---

## Example 2: Fibonacci Sequence

Definition:

```
fib(n) = fib(n-1) + fib(n-2)
fib(0) = 0
fib(1) = 1
```

Implementation:

```python
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
```

Important note:

* This version is **inefficient** for large `n`
* Used mainly for learning recursion

---

## How Recursion Works Internally (Call Stack)

Each recursive call:

* is pushed onto the **call stack**
* waits for the inner call to finish
* resumes execution after the return

Example for `factorial(3)`:

```
factorial(3)
→ 3 * factorial(2)
→ 3 * (2 * factorial(1))
→ 3 * (2 * (1 * factorial(0)))
→ 3 * 2 * 1 * 1
```

Calls unwind in **reverse order**.

---

## Base Case — The Most Important Part

The base case:

* prevents infinite recursion
* defines the simplest problem

Bad recursion (no base case):

```python
def bad(n):
    return bad(n - 1)
```

This will cause a runtime error.

---

## Recursion vs Iteration

Many recursive problems can also be solved using loops.

Example: factorial using a loop

```python
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
```

### Comparison

| Recursion              | Iteration              |
| ---------------------- | ---------------------- |
| Elegant                | Often faster           |
| Uses call stack        | Uses loop variables    |
| Risk of stack overflow | Safer for large inputs |

---

## Python Recursion Limit

Python limits recursion depth to avoid crashing the program.

```python
import sys
sys.getrecursionlimit()
```

Deep recursion can raise:

```
RecursionError: maximum recursion depth exceeded
```

This is why recursion must be used carefully.

---

## Tail Recursion (Important Concept)

Tail recursion occurs when the recursive call is the **last operation** in the function.

Example:

```python
def factorial_tail(n, acc=1):
    if n == 0:
        return acc
    return factorial_tail(n - 1, acc * n)
```

Important note:

* Python does **not** optimize tail recursion
* Still counts toward recursion depth

---

## When to Use Recursion

Use recursion when:

* working with trees or nested structures
* implementing divide-and-conquer algorithms
* clarity is improved compared to loops

Avoid recursion when:

* input size is large
* performance is critical
* iterative solution is clearer

---

## Common Recursion Mistakes

* Missing base case
* Base case never reached
* Incorrect reduction of the problem
* Assuming Python optimizes tail recursion

---

## Recursion and Functions (Big Picture)

Recursion reinforces:

* function calls
* return values
* call stack behavior

Understanding recursion deepens understanding of **functions themselves**.

---

## Conclusion

* Always define the base case first
* Ensure each recursive call moves closer to the base case
* Prefer iteration if recursion hurts readability
* Recursion is a tool, not a default choice

---
