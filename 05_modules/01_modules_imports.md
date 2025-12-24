# Modules and Imports

---

## Module

A module is a single Python file (`.py`) that contains Python code and is loaded and executed once by the interpreter, exposing its contents through a namespace.

This means:

* every `.py` file is a module
* functions, classes, and variables inside the file belong to that module
* Python treats the file as a reusable unit of code

---

## Why modules are needed

If all code lived in one file:

* files would grow uncontrollably
* names would collide easily
* reuse would require copy-pasting
* testing and maintenance would be painful

Modules let us:

* split code by responsibility
* reuse logic across files
* control where names come from

---

## Import statement

An import statement instructs the interpreter to locate a module, execute it if it has not already been executed, and bind the resulting module object or selected attributes to names in the current namespace.

An import does **three things**:

* finds the module
* executes the module
* creates a reference to it

---

## What actually happens during import

When Python encounters:

```python
import math_utils
```

Python:

* searches for `math_utils`
* reads the corresponding file
* executes the file from top to bottom
* creates a module object
* stores it in memory

The execution step is critical.

Importing is not passive loading — it **runs the file**.

---

## Why imports run only once

If the same module is imported again:

```python
import math_utils
import math_utils
```

Python does not execute the file again.

The module object is cached internally, and subsequent imports reuse the same object.

This explains:

* why global state persists
* why side effects happen only once

---

## Accessing module contents

After:

```python
import math_utils
```

Everything inside the module is accessed through its namespace:

```python
math_utils.add(2, 3)
```

This makes it explicit:

* where a name comes from
* which file owns it

---

## Importing specific names

Instead of importing the whole module:

```python
import math_utils
```

I can write:

```python
from math_utils import add
```

Now:

* `add` is bound directly in the current namespace
* the module name is no longer required

This is convenient, but reduces clarity.

---

## Import aliasing

Modules or names can be aliased:

```python
import math_utils as mu
from math_utils import add as add_numbers
```

Aliasing:

* does not create a copy
* simply creates another reference

---

## Namespace

A namespace is a mapping between names and objects used by Python to resolve identifiers during execution.

Modules introduce their own namespaces.

This is why:

* `math_utils.add` and `other_utils.add` can coexist
* name collisions are avoided when using module-qualified access

---

## `from module import *`

This form imports all public names from a module into the current namespace.

Problems with this approach:

* origin of names becomes unclear
* existing names may be overwritten
* debugging becomes difficult

Avoid this in most situations.

---

## Code execution on import

Any top-level code inside a module runs when the module is imported.

Example:

```python
print("loaded")
```

Importing the module will print `loaded`.

This behavior explains:

* unexpected output
* side effects during import

This is controlled later using execution context.

---


