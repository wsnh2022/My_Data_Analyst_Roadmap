# Core Data Skills Tutorial: EDA (Exploratory Data Analysis)

This tutorial breaks down EDA (Exploratory Data Analysis) skills into different proficiency levels. Your goal is to reach an **Intermediate (🟡)** level of understanding.

---

## 🔵 Basic Proficiency: Understanding the Purpose and Basic Data Inspection

At this level, you understand what EDA is for and can perform initial inspections of a dataset to get a high-level overview.

### 1. What is EDA?

*   **Concept:** Exploratory Data Analysis (EDA) is an approach to analyzing data sets to summarize their main characteristics, often with visual methods. It's the process of getting to know your data *before* formal modeling or hypothesis testing.
*   **Purpose:**
    *   To understand the structure and content of the data.
    *   To identify patterns, trends, and relationships.
    *   To spot anomalies, outliers, or errors that might need further cleaning.
    *   To formulate hypotheses for further analysis.

### 2. Initial Data Inspection (using Pandas)

After loading your data into a Pandas DataFrame, these are your first steps:

*   **`df.head()` / `df.tail()`:** Quickly view the first/last few rows to get a sense of the data's structure and content.
    ```python
    import pandas as pd
    # Assuming df is your DataFrame
    print(df.head())
    ```
*   **`df.info()`:** Get a concise summary of the DataFrame, including:
    *   Number of entries (rows).
    *   Number of columns.
    *   Column names and their data types (`dtype`).
    *   Number of non-null values per column (useful for spotting missing data).
    *   Memory usage.
    ```python
    print(df.info())
    ```
*   **`df.shape`:** Returns a tuple representing the dimensions (rows, columns) of the DataFrame.
    ```python
    print(df.shape)
    ```
*   **`df.describe()`:** Generates descriptive statistics for numerical columns, including count, mean, standard deviation, min, max, and quartiles.
    ```python
    print(df.describe())
    ```
*   **`df['column'].unique()`:** Shows all unique values in a specific column (useful for categorical data to spot inconsistencies).
    ```python
    print(df['Region'].unique())
    ```
*   **`df['column'].value_counts()`:** Shows the count of each unique value in a column.
    ```python
    print(df['ProductCategory'].value_counts())
    ```

### Realistic Example: Initial Look at Sales Data

You've just received a `sales_data.csv` file and want to get a quick overview.

```python
import pandas as pd

sales_df = pd.read_csv('sales_data.csv')

print("First 5 rows of Sales Data:")
print(sales_df.head())

print("\nInfo about Sales Data:")
sales_df.info()

print("\nDescriptive Statistics for Sales Data:")
print(sales_df.describe())

print("\nUnique Regions in Sales Data:")
print(sales_df['Region'].unique())

print("\nCounts of Sales by Product Category:")
print(sales_df['ProductCategory'].value_counts())
```

---

## 🟡 Intermediate Proficiency: Univariate and Bivariate Analysis with Visualizations

At this level, you can perform deeper analysis on individual variables and relationships between two variables, using appropriate visualizations to uncover patterns.

### 1. Univariate Analysis (Analyzing Single Variables)

*   **Numerical Variables:**
    *   **Histograms:** Show the distribution of a single numerical variable. Helps identify skewness, modality, and outliers.
        ```python
        import matplotlib.pyplot as plt
        import seaborn as sns
        sns.histplot(data=df, x='SalesAmount', kde=True)
        plt.title('Distribution of Sales Amount')
        plt.show()
        ```
    *   **Box Plots:** Show the distribution, median, quartiles, and potential outliers.
        ```python
        sns.boxplot(data=df, y='Age')
        plt.title('Distribution of Customer Age')
        plt.show()
        ```
*   **Categorical Variables:**
    *   **Bar Charts (Count Plots):** Show the frequency of each category.
        ```python
        sns.countplot(data=df, x='Gender')
        plt.title('Customer Gender Distribution')
        plt.show()
        ```

### 2. Bivariate Analysis (Analyzing Relationships Between Two Variables)

*   **Numerical vs. Numerical:**
    *   **Scatter Plots:** Show the relationship between two numerical variables. Helps identify correlation, clusters, and outliers.
        ```python
        sns.scatterplot(data=df, x='AdSpend', y='Sales')
        plt.title('Ad Spend vs. Sales')
        plt.show()
        ```
    *   **Correlation Matrix:** Quantifies the linear relationship between numerical variables.
        ```python
        print(df[['SalesAmount', 'Quantity', 'Profit']].corr())
        ```
*   **Categorical vs. Numerical:
    *   **Grouped Bar Charts:** Show the average (or sum) of a numerical variable for different categories.
        ```python
        sns.barplot(data=df, x='Region', y='SalesAmount')
        plt.title('Average Sales by Region')
        plt.show()
        ```
    *   **Box Plots (grouped):** Show the distribution of a numerical variable across different categories.
        ```python
        sns.boxplot(data=df, x='ProductCategory', y='Price')
        plt.title('Price Distribution by Product Category')
        plt.show()
        ```
*   **Categorical vs. Categorical:**
    *   **Count Plots (with `hue`):** Show the counts of one categorical variable broken down by another.
        ```python
        sns.countplot(data=df, x='Region', hue='ProductCategory')
        plt.title('Product Category Counts by Region')
        plt.show()
        ```
    *   **Crosstabulations (`pd.crosstab()`):** Create frequency tables.
        ```python
        print(pd.crosstab(df['Region'], df['ProductCategory']))
        ```

