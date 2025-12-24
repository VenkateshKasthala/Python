# Tuples in Python

---

## What is a Tuple?

A tuple is an **ordered, immutable collection** of elements.

* Ordered → elements have a fixed position
* Immutable → elements cannot be changed after creation
* Allows duplicate values

```python
point = (10, 20)
names = ("Alice", "Bob", "Alice")
```

---

## Tuple vs List (Core Difference)

| Feature     | List            | Tuple           |
| ----------- | --------------- | --------------- |
| Syntax      | `[]`            | `()`            |
| Mutable     | Yes             | No              |
| Ordered     | Yes             | Yes             |
| Performance | Slightly slower | Slightly faster |
| Use case    | Dynamic data    | Fixed data      |

The key difference is **immutability**.

---

## Creating Tuples

```python
empty = ()
single = (1,)      # comma is required
values = (1, 2, 3)
```

Why the comma matters:

```python
x = (1)    # int
x = (1,)   # tuple
```

---

## Accessing Tuple Elements

```python
coords = (10, 20, 30)
print(coords[0])
print(coords[-1])
```

Tuples support indexing and slicing like lists.

---

## Tuple Immutability (Very Important)

Once created, tuples **cannot be modified**.

```python
coords[0] = 99  # TypeError
```

This immutability provides:

* safety
* predictability
* protection against accidental changes

---

## Tuples and Functions (Extremely Important)

### Returning Multiple Values

Python functions often return multiple values using tuples.

```python
def get_stats(numbers):
    return min(numbers), max(numbers), sum(numbers)

stats = get_stats([1, 2, 3])
```

The return value is a tuple.

---

## Tuple Unpacking

Tuple unpacking assigns tuple elements to variables.

```python
a, b = (10, 20)
```

Used heavily in industry code.

---

### Unpacking in loops

```python
pairs = [(1, "a"), (2, "b")]
for num, letter in pairs:
    print(num, letter)
```

---

### Swapping variables (classic Python idiom)

```python
a, b = 5, 10
b, a = a, b
```

No temporary variable needed.

---

## Nested Tuples

```python
data = ((1, 2), (3, 4))
```

Tuples can contain mutable objects (like lists), but the tuple itself remains immutable.

---

## Tuples as Dictionary Keys

Tuples are **hashable**, so they can be used as dictionary keys.

```python
locations = {
    (40.7, -74.0): "New York",
    (34.0, -118.2): "Los Angeles"
}
```

Lists cannot be used as dictionary keys.

---

## Performance Notes (High Level)

* Tuples use less memory than lists
* Faster iteration in many cases
* Safer for fixed-size data

---

## When to Use Tuples

Use tuples when:

* data should not change
* representing records or coordinates
* returning multiple values from functions
* using values as dictionary keys

Use lists when:

* data needs to change
* elements will be added or removed

---

## Common Tuple Mistakes

* Forgetting the comma in single-element tuples
* Trying to modify tuple values
* Using lists where tuples provide better safety

---

## Conclusion

* Tuples are about immutability and safety
* Prefer tuples for fixed data
* Tuple unpacking is a core Python skill
* Many Python APIs return tuples

---
