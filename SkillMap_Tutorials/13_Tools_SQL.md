# Tools Tutorial: SQL

This tutorial breaks down SQL skills into different proficiency levels. Your goal is to reach an **Intermediate (🟡)** level of understanding.

---

## 🔵 Basic Proficiency: Retrieving and Filtering Data

At this level, you can connect to a database, retrieve specific columns and rows, and sort your results.

### 1. What is SQL?

*   **Concept:** SQL (Structured Query Language) is the standard language for communicating with relational databases. It's how you ask a database for information.
*   **Why it's essential:** Most organizational data is stored in databases. SQL is the primary way data analysts access and manipulate this data.

### 2. Basic Query Structure

All SQL queries follow a logical structure, even if you don't use all clauses every time.

```sql
SELECT column1, column2, ...
FROM table_name
WHERE condition
ORDER BY column_name ASC/DESC;
```

### 3. Core Commands

*   **`SELECT` and `FROM`:**
    *   `SELECT column_name(s)`: Specifies which columns you want to retrieve.
    *   `SELECT *`: Retrieves all columns.
    *   `FROM table_name`: Specifies the table you are querying.
    *   **Example:** `SELECT ProductName, Price FROM Products;`

*   **`WHERE` Clause (Filtering Rows):**
    *   Filters records based on a specified condition.
    *   **Operators:** `=`, `!=` (or `<>`), `>`, `<`, `>=`, `<=`, `LIKE` (for pattern matching), `IN` (for a list of values), `BETWEEN` (for a range).
    *   **Logical Operators:** `AND`, `OR`, `NOT`.
    *   **Example:** `SELECT * FROM Orders WHERE OrderAmount > 100;`
    *   **Example:** `SELECT CustomerName FROM Customers WHERE Country = 'USA' AND City = 'New York';`

*   **`ORDER BY` Clause (Sorting Results):**
    *   Sorts the result set in ascending (`ASC`, default) or descending (`DESC`) order.
    *   **Example:** `SELECT ProductName, Price FROM Products ORDER BY Price DESC;`

### Realistic Example: Finding High-Value Orders

You have an `Orders` table with `OrderID`, `CustomerID`, `OrderDate`, and `OrderAmount`.

**Task:** Retrieve the `OrderID`, `CustomerID`, and `OrderAmount` for all orders placed after January 1, 2025, with an `OrderAmount` greater than $500, sorted by `OrderAmount` from highest to lowest.

```sql
SELECT OrderID, CustomerID, OrderAmount
FROM Orders
WHERE OrderDate > '2025-01-01' AND OrderAmount > 500
ORDER BY OrderAmount DESC;
```

---

## 🟡 Intermediate Proficiency: Aggregation, Grouping, and Joins

At this level, you can summarize data using aggregate functions, group data for analysis, and combine data from multiple tables.

### 1. Aggregate Functions

These functions perform a calculation on a set of values and return a single value.

*   **`COUNT()`:** Counts the number of rows.
    *   `COUNT(*)`: Counts all rows.
    *   `COUNT(column_name)`: Counts non-NULL values in a column.
    *   `COUNT(DISTINCT column_name)`: Counts unique non-NULL values.
*   **`SUM()`:** Calculates the sum of a numeric column.
*   **`AVG()`:** Calculates the average of a numeric column.
*   **`MIN()`:** Finds the minimum value in a column.
*   **`MAX()`:** Finds the maximum value in a column.

### 2. `GROUP BY` Clause

*   **Concept:** Groups rows that have the same values in specified columns into summary rows. Aggregate functions are typically used with `GROUP BY`.
*   **Example:** `SELECT Region, SUM(Sales) FROM SalesData GROUP BY Region;`

### 3. `HAVING` Clause

*   **Concept:** Filters groups based on a condition, similar to `WHERE` but applied *after* `GROUP BY` and on aggregated results.
*   **Example:** `SELECT Region, SUM(Sales) FROM SalesData GROUP BY Region HAVING SUM(Sales) > 10000;`

### 4. `JOIN` Clauses

*   **Concept:** Used to combine rows from two or more tables based on a related column between them.
*   **`INNER JOIN`:** Returns only the rows where there is a match in *both* tables.
    *   **Example:** `SELECT O.OrderID, C.CustomerName FROM Orders O INNER JOIN Customers C ON O.CustomerID = C.CustomerID;`
*   **`LEFT JOIN` (or `LEFT OUTER JOIN`):** Returns all rows from the left table, and the matching rows from the right table. If there's no match, NULLs are returned for the right table's columns.
    *   **Example:** `SELECT C.CustomerName, O.OrderID FROM Customers C LEFT JOIN Orders O ON C.CustomerID = O.CustomerID;` (Shows all customers, even those with no orders).

