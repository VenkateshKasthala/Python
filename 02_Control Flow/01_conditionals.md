# Conditionals in Python

Conditional statements allow a program to make **decisions** based on conditions.

---

## 1. If Statement

Executes a block of code **only if a condition is True**.

Syntax:

```python
if condition:
    # code block
```

Example:

```python
age = 16
if age < 18:
    print("You are a minor")
```

Notes:

* The code block runs **only** if the condition evaluates to `True`.
* Indentation defines the scope of the block.

---

## 2. If-Else Statement

Provides an alternative block to execute **if the condition is False**.

Syntax:

```python
if condition:
    # code block 1
else:
    # code block 2
```

Example:

```python
age = 20
if age < 18:
    print("Minor")
else:
    print("Adult")
```

---

## 3. Elif Statement

Allows checking **multiple conditions sequentially**.

Syntax:

```python
if condition1:
    # code block 1
elif condition2:
    # code block 2
else:
    # code block 3
```

Example:

```python
age = 70
if age < 18:
    print("Minor")
elif age < 65:
    print("Adult")
else:
    print("Senior")
```

Notes:

* `elif` is short for "else if"
* You can have **any number of `elif` blocks**
* The `else` block is optional

---

## 4. Nested Conditionals

You can place **if statements inside other if statements** for more complex decisions.

Example:

```python
age = 25
is_student = True

if age < 30:
    if is_student:
        print("Young student")
    else:
        print("Young professional")
else:
    print("Adult")
```

Notes:

* Keep nesting shallow to maintain readability
* Complex nested conditions can often be simplified with logical operators

---

## Conclusion

* Conditional statements control the flow of the program
* Indentation is critical in Python
* Prefer readability over complex nested ifs
* Logical operators (`and`, `or`, `not`) can often simplify multiple conditions
