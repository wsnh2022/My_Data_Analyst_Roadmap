# Cheatsheet: Power BI DAX

## Core Concept
*   **DAX (Data Analysis Expressions):** Formula language for Power BI, Power Pivot (Excel), and SSAS Tabular.
*   **Purpose:** Create custom calculations and measures for deeper analysis and flexible reporting.

## Key DAX Calculation Types
*   **Calculated Columns:**
    *   **Concept:** New column added to a table, calculated row-by-row.
    *   **When:** At data refresh. Values stored in model.
    *   **Use:** For new attributes (e.g., `Profit Margin %` per product, `Age Group`).
*   **Measures:**
    *   **Concept:** Dynamic calculation evaluated on-the-fly based on visual context.
    *   **When:** At query time. Values NOT stored in model.
    *   **Use:** For aggregations (e.g., `Total Sales`, `YoY Growth`).

## Basic DAX Functions
*   **Aggregation:** `SUM()`, `AVERAGE()`, `COUNT()`, `COUNTROWS()`, `DISTINCTCOUNT()`.
*   **Logical:** `IF()`, `AND()`, `OR()`.
*   **Mathematical:** `DIVIDE()`, `SUMX()` (iterator).

## Intermediate DAX Concepts
*   **Filter Context:** The set of filters applied to your data model by visuals, slicers, etc. Measures are evaluated within this context.
*   **`CALCULATE()`:** The most powerful DAX function. Allows you to **modify the filter context** for an expression.
    *   `CALCULATE(<expression>, <filter1>, <filter2>, ...)`
*   **Time Intelligence Functions:** Require a marked Date Table.
    *   `TOTALYTD()`: Year-to-date total.
    *   `SAMEPERIODLASTYEAR()`: Value for the same period in the previous year.
    *   `DATEADD()`: Shifts filter context by specified intervals.

## Advanced DAX Concepts
*   **Context Transition:** Automatic conversion of row context to filter context when a measure is used in a row context (e.g., inside an iterator or calculated column).
*   **Iterator Functions (`X` functions):** `SUMX()`, `AVERAGEX()`, `MAXX()`, `MINX()`. Iterate row-by-row over a table, evaluate an expression, then aggregate.
*   **Filter Manipulation Functions:** `ALL()`, `ALLEXCEPT()`, `ALLSELECTED()`, `KEEPFILTERS()`.
*   **Variables (`VAR`):** Improve readability and performance by storing intermediate results.

## Proficiency Levels Summary

### 🔵 Basic
*   Understand the fundamental difference between **measures** and **calculated columns**.
*   Write basic aggregation measures (`SUM`, `AVERAGE`, `COUNT`).
*   Create simple calculated columns (e.g., `Line Total`).

### 🟡 Intermediate
*   Understand the concept of **Filter Context**.
*   Master the **`CALCULATE()`** function to modify filter context.
*   Perform common **Time Intelligence** calculations (e.g., `Sales Last Year`, `YoY Sales Growth %`, `Sales YTD`).
*   Apply DAX to solve common business questions related to sales, profit, and time-based comparisons.

### 🟢 Strong
*   Master **Context Transition** and effectively use **iterator functions (`X` functions)** for complex row-level calculations.
*   Utilize advanced filter manipulation functions (`ALL`, `ALLEXCEPT`, `KEEPFILTERS`).
*   Design and implement complex DAX patterns (e.g., customer segmentation by purchase frequency).
*   Optimize DAX for performance in large data models.
*   Understand the interplay between data model design and DAX calculations for robust and scalable solutions.
