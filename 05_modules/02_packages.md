# Packages and Project Structure (Notes)

A module is a file. A package is about organizing multiple modules so imports stay clean as the project grows.

---

## Package

A package is a directory that groups related modules and enables hierarchical organization of code.

A package exists to answer a practical problem:

* projects grow beyond a few files
* names start colliding
* imports become messy

Packages give structure.

---

## What a package looks like

Example structure:

```text
project/
  app/
    main.py
    utils.py
```

Here:

* `main.py` and `utils.py` are modules
* `app` is a directory that groups them

In modern Python, a directory can be treated as a package depending on how imports are structured.

---

## `__init__.py`

`__init__.py` is a file placed inside a package directory.

It can:

* mark a directory as a package (historically required)
* run package initialization code
* define what is exported when importing from the package

Example:

```text
project/
  app/
    __init__.py
    main.py
    utils.py
```

A key point:

* `__init__.py` is executed when the package is imported

---

## Importing from a package

Given:

```text
project/
  app/
    __init__.py
    utils.py
```

A common import pattern:

```python
from app import utils
utils.some_function()
```

Or import a name inside the module:

```python
from app.utils import some_function
some_function()
```

---

## Absolute imports

An absolute import specifies the full path from the top-level package.

Example:

```python
from app.utils import some_function
```

This style is often the easiest to read because it is explicit.

---

## Relative imports

A relative import specifies location relative to the current module.

Example (inside `app/main.py`):

```python
from .utils import some_function
```

The dot means:

* `.` current package
* `..` parent package

Relative imports are useful inside packages, but can be confusing when running files directly.

---

## Running files directly vs running as a module

A common confusion:

* running `python app/main.py`
* then relative imports break

Because relative imports rely on package context.

Running as a module typically preserves package context:

```bash
python -m app.main
```

Execution context is its own topic, but this is where the import behavior starts showing up.

---

## Project structure that stays sane

A simple pattern that scales:

```text
project/
  app/
    __init__.py
    main.py
    utils.py
  tests/
    test_utils.py
```

Guidelines that prevent headaches:

* keep related modules together
* avoid naming modules the same as standard library modules
* prefer absolute imports when clarity matters

---

## Circular imports (early warning)

Circular imports happen when:

* module A imports module B
* module B imports module A

This often appears after splitting code into many files.

A typical cause:

* code that should be shared is placed in the wrong module

The usual fix:

* move shared code into a third module
* import locally inside a function (only if necessary)

---

## Conclusion

* module = file
* package = directory that groups modules
* `__init__.py` can run code on import
* absolute imports are explicit
* relative imports depend on package context
* running with `python -m` often avoids import confusion
