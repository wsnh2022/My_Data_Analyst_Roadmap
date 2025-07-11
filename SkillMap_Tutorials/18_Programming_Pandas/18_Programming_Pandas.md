# Programming (Python) Tutorial: Pandas

This tutorial breaks down Pandas skills into different proficiency levels. Your goal is to reach an **Intermediate (🟡)** level of understanding.

---

## 🔵 Basic Proficiency: Understanding DataFrames and Basic Operations

At this level, you understand what a Pandas DataFrame is and can perform fundamental operations like reading data, inspecting it, and selecting columns.

### 1. What is Pandas?

*   **Concept:** Pandas is a powerful, open-source Python library for data manipulation and analysis. It provides data structures and functions that make working with structured data (like tables or spreadsheets) easy and efficient.
*   **Key Data Structure:** The **DataFrame**. Think of it as a table with rows and columns, similar to an Excel spreadsheet or a SQL table.

### 2. Getting Started: Importing Pandas

```python
import pandas as pd
```
*   `pd` is the conventional alias for Pandas.

### 3. Reading Data

*   **`pd.read_csv()`:** Reads data from a CSV (Comma Separated Values) file.
*   **`pd.read_excel()`:** Reads data from an Excel file.

```python
# Example: Reading a CSV file into a DataFrame
df = pd.read_csv('sales_data.csv')
```

### 4. Inspecting DataFrames

*   **`df.head()`:** Displays the first 5 rows of the DataFrame (useful for a quick look).
*   **`df.tail()`:** Displays the last 5 rows.
*   **`df.info()`:** Provides a concise summary of the DataFrame, including data types, non-null values, and memory usage.
*   **`df.shape`:** Returns a tuple representing the dimensions of the DataFrame (rows, columns).
*   **`df.columns`:** Returns a list of column names.

### 5. Selecting Columns

*   **Single Column:** Returns a Pandas Series (a 1-dimensional array).
    ```python
    product_column = df['Product']
    ```
*   **Multiple Columns:** Returns a DataFrame.
    ```python
    subset_df = df[['Product', 'Sales']]
    ```

### Realistic Example: Exploring a Customer List

You have a CSV file named `customers.csv` with columns like `CustomerID`, `Name`, `Email`, `City`, `Age`, `LastPurchaseDate`.

```python
import pandas as pd

# Read the data
customers_df = pd.read_csv('customers.csv')

# See the first few rows
print("First 5 rows:")
print(customers_df.head())

# Get a summary of the data types and non-null counts
print("\nDataFrame Info:")
customers_df.info()

# Check the dimensions
print(f"\nDataFrame Shape: {customers_df.shape}")

# Select only the 'Name' and 'Email' columns
contact_info = customers_df[['Name', 'Email']]
print("\nContact Info (first 5 rows):")
print(contact_info.head())
```

---

## 🟡 Intermediate Proficiency: Filtering, Grouping, and Basic Data Cleaning

At this level, you can filter rows based on conditions, group data for aggregation, create new columns, and handle basic missing values.

### 1. Filtering Rows

*   **Concept:** Selecting rows that meet specific criteria.
*   **Single Condition:**
    ```python
    # Select customers from 'New York'
    ny_customers = df[df['City'] == 'New York']
    ```
*   **Multiple Conditions (using `&` for AND, `|` for OR, `~` for NOT):
    ```python
    # Select customers from 'New York' who are over 30
    ny_old_customers = df[(df['City'] == 'New York') & (df['Age'] > 30)]
    ```
*   **`isin()`:** For filtering by multiple values in a column.
    ```python
    # Select customers from 'New York' or 'Los Angeles'
    major_city_customers = df[df['City'].isin(['New York', 'Los Angeles'])]
    ```

### 2. Creating New Columns

*   **Concept:** Adding new columns based on existing ones.
    ```python
    # Calculate profit from sales and cost
    df['Profit'] = df['Sales'] - df['Cost']

    # Categorize customers based on age
    df['AgeGroup'] = pd.cut(df['Age'], bins=[0, 18, 35, 65, 100], labels=['Child', 'Young Adult', 'Adult', 'Senior'])
    ```

### 3. Grouping and Aggregating Data

*   **Concept:** Similar to `GROUP BY` in SQL. Used to summarize data by categories.
*   **`groupby()` and `agg()`:**
    ```python
    # Calculate total sales by region
    sales_by_region = df.groupby('Region')['Sales'].sum()

    # Calculate total sales and average profit by product category
    category_summary = df.groupby('Category').agg({
        'Sales': 'sum',
        'Profit': 'mean'
    })
    ```

### 4. Basic Data Cleaning

*   **Handling Missing Values:**
    *   `df.isnull().sum()`: Count missing values per column.
    *   `df.dropna()`: Remove rows with any missing values.
    *   `df.fillna(value)`: Fill missing values with a specific value (e.g., 0, mean, median).
