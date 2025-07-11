# Core Data Skills Tutorial: Data Modeling

This tutorial breaks down Data Modeling skills into different proficiency levels. Your goal is to reach a **Basic (🔵)** level of understanding.

---

## 🔵 Basic Proficiency: Understanding the Concept and Simple Relationships

At this level, you understand what data modeling is and can identify basic relationships between tables.

### 1. What is Data Modeling?

*   **Concept:** Data modeling is the process of creating a visual representation or blueprint of a database or data system. It defines the structure of the data, how different pieces of data relate to each other, and the rules governing the data.
*   **Why it's essential for analysts:**
    *   **Understanding Data:** Helps you comprehend complex datasets and how information is organized.
    *   **Querying Data:** Essential for writing correct and efficient SQL queries (especially `JOIN`s) or building relationships in BI tools.
    *   **Communication:** Provides a common language for discussing data structures with engineers, other analysts, and business stakeholders.

### 2. Key Concepts

*   **Table (or Entity):** A collection of related data organized in rows and columns. Each table represents a distinct entity (e.g., `Customers`, `Products`, `Orders`).
*   **Column (or Attribute):** A specific piece of information within a table (e.g., `CustomerName`, `ProductID`, `OrderDate`).
*   **Row (or Record):** A single entry in a table, representing one instance of the entity.

### 3. Primary Keys and Foreign Keys

These are fundamental for establishing relationships between tables.

*   **Primary Key (PK):** A column (or set of columns) in a table that uniquely identifies each row in that table. It cannot contain duplicate values or NULL values.
    *   *Example:* `CustomerID` in a `Customers` table.
*   **Foreign Key (FK):** A column (or set of columns) in one table that refers to the Primary Key in another table. It establishes a link between the two tables.
    *   *Example:* `CustomerID` in an `Orders` table, which links back to the `CustomerID` in the `Customers` table.

### 4. Basic Relationships: One-to-Many

*   **Concept:** The most common type of relationship. One record in Table A can be related to many records in Table B, but one record in Table B can only be related to one record in Table A.
*   **How it's established:** By placing the Primary Key of the "one" side into the "many" side as a Foreign Key.
*   **Example:**
    *   One `Customer` can place Many `Orders`.
    *   `Customers` table (PK: `CustomerID`) <---- `Orders` table (FK: `CustomerID`)

### Realistic Example: Customer and Order Data

Imagine you have two simple tables:

**`Customers` Table:**
| CustomerID (PK) | CustomerName |
|-----------------|--------------|
| 1               | Alice        |
| 2               | Bob          |

**`Orders` Table:**
| OrderID (PK) | CustomerID (FK) | OrderAmount |
|--------------|-----------------|-------------|
| 101          | 1               | 50          |
| 102          | 2               | 75          |
| 103          | 1               | 30          |

*   **Relationship:** One-to-Many from `Customers` to `Orders`.
*   **Interpretation:** Alice (CustomerID 1) has placed two orders (101 and 103). Bob (CustomerID 2) has placed one order (102).

---

## 🟡 Intermediate Proficiency: Star Schema and Data Marts

At this level, you understand the concept of a star schema, its components (fact and dimension tables), and why it's commonly used for analytical purposes.

### 1. Star Schema

*   **Concept:** The most common and widely used data modeling technique for data warehouses and analytical systems. It's called a "star schema" because its diagram resembles a star, with a central fact table connected to multiple dimension tables.
*   **Purpose:** Designed for fast query performance and ease of understanding for business users and analysts.

### 2. Components of a Star Schema

*   **Fact Table:**
    *   **Concept:** The central table in a star schema. It contains the **quantitative, numerical data** (measures) that you want to analyze.
    *   **Characteristics:**
        *   Contains foreign keys to all associated dimension tables.
        *   Typically contains numerical measures (e.g., `SalesAmount`, `QuantitySold`, `Profit`).
        *   Usually very large (many rows).
    *   *Example:* `FactSales` table containing individual sales transactions.

*   **Dimension Tables:**
    *   **Concept:** Tables that surround the fact table. They contain the **descriptive, categorical data** (attributes) that provide context to the facts.
    *   **Characteristics:**
        *   Contains a primary key that links to the fact table's foreign key.
        *   Contains descriptive attributes (e.g., `ProductName`, `CustomerName`, `Region`, `Date`).
        *   Relatively small (fewer rows) compared to fact tables.
    *   *Examples:* `DimProduct`, `DimCustomer`, `DimDate`, `DimGeography`.

### 3. Data Mart

*   **Concept:** A subset of a data warehouse that is designed to serve a specific business function or department (e.g., a Sales Data Mart, a Marketing Data Mart).
*   **Relationship to Star Schema:** Data marts are often implemented using star schemas.

### Realistic Example: Sales Data Mart with Star Schema

You are building a data model for analyzing sales performance.

