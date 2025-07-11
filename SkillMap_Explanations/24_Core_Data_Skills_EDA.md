# Core Data Skills: EDA (Exploratory Data Analysis)

Exploratory Data Analysis (EDA) is an approach to analyzing data sets to summarize their main characteristics, often with visual methods. It is what you do **after** data cleaning to really get to know your data.

The goal of EDA is not to produce a polished final report, but to **explore, ask questions, and uncover potential insights, patterns, and anomalies** that can guide your formal modeling and analysis later on.

EDA is a philosophy of investigation. It's about being a detective and letting the data tell you a story.

---

## The Core Questions of EDA

When you are performing EDA, you are constantly asking questions about your data:

1.  **What is the structure of my data?** (Rows, columns, data types)
2.  **What is the distribution of my variables?** (Central tendency, spread, shape)
3.  **Are there relationships between my variables?** (Correlations, associations)
4.  **Are there any interesting groups or clusters in my data?**
5.  **Are there any outliers or anomalies that I missed during cleaning?**

---

## The EDA Toolkit

EDA relies on a combination of statistical summaries and, most importantly, data visualization.

### 1. Univariate Analysis (Analyzing one variable at a time)

This is where you look at each variable individually to understand its characteristics.

*   **For Categorical Variables:**
    -   **Statistic:** Frequency counts, percentages.
    -   **Visualization:** **Bar chart** or **count plot** to see the frequency of each category. **Pie chart** (use with caution) to see the proportion of each category.

*   **For Numerical Variables:**
    -   **Statistic:** Measures of central tendency (mean, median, mode) and measures of spread (standard deviation, variance, range, quartiles).
    -   **Visualization:** **Histogram** to see the shape of the distribution. **Box plot** to see the quartiles, median, and identify potential outliers.

### 2. Bivariate Analysis (Analyzing two variables at a time)

This is where you start to look for relationships between variables.

*   **Numerical vs. Numerical:**
    -   **Statistic:** Correlation coefficient (e.g., Pearson).
    -   **Visualization:** **Scatter plot** to see the relationship visually. You can add a regression line to see the trend.

*   **Categorical vs. Numerical:**
    -   **Statistic:** Grouped statistics (e.g., the mean of the numerical variable for each category).
    -   **Visualization:** **Box plot** (one for each category), **violin plot**, or **bar chart** showing the aggregated value.

*   **Categorical vs. Categorical:**
    -   **Statistic:** Contingency table (also called a cross-tabulation).
    -   **Visualization:** **Grouped bar chart** or **stacked bar chart**.

### 3. Multivariate Analysis (Analyzing more than two variables at a time)

This is where you look for more complex interactions.

*   **Visualizations:**
    -   **Pair Plot:** A grid of scatter plots that shows the relationship between every pair of numerical variables in your dataset.
    -   **Heatmap:** A graphical representation of data where the individual values contained in a matrix are represented as colors. Often used to visualize a correlation matrix.
    -   **Using visual encodings:** You can add more variables to a plot by using color, size, or shape. For example, in a scatter plot of `Sales` vs. `Advertising`, you could make the color of the points represent the `Region`.

---

## Realistic EDA Workflow (in a Jupyter Notebook)

1.  **Load Clean Data:** Start with the data you cleaned in the previous step.
2.  **Initial Overview:** Use `df.info()`, `df.describe()`, and `df.head()` to remind yourself of the data's structure.
3.  **Univariate Analysis:**
    -   Create histograms and box plots for all key numerical variables.
    -   Create bar charts for all key categorical variables.
    -   Write down your observations. Is the data skewed? Are there outliers?
4.  **Bivariate Analysis:**
    -   Create a correlation matrix and visualize it with a heatmap to see the relationships between numerical variables.
    -   Create scatter plots for the most interesting pairs of numerical variables.
    -   Create box plots or bar charts to see how numerical variables differ across categories.
    -   Write down your observations. Are there strong correlations? Do certain categories have higher values?
5.  **Ask Deeper Questions:** Based on your initial findings, ask more specific questions and create new plots to answer them. For example, "The West region has the highest sales. Is this true for all product categories?"
6.  **Summarize Findings:** At the end of your notebook, summarize your key findings from the exploration.

---

## Summary

-   **EDA** is an **iterative, exploratory process** of getting to know your data.
-   It is driven by **asking questions** and **visualizing** the answers.
-   It helps you **uncover patterns, identify anomalies, and generate hypotheses**.
-   It is the bridge between **data cleaning** and **formal modeling or reporting**.
-   A thorough EDA is one of the strongest indicators of a skilled and thoughtful data analyst.
