# Programming (Python) Tutorial: NumPy

This tutorial breaks down NumPy skills into different proficiency levels. Your goal is to reach an **Intermediate (🟡)** level of understanding.

---

## 🔵 Basic Proficiency: Understanding Arrays and Basic Creation

At this level, you understand what a NumPy array is, why it's used, and how to create basic arrays.

### 1. What is NumPy?

*   **Concept:** NumPy (Numerical Python) is the fundamental library for numerical computing in Python. It provides a powerful array object and tools for working with these arrays efficiently.
*   **Why it's essential:** NumPy arrays are much faster and more memory-efficient than standard Python lists for numerical operations. Many other scientific computing libraries (like Pandas) are built on top of NumPy.

### 2. The `ndarray` (N-dimensional Array)

*   **Concept:** The core data structure in NumPy. It's a grid of values, all of the same type, and is indexed by a tuple of non-negative integers.
*   **Key Characteristics:**
    *   **Homogeneous:** All elements in a NumPy array must be of the same data type (e.g., all integers, all floats).
    *   **Fixed Size:** Once created, the size of an array cannot be changed.

### 3. Getting Started: Importing NumPy

```python
import numpy as np
```
*   `np` is the conventional alias for NumPy.

### 4. Basic Array Creation

*   **From a Python List:**
    ```python
    my_list = [1, 2, 3, 4, 5]
    my_array = np.array(my_list)
    print(my_array)
    # Output: [1 2 3 4 5]
    ```
*   **Zeros and Ones:**
    ```python
    zeros_array = np.zeros(5) # Creates an array of 5 zeros
    print(zeros_array)
    # Output: [0. 0. 0. 0. 0.]

    ones_array = np.ones((2, 3)) # Creates a 2x3 array of ones
    print(ones_array)
    # Output:
    # [[1. 1. 1.]
    #  [1. 1. 1.]]
    ```
