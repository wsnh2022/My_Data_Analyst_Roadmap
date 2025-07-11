# Programming (Python): NumPy

NumPy (Numerical Python) is the fundamental package for scientific computing in Python. It is a Python library that provides a multidimensional array object, various derived objects (such as masked arrays and matrices), and an assortment of routines for fast operations on arrays, including mathematical, logical, shape manipulation, sorting, selecting, I/O, discrete Fourier transforms, basic linear algebra, basic statistical operations, random simulation and much more.

At the core of the NumPy package, is the **ndarray** object. This encapsulates n-dimensional arrays of homogeneous data types.

---

## NumPy Arrays vs. Python Lists

While a Python list can contain different data types, all of the elements in a NumPy array must be of the same data type. This homogeneity is what makes NumPy arrays so powerful and efficient.

**Key advantages of NumPy arrays:**

*   **More compact:** They take up less space in memory than Python lists.
*   **Faster:** Operations on NumPy arrays are much faster than on Python lists. This is because NumPy uses C and Fortran in the background to perform the operations.
*   **More convenient:** NumPy provides a large number of built-in functions that make it easy to work with arrays.

---

## Realistic Example: Working with Numerical Data

Imagine you have a list of temperatures in Celsius and you want to convert them to Fahrenheit.

**Using Python lists:**

```python
# A list of temperatures in Celsius
celsius = [20.1, 20.8, 21.9, 22.5, 22.7, 22.3, 21.8, 21.2, 20.9, 20.1]

# To convert to Fahrenheit, you would have to loop through the list
fahrenheit = []
for temp in celsius:
    fahrenheit.append(temp * 9/5 + 32)

print(fahrenheit)
```

**Using NumPy arrays:**

```python
import numpy as np

# Create a NumPy array from the list
celsius_array = np.array(celsius)

# With NumPy, you can perform the operation on the entire array at once.
# This is called vectorization.
fahrenheit_array = celsius_array * 9/5 + 32

print(fahrenheit_array)
```

This is not only more concise but also significantly faster for large arrays.

---

## Key NumPy Features

*   **Creating Arrays:** You can create arrays from lists, or use built-in functions like `np.zeros()`, `np.ones()`, `np.arange()`, and `np.linspace()`.

*   **Mathematical Operations:** You can perform element-wise operations on arrays (like in the example above). NumPy also provides a wide range of mathematical functions (`np.sin()`, `np.cos()`, `np.exp()`, etc.).

*   **Aggregation:** You can perform aggregations like `np.sum()`, `np.mean()`, `np.std()`, `np.min()`, and `np.max()` on arrays.

*   **Indexing and Slicing:** You can select elements and subarrays from a NumPy array using syntax similar to Python lists, but with more advanced capabilities for multidimensional arrays.

*   **Linear Algebra:** NumPy provides a suite of linear algebra functions, such as matrix multiplication, determinants, and eigenvalues.

---

## The Relationship with Pandas

Pandas is built on top of NumPy. In fact, a Pandas DataFrame is essentially a collection of NumPy arrays. The columns of a DataFrame are Pandas Series, and each Series is backed by a NumPy array.

This means that when you are performing operations on a Pandas DataFrame, you are often using NumPy in the background. Understanding NumPy helps you understand how Pandas works at a deeper level.

---

## Summary

-   **NumPy** is the foundation of the scientific Python ecosystem.
-   Its core data structure is the powerful and efficient **ndarray**.
-   It allows for fast, **vectorized** operations on numerical data.
-   It is a dependency for many other data science libraries, including **Pandas**.
-   While you may not always use NumPy directly as a data analyst (you'll often use it through Pandas), it's a crucial library to understand, as it powers the tools you use every day.
