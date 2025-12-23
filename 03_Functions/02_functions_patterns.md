# Functions in Python — Patterns and Variations

---

## 1. Default Arguments

Default arguments allow a function parameter to have a **predefined value** if no argument is passed.

```python
def greet(name, message="Hello"):
    return f"{message}, {name}!"

print(greet("Alice"))
print(greet("Bob", "Hi"))
```

Explanation:

* `message` has a default value
* If not provided, Python uses the default

### Important rule

Default arguments are evaluated **once**, at function definition time.
Avoid using mutable defaults (like lists or dicts).

Bad example:

```python
def add_item(item, items=[]):
    items.append(item)
    return items
```

Correct approach:

```python
def add_item(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

---

## 2. Keyword Arguments

Keyword arguments allow passing values by **parameter name**, improving clarity.

```python
def calculate_price(price, tax, discount):
    return price + tax - discount

calculate_price(price=100, tax=10, discount=5)
```

Benefits:

* Improves readability
* Avoids positional mistakes
* Order does not matter

---

## 3. Positional vs Keyword Arguments

```python
def example(a, b, c):
    return a + b + c

example(1, 2, 3)              # positional
example(a=1, b=2, c=3)        # keyword
example(1, b=2, c=3)          # mixed (valid)
```

Rule:

* Positional arguments must come **before** keyword arguments

---

## 4. Variable-Length Arguments (`*args`)

`*args` allows a function to accept **any number of positional arguments**.

```python
def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total

sum_all(1, 2, 3, 4)
```

Notes:

* `args` is a tuple
* Name `args` is a convention

---

## 5. Keyword Variable-Length Arguments (`**kwargs`)

`**kwargs` allows a function to accept **any number of keyword arguments**.

```python
def user_profile(**kwargs):
    return kwargs

user_profile(name="Alice", age=30, city="NY")
```

Notes:

* `kwargs` is a dictionary
* Useful for flexible APIs

---

## 6. Combining Arguments

```python
def demo(a, b, *args, **kwargs):
    return a, b, args, kwargs

demo(1, 2, 3, 4, x=10, y=20)
```

Order matters:

1. positional
2. `*args`
3. keyword-only
4. `**kwargs`

---

## 7. Returning Multiple Values

Python allows returning multiple values as a tuple.

```python
def operations(a, b):
    return a + b, a - b, a * b

add, sub, mul = operations(5, 3)
```

This is commonly used in industry code.

---

## 8. Docstrings (Industry Standard)

Docstrings document what a function does.

```python
def calculate_area(radius):
    """Calculate area of a circle."""
    return 3.14 * radius * radius
```

Benefits:

* Improves readability
* Enables documentation tools
* Helps IDEs show help text

---

## 9. Functions Calling Other Functions

```python
def square(n):
    return n * n

def sum_of_squares(a, b):
    return square(a) + square(b)
```

This pattern builds complex logic from small functions.

---

## Conclusion

* Use default arguments carefully
* Prefer keyword arguments for clarity
* Use `*args` and `**kwargs` for flexibility
* Return values, do not print
* Write small, focused functions
* Add docstrings for clarity
* Functions are flexible and reusable
* APIs rely heavily on `*args` and `**kwargs`
* Docstrings are expected
