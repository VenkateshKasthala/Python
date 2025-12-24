# Sets in Python

---

## What is a Set?

A set is an **unordered, mutable collection of unique elements**.

Key properties:

* **Unordered** → no guaranteed position or index
* **Unique elements** → duplicates are automatically removed
* **Mutable** → elements can be added or removed

```python
nums = {1, 2, 3}
```

---

## Why Sets Matter

Sets excel at:

* removing duplicates
* fast membership checks
* mathematical set operations (union, intersection, difference)

In industry code, sets are commonly used for **validation, filtering, and deduplication**.

---

## Creating Sets

```python
empty = set()        # NOT {}
values = {1, 2, 3}
```

Why `{}` is not a set:

* `{}` creates an empty dictionary
* `set()` creates an empty set

---

## Automatic Deduplication

```python
nums = {1, 2, 2, 3, 3}
print(nums)  # {1, 2, 3}
```

This property makes sets ideal for removing duplicates.

---

## Accessing Elements

Sets do **not** support indexing or slicing.

```python
# nums[0]  ❌ TypeError
```

You iterate over sets instead:

```python
for n in nums:
    print(n)
```

---

## Adding Elements

```python
nums.add(4)
nums.update([5, 6])
```

* `add()` → adds one element
* `update()` → adds multiple elements

---

## Removing Elements

```python
nums.remove(3)    # KeyError if not found
nums.discard(10)  # no error if not found
nums.pop()        # removes arbitrary element
```

Choose `discard` when safety matters.

---

## Membership Testing (VERY IMPORTANT)

Set membership is **extremely fast**.

```python
if 3 in nums:
    print("Found")
```

Time complexity:

* Set lookup → **O(1)** average
* List lookup → **O(n)**

This is one of the biggest reasons to use sets.

---

## Set Operations (Core Strength)

### Union (combine elements)

```python
a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)
```

---

### Intersection (common elements)

```python
print(a & b)
```

---

### Difference (elements in a but not b)

```python
print(a - b)
```

---

### Symmetric Difference (in either, not both)

```python
print(a ^ b)
```

---

## Set Methods

```python
a.union(b)
a.intersection(b)
a.difference(b)
a.symmetric_difference(b)
```

These are equivalent to operators.

---

## Sets and Functions

Sets can be passed to functions like lists.

```python
def unique_items(items):
    return set(items)
```

---

## Frozen Sets (Immutable Sets)

A `frozenset` is an **immutable set**.

```python
fs = frozenset([1, 2, 3])
```

Why this matters:

* can be used as dictionary keys
* safe from modification

---

## Common Use Cases (Real World)

### Remove duplicates from a list

```python
unique = list(set([1, 2, 2, 3]))
```

---

### Fast validation

```python
allowed = {"read", "write", "execute"}
if action in allowed:
    pass
```

---

### Find common items

```python
common_users = set(group_a) & set(group_b)
```

---

## Common Mistakes

* Expecting order in sets
* Using sets when duplicates matter
* Trying to index a set

---

## Performance Notes (High Level)

* Membership check → O(1)
* Add/remove → O(1) average
* No indexing

---

## Conclusion

* Use sets for uniqueness
* Convert to list if order is needed
* sets are used heavily for validation and filtering
* preferred over lists for membership checks
* frozen sets used when immutability is required
