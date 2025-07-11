# Cheatsheet: Python Syntax + Jupyter

## Python Core Syntax
*   **Variables:** Store data (no explicit type declaration).
    *   `name = "Alice"`, `age = 30`, `price = 19.99`
*   **Data Types:**
    *   `str` (string): Text (`"hello"`)
    *   `int` (integer): Whole numbers (`10`)
    *   `float` (floating-point): Decimal numbers (`3.14`)
    *   `bool` (boolean): `True` or `False`
*   **Basic Operations:**
    *   Arithmetic: `+`, `-`, `*`, `/`, `**`, `%`
    *   Comparison: `==`, `!=`, `>`, `<`, `>=`, `<=`
    *   Logical: `and`, `or`, `not`
*   **`print()`:** Display output (`print(f"Hello, {name}!")` for f-strings).
*   **Comments:** `#` for single-line comments.

## Python Data Structures
*   **List (`[]`):** Ordered, mutable collection (`fruits = ["apple", "banana"]`).
*   **Dictionary (`{}`):** Unordered, mutable key-value pairs (`customer = {"name": "Bob", "age": 25}`).
*   **Tuple (`()`):** Ordered, immutable collection (`coordinates = (10, 20)`).

## Control Flow
*   **`if/elif/else`:** Conditional execution.
*   **`for` loops:** Iterate over sequences.
    *   `for item in my_list:`
    *   `for i in range(5):`

## Functions
*   **`def`:** Define reusable blocks of code.
    *   `def greet(name): return f"Hello, {name}!"`

## Jupyter Notebook
*   **Purpose:** Interactive web application for live code, text, and visualizations.
*   **Cells:**
    *   **Code Cells:** Write and execute Python code.
    *   **Markdown Cells:** Write explanatory text (using Markdown syntax).
*   **Running Cells:** `Shift + Enter`.
*   **Kernel:** Executes the code.

## Proficiency Levels Summary

### 🔵 Basic
*   Understand fundamental Python syntax (variables, basic data types, `print()`).
*   Perform simple arithmetic and logical operations.
*   Understand the concept of Jupyter Notebooks (interactive environment).
*   Run code and Markdown cells in Jupyter.

### 🟡 Intermediate
*   Utilize Python's core data structures: **lists, dictionaries, and tuples**.
*   Implement **control flow** using `if/elif/else` statements and `for` loops.
*   Define and call **functions** to create reusable code.
*   Use Jupyter Notebooks for iterative data exploration, combining code, output, and narrative text.

### 🟢 Strong
*   Understand basic **Object-Oriented Programming (OOP)** concepts (classes, objects, methods).
*   Implement **error handling** using `try-except` blocks.
*   Organize code into **modules and packages** for better structure and reusability.
*   Leverage Jupyter's advanced features for more complex data analysis workflows (e.g., magic commands, widgets).
*   Write clean, well-structured, and maintainable Python code within a Jupyter environment.