**`FactSales` Table (Central Fact Table):**
| SalesKey (PK) | DateKey (FK) | ProductKey (FK) | CustomerKey (FK) | SalesAmount | QuantitySold | Profit |
|---------------|--------------|-----------------|------------------|-------------|--------------|--------|
| 1             | 20250711     | 101             | 1                | 150.00      | 1            | 50.00  |
| 2             | 20250711     | 102             | 2                | 200.00      | 2            | 70.00  |

**`DimDate` Table (Dimension):**
| DateKey (PK) | FullDate   | Year | Month | DayOfWeek |
|--------------|------------|------|-------|-----------|
| 20250711     | 2025-07-11 | 2025 | 7     | Friday    |

**`DimProduct` Table (Dimension):**
| ProductKey (PK) | ProductName | Category    | Brand |
|-----------------|-------------|-------------|-------|
| 101             | Laptop      | Electronics | Dell  |
| 102             | Mouse       | Accessories | Logitech |

**`DimCustomer` Table (Dimension):**
| CustomerKey (PK) | CustomerName | City     | Region |
|------------------|--------------|----------|--------|
| 1                | Alice        | New York | East   |
| 2                | Bob          | London   | Europe |

*   **Benefit:** To find `Total Sales by Region`, you simply join `FactSales` to `DimCustomer` on `CustomerKey` and aggregate. This is much faster and simpler than joining many large tables in a complex transactional database.

---

## 🟢 Strong Proficiency: Advanced Modeling Concepts and Performance Considerations

At this level, you can design more complex data models, understand different relationship types, handle slowly changing dimensions, and optimize models for performance in BI tools.

### 1. Advanced Relationship Types

*   **Many-to-Many Relationships:**
    *   **Concept:** A record in Table A can relate to many records in Table B, and a record in Table B can relate to many records in Table A.
    *   **How to handle:** Typically resolved using a **bridge table** (or junction table) that contains the primary keys of both tables.
    *   *Example:* A `Student` can take Many `Courses`, and a `Course` can have Many `Students`. A `StudentCourse` bridge table would link them.
*   **Role-Playing Dimensions:**
    *   **Concept:** When a single dimension table (e.g., `DimDate`) is used multiple times in a fact table, each serving a different role.
    *   *Example:* In a `FactSales` table, you might have `OrderDateKey`, `ShipDateKey`, and `DeliveryDateKey`, all linking back to the `DimDate` table.

### 2. Slowly Changing Dimensions (SCDs)

*   **Concept:** Dimensions whose attributes change over time (e.g., a customer's address, a product's category). You need a strategy to track these changes while maintaining historical accuracy.
*   **SCD Type 1 (Overwrite):** The old value is simply overwritten with the new value. No history is kept.
*   **SCD Type 2 (New Row):** A new row is added to the dimension table for each change, with start and end dates to indicate the period of validity. This preserves history.

### 3. Data Model Optimization for BI Tools

*   **Cardinality:** Understanding the number of unique values in a column. High cardinality can impact performance.
*   **Data Types:** Using appropriate data types (e.g., `Integer` instead of `Text` for IDs) to reduce memory footprint and improve performance.
*   **Hiding Columns:** Hiding foreign key columns in dimension tables and primary key columns in fact tables from the report view to simplify the user experience.
*   **Aggregations:** Creating pre-calculated summary tables to speed up queries on large datasets.
*   **Calculated Columns vs. Measures:** Understanding when to use each for optimal performance (measures are generally preferred for aggregations).

### Realistic Example: Analyzing Customer Demographics Over Time

You have a `FactSales` table and a `DimCustomer` table. The `DimCustomer` table uses SCD Type 2 to track changes in customer demographics (e.g., `Region`).

**`DimCustomer` Table (SCD Type 2):**
| CustomerKey (PK) | CustomerName | Region   | StartDate  | EndDate    |
|------------------|--------------|----------|------------|------------|
| 1                | Alice        | East     | 2020-01-01 | 2022-12-31 |
| 1                | Alice        | West     | 2023-01-01 | 9999-12-31 |

**Your Analysis (Strong Proficiency):**

1.  **Model Design:** You ensure the `FactSales` table links to `DimCustomer` using the `CustomerKey` and that the relationship is set up correctly to handle the SCD Type 2 (e.g., using DAX `USERELATIONSHIP` or specific join logic in SQL).
2.  **Historical Analysis:** You can now accurately analyze sales by the customer's `Region` *at the time of the sale*, even if their region changed later.
    *   *Example:* You can show that Alice's sales contributed to the "East" region's performance in 2021 and to the "West" region's performance in 2024.
3.  **Performance Tuning:** You monitor query performance in your BI tool. If a report is slow, you investigate the data model, check for high-cardinality columns, and consider creating aggregations or optimizing DAX/SQL queries.

This level of proficiency allows you to design robust, flexible, and high-performing data models that can support complex analytical requirements and provide accurate historical insights, which is critical for enterprise-level data analysis.
