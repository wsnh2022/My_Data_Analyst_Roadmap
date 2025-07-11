# Tools: Power Query

Power Query (also known as "Get & Transform" in recent versions of Excel and Power BI) is a data connection and preparation tool. It allows you to connect to a wide variety of data sources, and then clean, transform, and reshape the data before it's even loaded into your spreadsheet or data model.

Think of it as an **automated ETL (Extract, Transform, Load) tool** built into Excel and Power BI.

---

## The Power Query Workflow

1.  **Connect:** Connect to a data source (e.g., a text/CSV file, an Excel workbook, a database, a website).
2.  **Transform:** Clean and shape the data using the intuitive Power Query Editor. Every step you take is recorded.
3.  **Load:** Load the transformed data into an Excel table, the Excel Data Model, or the Power BI Data Model.

---

## Realistic Example: Cleaning Messy Sales Data

Imagine you receive a monthly sales report as a CSV file. The file is messy and requires several cleaning steps before you can analyze it:

*   There are several blank rows at the top.
*   The column headers are in the fifth row.
*   There are extra, unnecessary columns.
*   The `SaleDate` column is formatted as text (e.g., "2025-07-11").
*   The `Region` column has inconsistent capitalization (e.g., "north", "North", "NORTH").
*   You only want to analyze sales from the "USA".

**Without Power Query**, you would have to perform these cleaning steps manually in Excel every single month. This is tedious and prone to errors.

**With Power Query**, you build a reusable query:

1.  **Connect:** In Excel or Power BI, go to `Data > Get Data > From Text/CSV` and select your file.
2.  **Transform (in the Power Query Editor):**
    *   **Remove Top Rows:** Use the `Remove Rows > Remove Top Rows` feature to get rid of the blank rows.
    *   **Promote Headers:** Use the `Use First Row as Headers` button to fix the headers.
    *   **Choose Columns:** Use `Choose Columns` to select only the columns you need.
    *   **Change Data Type:** Select the `SaleDate` column and change its type to `Date`.
    *   **Transform Text:** Select the `Region` column and use `Transform > Format > Capitalize Each Word` to make the capitalization consistent.
    *   **Filter Data:** Click the filter button on the `Country` column and select only "USA".

3.  **Load:** Click `Close & Load`. The clean, transformed data is loaded into a new Excel sheet.

**The Magic of Automation:**

Next month, when you get the new sales report, you don't have to do any of this again. You simply save the new file with the same name in the same location, go to your Excel sheet, and click `Data > Refresh All`. Power Query will automatically perform all the recorded steps on the new data in seconds.

---

## Key Features and Transformations

-   **Merge Queries:** Similar to a VLOOKUP or SQL JOIN, you can merge two tables based on a common column.
-   **Append Queries:** Stack multiple tables (with the same columns) on top of each other.
-   **Unpivot Columns:** A powerful transformation that turns wide data (e.g., a column for each month) into tall data (one column for the month and one for the value). This is often necessary for PivotTables and Power BI.
-   **Add Custom Columns:** Create new columns using formulas (written in a language called "M").
-   **Split Columns:** Split a column by a delimiter (e.g., split a `FullName` column into `FirstName` and `LastName`).

---

## Summary

-   **Power Query** is a tool for **automating data cleaning and preparation**.
-   It records your transformation steps so you can **reuse them with a single click**.
-   It can handle a wide variety of data sources and complex transformations.
-   It is a fundamental skill for anyone who works with data in Excel or Power BI, as it saves a huge amount of time and prevents errors.
