# Programming (Python) Tutorial: Matplotlib & Seaborn

This tutorial breaks down Matplotlib and Seaborn skills into different proficiency levels. Your goal is to reach an **Intermediate (🟡)** level of understanding.

---

## 🔵 Basic Proficiency: Creating Simple Plots with Matplotlib

At this level, you can create basic static plots using Matplotlib to visualize data.

### 1. What is Matplotlib?

*   **Concept:** Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python. It is the foundational plotting library in Python.
*   **Key Module:** `matplotlib.pyplot` is a collection of command-style functions that make Matplotlib work like MATLAB. It's the most common way to use Matplotlib for basic plotting.

### 2. Getting Started: Importing Matplotlib

```python
import matplotlib.pyplot as plt
```
*   `plt` is the conventional alias for `matplotlib.pyplot`.

### 3. Basic Plot Types

*   **Line Plot (`plt.plot()`):** Used to show trends over time or continuous data.
    ```python
    # Example: Monthly Sales Trend
    months = [1, 2, 3, 4, 5, 6]
    sales = [100, 120, 150, 130, 170, 180]
    plt.plot(months, sales)
    plt.show()
    ```
*   **Scatter Plot (`plt.scatter()`):** Used to show the relationship between two numerical variables.
    ```python
    # Example: Relationship between Hours Studied and Exam Score
    hours_studied = [1, 2, 3, 4, 5]
    exam_scores = [60, 70, 85, 90, 95]
    plt.scatter(hours_studied, exam_scores)
    plt.show()
    ```
*   **Bar Chart (`plt.bar()`):** Used to compare quantities across different categories.
    ```python
    # Example: Sales by Product Category
    products = ['A', 'B', 'C']
    sales = [200, 150, 300]
    plt.bar(products, sales)
    plt.show()
    ```
*   **Histogram (`plt.hist()`):** Used to show the distribution of a single numerical variable.
    ```python
    # Example: Distribution of Customer Ages
    ages = [22, 25, 30, 35, 28, 40, 25, 32, 22, 30]
    plt.hist(ages, bins=5)
    plt.show()
    ```

### 4. Basic Customization

*   **Titles and Labels:**
    *   `plt.title("My Plot Title")`
    *   `plt.xlabel("X-axis Label")`
    *   `plt.ylabel("Y-axis Label")`
*   **Showing the Plot:** `plt.show()`

### Realistic Example: Daily Website Visitors

You have daily website visitor counts and want to visualize the trend and distribution.

```python
import matplotlib.pyplot as plt
import numpy as np

days = np.arange(1, 11)
visitors = [120, 135, 150, 140, 160, 175, 180, 165, 190, 200]

# Line plot for trend
plt.figure(figsize=(8, 4))
plt.plot(days, visitors, marker='o')
plt.title('Daily Website Visitors Trend')
plt.xlabel('Day')
plt.ylabel('Visitors')
plt.grid(True)
plt.show()

# Histogram for distribution
plt.figure(figsize=(6, 4))
plt.hist(visitors, bins=4, edgecolor='black')
plt.title('Distribution of Daily Visitors')
plt.xlabel('Visitors Count')
plt.ylabel('Frequency')
plt.show()
```

---

## 🟡 Intermediate Proficiency: Using Seaborn for Statistical Plots and Enhanced Aesthetics

At this level, you can use Seaborn to create more aesthetically pleasing and statistically oriented plots, often with less code, and combine it with Matplotlib for customization.

### 1. What is Seaborn?

*   **Concept:** Seaborn is a Python data visualization library based on Matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics.
*   **Why use it?** Seaborn simplifies the creation of complex plots, has better default aesthetics, and is designed to work well with Pandas DataFrames.

### 2. Getting Started: Importing Seaborn

```python
import seaborn as sns
```
*   `sns` is the conventional alias for Seaborn.

### 3. Common Seaborn Plot Types

*   **Scatter Plot with Regression Line (`sns.lmplot()` or `sns.regplot()`):** Shows the relationship between two variables and fits a regression line.
    ```python
    import pandas as pd
    data = pd.DataFrame({'AdSpend': [10, 20, 30, 40, 50], 'Sales': [100, 120, 150, 180, 220]})
    sns.lmplot(x='AdSpend', y='Sales', data=data)
    plt.show()
    ```
*   **Bar Plot (`sns.barplot()`):** Shows the mean of a numerical variable for different categories.
    ```python
    data = pd.DataFrame({'Region': ['East', 'West', 'East', 'West'], 'Sales': [100, 150, 120, 180]})
    sns.barplot(x='Region', y='Sales', data=data)
    plt.show()
    ```
*   **Box Plot (`sns.boxplot()`):** Shows the distribution of a numerical variable across different categories, highlighting median, quartiles, and outliers.
    ```python
    data = pd.DataFrame({'Product': ['A', 'A', 'B', 'B'], 'Price': [10, 12, 15, 25]})
    sns.boxplot(x='Product', y='Price', data=data)
    plt.show()
    ```
*   **Count Plot (`sns.countplot()`):** Shows the counts of observations in each category.
    ```python
    data = pd.DataFrame({'Gender': ['Male', 'Female', 'Male', 'Female', 'Male']})
    sns.countplot(x='Gender', data=data)
    plt.show()
    ```

### 4. Customization with Matplotlib

Since Seaborn is built on Matplotlib, you can use Matplotlib functions to further customize Seaborn plots (e.g., adding titles, labels, saving figures).

### Realistic Example: Customer Demographics and Spending