*   **`arange()`:** Creates arrays with regularly incrementing values (similar to Python's `range()`).
    ```python
    range_array = np.arange(0, 10, 2) # Start, Stop (exclusive), Step
    print(range_array)
    # Output: [0 2 4 6 8]
    ```

### 5. Array Attributes

*   **`array.shape`:** Returns a tuple indicating the size of the array in each dimension.
*   **`array.ndim`:** Returns the number of dimensions (axes) of the array.
*   **`array.dtype`:** Returns the data type of the elements in the array.

### Realistic Example: Daily Temperature Readings

You have a list of daily high temperatures for a week and want to store them in a NumPy array.

```python
import numpy as np

daily_temps_celsius = [25.5, 26.1, 24.9, 27.0, 26.5, 25.8, 27.2]

# Create a NumPy array
temps_array = np.array(daily_temps_celsius)
print("Temperature Array:", temps_array)

# Check its type and shape
print("Data Type:", temps_array.dtype)
print("Shape:", temps_array.shape)
print("Number of Dimensions:", temps_array.ndim)
```

---

## 🟡 Intermediate Proficiency: Array Operations, Indexing, and Basic Math

At this level, you can perform element-wise operations, select and slice array elements, and use basic mathematical functions.

### 1. Element-wise Operations (Vectorization)

*   **Concept:** NumPy allows you to perform mathematical operations on entire arrays without writing explicit loops. This is called vectorization and is much faster.
*   **Arithmetic:**
    ```python
    arr = np.array([1, 2, 3])
    print(arr + 10)    # Output: [11 12 13]
    print(arr * 2)     # Output: [2 4 6]
    print(arr + arr)   # Output: [2 4 6]
    ```
*   **Comparison:**
    ```python
    arr = np.array([10, 20, 30, 40])
    print(arr > 25)    # Output: [False False  True  True]
    ```

### 2. Indexing and Slicing

*   **1D Arrays:** Similar to Python lists.
    ```python
    arr = np.array([10, 20, 30, 40, 50])
    print(arr[0])      # Output: 10 (first element)
    print(arr[1:4])    # Output: [20 30 40] (slice from index 1 up to 4-1)
    ```
*   **2D Arrays (Matrices):** Use `[row_index, column_index]`.
    ```python
    matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(matrix[0, 0])   # Output: 1 (first row, first column)
    print(matrix[1, :])   # Output: [4 5 6] (second row, all columns)
    print(matrix[:, 2])   # Output: [3 6 9] (all rows, third column)
    ```
*   **Boolean Indexing:** Using a boolean array to select elements.
    ```python
    arr = np.array([10, 20, 30, 40])
    filtered_arr = arr[arr > 25] # Select elements greater than 25
    print(filtered_arr)         # Output: [30 40]
    ```

### 3. Basic Mathematical Functions

*   **Aggregation:**
    ```python
    arr = np.array([1, 2, 3, 4, 5])
    print(np.sum(arr))    # Output: 15
    print(np.mean(arr))   # Output: 3.0
    print(np.max(arr))    # Output: 5
    print(np.min(arr))    # Output: 1
    ```
*   **Axis-wise Operations (for 2D arrays):**
    ```python
    matrix = np.array([[1, 2, 3], [4, 5, 6]])
    print(np.sum(matrix, axis=0)) # Sum columns: [5 7 9]
    print(np.sum(matrix, axis=1)) # Sum rows: [ 6 15]
    ```

### Realistic Example: Converting Temperatures and Basic Statistics

Continuing with daily temperatures, now you want to convert them to Fahrenheit and find the average.

```python
import numpy as np

daily_temps_celsius = np.array([25.5, 26.1, 24.9, 27.0, 26.5, 25.8, 27.2])

# Convert to Fahrenheit: F = C * 9/5 + 32
temps_fahrenheit = daily_temps_celsius * 9/5 + 32
print("Temperatures in Fahrenheit:", temps_fahrenheit)

# Find days where temperature was above 26 Celsius
hot_days = daily_temps_celsius[daily_temps_celsius > 26]
print("Days above 26C:", hot_days)

# Calculate average and standard deviation of Celsius temperatures
mean_celsius = np.mean(daily_temps_celsius)
std_dev_celsius = np.std(daily_temps_celsius)
print(f"Average Celsius: {mean_celsius:.2f}, Std Dev Celsius: {std_dev_celsius:.2f}")
```

---

## 🟢 Strong Proficiency: Reshaping, Broadcasting, and Linear Algebra

At this level, you can efficiently manipulate array shapes, understand broadcasting rules, and perform fundamental linear algebra operations.

### 1. Reshaping Arrays

*   **`reshape()`:** Changes the shape of an array without changing its data.
    ```python
    arr = np.arange(1, 10) # [1 2 3 4 5 6 7 8 9]
    matrix = arr.reshape(3, 3)
    print(matrix)
    # Output:
    # [[1 2 3]
    #  [4 5 6]
    #  [7 8 9]]
    ```
*   **`flatten()` / `ravel()`:** Converts a multi-dimensional array into a 1D array.
*   **`newaxis`:** Adds a new dimension to an array.

### 2. Broadcasting

*   **Concept:** NumPy's ability to perform operations on arrays of different shapes. It automatically expands the smaller array to match the shape of the larger array, provided they are compatible.
    ```python
    arr1 = np.array([[1, 2, 3], [4, 5, 6]]) # Shape (2, 3)
    arr2 = np.array([10, 20, 30])         # Shape (3,)
    print(arr1 + arr2)
    # Output:
    # [[11 22 33]
    #  [14 25 36]] (arr2 is broadcast across rows of arr1)
    ```

### 3. Linear Algebra Operations

NumPy provides a `linalg` module for common linear algebra tasks.

*   **Dot Product (`np.dot()` or `@` operator):** Matrix multiplication.
    ```python
    A = np.array([[1, 2], [3, 4]])
    B = np.array([[5, 6], [7, 8]])
    print(A @ B)
    # Output:
    # [[19 22]
    #  [43 50]]
    ```
*   **Inverse (`np.linalg.inv()`):** Calculates the inverse of a matrix.
*   **Determinant (`np.linalg.det()`):** Calculates the determinant of a matrix.

### 4. Performance Considerations

*   **Vectorization:** Always prefer vectorized NumPy operations over Python loops for performance-critical code.
*   **Memory Efficiency:** NumPy arrays are more memory-efficient than lists, especially for large datasets.

### Realistic Example: Image Processing (Conceptual)

Images can be represented as NumPy arrays (e.g., a grayscale image is a 2D array of pixel intensities, a color image is a 3D array).

```python
import numpy as np
# import matplotlib.pyplot as plt # For visualization

# Simulate a grayscale image (10x10 pixels)
image = np.random.randint(0, 256, size=(10, 10), dtype=np.uint8)

# Apply a simple brightness adjustment (add 50 to all pixels, clip at 255)
brightened_image = np.clip(image + 50, 0, 255)

# Simulate a simple blur (average with neighbors - conceptual)
# This would typically involve convolution, but for illustration:
blurred_image = np.zeros_like(image, dtype=np.float32)
for i in range(1, image.shape[0] - 1):
    for j in range(1, image.shape[1] - 1):
        blurred_image[i, j] = np.mean(image[i-1:i+2, j-1:j+2])
blurred_image = blurred_image.astype(np.uint8)

# print("Original Image (top-left 3x3):")
# print(image[:3,:3])
# print("Brightened Image (top-left 3x3):")
# print(brightened_image[:3,:3])
# print("Blurred Image (top-left 3x3):")
# print(blurred_image[:3,:3])

# plt.imshow(image, cmap='gray')
# plt.title("Original Image")
# plt.show()
# plt.imshow(brightened_image, cmap='gray')
# plt.title("Brightened Image")
# plt.show()
```

This example, even if conceptual, highlights how NumPy's array operations and broadcasting are fundamental to fields like image processing, where operations are applied uniformly across large grids of data. Understanding these concepts allows you to work with high-dimensional data efficiently and effectively.
