# Tools: Power BI DAX

DAX (Data Analysis Expressions) is the formula language used in Power BI, as well as other Microsoft BI tools like Power Pivot for Excel and SQL Server Analysis Services (SSAS).

While the simple drag-and-drop features in Power BI can answer many questions, DAX is what unlocks the true analytical power of the tool. It allows you to create sophisticated and flexible calculations that go far beyond simple sums and averages.

Think of it like this: If Power BI is the car, DAX is the engine.

---

## Calculated Columns vs. Measures

This is the most fundamental concept to understand in DAX. You can create two types of calculations:

### 1. Calculated Columns

*   **What they are:** A new column that is added to a table in your data model. The formula is calculated for each row of the table and the results are stored in the model.
*   **When to use them:** When you want to create a new, static attribute for your data that you can use in slicers, filters, or as a category in a chart. The value is calculated once during data refresh and doesn't change based on user interaction.

*   **Realistic Example: Price Tiers**
    Imagine you have a `Products` table with a `Price` column. You want to categorize your products into "Low", "Medium", and "High" price tiers.

    You would create a **calculated column** with a DAX formula like this:

    ```dax
    Price Tier = 
    IF(
        Products[Price] < 50, 
        "Low", 
        IF(
            Products[Price] < 200, 
            "Medium", 
            "High"
        )
    )
    ```

    This creates a new column in your `Products` table that you can now use to slice and dice your sales data.

### 2. Measures

*   **What they are:** A formula that is calculated *on-the-fly* at the time you use it in a visual. The result is not stored in your model and it dynamically responds to the context of the visual (i.e., the filters applied by the user).
*   **When to use them:** For almost all aggregations and calculations that you want to display in your visuals (e.g., on a card, in a bar chart, in a matrix). This is where you will do most of your work in DAX.

*   **Realistic Example: Year-Over-Year Sales Growth**
    You want to calculate the sales growth compared to the previous year. This needs to be dynamic; if the user filters the report to a specific region or product category, the calculation should update.

    You would create a **measure** using powerful **Time Intelligence** functions in DAX:

    ```dax
    Total Sales = SUM(Sales[SalesAmount])
    ```

    ```dax
    Sales Last Year = 
    CALCULATE(
        [Total Sales], 
        SAMEPERIODLASTYEAR(Dates[Date])
    )
    ```

    ```dax
    YoY Sales Growth % = 
    DIVIDE(
        [Total Sales] - [Sales Last Year], 
        [Sales Last Year]
    )
    ```

    Now you can put `YoY Sales Growth %` on a card or in a chart, and it will always show the correct, context-aware result.

---

## Key DAX Concepts and Functions

*   **Evaluation Context:** This is the "environment" in which a DAX formula is calculated. It includes the **Filter Context** (what the user has sliced/filtered) and the **Row Context** (the current row, used in calculated columns).
*   **`CALCULATE()`:** The most important function in DAX. It allows you to modify the filter context. In the example above, `CALCULATE` changes the context to be the same period in the previous year.
*   **Iterator Functions (`SUMX`, `AVERAGEX`):** These functions iterate over a table row by row and perform a calculation. For example, `SUMX(Sales, Sales[Quantity] * Sales[Price])` calculates the revenue for each row first, and then sums up the result.
*   **Time Intelligence Functions:** A family of functions (`SAMEPERIODLASTYEAR`, `DATESYTD`, etc.) that make it easy to perform common time-based calculations.

---

## Summary

-   **DAX** is the formula language for Power BI.
-   It's used to create **calculated columns** (for static, row-level attributes) and **measures** (for dynamic, aggregated calculations).
-   Understanding the difference between these two is the first and most important step.
-   Functions like `CALCULATE` and the Time Intelligence functions are what give DAX its power and flexibility.
-   While you can build simple reports without it, mastering DAX is what separates a basic Power BI user from an advanced data analyst.
