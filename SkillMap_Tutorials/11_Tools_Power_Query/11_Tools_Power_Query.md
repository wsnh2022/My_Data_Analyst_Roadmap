# Tools Tutorial: Power Query

This tutorial breaks down Power Query skills into different proficiency levels. Your goal is to reach an **Intermediate (🟡)** level of understanding.

---

## 🔵 Basic Proficiency: Connecting to Data and Simple Transformations

At this level, you understand what Power Query is for, can connect to common data sources, and perform basic cleaning and shaping operations.

### 1. What is Power Query?

*   **Concept:** Power Query (also known as "Get & Transform" in Excel) is a data connection and preparation tool. It allows you to **Extract, Transform, and Load (ETL)** data from various sources into Excel or Power BI.
*   **Why use it?** To automate repetitive data cleaning tasks, combine data from different sources, and ensure data consistency.

### 2. Connecting to Data Sources

*   **In Excel:** Go to `Data` tab > `Get Data`.
*   **In Power BI Desktop:** Go to `Home` tab > `Get Data`.
*   **Common Sources:** Excel Workbook, Text/CSV, Folder, Web, SQL Server Database.

### 3. The Power Query Editor Interface

*   **Queries Pane:** Lists all your queries.
*   **Data Preview Pane:** Shows a preview of your data.
*   **Query Settings Pane:** Shows the `Properties` (query name) and `Applied Steps` (a list of all transformations you've performed).

### 4. Basic Transformations

*   **Remove Columns:** Select a column and click `Remove Columns`.
*   **Choose Columns:** Select only the columns you want to keep.
*   **Remove Rows:** Remove top/bottom rows, blank rows, or duplicate rows.
*   **Use First Row as Headers:** Promotes the first row of data to become the column headers.
*   **Change Data Type:** Crucial for ensuring columns are correctly interpreted (e.g., Text to Number, Text to Date).
*   **Filter Rows:** Filter data based on values in a column (e.g., keep only rows where `Region` is "East").

### Realistic Example: Importing and Cleaning a CSV File

You receive a monthly sales CSV file. It has some introductory rows you don't need, and the `Date` column is imported as text.

1.  **Get Data:** `Data > Get Data > From Text/CSV`, select your file.
2.  **Remove Top Rows:** In the Power Query Editor, `Home > Remove Rows > Remove Top Rows`, enter the number of rows to skip.
3.  **Use First Row as Headers:** Click `Use First Row as Headers`.
4.  **Change Data Type:** Select the `Date` column, then `Home > Data Type` and choose `Date`.
5.  **Load:** Click `Close & Load` to bring the cleaned data into Excel.

**The Magic:** Next month, when you get the new CSV, just save it with the same name, and click `Data > Refresh All` in Excel. Power Query will re-run all these steps automatically.

---

## 🟡 Intermediate Proficiency: Combining Data and Advanced Transformations

At this level, you can combine data from multiple sources, perform more complex transformations, and understand the importance of the `Applied Steps`.

### 1. Combining Queries

*   **Merge Queries (Joins):** Combines two tables based on a common column (like a SQL JOIN or Excel VLOOKUP).
    *   **Types:** Inner, Left Outer, Right Outer, Full Outer, Left Anti, Right Anti.
    *   **Realistic Example:** Merge a `Sales` table (with `ProductID`) with a `Products` table (with `ProductID` and `ProductName`) to add product names to your sales data.
*   **Append Queries (Unions):** Stacks two or more tables on top of each other (like a SQL UNION).
    *   **Realistic Example:** Combine sales data from `Sales_Q1.xlsx`, `Sales_Q2.xlsx`, `Sales_Q3.xlsx`, and `Sales_Q4.xlsx` into a single annual sales table.

### 2. Advanced Transformations

*   **Split Column:** Split a column by a delimiter (e.g., split "John Doe" into "John" and "Doe" by space).
*   **Group By:** Aggregate data based on one or more columns (like SQL GROUP BY or Excel PivotTable).
    *   **Realistic Example:** Group sales data by `Region` and `Product Category` to sum `Sales Amount`.
*   **Unpivot Columns:** Transforms columns into rows. This is crucial for converting "wide" data (e.g., a column for each month) into "tall" data, which is often required for proper analysis in BI tools.
    *   **Realistic Example:** You have a table where each column is a month (`Jan Sales`, `Feb Sales`, `Mar Sales`). Unpivot these columns to get two columns: `Month` and `Sales Value`.
*   **Add Custom Column:** Create a new column using a formula (written in M language, but often built with a GUI).
    *   **Realistic Example:** Create a `Profit Margin` column: `[Profit] / [Sales]`.

### 3. Understanding Applied Steps

*   **Concept:** Every transformation you perform in Power Query Editor is recorded as an "Applied Step." This creates a reproducible workflow.
*   **Editing Steps:** You can click on any step to see what it did, rename it, or delete it. This allows for easy modification and debugging of your data preparation process.
*   **Order Matters:** The order of steps is crucial. Changing the order can significantly alter the outcome.

### Realistic Example: Combining and Cleaning Regional Sales Data

You have sales data for `North Region` and `South Region` in separate Excel sheets. Both sheets have `Date`, `Product`, `Quantity`, and `Revenue` columns, but the `Product` column in the North Region sheet has inconsistent casing.

1.  **Create Queries for Each Region:** Get data from each Excel sheet, creating two separate queries (`North Sales`, `South Sales`).
2.  **Clean `North Sales`:** In the `North Sales` query, select the `Product` column, then `Transform > Format > Capitalize Each Word` to standardize casing.
3.  **Append Queries:** Create a new query by appending `North Sales` and `South Sales` to create a `Combined Sales` query.
4.  **Group and Summarize:** In the `Combined Sales` query, use `Group By` to sum `Revenue` by `Product` and `Date`.
5.  **Load:** Load the `Combined Sales` query into Excel or Power BI.

---

## 🟢 Strong Proficiency: Advanced M Language, Error Handling, and Performance Optimization

At this level, you can write and modify M code directly, handle complex data scenarios, optimize query performance, and understand Power Query's role in enterprise data solutions.

### 1. M Language (Power Query Formula Language)

*   **Concept:** The functional programming language that Power Query uses behind the scenes. Every action you perform in the GUI generates M code.
*   **Advanced Editor:** You can view and edit the M code directly by going to `View > Advanced Editor`.
*   **Custom Functions:** Write your own M functions to encapsulate complex logic and reuse it across multiple queries.
    *   **Realistic Example:** Create a custom function to clean and transform a specific type of messy CSV file, then apply it to all files in a folder.

### 2. Error Handling

*   **Identifying Errors:** Power Query highlights errors (e.g., data type conversion failures).
*   **Replacing Errors:** Use `Replace Errors` to substitute error values with nulls or specific values.
*   **Removing Errors:** Use `Remove Rows > Remove Errors` to delete rows containing errors.
*   **Try...Otherwise:** Use M language's `try ... otherwise` construct for more sophisticated error handling within custom columns or functions.

### 3. Query Performance Optimization

*   **Query Folding:** The most important concept. Power Query tries to translate your transformations back into the source database's native query language (e.g., SQL). This means the data is filtered and aggregated at the source, reducing the amount of data transferred and processed by Power Query.
    *   **How to ensure it:** Perform filtering and column removal steps early in your query. Avoid transformations that break query folding (e.g., merging queries from different data sources early on, or certain custom M functions).
*   **Disable Load:** For intermediate queries that are only used to feed other queries (e.g., a `Products` query that is merged into `Sales`), disable their load to the data model to save memory and improve performance.

### 4. Parameterization

*   **Concept:** Use parameters to make your queries dynamic (e.g., a parameter for a file path, a database name, or a filter value).
*   **Realistic Example:** Create a parameter for the `Year` in your sales report, so users can easily change the year without modifying the query.

### Realistic Scenario: Building a Dynamic Sales Report from a Folder of Files

You receive monthly sales reports as separate Excel files in a folder. Each file has the same structure, but you only want to analyze data from a specific year, and you need to handle potential data entry errors.

**Your Approach (Strong Proficiency):**

1.  **Connect to Folder:** `Get Data > From File > From Folder`, select the folder containing the monthly files.
2.  **Combine & Transform:** Power Query automatically creates a function to combine the files. You then refine this function to include necessary cleaning steps (e.g., changing data types, removing unnecessary columns).
3.  **Add Parameter for Year:** Create a new parameter called `ReportYear`.
4.  **Filter by Parameter:** Add a filter step to your combined query to only include data where the `Date` column's year matches the `ReportYear` parameter.
5.  **Error Handling:** Add steps to replace errors in numerical columns with nulls, or to remove rows with critical errors.
6.  **Optimize:** Ensure query folding is happening where possible (e.g., by filtering the year early).
7.  **Load:** Load the final, cleaned, and filtered data into your data model.

This strong proficiency allows you to build robust, automated, and flexible data pipelines directly within Excel or Power BI, significantly reducing manual effort and improving data reliability.
