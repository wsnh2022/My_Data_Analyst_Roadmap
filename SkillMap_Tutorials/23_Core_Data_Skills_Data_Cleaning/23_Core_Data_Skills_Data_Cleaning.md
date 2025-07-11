# Core Data Skills Tutorial: Data Cleaning

This tutorial breaks down Data Cleaning skills into different proficiency levels. Your goal is to reach a **Strong (🟢)** level of understanding.

---

## 🔵 Basic Proficiency: Identifying Common Issues and Simple Fixes

At this level, you can recognize common data quality problems and apply straightforward methods to fix them, primarily using visual inspection or basic functions.

### 1. What is Data Cleaning?

*   **Concept:** The process of detecting and correcting (or removing) corrupt, inaccurate, or irrelevant records from a dataset. It's about ensuring data quality and consistency.
*   **Why it's essential:** "Garbage In, Garbage Out." Flawed data leads to flawed analysis and incorrect conclusions.

### 2. Common Data Quality Issues

*   **Missing Values:** Empty cells or `null`/`NaN` values where data should be.
    *   *Example:* A customer record with no `Email` address.
*   **Inconsistent Formatting:** Data represented in different ways.
    *   *Example:* `USA`, `U.S.A.`, `United States` for the same country.
    *   *Example:* `2025-01-01`, `01/01/2025`, `Jan 1, 2025` for dates.
*   **Duplicates:** Identical rows or records appearing more than once.
    *   *Example:* The same customer order appearing twice in a sales table.
*   **Incorrect Data Types:** Data stored in a format that doesn't match its content.
    *   *Example:* A `Price` column stored as text (`"$10.50"`) instead of a number (`10.50`).
*   **Outliers/Errors:** Values that are unusually high or low, often due to data entry mistakes.
    *   *Example:* An `Age` of `200` or a `Quantity` of `-5`.

### 3. Simple Fixes (Conceptual/Excel-like)

*   **Missing Values:**
    *   **Delete:** Manually delete rows with missing critical data.
    *   **Fill:** Manually fill in obvious missing values (e.g., if you know the value).
*   **Inconsistent Formatting:**
    *   **Manual Correction:** Go through and manually change inconsistent entries.
    *   **Find & Replace:** Use `Ctrl+F` to find and replace common inconsistencies.
*   **Duplicates:**
    *   **Remove Duplicates:** Use Excel's built-in "Remove Duplicates" feature.
*   **Incorrect Data Types:**
    *   **Text to Columns:** Use Excel's "Text to Columns" to split and convert data.
*   **Outliers/Errors:**
    *   **Visual Inspection:** Look at the data and identify obvious errors.
    *   **Manual Correction:** Change incorrect values if the correct value is known.

### Realistic Example: Cleaning a Small Survey Dataset

You have a small Excel sheet with survey responses. You notice some issues.

| ID | Age | Gender | City      | Rating |
|----|-----|--------|-----------|--------|
| 1  | 25  | Male   | New York  | 4      |
| 2  | 30  | Female | LA        | 5      |
| 3  |     | Male   | New York  | 3      |
| 4  | 25  | Female | Los Angeles | 4      |
| 5  | 500 | Female | New York  | 2      |\
| 6  | 30  | Female | LA        | 5      |

*   **Missing Value:** ID 3 has no `Age`.
*   **Inconsistent Formatting:** `LA` vs. `Los Angeles` in `City`.
*   **Duplicate:** ID 2 and ID 6 are identical.
*   **Outlier/Error:** ID 5 has `Age` 500.

At a basic level, you would manually address these issues in Excel.

---

## 🟡 Intermediate Proficiency: Using Pandas for Systematic Cleaning

At this level, you can systematically identify and address common data quality issues using Pandas in Python, making your cleaning process more efficient and reproducible.

### 1. Identifying Issues with Pandas

*   **Missing Values:**
    *   `df.isnull().sum()`: Counts missing values per column.
    *   `df.isna().sum()`: Same as `isnull()`. `df.notna().sum()` counts non-missing.
