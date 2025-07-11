# Cheatsheet: EDA (Exploratory Data Analysis)

## Core Concept
*   **Purpose:** To summarize main characteristics of a dataset, often with visual methods.
*   **Goal:** Explore, ask questions, uncover patterns, anomalies, and formulate hypotheses *before* formal modeling.
*   **Philosophy:** Be a detective; let the data tell a story.

## Initial Data Inspection (Pandas)
*   `df.head()`, `df.tail()`: Quick view of rows.
*   `df.info()`: Data types, non-null counts, memory usage.
*   `df.shape`: Dimensions (rows, columns).
*   `df.describe()`: Descriptive statistics for numerical columns.
*   `df['col'].unique()`: Unique values (spot inconsistencies).
*   `df['col'].value_counts()`: Frequency of unique values.

## Univariate Analysis (Single Variable)
*   **Numerical:**
    *   **Stats:** Mean, Median, Mode, Std Dev, Variance, Quartiles.
    *   **Visuals:** Histogram (distribution, skew), Box Plot (distribution, outliers).
*   **Categorical:**
    *   **Stats:** Frequency counts, percentages.
    *   **Visuals:** Bar Chart/Count Plot (frequency).

## Bivariate Analysis (Two Variables)
*   **Numerical vs. Numerical:**
    *   **Stats:** Correlation coefficient.
    *   **Visuals:** Scatter Plot (relationship, clusters, outliers).
*   **Categorical vs. Numerical:**
    *   **Stats:** Grouped means/medians.
    *   **Visuals:** Box Plot (grouped), Bar Plot (average by category).
*   **Categorical vs. Categorical:**
    *   **Stats:** Crosstabulation (`pd.crosstab()`).
    *   **Visuals:** Grouped/Stacked Bar Chart.

## Multivariate Analysis (Three+ Variables)
*   **Visuals:**
    *   `sns.pairplot()`: Grid of scatter plots for all numerical pairs.
    *   `sns.heatmap()`: Correlation matrix visualization.
    *   `sns.FacetGrid()`: Grids of plots based on categorical variables.
    *   Using `hue`, `size`, `style` in plots to add dimensions.

## EDA Workflow
1.  Load Clean Data.
2.  Initial Overview (`info`, `describe`, `head`).
3.  Univariate Analysis (histograms, box plots, bar charts).
4.  Bivariate Analysis (scatter plots, correlation matrix, grouped plots).
5.  Ask Deeper Questions & Iterate.
6.  Summarize Findings.

## Proficiency Levels Summary

### 🔵 Basic
*   Understand the purpose of EDA (getting to know the data).
*   Perform initial data inspections using Pandas (`head`, `info`, `shape`, `describe`).
*   Identify basic data characteristics (data types, missing values, unique values).

### 🟡 Intermediate
*   Perform **univariate analysis** using appropriate statistical summaries and visualizations (histograms, box plots, bar charts).
*   Perform **bivariate analysis** to explore relationships between two variables (scatter plots, grouped bar/box plots, correlation matrices).
*   Use Matplotlib and Seaborn effectively for common EDA visualizations.
*   Identify basic patterns, trends, and potential outliers.

### 🟢 Strong
*   Conduct **multivariate analysis** using advanced visualization techniques (`pairplot`, `heatmap`, `FacetGrid`).
*   Use EDA to **generate and refine hypotheses** for further analysis.
*   Perform iterative, deep-dive exploration of complex datasets, slicing and dicing data to uncover hidden patterns.
*   Translate EDA findings into actionable insights and communicate them effectively.
*   Understand the importance of EDA as a continuous process throughout the data analysis lifecycle.
