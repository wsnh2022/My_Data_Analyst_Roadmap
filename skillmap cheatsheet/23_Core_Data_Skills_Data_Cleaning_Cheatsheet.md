# Cheatsheet: Data Cleaning

## Core Concept
*   **Purpose:** Detecting and correcting (or removing) corrupt, inaccurate, or irrelevant records from a dataset.
*   **Principle:** "Garbage In, Garbage Out" (GIGO) - quality analysis requires quality data.

## Common Data Quality Issues
*   **Missing Values:** Empty cells (`NaN`, `null`).
*   **Inconsistent Formatting:** Variations in data representation (e.g., `USA`, `U.S.A.`; `Male`, `male`).
*   **Duplicates:** Identical rows or records.
*   **Incorrect Data Types:** Numeric data stored as text, dates as strings.
*   **Outliers/Errors:** Extreme values, often due to data entry mistakes.

## Basic Cleaning Techniques (Conceptual/Excel-like)
*   Manual deletion/correction.
*   Find & Replace.
*   Excel's "Remove Duplicates" feature.

## Systematic Cleaning with Pandas
*   **Identifying Issues:**
    *   `df.isnull().sum()`: Count missing values.
    *   `df.info()`: Check data types and non-null counts.
    *   `df.duplicated().sum()`: Count duplicates.
    *   `df['col'].unique()`, `df['col'].value_counts()`: Spot inconsistencies.
*   **Handling Missing Values:**
    *   `df.dropna()`: Remove rows/columns with missing data.
    *   `df.fillna(value)`: Fill with specific value (0, mean, median, mode).
*   **Correcting Data Types:**
    *   `pd.to_datetime()`, `pd.to_numeric()`, `df.astype()`.
*   **Removing Duplicates:** `df.drop_duplicates()`.
*   **Standardizing Text:** `df['col'].str.lower()`, `.str.strip()`, `.str.replace()`.

## Advanced Cleaning Techniques
*   **Missing Value Imputation:** `ffill`/`bfill`, `interpolate()`, model-based imputation.
*   **Inconsistency Handling:** Fuzzy matching (`fuzzywuzzy`), Regular Expressions (`.str.contains()`, `.str.extract()`).
*   **Outlier Detection & Treatment:** Statistical methods (Z-scores, IQR), visualization (box plots), capping/transformation.
*   **Data Validation:** Programmatic checks (`pandera`, `great_expectations`, `assert` statements).
*   **Reusable Pipelines:** Encapsulating cleaning steps into functions/classes.

## Proficiency Levels Summary

### 🔵 Basic
*   Understand the importance of data cleaning.
*   Identify common data quality issues (missing, inconsistent, duplicates, errors).
*   Perform simple fixes manually or using basic software features (e.g., Excel's remove duplicates).

### 🟡 Intermediate
*   Systematically identify data quality issues using Pandas (`isnull`, `info`, `duplicated`, `unique`).
*   Apply common Pandas functions for cleaning: `dropna`, `fillna`, `to_datetime`, `to_numeric`, `drop_duplicates`, `str` methods.
*   Clean data in a reproducible manner.

### 🟢 Strong
*   Handle complex missing value imputation (interpolation, model-based).
*   Address advanced inconsistencies using fuzzy matching or regular expressions.
*   Implement outlier detection and treatment strategies.
*   Develop robust data validation checks and assertions.
*   Build reusable data cleaning functions or pipelines for automation and maintainability.
*   Understand the implications of cleaning choices on analysis results.