*   **Data Types:**
    *   `df.info()`: Shows data types for all columns.
    *   `df.dtypes`: Returns a Series with the dtype of each column.
*   **Duplicates:**
    *   `df.duplicated().sum()`: Counts duplicate rows.
    *   `df.duplicated(subset=['col1', 'col2']).sum()`: Counts duplicates based on specific columns.
*   **Unique Values/Inconsistencies:**
    *   `df['column'].unique()`: Shows all unique values in a column (great for spotting inconsistencies).
    *   `df['column'].value_counts()`: Shows the frequency of each unique value.

### 2. Systematic Cleaning with Pandas

*   **Handling Missing Values:**
    *   `df.dropna(axis=0/1, how='any'/'all')`: Removes rows (`axis=0`) or columns (`axis=1`) with missing values.
    *   `df.fillna(value)`: Fills missing values with a specified value (e.g., 0, mean, median, mode).
        *   `df['Age'].fillna(df['Age'].mean(), inplace=True)`
*   **Correcting Data Types:**
    *   `pd.to_datetime(df['DateColumn'])`: Converts to datetime objects.
    *   `pd.to_numeric(df['PriceColumn'], errors='coerce')`: Converts to numeric, turning unparseable values into `NaN`.
    *   `df['Column'].astype(str/int/float)`: Changes data type.
*   **Removing Duplicates:**
    *   `df.drop_duplicates(inplace=True)`: Removes duplicate rows.
    *   `df.drop_duplicates(subset=['col1', 'col2'], inplace=True)`: Removes duplicates based on a subset of columns.
*   **Standardizing Text Data:**
    *   `df['Column'].str.lower()`: Converts to lowercase.
    *   `df['Column'].str.strip()`: Removes leading/trailing whitespace.
    *   `df['Column'].str.replace('old', 'new')`: Replaces substrings.

### Realistic Example: Cleaning a Customer Feedback Dataset

You have a `feedback_df` with `FeedbackID`, `Rating`, `Comment`, `SubmissionDate`, `UserLocation`.

```python
import pandas as pd
import numpy as np

# Sample DataFrame (simulating issues)
feedback_data = {
    'FeedbackID': [1, 2, 3, 4, 5, 6, 7],
    'Rating': [5, 4, np.nan, 3, 5, 4, 10],
    'Comment': ['Great!', 'Good', '' , 'Okay', 'Great!', 'Good', 'Terrible'],
    'SubmissionDate': ['2025-01-10', '2025-01-11', '2025-01-12', '2025-01-13', '2025-01-10', '2025-01-11', '2025-01-14'],
    'UserLocation': ['NY', 'ca', 'NY', 'CA', 'NY', 'ca', 'Texas']
}
feedback_df = pd.DataFrame(feedback_data)

print("Original DataFrame:\n", feedback_df)
print("\nMissing values before cleaning:\n", feedback_df.isnull().sum())
print("\nUnique UserLocations before cleaning:\n", feedback_df['UserLocation'].unique())

# 1. Handle Missing Ratings: Fill with median
median_rating = feedback_df['Rating'].median()
feedback_df['Rating'].fillna(median_rating, inplace=True)

# 2. Handle empty comments: Fill with 'No Comment'
feedback_df['Comment'].replace('', 'No Comment', inplace=True)

# 3. Standardize UserLocation: Convert to uppercase
feedback_df['UserLocation'] = feedback_df['UserLocation'].str.upper()

# 4. Correct Rating Outlier: Assume max rating is 5
feedback_df['Rating'] = feedback_df['Rating'].apply(lambda x: 5 if x > 5 else x)

# 5. Convert SubmissionDate to datetime
feedback_df['SubmissionDate'] = pd.to_datetime(feedback_df['SubmissionDate'])

# 6. Remove Duplicates (based on all columns)
feedback_df.drop_duplicates(inplace=True)

print("\nCleaned DataFrame:\n", feedback_df)
print("\nMissing values after cleaning:\n", feedback_df.isnull().sum())
print("\nUnique UserLocations after cleaning:\n", feedback_df['UserLocation'].unique())
```

