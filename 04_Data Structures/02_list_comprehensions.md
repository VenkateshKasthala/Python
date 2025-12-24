# List Comprehensions in Python

List comprehensions are a concise way to build lists. They are powerful, but should be used only when they remain readable.

---

## What is a List Comprehension?

A list comprehension creates a new list from an iterable in a single expression.

General form:

```python
[expression for item in iterable]
```

Example:

```python
nums = [1, 2, 3, 4]
squares = [x * x for x in nums]
```

Equivalent loop:

```python
squares = []
for x in nums:
    squares.append(x * x)
```

---

## Why List Comprehensions Matter

They help you write code that is:

* concise
* expressive
* often faster than manual loops (in CPython, in many cases)

But the main benefit is **clarity when used correctly**.

---

## 1. Basic Transformation

```python
names = ["alice", "bob", "charlie"]
upper_names = [name.upper() for name in names]
```

---

## 2. Filtering with an `if`

Keep only items that satisfy a condition:

```python
nums = [1, 2, 3, 4, 5, 6]
evens = [x for x in nums if x % 2 == 0]
```

Equivalent loop:

```python
evens = []
for x in nums:
    if x % 2 == 0:
        evens.append(x)
```

---

## 3. Transform + Filter Together

```python
nums = [1, 2, 3, 4, 5, 6]
result = [x * x for x in nums if x % 2 == 0]
# squares of even numbers
```

---

## 4. Conditional Expression inside a Comprehension

This changes the value based on a condition.

```python
nums = [-2, -1, 0, 1, 2]
labels = ["pos" if x > 0 else "non-pos" for x in nums]
```

Important:

* This is different from filtering
* Filtering decides **whether to include an item**
* Conditional expression decides **what value to include**

---

## 5. Nested List Comprehensions (Use Carefully)

### Flatten a 2D list

```python
matrix = [[1, 2, 3], [4, 5, 6]]
flat = [x for row in matrix for x in row]
```

Equivalent loop:

```python
flat = []
for row in matrix:
    for x in row:
        flat.append(x)
```

Guideline:

* nested comprehensions are okay if they stay readable
* if it takes effort to parse, prefer loops

---

## 6. Common Patterns You’ll See in Industry

### Strip and clean strings

```python
raw = ["  a ", " b", "c  "]
clean = [s.strip() for s in raw]
```

### Parse and filter

```python
values = ["1", "2", "x", "3"]
nums = [int(v) for v in values if v.isdigit()]
```

### Build pairs using `enumerate`

```python
items = ["a", "b", "c"]
pairs = [(i, v) for i, v in enumerate(items)]
```

---

## 7. When NOT to Use List Comprehensions

Avoid comprehensions when:

* the logic needs multiple steps
* you need try/except
* you need complex nested conditions
* readability suffers

In such cases, use a normal loop.

---

## 8. Industry Preference

Many codebases prefer comprehensions for simple transformations and filters.

However, industry-level Python values:

> **Readable code over short code**

A good rule:

* If it fits on one line and reads naturally, use a comprehension
* If you need multiple lines or comments, use a loop

---

## Conclusion

* Comprehensions are best for simple transform/filter
* Don’t force everything into a one-liner
* Use loops when logic becomes multi-step
* Keep code readable for future me
