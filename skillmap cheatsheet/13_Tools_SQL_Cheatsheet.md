# Cheatsheet: SQL

## Core Concept
*   **Purpose:** Standard language for interacting with relational databases.
*   **Function:** Requesting, retrieving, and manipulating data.

## Basic Query Structure
```sql
SELECT column1, column2
FROM table_name
WHERE condition
GROUP BY column1
HAVING aggregate_condition
ORDER BY column1 ASC/DESC;
```

## Key Clauses/Commands
*   **`SELECT`:** Specifies columns to retrieve (`*` for all).
*   **`FROM`:** Specifies the table(s).
*   **`WHERE`:** Filters rows based on conditions (`=`, `!=`, `>`, `<`, `>=`, `<=`, `LIKE`, `IN`, `BETWEEN`, `AND`, `OR`, `NOT`).
*   **`ORDER BY`:** Sorts the result set (`ASC` for ascending, `DESC` for descending).
*   **`GROUP BY`:** Groups rows with same values for aggregation.
*   **`HAVING`:** Filters groups based on aggregate conditions (used after `GROUP BY`).

## Aggregate Functions
*   `COUNT()`: Counts rows/values.
*   `SUM()`: Sums numeric values.
*   `AVG()`: Calculates average.
*   `MIN()`: Finds minimum value.
*   `MAX()`: Finds maximum value.

## JOINs (Combining Tables)
*   **`INNER JOIN`:** Returns only matching rows from both tables.
*   **`LEFT JOIN` (or `LEFT OUTER JOIN`):** Returns all rows from left table, and matching from right (NULLs if no match).
*   **`RIGHT JOIN` (or `RIGHT OUTER JOIN`):** Returns all rows from right table, and matching from left (NULLs if no match).
*   **`FULL JOIN` (or `FULL OUTER JOIN`):** Returns all rows when there is a match in either table.

## Advanced Concepts
*   **Subqueries:** Nested queries (in `SELECT`, `FROM`, `WHERE`).
*   **Common Table Expressions (CTEs) (`WITH` clause):** Named temporary result sets for complex queries, improving readability.
*   **Window Functions:** Perform calculations across a set of related rows without collapsing them (`ROW_NUMBER()`, `RANK()`, `LAG()`, `LEAD()`, `SUM() OVER()`).

## Proficiency Levels Summary

### 🔵 Basic
*   Connect to a database.
*   Retrieve specific columns and all columns (`SELECT`, `FROM`).
*   Filter rows using `WHERE` clause with basic operators.
*   Sort results using `ORDER BY`.

### 🟡 Intermediate
*   Use aggregate functions (`COUNT`, `SUM`, `AVG`, `MIN`, `MAX`).
*   Group data using `GROUP BY`.
*   Filter grouped data using `HAVING`.
*   Combine data from two or more tables using `INNER JOIN` and `LEFT JOIN`.
*   Write queries to answer common business questions (e.g., total sales by region).

### 🟢 Strong
*   Write complex queries using **subqueries** and **Common Table Expressions (CTEs)**.
*   Utilize **Window Functions** for advanced analytical tasks (e.g., running totals, ranking).
*   Understand and apply different `JOIN` types effectively.
*   Consider database performance and write optimized queries (e.g., understanding indexing, avoiding `SELECT *` in production).
*   Solve multi-step data problems using SQL (e.g., cohort analysis, funnel analysis).
