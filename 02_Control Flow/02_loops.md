# Loops in Python

Loops are essential for automation, iteration over data, and performing repetitive tasks efficiently.

---

## 1. For Loop

Iterates over a **sequence** (list, tuple, string, range) and executes the block for each item.

Syntax:

```python
for variable in sequence:
    # code block
```

Example:

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

Using `range()`:

```python
for i in range(5):  # 0 to 4
    print(i)
```

Notes:

* `range(start, stop, step)` generates a sequence of numbers
* For loops are commonly used when the number of iterations is **known or fixed**

---

## 2. While Loop

Repeats the block as long as a **condition is True**.

Syntax:

```python
while condition:
    # code block
```

Example:

```python
count = 0
while count < 5:
    print(count)
    count += 1
```

Notes:

* Ensure the condition eventually becomes False to avoid **infinite loops**
* While loops are commonly used when the number of iterations is **unknown or depends on a condition**

---

## 3. Break and Continue

### Break

Exits the loop immediately.

Example:

```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

### Continue

Skips the current iteration and moves to the next.

Example:

```python
for i in range(5):
    if i == 3:
        continue
    print(i)
```

Notes:

* Use `break` and `continue` sparingly for clarity
* Useful for controlling loops without complex conditions

---

## 4. Nested Loops

You can place **loops inside loops** for multi-dimensional iteration.

Example:

```python
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")
```

Notes:

* Be cautious: nested loops can increase complexity and execution time
* Useful for working with grids, matrices, or combinations

---

## 5. Notes to Self

* Choose `for` when iterating over sequences or known range
* Choose `while` when looping depends on a condition
* Always ensure loops terminate
* Avoid deep nesting where possible
* `break` and `continue` can simplify some loop logic
