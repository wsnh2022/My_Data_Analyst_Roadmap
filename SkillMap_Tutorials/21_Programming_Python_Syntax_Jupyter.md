# Programming (Python) Tutorial: Python Syntax + Jupyter

This tutorial breaks down Python Syntax and Jupyter Notebook skills into different proficiency levels. Your goal is to reach a **Basic (🔵)** level of understanding.

---

## 🔵 Basic Proficiency: Understanding Core Syntax and Jupyter Basics

At this level, you understand fundamental Python syntax, can write simple scripts, and are comfortable using Jupyter Notebooks for interactive coding.

### 1. Python Core Syntax

*   **Variables:** Used to store data. No explicit type declaration needed.
    ```python
    # Assigning values to variables
    name = "Alice"
    age = 30
    price = 19.99
    is_active = True
    ```
*   **Data Types (Basic):**
    *   `str` (string): Text, e.g., `"hello"`
    *   `int` (integer): Whole numbers, e.g., `10`
    *   `float` (floating-point): Decimal numbers, e.g., `3.14`
    *   `bool` (boolean): `True` or `False`
*   **Basic Operations:**
    *   **Arithmetic:** `+`, `-`, `*`, `/`, `**` (exponentiation), `%` (modulo)
    *   **Comparison:** `==` (equal to), `!=` (not equal to), `>`, `<`, `>=`, `<=`
    *   **Logical:** `and`, `or`, `not`
*   **Print Function:** Used to display output.
    ```python
    print("Hello, World!")
    print(f"My name is {name} and I am {age} years old.") # f-string for easy formatting
    ```
*   **Comments:** Use `#` for single-line comments.

### 2. Jupyter Notebook Basics

*   **Concept:** An interactive web application that allows you to create and share documents containing live code, equations, visualizations, and narrative text. It's ideal for data exploration and analysis.
*   **Cells:** The fundamental building blocks of a Jupyter Notebook.
    *   **Code Cells:** Where you write and execute Python code.
    *   **Markdown Cells:** Where you write explanatory text, headings, lists, etc., using Markdown syntax.
*   **Running Cells:** Select a cell and press `Shift + Enter`.
*   **Saving:** Notebooks are saved as `.ipynb` files.

### Realistic Example: Simple Data Calculation in Jupyter

You want to calculate the total cost of items and display a summary.

**In a Code Cell:**
```python
# Define variables
item_price = 25.50
quantity = 3
discount_rate = 0.10 # 10% discount

# Calculate subtotal
subtotal = item_price * quantity

# Calculate discount amount
discount_amount = subtotal * discount_rate

# Calculate final total
final_total = subtotal - discount_amount

# Print results using f-strings
print(f"Item Price: ${item_price:.2f}")
print(f"Quantity: {quantity}")
print(f"Subtotal: ${subtotal:.2f}")
print(f"Discount ({discount_rate*100:.0f}%): ${discount_amount:.2f}")
print(f"Final Total: ${final_total:.2f}")
```

**In a Markdown Cell (above the code):**
```markdown
# Sales Calculation Example

This section demonstrates a simple calculation for a sales transaction, including a discount.
```

---

## 🟡 Intermediate Proficiency: Data Structures, Control Flow, and Functions

At this level, you can use Python's core data structures, implement conditional logic and loops, and write simple reusable functions.

### 1. Python Data Structures

*   **Lists:** Ordered, mutable (changeable) collections of items. Defined with square brackets `[]`.
    ```python
    fruits = ["apple", "banana", "cherry"]
    print(fruits[0]) # Access by index: apple
    fruits.append("orange") # Add item
    ```
*   **Dictionaries:** Unordered, mutable collections of key-value pairs. Defined with curly braces `{}`.
    ```python
    customer = {"name": "Bob", "age": 25, "city": "London"}
    print(customer["name"]) # Access by key: Bob
    customer["age"] = 26 # Update value
    ```
*   **Tuples:** Ordered, immutable (unchangeable) collections of items. Defined with parentheses `()`.
    ```python
    coordinates = (10, 20)
    ```

### 2. Control Flow

*   **`if`, `elif`, `else` (Conditional Statements):** Execute different code blocks based on conditions.
    ```python
    score = 85
    if score >= 90:
        print("Grade A")
    elif score >= 80:
        print("Grade B")
    else:
        print("Grade C")
    ```
*   **`for` loops (Iteration):** Iterate over sequences (lists, strings, ranges).
    ```python
    for fruit in fruits:
        print(fruit)

    for i in range(5): # Loops 5 times (0, 1, 2, 3, 4)
        print(i)
    ```

### 3. Functions

*   **Concept:** Reusable blocks of code that perform a specific task. Defined using `def`.
*   **Defining and Calling:**
    ```python
    def greet(name):
        return f"Hello, {name}!"

    message = greet("Alice")
    print(message)
    ```

### Realistic Example: Processing Customer Data in Jupyter

You have a list of customer records, and you want to process them to categorize their age and calculate a loyalty bonus.

