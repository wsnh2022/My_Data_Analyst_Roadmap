# Cheatsheet: NumPy

## Core Concept
*   **Purpose:** Fundamental Python library for numerical computing.
*   **Key Data Structure:** **`ndarray`** (N-dimensional array).
*   **Advantages over Python lists:** Faster, more memory-efficient, more convenient for numerical operations.

## Getting Started
*   `import numpy as np`

## Array Creation
*   `np.array([1, 2, 3])`: From a Python list.
*   `np.zeros((rows, cols))`: Array of zeros.
*   `np.ones((rows, cols))`: Array of ones.
*   `np.arange(start, stop, step)`: Array with a range of values.
*   `np.linspace(start, stop, num)`: Array with evenly spaced numbers over a specified interval.

## Array Attributes
*   `array.shape`: Dimensions of the array.
*   `array.ndim`: Number of dimensions.
*   `array.dtype`: Data type of elements.

## Array Operations
*   **Element-wise Operations (Vectorization):** Arithmetic (`+`, `-`, `*`, `/`), comparison (`>`, `<`, `==`), logical operations applied to entire arrays without explicit loops.
    *   `arr * 2`, `arr1 + arr2`
*   **Indexing & Slicing:**
    *   `arr[index]`, `arr[start:end:step]` (1D).
    *   `matrix[row_index, col_index]`, `matrix[:, col_index]` (2D).
    *   **Boolean Indexing:** `arr[arr > 5]`.

## Mathematical Functions
*   **Aggregation:** `np.sum()`, `np.mean()`, `np.std()`, `np.min()`, `np.max()`.
*   **Axis-wise Operations:** `np.sum(array, axis=0)` (column-wise), `np.sum(array, axis=1)` (row-wise).
*   **Universal Functions (ufuncs):** `np.sin()`, `np.cos()`, `np.exp()`, `np.log()` (element-wise application).

## Advanced Concepts
*   **Reshaping:** `array.reshape(new_shape)`.
*   **Broadcasting:** NumPy's ability to perform operations on arrays of different shapes (if compatible).
*   **Linear Algebra (`np.linalg`):** `np.dot()` (dot product/matrix multiplication), `np.linalg.inv()` (inverse), `np.linalg.det()` (determinant).

## Proficiency Levels Summary

### 🔵 Basic
*   Understand what a NumPy array is and its advantages over Python lists.
*   Create basic 1D and 2D arrays using `np.array()`, `np.zeros()`, `np.ones()`, `np.arange()`.
*   Access array attributes (`shape`, `ndim`, `dtype`).

### 🟡 Intermediate
*   Perform element-wise operations (vectorization) on arrays.
*   Use indexing and slicing to select specific elements or subarrays.
*   Apply basic mathematical and aggregation functions (`sum`, `mean`, `std`, `max`, `min`).
*   Understand axis-wise operations for multi-dimensional arrays.

### 🟢 Strong
*   Efficiently reshape arrays (`reshape`, `flatten`, `newaxis`).
*   Understand and leverage **broadcasting rules** for operations on arrays of different shapes.
*   Perform fundamental **linear algebra operations** (`np.dot`, `np.linalg.inv`).
*   Optimize code for performance by preferring vectorized NumPy operations over Python loops.
*   Apply NumPy concepts to more complex numerical problems (e.g., image manipulation, scientific simulations).
