# Tools Tutorial: Power BI DAX

This tutorial breaks down Power BI DAX skills into different proficiency levels. Your goal is to reach an **Intermediate (🟡)** level of understanding.

---

## 🔵 Basic Proficiency: Understanding Measures vs. Calculated Columns and Simple Aggregations

At this level, you understand the fundamental difference between measures and calculated columns and can write basic aggregation formulas.

### 1. What is DAX?

*   **Concept:** DAX (Data Analysis Expressions) is the formula language used in Power BI (and Power Pivot for Excel, SSAS Tabular). It's a collection of functions, operators, and constants that can be used in formulas to calculate and return one or more values.
*   **Why it's essential:** DAX allows you to create custom calculations that go beyond simple sums and averages, enabling deeper analysis and more flexible reporting.

### 2. Measures vs. Calculated Columns

This is the most crucial distinction in DAX:

*   **Calculated Columns:**
    *   **Concept:** A new column added to an existing table in your data model. The formula is evaluated **row by row** within the table.
    *   **When calculated:** At data refresh time. The values are stored in the model.
    *   **Use Case:** When you need a new attribute for your data that you can use in rows, columns, or filters (e.g., `Profit Margin %` per product, `Age Group`).
    *   **Example:** `Profit Margin % = DIVIDE([Profit], [Sales])` (calculated for each row of a sales table).

*   **Measures:**
    *   **Concept:** A dynamic calculation that is evaluated **on-the-fly** based on the context of the visual (filters applied by the user).
    *   **When calculated:** At query time (when you drag it into a visual). The values are NOT stored in the model.
    *   **Use Case:** For aggregations and calculations that respond to user interaction (e.g., `Total Sales`, `Average Order Value`, `Year-over-Year Growth`).
    *   **Example:** `Total Sales = SUM(Sales[SalesAmount])`

### 3. Basic Aggregation Measures

These are the building blocks of most DAX analysis.

*   `SUM(Column)`: Sums all numbers in a column.
*   `AVERAGE(Column)`: Calculates the average of numbers in a column.
*   `COUNT(Column)`: Counts the number of non-blank values in a column.
*   `COUNTROWS(Table)`: Counts the number of rows in a table.
*   `DISTINCTCOUNT(Column)`: Counts the number of unique values in a column.

### Realistic Example: Sales Data Analysis

You have a `Sales` table with `OrderID`, `ProductID`, `Quantity`, `UnitPrice`, `Cost`.

**Task 1: Create a Calculated Column for `Line Total`**

```dax
Line Total = Sales[Quantity] * Sales[UnitPrice]
```
*   This column will be added to your `Sales` table, showing the total for each line item.

**Task 2: Create a Measure for `Total Sales`**

```dax
Total Sales = SUM(Sales[Line Total])
```
*   When you drag `Total Sales` into a card visual, it shows the grand total. If you put it in a table with `Region`, it shows total sales per region.

**Task 3: Create a Measure for `Total Profit`**

```dax
Total Profit = SUM(Sales[Quantity] * (Sales[UnitPrice] - Sales[Cost]))
```
*   This calculates profit for each line item and then sums it up.

---

## 🟡 Intermediate Proficiency: Filter Context, CALCULATE, and Time Intelligence

At this level, you understand the concept of filter context, can use the powerful `CALCULATE` function, and perform common time intelligence calculations.

### 1. Filter Context

*   **Concept:** Filter context is the set of filters applied to your data model by the visuals, slicers, and other filters on your report page. Measures are evaluated within this context.
*   **Example:** If you have a `Total Sales` measure and you put it in a table visual with `Region`, the filter context for each row of the table is the specific region (e.g., "North"). So, `Total Sales` for the "North" row will only sum sales for the North region.

### 2. The `CALCULATE` Function

*   **Concept:** `CALCULATE` is the most powerful and versatile function in DAX. It allows you to **modify the filter context** in which an expression is evaluated.
*   **Syntax:** `CALCULATE(<expression>, <filter1>, <filter2>, ...)`
*   **How it works:** It evaluates the `<expression>` (usually a measure) under the influence of the new `<filter>` arguments.

*   **Example: `Sales for California`**
    ```dax
    Sales for California = CALCULATE([Total Sales], Geography[State] = "California")
    ```
    *   This measure will always return the total sales for California, regardless of any other filters applied to the report.

### 3. Time Intelligence Functions

These functions allow you to perform calculations across time periods (e.g., year-over-year, year-to-date). They require a properly marked **Date Table** in your model.

*   `TOTALYTD(Expression, Dates)`: Calculates the expression from the beginning of the year to the current date.
*   `SAMEPERIODLASTYEAR(Dates)`: Shifts the filter context to the same period in the previous year.
*   `DATEADD(Dates, Number_of_Intervals, Interval)`: Shifts the filter context by a specified number of intervals (e.g., -1 year, 1 month).

### Realistic Example: Analyzing Sales Growth

