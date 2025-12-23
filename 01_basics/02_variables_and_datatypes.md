# Variables and Data Types

## Variables

### What a variable is

A variable is a **name that refers to a value** stored in memory.

In Python, variables are created **when a value is assigned** to a name. There is no separate declaration step.

Example (conceptual):

```python
x = 10
name = "Python"
```

Here:

* `x` refers to the integer value `10`
* `name` refers to the string value `"Python"`

---

### Variable naming rules

* Must start with a letter or underscore (`_`)
* Can contain letters, numbers, and underscores
* Cannot start with a number
* Case-sensitive (`value` and `Value` are different)

Valid examples:

```text
count
_total
user_name
```

Invalid examples:

```text
2count
user-name
```

---

### Python is dynamically typed

Python is **dynamically typed**, which means:

* The type is associated with the **value**, not the variable name
* A variable can refer to different types at different times

Example:

```python
x = 10      # x refers to an int
x = "ten"  # x now refers to a string
```

This makes Python flexible, but it also means developers must be careful and write clear code.

---

## Data Types

### What a data type is

A data type defines:

* what kind of value is stored
* what operations can be performed on it

Python has several built-in data types. These notes focus on the most common ones.

---

### Common built-in data types

#### Integer (`int`)

Whole numbers without decimals.

```python
a = 10
b = -3
```

#### Float (`float`)

Numbers with decimal points.

```python
pi = 3.14
```

#### String (`str`)

Textual data enclosed in quotes.

```python
name = "Python"
```

#### Boolean (`bool`)

Represents truth values.

```python
is_active = True
is_valid = False
```

#### None (`NoneType`)

Represents the absence of a value.

```python
result = None
```

---

### Checking data types

The built-in `type()` function can be used to check the type of a value.

Example:

```python
type(10)        # int
type(3.14)      # float
type("hello")  # str
type(True)      # bool
```

---

## Notes on mutability (high-level)

Some data types can be modified after creation, while others cannot.

At a high level:

* `int`, `float`, `str`, `bool` are **immutable**
