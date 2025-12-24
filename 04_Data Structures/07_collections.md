# Python `collections`

The `collections` module provides **specialized container data structures** that extend and optimize the built-in ones (`list`, `dict`, `set`).

---

## Why `collections` Exists

Built-in data structures are powerful, but common patterns appear again and again:

* counting items
* grouping values
* queue-like behavior
* default values for missing keys

The `collections` module provides **ready-made, optimized solutions** for these patterns.

---

## Most Important `collections` Types

We will focus on the **industry-critical** ones:

1. `Counter`
2. `defaultdict`
3. `deque`
4. `namedtuple` (conceptual)

---

# Counter

## What is `Counter`?

`Counter` is a specialized dictionary for **counting hashable objects**.

Instead of manually managing counts, `Counter` does it automatically.

```python
from collections import Counter
```

---

## Basic Example

```python
from collections import Counter

items = ["a", "b", "a", "c", "b", "a"]
counts = Counter(items)
print(counts)
```

Output:

```
Counter({'a': 3, 'b': 2, 'c': 1})
```

---

## Manual Counting vs Counter

### Manual approach

```python
counts = {}
for item in items:
    counts[item] = counts.get(item, 0) + 1
```

### Counter approach

```python
counts = Counter(items)
```

Cleaner, safer, and faster.

---

## Common Counter Operations

### Most common elements

```python
counts.most_common(2)
```

### Update counts

```python
counts.update(["a", "b"])
```

### Counter arithmetic

```python
c1 = Counter(a=3, b=1)
c2 = Counter(a=1, b=2)

c1 + c2
```

---

## When to Use Counter

* word frequency
* event counting
* log analysis
* data summaries

---

# defaultdict — Dictionaries with Defaults

## What is `defaultdict`?

A `defaultdict` automatically provides a **default value** for missing keys.

```python
from collections import defaultdict
```

---

## Why `defaultdict` Matters

Avoids repetitive `if key not in dict` checks.

---

## Example: Grouping Values (Very Common)

### Without defaultdict

```python
groups = {}
for key, value in pairs:
    if key not in groups:
        groups[key] = []
    groups[key].append(value)
```

### With defaultdict

```python
groups = defaultdict(list)
for key, value in pairs:
    groups[key].append(value)
```

Much cleaner.

---

## Common Default Factories

```python
defaultdict(list)
defaultdict(int)
defaultdict(set)
```

Example:

```python
counts = defaultdict(int)
counts["a"] += 1
```

---

## When to Use defaultdict

* grouping data
* counting
* building nested structures

---

# deque — Double-Ended Queue

## What is `deque`?

A `deque` (double-ended queue) is optimized for **fast appends and pops from both ends**.

```python
from collections import deque
```

---

## Why Not Just Use a List?

List performance:

* append/pop at end → fast
* insert/pop at start → slow (O(n))

Deque performance:

* append/pop at both ends → O(1)

---

## Basic deque Usage

```python
from collections import deque

q = deque()
q.append(1)
q.appendleft(0)
q.pop()
q.popleft()
```

---

## Common deque Use Cases

* queues
* sliding window problems
* BFS algorithms
* task scheduling

---

## deque with maxlen

```python
q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
q.append(4)
print(q)
```

Oldest elements are automatically discarded.

---

# namedtuple — Lightweight Data Objects

## What is `namedtuple`?

`namedtuple` creates tuple-like objects with **named fields**.

```python
from collections import namedtuple
```

---

## Example

```python
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
p = Point(10, 20)
print(p.x, p.y)
```

---

## Why namedtuple Exists

* more readable than plain tuples
* immutable
* lightweight alternative to classes

---

## When to Use namedtuple

* fixed data records
* simple structured data
* performance-sensitive code

---

## Comparison Summary

| Tool        | Use Case                    |
| ----------- | --------------------------- |
| Counter     | frequency counting          |
| defaultdict | auto-initialize dict values |
| deque       | fast queue/stack            |
| namedtuple  | lightweight structured data |

---

## Notes to Self

* Prefer `Counter` over manual counting
* Prefer `defaultdict` for grouping
* Prefer `deque` for queue behavior
* Use `namedtuple` for simple immutable records
