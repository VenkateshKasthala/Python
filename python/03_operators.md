# Operators in Python

Operators are special symbols or keywords that perform operations on values (operands). They are essential for performing calculations, making decisions, and controlling program flow.

---

## 1. Arithmetic Operators

Used to perform mathematical operations.

| Operator | Description         | Example      |
| -------- | ------------------- | ------------ |
| +        | Addition            | 2 + 3 => 5   |
| -        | Subtraction         | 5 - 2 => 3   |
| *        | Multiplication      | 2 * 3 => 6   |
| /        | Division            | 5 / 2 => 2.5 |
| //       | Floor Division      | 5 // 2 => 2  |
| %        | Modulus (remainder) | 5 % 2 => 1   |
| **       | Exponentiation      | 2 ** 3 => 8  |

Example in Python:

```python
a = 10
b = 3

print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.3333
print(a // b)  # 3
print(a % b)   # 1
print(a ** b)  # 1000
```

---

## 2. Comparison Operators

Used to **compare values** and return a boolean (`True`/`False`).

| Operator | Description      | Example        |
| -------- | ---------------- | -------------- |
| ==       | Equal to         | 5 == 5 => True |
| !=       | Not equal to     | 5 != 3 => True |
| >        | Greater than     | 5 > 3 => True  |
| <        | Less than        | 3 < 5 => True  |
| >=       | Greater or equal | 5 >= 5 => True |
| <=       | Less or equal    | 3 <= 5 => True |

Example in Python:

```python
a = 5
b = 3
print(a == b)  # False
print(a != b)  # True
print(a > b)   # True
print(a < b)   # False
print(a >= 5)  # True
print(b <= 5)  # True
```

---

## 3. Logical Operators

Used to combine boolean expressions.

| Operator | Description               | Example                 |
| -------- | ------------------------- | ----------------------- |
| and      | True if both True         | True and False => False |
| or       | True if at least one True | True or False => True   |
| not      | Negation                  | not True => False       |

Example in Python:

```python
a = True
b = False

print(a and b)  # False
print(a or b)   # True
print(not a)    # False
```

---

## 4. Assignment Operators

Used to **assign values** to variables, often in combination with operations.

| Operator | Description             | Example               |
| -------- | ----------------------- | --------------------- |
| =        | Assign                  | x = 5                 |
| +=       | Add and assign          | x += 2 -> x = x + 2   |
| -=       | Subtract and assign     | x -= 2 -> x = x - 2   |
| *=       | Multiply and assign     | x *= 3 -> x = x * 3   |
| /=       | Divide and assign       | x /= 2 -> x = x / 2   |
| %=       | Modulus and assign      | x %= 3 -> x = x % 3   |
| //=      | Floor divide and assign | x //= 2 -> x = x // 2 |
| **=      | Exponent and assign     | x **= 3 -> x = x ** 3 |

Example in Python:

```python
x = 5
x += 3
print(x)  # 8
x *= 2
print(x)  # 16
```

---

