# Cheatsheet: Power Query

## Core Concept
*   **Purpose:** Data connection, cleaning, transformation, and loading (ETL) tool within Excel and Power BI.
*   **Benefit:** Automates repetitive data preparation tasks, ensures data consistency, and combines data from various sources.
*   **Key Feature:** Records `Applied Steps` to create a reproducible workflow.

## Power Query Editor Interface
*   **Queries Pane:** List of all queries.
*   **Data Preview Pane:** Shows data.
*   **Query Settings Pane:** `Properties` (query name) and `Applied Steps` (history of transformations).

## Common Transformations
*   **Column Management:** `Remove Columns`, `Choose Columns`, `Rename Columns`.
*   **Row Management:** `Remove Rows` (top/bottom/blank/duplicates), `Keep Rows`.
*   **Data Type:** `Change Data Type` (crucial for correct interpretation).
*   **Headers:** `Use First Row as Headers`.
*   **Filtering:** `Filter Rows` (by value, text, number, date).
*   **Splitting:** `Split Column` (by delimiter, number of characters).
*   **Grouping:** `Group By` (aggregate data by categories).
*   **Unpivoting:** `Unpivot Columns` (transforms wide data to tall data, essential for BI tools).
*   **Custom Column:** `Add Custom Column` (create new columns with formulas).

## Combining Queries
*   **Merge Queries:** Combines two tables based on a common column (like SQL JOIN or VLOOKUP).
*   **Append Queries:** Stacks two or more tables on top of each other (like SQL UNION).

## Proficiency Levels Summary

### 🔵 Basic
*   Understand Power Query's purpose (data prep, automation).
*   Connect to common data sources (CSV, Excel).
*   Perform basic transformations: remove columns/rows, change data type, use first row as headers, simple filtering.
*   Load data into Excel/Power BI.

### 🟡 Intermediate
*   Combine data from multiple sources using `Merge Queries` (various join types) and `Append Queries`.
*   Apply advanced transformations: `Group By`, `Unpivot Columns`, `Add Custom Column`.
*   Understand the importance and functionality of `Applied Steps` (editing, reordering).
*   Use Power Query to automate recurring data cleaning and integration tasks.

### 🟢 Strong
*   Write and modify M language (Power Query Formula Language) directly in the Advanced Editor.
*   Create custom M functions for reusable logic.
*   Implement robust error handling within queries.
*   Understand and ensure **Query Folding** for performance optimization.
*   Use parameters to create dynamic and flexible queries.
*   Design and build complex, automated data pipelines within Power Query for enterprise-level solutions.