### Realistic Example: Analyzing Product Sales by Category

You have two tables: `Products` (`ProductID`, `ProductName`, `Category`) and `OrderDetails` (`OrderID`, `ProductID`, `Quantity`, `Price`).

**Task:** Find the total revenue for each product category, but only for categories that have generated more than $10,000 in total revenue. Order the results by total revenue descending.

```sql
SELECT
    P.Category,
    SUM(OD.Quantity * OD.Price) AS TotalRevenue
FROM
    Products P
INNER JOIN
    OrderDetails OD ON P.ProductID = OD.ProductID
GROUP BY
    P.Category
HAVING
    SUM(OD.Quantity * OD.Price) > 10000
ORDER BY
    TotalRevenue DESC;
```

---

## 🟢 Strong Proficiency: Subqueries, CTEs, Window Functions, and Performance

At this level, you can write complex, efficient queries using advanced SQL features, understand database performance considerations, and optimize your queries.

### 1. Subqueries (Nested Queries)

*   **Concept:** A query nested inside another SQL query. It can be used in `SELECT`, `FROM`, or `WHERE` clauses.
*   **Example (in WHERE):** Find customers who have placed more than the average number of orders.
    ```sql
    SELECT CustomerID, COUNT(OrderID)
    FROM Orders
    GROUP BY CustomerID
    HAVING COUNT(OrderID) > (SELECT AVG(OrderCount) FROM (SELECT COUNT(OrderID) AS OrderCount FROM Orders GROUP BY CustomerID) AS SubQueryAlias);
    ```

### 2. Common Table Expressions (CTEs) - `WITH` Clause

*   **Concept:** Named temporary result sets that you can reference within a single `SELECT`, `INSERT`, `UPDATE`, or `DELETE` statement. They improve readability and reusability of complex queries.
*   **Example:** Calculate the average order value for each customer and then find customers whose average order value is above the overall average.
    ```sql
    WITH CustomerAvgOrder AS (
        SELECT
            CustomerID,
            AVG(OrderAmount) AS AvgOrderValue
        FROM
            Orders
        GROUP BY
            CustomerID
    )
    SELECT
        CA.CustomerID,
        CA.AvgOrderValue
    FROM
        CustomerAvgOrder CA
    WHERE
        CA.AvgOrderValue > (SELECT AVG(AvgOrderValue) FROM CustomerAvgOrder);
    ```

### 3. Window Functions

*   **Concept:** Perform calculations across a set of table rows that are related to the current row. Unlike aggregate functions, window functions do not collapse rows.
*   **Common Functions:** `ROW_NUMBER()`, `RANK()`, `LAG()`, `LEAD()`, `SUM() OVER()`, `AVG() OVER()`.
*   **Example:** Calculate a running total of sales for each customer.
    ```sql
    SELECT
        CustomerID,
        OrderDate,
        OrderAmount,
        SUM(OrderAmount) OVER (PARTITION BY CustomerID ORDER BY OrderDate) AS RunningTotalSales
    FROM
        Orders
    ORDER BY
        CustomerID, OrderDate;
    ```

### 4. Performance Considerations

*   **Indexing:** Understand how indexes speed up data retrieval and when to recommend them.
*   **Query Optimization:** Writing efficient queries (e.g., avoiding `SELECT *` in production, using `WHERE` clauses effectively, understanding join types).
*   **Execution Plans:** Ability to read and interpret query execution plans to identify bottlenecks.

### Realistic Example: Customer Cohort Analysis

You want to perform a cohort analysis to see how customer spending changes over time based on their acquisition month.

**Task:** For each customer, find their first order date (acquisition month) and then calculate their total spending in each subsequent month.

```sql
WITH CustomerFirstOrder AS (
    SELECT
        CustomerID,
        MIN(OrderDate) AS FirstOrderDate
    FROM
        Orders
    GROUP BY
        CustomerID
)
SELECT
    CFO.CustomerID,
    DATE_TRUNC('month', CFO.FirstOrderDate) AS AcquisitionMonth,
    DATE_TRUNC('month', O.OrderDate) AS OrderMonth,
    SUM(O.OrderAmount) AS MonthlySpend
FROM
    Orders O
INNER JOIN
    CustomerFirstOrder CFO ON O.CustomerID = CFO.CustomerID
GROUP BY
    CFO.CustomerID,
    DATE_TRUNC('month', CFO.FirstOrderDate),
    DATE_TRUNC('month', O.OrderDate)
ORDER BY
    CFO.CustomerID, OrderMonth;
```

This query uses CTEs and date functions to prepare the data for a cohort analysis, demonstrating a strong command of SQL for complex analytical tasks.
