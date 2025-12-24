# Dictionaries in Python

---

## What is a Dictionary?

A dictionary is a **mapping** of **keys** to **values**.

* Keys must be **unique**
* Values can be anything
* Dictionaries are **mutable**
* Dictionaries preserve insertion order (Python 3.7+ behavior)

Example:

```python
user = {
    "name": "Alice",
    "age": 30,
    "is_active": True
}
```

---

## Why Dictionaries Matter

In real-world and industry Python:

* JSON looks like dictionaries
* configuration files map keys to settings
* APIs return key-value structures
* dictionaries model objects/entities naturally

A dictionary is often the best choice when:

* you need fast lookup by a key
* data is naturally named/structured

---

## Creating Dictionaries

### Literal syntax

```python
empty = {}
user = {"name": "Alice", "age": 30}
```

### Using `dict()`

```python
user = dict(name="Alice", age=30)
```

### From a list of pairs

```python
pairs = [("a", 1), ("b", 2)]
d = dict(pairs)
```

---

## Accessing Values

```python
user = {"name": "Alice", "age": 30}
print(user["name"])  # Alice
```

### Important: KeyError

If a key does not exist:

```python
user["city"]  # KeyError
```

Safer access using `get()`:

```python
print(user.get("city"))          # None
print(user.get("city", "NA"))   # NA
```

---

## Adding and Updating Values

```python
user["city"] = "NY"
user["age"] = 31
```

---

## Removing Keys

```python
user.pop("age")      # removes key and returns its value
user.pop("missing", None)  # safe pop with default

del user["city"]     # deletes key
```

---

## Checking Membership

Membership checks operate on keys:

```python
if "name" in user:
    print("Key exists")
```

To check values, use:

```python
if "Alice" in user.values():
    print("Value exists")
```

---

## Iterating Over Dictionaries (Very Important)

### Iterate over keys (default)

```python
for key in user:
    print(key)
```

### Iterate over values

```python
for value in user.values():
    print(value)
```

### Iterate over key-value pairs

```python
for key, value in user.items():
    print(key, value)
```

Industry pattern: `.items()` is extremely common.

---

## Dictionary Methods You’ll Use Often

* `keys()` → view of keys
* `values()` → view of values
* `items()` → view of (key, value)
* `get()` → safe access
* `update()` → merge/update

Example:

```python
user.update({"age": 32, "country": "USA"})
```

---

## Keys: What can be a key?

Keys must be **hashable** (immutable).

✅ Allowed keys:

* strings
* numbers
* tuples (containing immutable values)
* frozenset

❌ Not allowed:

* lists
* dictionaries
* sets

Example:

```python
locations = {
    (40.7, -74.0): "New York",
    (34.0, -118.2): "Los Angeles"
}
```

---

## Common Patterns in Industry

### 1. Counting frequency (very common)

```python
words = ["a", "b", "a", "c", "b", "a"]
counts = {}

for w in words:
    counts[w] = counts.get(w, 0) + 1
```

---

### 2. Grouping values by key

```python
pairs = [("A", 1), ("B", 2), ("A", 3)]
groups = {}

for k, v in pairs:
    groups.setdefault(k, []).append(v)
```

Notes:

* `setdefault(k, default)` returns existing value or sets a default

---

### 3. Merging dictionaries

```python
a = {"x": 1}
b = {"y": 2}

merged = {**a, **b}
```

If keys overlap, later values win.

---

### 4. Dictionary comprehension

```python
nums = [1, 2, 3]
squares = {x: x*x for x in nums}
```

---

## Mutability, Copying, and Nested Dictionaries

Dictionaries are mutable and passed by reference.

```python
a = {"x": 1}
b = a
b["x"] = 99
print(a)  # also changed
```

Copy safely:

```python
c = a.copy()  # shallow copy
```

For nested dictionaries/lists, shallow copy is not enough.

---

## Performance Notes 

* Lookup by key is **O(1)** average
* Insert is **O(1)** average
* Very efficient for large-scale key-based access

---

## Common Mistakes

* Using unhashable types as keys
* Confusing `in` (checks keys, not values)
* Modifying nested data without copying

---

## Conclusion

* Use dict when you need key-based lookup
* dict is everywhere (JSON, configs, APIs)
* `.get()` and `.items()` are common patterns
* dict comprehensions improve clarity when simple
* understanding hashing and mutability prevents bugs