You have a Pandas DataFrame `customer_data` with `Age`, `Gender`, and `TotalSpent`.

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample DataFrame
customer_data = pd.DataFrame({
    'Age': [25, 30, 35, 40, 28, 32, 45, 50, 22, 38],
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female'],
    'TotalSpent': [100, 150, 120, 200, 110, 160, 250, 300, 90, 180]
})

# Relationship between Age and TotalSpent with regression line
plt.figure(figsize=(8, 5))
sns.regplot(x='Age', y='TotalSpent', data=customer_data)
plt.title('Age vs. Total Spending')
plt.xlabel('Customer Age')
plt.ylabel('Total Spent ($)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.show()

# Distribution of TotalSpent by Gender using a box plot
plt.figure(figsize=(6, 5))
sns.boxplot(x='Gender', y='TotalSpent', data=customer_data)
plt.title('Total Spending Distribution by Gender')
plt.xlabel('Gender')
plt.ylabel('Total Spent ($)')
plt.show()
```

---

## 🟢 Strong Proficiency: Advanced Visualizations, Customization, and Storytelling

At this level, you can create complex, multi-layered visualizations, fine-tune every aspect of your plots for publication-quality output, and use visualization to tell compelling data stories.

### 1. Advanced Seaborn Plots

*   **Heatmaps (`sns.heatmap()`):** For visualizing correlation matrices or other matrix-like data.
    ```python
    corr_matrix = customer_data.corr(numeric_only=True)
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
    plt.title('Correlation Matrix')
    plt.show()
    ```
*   **Pair Plots (`sns.pairplot()`):** For visualizing relationships between all pairs of variables in a DataFrame.
    ```python
    sns.pairplot(customer_data, hue='Gender') # 'hue' adds a categorical dimension
    plt.show()
    ```
*   **Violin Plots (`sns.violinplot()`):** Combines box plot with kernel density estimation, showing the distribution shape.

### 2. Matplotlib Subplots and Layouts

*   **`plt.subplots()`:** Creates a figure and a set of subplots, allowing you to arrange multiple plots in a grid.
    ```python
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))
    sns.histplot(data=customer_data, x='Age', ax=axes[0])
    sns.boxplot(data=customer_data, y='TotalSpent', ax=axes[1])
    plt.tight_layout()
    plt.show()
    ```
*   **`GridSpec`:** For more complex subplot layouts.

### 3. Fine-tuning Aesthetics and Customization

*   **Styles:** `sns.set_style()`, `plt.style.use()` for overall plot aesthetics.
*   **Color Palettes:** `sns.color_palette()`, `cmap` arguments for controlling colors.
*   **Annotations:** Adding text, arrows, and shapes to highlight specific points on a plot.
*   **Legends and Titles:** Advanced control over placement, font, and content.
*   **Saving Plots:** `plt.savefig('my_plot.png', dpi=300, bbox_inches='tight')` for high-resolution output.

### 4. Using Visualization for Storytelling

*   **Progressive Disclosure:** Revealing information step-by-step across multiple plots or by adding annotations.
*   **Highlighting Key Insights:** Using color, size, or text to draw attention to the most important findings.
*   **Dashboard-like Layouts:** Combining multiple related plots into a single, cohesive visual narrative.

### Realistic Example: Comprehensive Sales Performance Analysis

You need to create a series of plots to tell a story about sales performance, showing trends, distributions, and comparisons.

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample Sales Data
sales_data = pd.DataFrame({
    'Date': pd.to_datetime(pd.date_range(start='2024-01-01', periods=100, freq='D')),
    'Region': np.random.choice(['North', 'South', 'East', 'West'], 100),
    'ProductCategory': np.random.choice(['Electronics', 'Clothing', 'Home Goods'], 100),
    'Sales': np.random.randint(50, 500, 100) + np.arange(100) * 2 # Adding a trend
})

# Create a figure with multiple subplots
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Comprehensive Sales Performance Analysis', fontsize=16)

# Plot 1: Daily Sales Trend
sns.lineplot(x='Date', y='Sales', data=sales_data, ax=axes[0, 0])
axes[0, 0].set_title('Daily Sales Trend')
axes[0, 0].set_xlabel('')
axes[0, 0].set_ylabel('Sales ($)')
axes[0, 0].tick_params(axis='x', rotation=45)

# Plot 2: Sales Distribution by Region (Box Plot)
sns.boxplot(x='Region', y='Sales', data=sales_data, ax=axes[0, 1])
axes[0, 1].set_title('Sales Distribution by Region')
axes[0, 1].set_xlabel('')
axes[0, 1].set_ylabel('Sales ($)')

# Plot 3: Sales by Product Category (Bar Plot)
sns.barplot(x='ProductCategory', y='Sales', data=sales_data.groupby('ProductCategory')['Sales'].sum().reset_index(), ax=axes[1, 0])
axes[1, 0].set_title('Total Sales by Product Category')
axes[1, 0].set_xlabel('')
axes[1, 0].set_ylabel('Total Sales ($)')

# Plot 4: Correlation Heatmap (Conceptual - need more numerical features for real correlation)
# For demonstration, let's create a dummy correlation matrix
dummy_corr = pd.DataFrame(np.random.rand(3,3), columns=['Sales', 'Cost', 'Profit'], index=['Sales', 'Cost', 'Profit'])
np.fill_diagonal(dummy_corr.values, 1)
sns.heatmap(dummy_corr, annot=True, cmap='viridis', fmt='.2f', ax=axes[1, 1])
axes[1, 1].set_title('Feature Correlation (Dummy)')

plt.tight_layout(rect=[0, 0.03, 1, 0.95]) # Adjust layout to prevent title overlap
plt.show()
```

This example demonstrates how to combine multiple plots, use different chart types, and apply basic customization to create a more comprehensive and insightful visual analysis, moving towards a strong proficiency in data visualization.