---

## 🟢 Strong Proficiency: Advanced Cleaning, Automation, and Data Validation

At this level, you can handle complex data cleaning scenarios, automate cleaning pipelines, implement robust data validation, and understand the implications of cleaning choices.

### 1. Advanced Missing Value Imputation

*   **Forward/Backward Fill:** `df.fillna(method='ffill')` or `df.fillna(method='bfill')` for time series or ordered data.
*   **Interpolation:** `df.interpolate()` to estimate missing values based on surrounding data points.
*   **Model-based Imputation:** Using machine learning models to predict missing values (e.g., `IterativeImputer` from `sklearn.impute`).

### 2. Advanced Inconsistency Handling

*   **Fuzzy Matching:** For highly inconsistent text data (e.g., `New York`, `N.Y.`, `NYC`), use libraries like `fuzzywuzzy` to find and standardize similar strings.
*   **Regular Expressions (`.str.contains()`, `.str.extract()`, `.str.replace()` with regex):** For complex pattern-based cleaning and extraction.

### 3. Outlier Detection and Treatment

*   **Statistical Methods:** Z-scores, IQR (Interquartile Range) method to programmatically identify outliers.
*   **Visualization:** Box plots, scatter plots to visually inspect outliers.
*   **Treatment:** Capping (winsorization), transformation, or removal (with careful consideration).

### 4. Data Validation and Assertions

*   **Concept:** Programmatically checking if your data meets certain quality rules *after* cleaning.
*   **Libraries:** `pandera`, `great_expectations` for defining and enforcing data schemas and expectations.
*   **Assertions:** Using `assert` statements in your code to ensure conditions are met.
    ```python
    assert df['Rating'].between(1, 5).all(), "Ratings must be between 1 and 5"
    assert df['SubmissionDate'].dtype == 'datetime64[ns]', "SubmissionDate must be datetime"
    ```

### 5. Building Reusable Cleaning Functions/Pipelines

*   **Concept:** Encapsulating cleaning steps into functions or classes to create a modular and reusable cleaning pipeline.
*   **Example:** A function that takes a raw DataFrame and returns a cleaned one.

### Realistic Scenario: Cleaning a Large E-commerce Transaction Dataset

You have a large `transactions_df` with millions of rows. It has various issues, including inconsistent product names, missing prices, and potential fraudulent transactions (outliers).

**Your Approach (Strong Proficiency):**

1.  **Load Data in Chunks:** For very large files, load in chunks to manage memory.
2.  **Initial Profiling:** Use `df.info()`, `df.describe()`, and `df.isnull().sum()` to get a quick overview.
3.  **Standardize Product Names:**
    *   Convert `ProductName` to lowercase and remove extra spaces.
    *   Use fuzzy matching to group similar product names (e.g., `"Laptop Pro"` and `"Laptop Pro Max"`) into a single standard name.
4.  **Handle Missing Prices:**
    *   If `Price` is missing, try to impute it based on the `ProductName` (e.g., use the median price for that product).
    *   If a product has no recorded price, fill with a default or flag for manual review.
5.  **Detect and Treat Outliers (Fraud):**
    *   Calculate Z-scores for `Quantity` and `Amount`.
    *   Identify transactions where `Quantity` or `Amount` are more than 3 standard deviations from the mean.
    *   Investigate these outliers. If confirmed as errors/fraud, either remove them or flag them for separate analysis.
6.  **Data Validation:**
    *   Assert that `Quantity` is always positive.
    *   Assert that `TransactionDate` is a valid datetime.
    *   Assert that `CustomerID` is never null.
7.  **Build a Cleaning Pipeline:** Create a Python function `clean_transactions(df)` that encapsulates all these steps, making the cleaning process repeatable and auditable.

This level of proficiency allows you to build robust, automated, and intelligent data cleaning solutions, ensuring the highest quality data for your analysis and models.
