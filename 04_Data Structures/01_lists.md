# Data Structures in Python

---

## What is a Data Structure?

A data structure is a way to **store, organize, and manage data** so it can be used efficiently.

In Python, data structures help answer questions like:

* How do I store multiple values?
* How do I access them?
* How do I modify them?
* How does performance change as data grows?

---

## Why Data Structures Matter

In industry-level code:

* Data is almost always grouped
* Logic operates on collections, not single values
* Performance and readability depend on choosing the right structure

Understanding data structures is **non-negotiable** for real-world Python.

---

## Core Built-in Data Structures in Python

Python provides four primary built-in data structures:

| Data Structure | Ordered    | Mutable | Allows Duplicates |
| -------------- | ---------- | ------- | ----------------- |
| List           | Yes        | Yes     | Yes               |
| Tuple          | Yes        | No      | Yes               |
| Set            | No         | Yes     | No                |
| Dictionary     | Yes (3.7+) | Yes     | Keys: No          |

We will cover each one in depth.

---

# Lists — The Workhorse of Python

## What is a List?

A list is an **ordered, mutable collection** of elements.

* Ordered → elements maintain position
* Mutable → elements can be changed
* Allows duplicates

```python
numbers = [1, 2, 3, 4]
names = ["Alice", "Bob", "Alice"]
```

---

## Creating Lists

```python
empty = []
nums = [1, 2, 3]
mixed = [1, "two", 3.0, True]
```

Lists can store **any data type**, including other lists.

```python
matrix = [[1, 2], [3, 4]]
```

---

## Accessing Elements (Indexing)

Lists use **zero-based indexing**.

```python
nums = [10, 20, 30]
print(nums[0])   # 10
print(nums[-1])  # 30
```

Negative indexing counts from the end.

---

## Slicing Lists

Slicing extracts a portion of a list.

```python
nums = [0, 1, 2, 3, 4]
print(nums[1:4])  # [1, 2, 3]
print(nums[:3])   # [0, 1, 2]
print(nums[::2])  # [0, 2, 4]
```

Slicing returns a **new list**.

---

## Modifying Lists (Mutability)

Lists can be changed after creation.

```python
nums = [1, 2, 3]
nums[1] = 20
print(nums)
```

This mutability is powerful but must be handled carefully.

---

## Common List Operations

### Adding Elements

```python
nums.append(4)
nums.extend([5, 6])
nums.insert(1, 10)
```

* `append` → adds one element
* `extend` → adds multiple elements
* `insert` → adds at a specific index

---

### Removing Elements

```python
nums.remove(10)
popped = nums.pop()
del nums[0]
```

* `remove` → removes by value
* `pop` → removes by index (returns value)
* `del` → deletes by index or slice

---

## Looping Through Lists

```python
for num in nums:
    print(num)
```

With index:

```python
for index, value in enumerate(nums):
    print(index, value)
```

---

## Checking Membership

```python
if 3 in nums:
    print("Found")
```

---

## List Length

```python
len(nums)
```

---

## Lists and Functions

Lists are passed to functions by **object reference**.

```python
def add_item(lst, item):
    lst.append(item)

items = []
add_item(items, "apple")
print(items)
```

This modifies the original list.

---

## Copying Lists

```python
a = [1, 2, 3]
b = a          # same reference
c = a.copy()   # shallow copy
```

```python
b.append(4)
print(a)  # also changed
```

Always copy lists when needed.

---

## Common List Pitfalls

* Modifying a list while iterating
* Unexpected shared references
* Overusing lists when a dict or set is better

---

## Performance Notes (High Level)

* Access by index → O(1)
* Append → O(1) amortized
* Insert/delete in middle → O(n)

---

## Conclusion

* Lists are mutable and powerful
* Copy lists intentionally
* Prefer clear loops over clever tricks
* Understand performance implications

---
