# Lambda, map, filter, and reduce — In Depth

This document explains **`lambda`**, **`map`**, **`filter`**, and **`reduce`** from first principles and then connects them to **real-world and industry usage**.

These tools come from the *functional programming* style in Python. They are powerful, but must be used carefully to maintain readability.

---

## 1. Lambda Functions

### What is a lambda?

A `lambda` is a **small, anonymous function** written in a single line.

Syntax:

```python
lambda arguments: expression
```

Key characteristics:

* No function name
* Single expression only
* Expression result is automatically returned
* Cannot contain statements (loops, assignments, try/except)

---

### Lambda vs normal function

Normal function:

```python
def square(x):
    return x * x
```

Lambda equivalent:

```python
square = lambda x: x * x
```

Both do the same thing.

---

### When lambda makes sense

Use `lambda` when:

* the logic is very small
* the function is used only once
* it improves readability

Avoid `lambda` when:

* logic is complex
* conditions are nested
* readability suffers

> Industry rule: **Readability > cleverness**

---

## 2. map() — Transforming Data

### What `map()` does

`map()` applies a function to **every element** in an iterable.

Syntax:

```python
map(function, iterable)
```

---

### Basic example

```python
numbers = [1, 2, 3, 4]

result = map(lambda x: x * x, numbers)
print(list(result))
```

Output:

```
[1, 4, 9, 16]
```

---

### Mental model

```
Input data  ->  Function  ->  Output data
[1,2,3,4]      x*x           [1,4,9,16]
```

---

### map() with multiple iterables

```python
a = [1, 2, 3]
b = [4, 5, 6]

result = map(lambda x, y: x + y, a, b)
print(list(result))
```

---

### Important note

* `map()` returns an **iterator**, not a list
* Results are computed lazily

---

## 3. filter() — Selecting Data

### What `filter()` does

`filter()` keeps only elements for which the function returns `True`.

Syntax:

```python
filter(function, iterable)
```

---

### Example

```python
numbers = [1, 2, 3, 4, 5, 6]

result = filter(lambda x: x % 2 == 0, numbers)
print(list(result))
```

Output:

```
[2, 4, 6]
```

---

### Mental model

```
Input data  ->  Condition  ->  Output data
[1,2,3,4]      x % 2 == 0     [2,4]
```

---

## 4. reduce() — Aggregating Data

### What is reduce?

`reduce()` repeatedly applies a function to **accumulate** values into a single result.

Unlike `map` and `filter`, `reduce` is not built-in and must be imported.

```python
from functools import reduce
```

---

### Syntax

```python
reduce(function, iterable[, initializer])
```

---

### Basic example (sum of numbers)

```python
from functools import reduce

numbers = [1, 2, 3, 4]

result = reduce(lambda a, b: a + b, numbers)
print(result)
```

How it works step-by-step:

```
((1 + 2) + 3) + 4 = 10
```

---

### reduce with initializer

```python
from functools import reduce

numbers = [1, 2, 3]

result = reduce(lambda a, b: a + b, numbers, 10)
print(result)
```

Explanation:

* initial value = 10
* computation starts as: `10 + 1`

---

### Common reduce use cases

* sum of values
* product of values
* merging dictionaries
* aggregations

Example (product):

```python
from functools import reduce

numbers = [1, 2, 3, 4]
product = reduce(lambda a, b: a * b, numbers)
```

---

## 5. Combining map, filter, and reduce

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]

result = reduce(
    lambda a, b: a + b,
    map(lambda x: x * x, filter(lambda x: x % 2 == 0, numbers))
)

print(result)
```

Meaning:

1. filter even numbers
2. square them
3. sum the result

---

## 6. Industry Reality (Very Important)

In professional Python code:

* `map`, `filter`, `reduce` are **used sparingly**
* List comprehensions are often preferred for clarity

Example using list comprehension:

```python
result = sum(x * x for x in numbers if x % 2 == 0)
```

This is often more readable than chained functional calls.

---

## 7. Comparison Summary

| Tool   | Purpose                |
| ------ | ---------------------- |
| lambda | inline, small function |
| map    | transform data         |
| filter | select data            |
| reduce | aggregate data         |

---

## Conclusion

* Use lambda only for very small logic
* Prefer readability over clever code
* map = transform
* filter = select
* reduce = aggregate
* Consider list comprehensions as default

---