You have a `Sales` table and a `Date` table (marked as a date table in Power BI) linked by `Date`.

**Task 1: Calculate `Sales Last Year`**

```dax
Sales Last Year = CALCULATE([Total Sales], SAMEPERIODLASTYEAR('Date'[Date]))
```
*   This measure will return the total sales for the corresponding period in the previous year, respecting any current filters (e.g., if filtered to July 2025, it shows sales for July 2024).

**Task 2: Calculate `Year-over-Year Sales Growth %`**

```dax
YoY Sales Growth % = 
DIVIDE(
    [Total Sales] - [Sales Last Year],
    [Sales Last Year]
)
```
*   This measure calculates the percentage growth. `DIVIDE` is used to handle division by zero gracefully.

**Task 3: Calculate `Year-to-Date Sales`**

```dax
Sales YTD = TOTALYTD([Total Sales], 'Date'[Date])
```
*   This measure will show the cumulative sales from the beginning of the year up to the current date in the filter context.

---

## 🟢 Strong Proficiency: Advanced Context Transition, Iterators, and Performance Optimization

At this level, you can master complex context transitions, use iterator functions effectively, and optimize DAX for performance in large models.

### 1. Context Transition

*   **Concept:** When a measure is used within a row context (e.g., inside an iterator function like `SUMX` or in a calculated column), the row context is automatically converted into an equivalent filter context. This is a subtle but powerful concept.
*   **Example:** `Total Sales for Each Product = SUMX(Products, [Total Sales])`
    *   `SUMX` iterates row by row over the `Products` table. For each row, the `[Total Sales]` measure (which is normally evaluated in filter context) is now evaluated in a filter context that includes the current product's filters. This allows `SUMX` to correctly sum sales for each product.

### 2. Iterator Functions (`X` functions)

*   **Concept:** Functions ending with `X` (e.g., `SUMX`, `AVERAGEX`, `MAXX`, `MINX`) iterate row by row over a specified table and evaluate an expression for each row, then perform an aggregation.
*   **Use Case:** When you need to perform a calculation on each row *before* aggregating.
*   **Realistic Example: `Total Profit` (more robust)**
    ```dax
    Total Profit = SUMX(
        Sales,
        Sales[Quantity] * (Sales[UnitPrice] - Sales[Cost])
    )
    ```
    *   This calculates the profit for each individual sales line and then sums those profits. This is generally more robust than `SUM(Sales[Quantity] * Sales[UnitPrice] - Sales[Cost])` if `Sales[Quantity]` or `Sales[UnitPrice]` are measures themselves.

### 3. Advanced Filter Manipulation

*   `ALL()`: Removes all filters from a table or column.
*   `ALLEXCEPT()`: Removes all filters from a table except those applied to specified columns.
*   `ALLSELECTED()`: Removes filters from the current query but keeps filters from slicers or other visuals.
*   `KEEPFILTERS()`: Preserves existing filters while applying new ones.

*   **Realistic Example: `Sales % of Total`**
    ```dax
    Sales % of Total = 
    DIVIDE(
        [Total Sales],
        CALCULATE([Total Sales], ALL(Sales))
    )
    ```
    *   This calculates the percentage of total sales for the current filter context. `ALL(Sales)` removes all filters from the `Sales` table, giving you the grand total sales.

### 4. Performance Optimization

*   **Data Model Design:** A well-designed star schema is the foundation of good DAX performance.
*   **Measure Optimization:** Writing efficient DAX code, avoiding unnecessary context transitions, and understanding the engine's behavior.
*   **Variables (`VAR`):** Using variables to store intermediate results can improve readability and performance by avoiding redundant calculations.

### Realistic Scenario: Customer Segmentation by Purchase Frequency

You want to segment customers based on their purchase frequency (e.g., how many orders they placed) and then analyze the total sales for each segment.

**Your Approach (Strong Proficiency):**

1.  **Calculate `Number of Orders` per Customer (Measure):**
    ```dax
    Number of Orders = DISTINCTCOUNT(Sales[OrderID])
    ```

2.  **Create `Customer Frequency Segment` (Calculated Column in `Customers` table):**
    ```dax
    Customer Frequency Segment = 
    VAR OrdersCount = CALCULATE([Number of Orders], RELATEDTABLE(Sales))
    RETURN
        IF(OrdersCount >= 10, "High Frequency",
        IF(OrdersCount >= 3, "Medium Frequency", "Low Frequency"))
    ```
    *   `RELATEDTABLE(Sales)` creates a table of sales related to the current customer in the row context. `CALCULATE` then transitions this row context into a filter context, allowing `[Number of Orders]` to be evaluated for that specific customer.

3.  **Analyze `Total Sales` by `Customer Frequency Segment`:** You can now drag `Customer Frequency Segment` into a visual and see `Total Sales` for each segment.

This demonstrates the interplay between calculated columns and measures, the power of context transition, and the ability to create complex business logic using DAX.
