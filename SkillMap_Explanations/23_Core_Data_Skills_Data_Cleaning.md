# Core Data Skills: Data Cleaning

Data cleaning (also known as data cleansing or data scrubbing) is the process of detecting and correcting (or removing) corrupt or inaccurate records from a record set, table, or database. It is one of the most important and, often, most time-consuming parts of the data analysis process.

**The GIGO Principle: Garbage In, Garbage Out.** If you analyze messy, inaccurate data, you will get messy, inaccurate results. The quality of your analysis is only as good as the quality of your data.

---

## Common Data Quality Issues

Data cleaning involves identifying and addressing several common types of issues:

### 1. Missing Data

*   **What it is:** Fields that are empty or have null values.
*   **Why it happens:** Data wasn't collected, it was lost during transfer, or it's not applicable for that entry.
*   **How to handle it:**
    -   **Remove:** You can remove the rows or columns with missing data. This is the easiest option, but you lose information.
    -   **Impute:** You can fill in the missing values. Common imputation techniques include filling with the mean, median, or mode of the column, or using a more sophisticated model to predict the missing value.

### 2. Inconsistent Formatting

*   **What it is:** Data that is represented in different ways. This is especially common with text data.
*   **Examples:**
    -   **Capitalization:** "USA", "usa", "U.S.A."
    -   **Dates:** "2025-07-11", "07/11/2025", "11-Jul-2025"
    -   **Categorical Values:** "Female", "F", "female", "1"
*   **How to handle it:** Standardize the values into a single, consistent format (e.g., convert all text to lowercase, parse all dates into a standard date format).

### 3. Duplicates

*   **What it is:** The same record appearing more than once in the dataset.
*   **Why it happens:** Data entry errors, or issues when merging data from multiple sources.
*   **How to handle it:** Identify and remove the duplicate rows.

### 4. Outliers and Errors

*   **What it is:** Data points that are significantly different from other observations. Some outliers are legitimate extreme values, while others are errors.
*   **Examples:**
    -   An age of `500`.
    -   A temperature of `-200` degrees Celsius.
    -   A product price of `$0`.
*   **How to handle it:**
    -   **Investigate:** Try to understand why the outlier exists. Is it a data entry error or a real value?
    -   **Correct or Remove:** If it's an error, you can try to correct it if you know the true value, or remove it. If it's a legitimate extreme value, you may choose to keep it, but be aware of its potential to skew your analysis (e.g., its effect on the mean).

### 5. Incorrect Data Types

*   **What it is:** Data that is stored in the wrong format.
*   **Example:** A `Date` column stored as a string, or a `Price` column with dollar signs and commas stored as text instead of a number.
*   **How to handle it:** Convert the columns to the correct data types (e.g., convert the string to a datetime object, remove the special characters and convert the price to a numeric type).

---

## The Data Cleaning Workflow (in Python with Pandas)

1.  **Initial Exploration:** Use `df.info()` and `df.describe()` to get a high-level overview of your data, including data types, non-null counts, and basic statistics.

2.  **Handling Missing Data:**
    *   Use `df.isnull().sum()` to see how many missing values are in each column.
    *   Use `df.dropna()` to remove rows/columns with missing data, or `df.fillna()` to impute them.

3.  **Correcting Data Types:**
    *   Use `pd.to_datetime()` to convert date columns.
    *   Use `pd.to_numeric()` to convert numeric columns.
    *   Use `df.astype()` for general type conversions.

4.  **Standardizing Text Data:**
    *   Use the `.str.lower()`, `.str.upper()`, or `.str.strip()` methods on a Series to clean up text.
    *   Use the `.str.replace()` method to replace specific substrings.

5.  **Handling Duplicates:**
    *   Use `df.duplicated().sum()` to count duplicate rows.
    *   Use `df.drop_duplicates()` to remove them.

6.  **Dealing with Outliers:**
    *   Use visualization (like box plots) to identify outliers.
    -   Filter the data to remove or cap extreme values (e.g., `df[df['Age'] < 100]`).

---

## Summary

-   **Data cleaning** is a critical and foundational step in any data analysis project.
-   It involves handling a variety of issues, including **missing data, inconsistent formats, duplicates, and outliers**.
-   Libraries like **Pandas** in Python provide a powerful toolkit for performing these cleaning tasks.
-   Investing time in data cleaning will dramatically improve the quality and reliability of your analysis.