*   **Removing Duplicates:**
    *   `df.duplicated().sum()`: Count duplicate rows.
    *   `df.drop_duplicates()`: Remove duplicate rows.

### Realistic Example: Analyzing E-commerce Orders

You have an `orders_df` with `OrderID`, `CustomerID`, `Product`, `Quantity`, `Price`, `OrderDate`, `Region`.

```python
# Calculate Total Price for each order line
orders_df['TotalPrice'] = orders_df['Quantity'] * orders_df['Price']

# Filter for orders in the 'East' region after 2024
east_orders_2024_plus = orders_df[(orders_df['Region'] == 'East') & (orders_df['OrderDate'] >= '2024-01-01')]

# Calculate total sales and average quantity by product
product_summary = orders_df.groupby('Product').agg({
    'TotalPrice': 'sum',
    'Quantity': 'mean'
})
print(product_summary)

# Check for missing values in 'Region' and fill with 'Unknown'
orders_df['Region'].fillna('Unknown', inplace=True)

# Remove duplicate order IDs (if any)
orders_df.drop_duplicates(subset=['OrderID'], inplace=True)
```

---

## 🟢 Strong Proficiency: Advanced Data Manipulation, Time Series, and Performance

At this level, you can perform complex data transformations, work with time series data, handle advanced data cleaning scenarios, and optimize Pandas operations for performance.

### 1. Advanced Data Manipulation

*   **`pivot_table()`:** Reshapes data, similar to Excel PivotTables, allowing for complex aggregations and multi-level indexing.
    ```python
    # Total sales by region and product category
pivot_table_sales = df.pivot_table(values='Sales', index='Region', columns='Category', aggfunc='sum')
    ```
*   **`merge()`:** Combines DataFrames based on common columns (like SQL JOINs).
    ```python
    # Merge sales data with product details
    merged_df = pd.merge(sales_df, products_df, on='ProductID', how='inner')
    ```
*   **`apply()`:** Apply a function along an axis of the DataFrame (row or column).
    ```python
    # Apply a custom function to categorize customers
    def categorize_customer(row):
        if row['TotalSpent'] > 1000: return 'High Value'
        elif row['TotalSpent'] > 500: return 'Medium Value'
        else: return 'Low Value'
    df['CustomerSegment'] = df.apply(categorize_customer, axis=1)
    ```

### 2. Working with Time Series Data

*   **Converting to Datetime:** `pd.to_datetime()`.
*   **Setting Index:** `df.set_index('DateColumn', inplace=True)`.
*   **Resampling:** Changing the frequency of time series data (e.g., daily to monthly).
    ```python
    # Resample daily sales to monthly sum
    monthly_sales = daily_sales_df.resample('M').sum()
    ```
*   **Rolling Windows:** Calculating rolling averages or sums.
    ```python
    # 7-day rolling average of sales
    df['7_Day_Avg_Sales'] = df['Sales'].rolling(window=7).mean()
    ```

### 3. Advanced Data Cleaning and Transformation

*   **String Operations (`.str` accessor):** Powerful methods for cleaning text data (e.g., `df['Column'].str.lower()`, `df['Column'].str.replace(' ', '')`).
*   **Handling Outliers:** Identifying and treating outliers (e.g., using `clip()` or custom functions).
*   **Data Type Optimization:** Using more memory-efficient data types (e.g., `category` for categorical data, smaller integer types).

### 4. Performance Considerations

*   **Vectorization:** Preferring built-in Pandas/NumPy operations over explicit Python loops for speed.
*   **`inplace=True`:** Understanding when to use it (modifies DataFrame directly) and when to avoid it (can lead to unexpected behavior).
*   **Chunking:** Reading large files in chunks to manage memory.

### Realistic Example: Analyzing Customer Behavior Over Time

You have a large dataset of customer transactions (`transactions_df`) with `CustomerID`, `TransactionDate`, `Amount`, `ProductCategory`.

```python
# Ensure TransactionDate is datetime and set as index
transactions_df['TransactionDate'] = pd.to_datetime(transactions_df['TransactionDate'])
transactions_df.set_index('TransactionDate', inplace=True)

# Calculate monthly total spending per customer
monthly_customer_spend = transactions_df.groupby([pd.Grouper(freq='M'), 'CustomerID'])['Amount'].sum().unstack(fill_value=0)

# Calculate 3-month rolling average of total sales
# First, get daily total sales
daily_sales = transactions_df.resample('D')['Amount'].sum()
daily_sales['3_Month_Avg_Sales'] = daily_sales.rolling(window=90).mean()

# Identify top 5 customers by total spending
top_customers = transactions_df.groupby('CustomerID')['Amount'].sum().nlargest(5)

# Merge with customer demographics (assuming customers_df exists)
# merged_customer_data = pd.merge(transactions_df, customers_df, on='CustomerID', how='left')
```

This level of proficiency allows you to tackle complex data analysis challenges, prepare data for modeling, and extract deep insights from large datasets efficiently using Pandas.
