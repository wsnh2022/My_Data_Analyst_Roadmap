# Cheatsheet: Pandas

## Core Concept
*   **Purpose:** Powerful Python library for data manipulation and analysis.
*   **Key Data Structure:** **DataFrame** (2-dimensional, tabular data with labeled rows/columns, like a spreadsheet or SQL table).

## Getting Started
*   `import pandas as pd`

## Basic Operations
*   **Reading Data:** `pd.read_csv()`, `pd.read_excel()`.
*   **Inspection:**
    *   `df.head()`, `df.tail()`: First/last rows.
    *   `df.info()`: Summary (data types, non-nulls).
    *   `df.shape`: Dimensions (rows, columns).
    *   `df.describe()`: Descriptive statistics for numerical columns.
    *   `df.columns`: List of column names.
*   **Selection:**
    *   `df['ColumnName']`: Select single column (returns Series).
    *   `df[['Col1', 'Col2']]`: Select multiple columns (returns DataFrame).

## Intermediate Operations
*   **Filtering Rows:**
    *   `df[df['Column'] == 'Value']`
    *   `df[(condition1) & (condition2)]` (AND), `(condition1) | (condition2)` (OR).
    *   `df[df['Column'].isin(['Val1', 'Val2'])]`
*   **Creating New Columns:** `df['NewCol'] = df['Col1'] * df['Col2']`.
*   **Grouping & Aggregation:**
    *   `df.groupby('Category')['Value'].sum()`
    *   `df.groupby('Category').agg({'Col1': 'sum', 'Col2': 'mean'})`
*   **Basic Data Cleaning:**
    *   **Missing Values:** `df.isnull().sum()`, `df.dropna()`, `df.fillna(value)`.
    *   **Duplicates:** `df.duplicated().sum()`, `df.drop_duplicates()`.

## Advanced Operations
*   **Data Reshaping:** `df.pivot_table()`.
*   **Combining DataFrames:** `pd.merge(df1, df2, on='Key', how='inner')` (SQL-like joins).
*   **Applying Functions:** `df.apply(function, axis=1)` (row-wise).
*   **Time Series:**
    *   `pd.to_datetime()`
    *   `df.set_index('DateColumn')`
    *   `df.resample('M').sum()` (resampling).
    *   `df.rolling(window=7).mean()` (rolling windows).
*   **String Operations:** `df['TextCol'].str.lower()`, `.str.strip()`, `.str.replace()`.
*   **Performance:** Prefer vectorized operations over loops.

## Proficiency Levels Summary

### 🔵 Basic
*   Understand the DataFrame as a tabular data structure.
*   Read data from CSV/Excel into a DataFrame.
*   Inspect DataFrame basics (`head`, `info`, `shape`).
*   Select single or multiple columns.

### 🟡 Intermediate
*   Filter DataFrame rows based on single or multiple conditions.
*   Create new columns from existing ones.
*   Group and aggregate data using `groupby()`.
*   Perform basic data cleaning: handle missing values (`dropna`, `fillna`), remove duplicates.

### 🟢 Strong
*   Perform advanced data manipulation: `pivot_table()`, `merge()`, `apply()`.
*   Work effectively with time series data (resampling, rolling windows).
*   Handle advanced data cleaning scenarios (string operations, outlier treatment).
*   Optimize Pandas operations for performance (vectorization).
*   Tackle complex data analysis challenges and prepare data for modeling.