### Realistic Example: Analyzing Customer Demographics and Spending

You have `customer_data` with `Age`, `Gender`, `Region`, and `TotalSpent`.

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

customer_data = pd.DataFrame({
    'Age': [25, 30, 35, 40, 28, 32, 45, 50, 22, 38],
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female'],
    'Region': ['East', 'West', 'East', 'West', 'East', 'West', 'East', 'West', 'East', 'West'],
    'TotalSpent': [100, 150, 120, 200, 110, 160, 250, 300, 90, 180]
})

# Univariate: Distribution of Age
sns.histplot(data=customer_data, x='Age', kde=True)
plt.title('Distribution of Customer Age')
plt.show()

# Bivariate: Total Spent vs. Age
sns.scatterplot(data=customer_data, x='Age', y='TotalSpent')
plt.title('Total Spent vs. Age')
plt.show()

# Bivariate: Total Spent by Gender
sns.boxplot(data=customer_data, x='Gender', y='TotalSpent')
plt.title('Total Spent by Gender')
plt.show()

# Bivariate: Total Spent by Region
sns.barplot(data=customer_data, x='Region', y='TotalSpent')
plt.title('Average Total Spent by Region')
plt.show()
```

---

## 🟢 Strong Proficiency: Multivariate Analysis, Hypothesis Generation, and Iterative Exploration

At this level, you can perform multivariate analysis, use EDA to generate and refine hypotheses, and conduct an iterative, deep-dive exploration of complex datasets.

### 1. Multivariate Analysis

*   **Concept:** Analyzing relationships among three or more variables simultaneously.
*   **Pair Plots (`sns.pairplot()`):** Creates a grid of scatter plots for all numerical variable pairs, and histograms for individual variables. Can add a categorical `hue`.
    ```python
    sns.pairplot(df, hue='Region')
    plt.show()
    ```
*   **Heatmaps of Correlation Matrices:** Visualizes the correlation between many numerical variables.
    ```python
    corr_matrix = df.corr(numeric_only=True)
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
    plt.title('Correlation Matrix')
    plt.show()
    ```
*   **Facet Grids (`sns.FacetGrid()`):** Create grids of plots based on categorical variables, allowing you to compare distributions or relationships across different subgroups.
    ```python
    g = sns.FacetGrid(df, col='Region', row='Gender')
    g.map(sns.scatterplot, 'Age', 'TotalSpent')
    plt.show()
    ```

### 2. Hypothesis Generation and Refinement

*   **Concept:** Use EDA findings to formulate specific, testable hypotheses. If an initial hypothesis is disproven, use EDA to refine it or generate new ones.
*   **Example:** Initial hypothesis: "Older customers spend more." EDA shows a non-linear relationship. Refined hypothesis: "Customers in their 30s and 40s spend the most."

### 3. Iterative Exploration

*   **Concept:** EDA is not a linear process. It's a cycle of questioning, visualizing, analyzing, and refining your understanding.
*   **Drill Down:** When you find an interesting pattern, drill down into that specific subset of data for deeper insights.
*   **Slice and Dice:** Continuously break down your data by different dimensions to uncover hidden patterns.

### Realistic Example: Deep Dive into Customer Churn Drivers

You are analyzing a `churn_df` with `CustomerID`, `MonthlyCharges`, `TotalCharges`, `ContractType`, `InternetService`, `Tenure`, `Churn`.

**Your Approach (Strong Proficiency):**

1.  **Initial Overview:** `df.info()`, `df.describe()`, `df.isnull().sum()`. (Identify `TotalCharges` as object type, convert to numeric, handle NaNs).
2.  **Univariate Analysis:**
    *   `sns.histplot(df['Tenure'])`: Most customers have short tenure or very long tenure (bimodal).
    *   `sns.countplot(df['ContractType'])`: Many month-to-month contracts.
3.  **Bivariate Analysis (Churn as Target):**
    *   `sns.boxplot(x='Churn', y='MonthlyCharges', data=df)`: Churned customers have higher monthly charges.
    *   `sns.boxplot(x='Churn', y='Tenure', data=df)`: Churned customers have lower tenure.
    *   `sns.countplot(x='InternetService', hue='Churn', data=df)`: Fiber Optic customers churn more.
4.  **Multivariate Analysis & Hypothesis Generation:**
    *   **Hypothesis:** "Customers with Fiber Optic internet and month-to-month contracts are most likely to churn, especially if they have low tenure."
    *   **Visual Confirmation (FacetGrid):**
        ```python
        g = sns.FacetGrid(df, col="InternetService", row="ContractType", hue="Churn", height=3, aspect=1.5)
        g.map(sns.scatterplot, "Tenure", "MonthlyCharges", alpha=0.7)
        g.add_legend()
        plt.show()
        ```
        *   This plot visually confirms the hypothesis: the highest density of churned customers (red dots) is indeed in the "Fiber Optic" and "Month-to-month" facets, concentrated at lower tenures and higher monthly charges.
5.  **Actionable Insights:** Based on this, you can recommend targeted interventions for these high-risk segments (e.g., offering long-term contract incentives to new Fiber Optic customers).

This iterative process of questioning, visualizing, and refining your understanding is the hallmark of strong EDA, allowing you to uncover deep, actionable insights from your data.
