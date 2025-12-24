# Assignment vs Shallow Copy vs Deep Copy
s
---

## 1. Core Rule (Memorize This)

> **Python variables store references, not values.**

Objects live in memory. Variables simply point to those objects.

---

## 2. Definitions (Write These First)

### Assignment

**Assignment means no copy happens.**

Two variables point to the **same object**.

```python
a = [1, 2, 3]
b = a
```

* One object in memory
* Changes through either variable affect the same object

---

### Shallow Copy

A **shallow copy**:

* creates a **new outer container**
* copies **references to inner objects**

Inner objects are **shared**.

Common ways to create a shallow copy:

```python
a.copy()
list(a)
a[:]
dict(a)
```

---

### Deep Copy

A **deep copy**:

* creates a **new outer container**
* recursively copies **all nested objects**

No objects are shared.

```python
import copy
copy.deepcopy(a)
```

---

## 3. Mental Model (Very Important)

Think of containers as **boxes** and elements as **items inside the boxes**.

| Operation    | Outer Box | Inner Items |
| ------------ | --------- | ----------- |
| Assignment   | Same      | Same        |
| Shallow Copy | New       | Same        |
| Deep Copy    | New       | New         |

---

# PART A: REGULAR (FLAT) DATA STRUCTURES

## A1. Assignment (Flat List)

```python
a = [1, 2, 3]
b = a
b.append(4)
```

Result:

```python
a == [1, 2, 3, 4]
b == [1, 2, 3, 4]
```

**Why:**

* Both variables point to the same list

---

## A2. Shallow Copy (Flat List)

```python
a = [1, 2, 3]
b = a.copy()
b.append(4)
```

Result:

```python
a == [1, 2, 3]
b == [1, 2, 3, 4]
```

**Why:**

* New list created
* Elements are immutable (ints)

✅ Shallow copy is sufficient for flat structures.

---

## A3. Deep Copy (Flat List)

```python
import copy
a = [1, 2, 3]
b = copy.deepcopy(a)
b.append(4)
```

Result is the same as shallow copy.

⚠️ Deep copy is unnecessary here.

---

# PART B: NESTED DATA STRUCTURES

## B1. Assignment (Nested List)

```python
a = [[1, 2], [3, 4]]
b = a
b[0].append(99)
```

Result:

```python
a == [[1, 2, 99], [3, 4]]
b == [[1, 2, 99], [3, 4]]
```

**Why:**

* Same outer list
* Same inner lists

❌ Most dangerous case

---

## B2. Shallow Copy (Nested List — Dangerous Case)

```python
a = [[1, 2], [3, 4]]
b = a.copy()
b[0].append(99)
```

Result:

```python
a == [[1, 2, 99], [3, 4]]
b == [[1, 2, 99], [3, 4]]
```

**Why this happens:**

* Outer list is new
* Inner lists are shared
* `b[0].append()` mutates the shared inner list

---

## B3. Shallow Copy (Nested List — Safe Operations)

```python
a = [[1, 2], [3, 4]]
b = a.copy()

b.append([9, 9])   # safe
b[0] = [100, 200]  # safe
```

**Why safe:**

* Only the outer container is modified
* Inner shared objects are not mutated

---

## B4. Deep Copy (Nested List — Correct Isolation)

```python
import copy
a = [[1, 2], [3, 4]]
b = copy.deepcopy(a)
b[0].append(99)
```

Result:

```python
a == [[1, 2], [3, 4]]
b == [[1, 2, 99], [3, 4]]
```

**Why:**

* Outer list is new
* Inner lists are also new
* No shared mutable objects

---

# PART C: DICTIONARIES (SAME RULES)

## C1. Assignment

```python
user = {"roles": ["admin"]}
copy_user = user
copy_user["roles"].append("editor")
```

Both variables change.

---

## C2. Shallow Copy

```python
copy_user = user.copy()
copy_user["roles"].append("editor")
```

Original still changes (shared inner list).

---

## C3. Deep Copy

```python
import copy
safe_user = copy.deepcopy(user)
safe_user["roles"].append("editor")
```

Original remains unchanged.

---

## 4. Debugging Tip (Very Useful)

Use `id()` to check object identity:

```python
print(id(a), id(b))
print(id(a[0]), id(b[0]))
```

Same `id` → same object.

---

## 5. When to Use What (Industry Checklist)

### Use Assignment when:

* you want shared state intentionally

### Use Shallow Copy when:

* data is flat
* nested items are immutable
* performance matters

### Use Deep Copy when:

* nested mutable data exists
* isolation is required
* working with API payloads or configs

---

## Final Take-away(Memorize)

```
Assignment   → same box, same items
Shallow copy → new box, same items
Deep copy    → new box, new items
```

