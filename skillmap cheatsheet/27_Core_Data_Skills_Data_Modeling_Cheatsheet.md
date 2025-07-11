# Cheatsheet: Data Modeling

## Core Concept
*   **Purpose:** Creating a conceptual blueprint of data and its relationships, especially for analytical systems.
*   **Goal for Analytics:** Organize data to be intuitive, performant, and scalable for querying and analysis.

## Key Components
*   **Table (Entity):** Collection of related data (rows/columns).
*   **Column (Attribute):** Specific piece of information.
*   **Row (Record):** Single entry in a table.
*   **Primary Key (PK):** Uniquely identifies each row in a table.
*   **Foreign Key (FK):** Column in one table that refers to the PK in another, establishing a link.

## Relationships
*   **One-to-Many (1:M):** Most common. One record in Table A relates to many in Table B (PK of A becomes FK in B).
*   **Many-to-Many (M:M):** Resolved with a **bridge table** (or junction table) containing PKs of both tables.
*   **Role-Playing Dimensions:** A single dimension table used multiple times in a fact table, each serving a different role (e.g., `DimDate` for `OrderDate`, `ShipDate`).

## Star Schema (Common for Analytics)
*   **Concept:** Central **Fact Table** connected to multiple **Dimension Tables**.
*   **Fact Table:**
    *   **Content:** Quantitative, numerical data (measures/metrics like `SalesAmount`, `QuantitySold`).
    *   **Characteristics:** Contains FKs to dimensions, typically very large (many rows).
*   **Dimension Tables:**
    *   **Content:** Descriptive, categorical data (attributes like `ProductName`, `CustomerName`, `Date`).
    *   **Characteristics:** Contains PK, relatively smaller (fewer rows).
*   **Benefits:** Simplicity, performance (efficient joins), intuitive for BI tools.

## Data Mart
*   **Concept:** A subset of a data warehouse, designed for a specific business function (often implemented with star schemas).

## Slowly Changing Dimensions (SCDs)
*   **Purpose:** Strategy to handle changes in dimension attributes over time while maintaining historical accuracy.
*   **SCD Type 1 (Overwrite):** Old value replaced by new; no history.
*   **SCD Type 2 (New Row):** New row added for each change, with start/end dates; preserves history.

## Proficiency Levels Summary

### 🔵 Basic
*   Understand what data modeling is (blueprint of data structure).
*   Identify tables, columns, rows, Primary Keys, and Foreign Keys.
*   Recognize and understand simple **one-to-many relationships** between tables.

### 🟡 Intermediate
*   Understand the concept and components of a **Star Schema** (Fact Tables and Dimension Tables).
*   Explain the purpose and benefits of using a star schema for analytical purposes.
*   Identify how a star schema simplifies querying and analysis in BI tools.
*   Understand the concept of a **Data Mart**.

### 🟢 Strong
*   Design and implement complex data models, including **many-to-many relationships** (using bridge tables) and **role-playing dimensions**.
*   Understand and apply **Slowly Changing Dimensions (SCDs)**, particularly Type 2, to maintain historical data accuracy.
*   Optimize data models for performance in BI tools (e.g., cardinality, data types, aggregations, calculated columns vs. measures).
*   Contribute to data governance by ensuring model integrity and consistency.