**In a Code Cell:**
```python
customers_data = [
    {"name": "Alice", "age": 32, "purchases": 5},
    {"name": "Bob", "age": 17, "purchases": 1},
    {"name": "Charlie", "age": 45, "purchases": 12},
    {"name": "David", "age": 28, "purchases": 3}
]

def get_age_category(age):
    if age < 18:
        return "Minor"
    elif age < 30:
        return "Young Adult"
    elif age < 50:
        return "Adult"
    else:
        return "Senior"

def calculate_loyalty_bonus(purchases):
    if purchases >= 10:
        return "High Bonus"
    elif purchases >= 5:
        return "Medium Bonus"
    else:
        return "No Bonus"

processed_customers = []
for customer in customers_data:
    age_cat = get_age_category(customer["age"])
    loyalty_bonus = calculate_loyalty_bonus(customer["purchases"])
    processed_customers.append({
        "name": customer["name"],
        "age_category": age_cat,
        "loyalty_bonus": loyalty_bonus
    })

for customer in processed_customers:
    print(f"Name: {customer["name"]}, Age Category: {customer["age_category"]}, Loyalty: {customer["loyalty_bonus"]}")
```

---

## 🟢 Strong Proficiency: Object-Oriented Programming (OOP) Basics, Error Handling, and Modules

At this level, you understand basic OOP concepts, can handle errors gracefully, and organize your code into reusable modules.

### 1. Object-Oriented Programming (OOP) Basics

*   **Concept:** A programming paradigm based on the concept of "objects," which can contain data (attributes) and code (methods).
*   **Classes:** Blueprints for creating objects.
*   **Objects:** Instances of a class.
*   **`__init__`:** The constructor method, called when a new object is created.
*   **Methods:** Functions defined inside a class.

    ```python
    class Product:
        def __init__(self, name, price, stock):
            self.name = name
            self.price = price
            self.stock = stock

        def get_stock_status(self):
            if self.stock > 0:
                return f"{self.name} is in stock ({self.stock} units)"
            else:
                return f"{self.name} is out of stock"

    laptop = Product("Laptop", 1200, 50)
    print(laptop.get_stock_status())
    ```

### 2. Error Handling (`try-except`)

*   **Concept:** Gracefully handling errors (exceptions) that might occur during program execution, preventing the program from crashing.
    ```python
    try:
        result = 10 / 0
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Execution attempt finished.")
    ```

### 3. Modules and Packages

*   **Concept:** Organizing code into separate files (modules) and directories (packages) for better organization, reusability, and maintainability.
*   **`import` statement:** Used to bring functionality from other modules into your current script.
    ```python
    # Assuming you have a file named my_utils.py with a function called calculate_total
    # my_utils.py:
    # def calculate_total(price, quantity): return price * quantity

    import my_utils
    total = my_utils.calculate_total(10, 5)
    print(total)

    # Importing specific functions
    from my_utils import calculate_total
    total = calculate_total(10, 5)
    ```

### Realistic Example: Building a Simple Inventory System in Jupyter

You want to create a small system to manage product inventory, including adding products, updating stock, and handling potential errors.

**In a Code Cell (representing `inventory_manager.py` module):**
```python
class InventoryItem:
    def __init__(self, product_id, name, initial_stock):
        self.product_id = product_id
        self.name = name
        self.stock = initial_stock

    def add_stock(self, quantity):
        if quantity < 0:
            raise ValueError("Quantity to add cannot be negative.")
        self.stock += quantity
        print(f"Added {quantity} units to {self.name}. New stock: {self.stock}")

    def remove_stock(self, quantity):
        if quantity < 0:
            raise ValueError("Quantity to remove cannot be negative.")
        if self.stock < quantity:
            raise ValueError(f"Not enough stock for {self.name}. Available: {self.stock}, Requested: {quantity}")
        self.stock -= quantity
        print(f"Removed {quantity} units from {self.name}. New stock: {self.stock}")

    def get_stock_info(self):
        return f"{self.name} (ID: {self.product_id}): {self.stock} units in stock."

# Example usage (in another cell or script)
# from inventory_manager import InventoryItem
```

**In another Code Cell (representing your main analysis script in Jupyter):**
```python
# Simulate importing from the module (in a real scenario, this would be in a separate .py file)
# For demonstration in a single notebook, we'll just define it above.

# Create some inventory items
item1 = InventoryItem("P001", "Laptop", 100)
item2 = InventoryItem("P002", "Mouse", 200)

print(item1.get_stock_info())
print(item2.get_stock_info())

# Try to add/remove stock with error handling
try:
    item1.add_stock(20)
    item2.remove_stock(250) # This will raise an error
except ValueError as e:
    print(f"Inventory Error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

print(item1.get_stock_info())
print(item2.get_stock_info())
```

This demonstrates how to structure code using classes, handle potential errors, and conceptually use modules, which are crucial for building more robust and maintainable Python applications for data analysis.
