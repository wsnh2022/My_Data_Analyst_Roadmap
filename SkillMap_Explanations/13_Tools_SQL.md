# Tools: SQL

SQL (Structured Query Language) is the standard language for interacting with relational databases. As a data analyst, SQL is your primary tool for **requesting, retrieving, and manipulating data** from these databases.

Most of the world's corporate data is stored in relational databases, so knowing SQL is not just a valuable skill—it's a fundamental requirement for almost any data analysis job.

---

## Core SQL Commands (Keywords)

SQL is made up of several key commands. Here are the most important ones for a data analyst:

*   **`SELECT`**: Used to select data from a database. You specify the columns you want.
*   **`FROM`**: Specifies the table you are selecting the data from.
*   **`WHERE`**: Used to filter records. You specify a condition, and only the records that meet that condition are returned.
*   **`GROUP BY`**: Groups rows that have the same values in specified columns into summary rows. It's often used with aggregate functions.
*   **`ORDER BY`**: Used to sort the result set in ascending (`ASC`) or descending (`DESC`) order.
*   **`JOIN`**: Used to combine rows from two or more tables based on a related column between them.

---

## Realistic Example: Querying a Customer Database

Imagine you have two tables in your database:

1.  **`Customers`** table:

| CustomerID | CustomerName | Country |
|------------|--------------|---------|
| 1          | John Smith   | USA     |
| 2          | Maria Garcia | Mexico  |
| 3          | Wei Chen     | China   |

2.  **`Orders`** table:

| OrderID | CustomerID | OrderDate  | OrderAmount |
|---------|------------|------------|-------------|
| 101     | 1          | 2025-07-10 | 150         |
| 102     | 2          | 2025-07-11 | 200         |
| 103     | 1          | 2025-07-11 | 50          |

**Your Task:** You want to find the total amount spent by each customer from the USA and order the results from highest to lowest spending.

**Your SQL Query:**

```sql
SELECT
    c.CustomerName,
    SUM(o.OrderAmount) AS TotalSpent
FROM
    Customers c
JOIN
    Orders o ON c.CustomerID = o.CustomerID
WHERE
    c.Country = 'USA'
GROUP BY
    c.CustomerName
ORDER BY
    TotalSpent DESC;
```

**Let's break down this query:**

1.  **`SELECT c.CustomerName, SUM(o.OrderAmount) AS TotalSpent`**: We are selecting the customer's name and calculating the sum of their order amounts. We are giving this new calculated column an alias `TotalSpent` for clarity.

2.  **`FROM Customers c JOIN Orders o ON c.CustomerID = o.CustomerID`**: We are joining the `Customers` table (aliased as `c`) with the `Orders` table (aliased as `o`). The `JOIN` is made on the `CustomerID` column, which exists in both tables.

3.  **`WHERE c.Country = 'USA'`**: We are filtering the results to include only customers from the USA.

4.  **`GROUP BY c.CustomerName`**: This is the key part for aggregation. It tells the database to group all the orders by customer name and then perform the `SUM()` function on each group.

5.  **`ORDER BY TotalSpent DESC`**: We are sorting the final result set by our new `TotalSpent` column in descending order (highest first).

**The Result:**

The query would return a single row for John Smith, as he is the only customer from the USA, showing his total spending of $200.

---

## Why SQL is Essential

-   **Direct Data Access:** It allows you to get the exact data you need, rather than relying on someone else to provide you with a CSV file.
-   **Efficiency:** You can perform filtering, aggregation, and joins on the database server, which is much more efficient than pulling millions of rows of raw data into Excel or Python to do the same work.
-   **Foundation for other tools:** Tools like Power BI and Tableau often generate SQL queries in the background. Understanding SQL helps you understand how these tools work and troubleshoot problems.

---

## Summary

-   **SQL** is the language of databases.
-   It allows you to **`SELECT`** data **`FROM`** tables, **`WHERE`** certain conditions are met.
-   You can **`JOIN`** multiple tables together and use **`GROUP BY`** to perform aggregations.
-   It is a non-negotiable, foundational skill for any data analyst.
