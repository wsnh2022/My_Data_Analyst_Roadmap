# Statistics: Correlation (Pearson)

Pearson correlation coefficient (often denoted as *r*) is a measure of the linear relationship between two continuous variables. It tells you both the strength and the direction of the relationship.

-   **Strength:** The value of *r* ranges from -1 to 1.
    -   A value close to 1 means a strong positive linear relationship.
    -   A value close to -1 means a strong negative linear relationship.
    -   A value close to 0 means a weak or no linear relationship.
-   **Direction:**
    -   A positive *r* means that as one variable increases, the other tends to increase.
    -   A negative *r* means that as one variable increases, the other tends to decrease.

---

## Realistic Example: Ice Cream Sales and Temperature

Imagine you own an ice cream shop and you want to see if there's a relationship between the daily temperature and your sales. You collect data for a week:

| Day       | Temperature (°C) | Ice Cream Sales ($) |
|-----------|------------------|---------------------|
| Monday    | 20               | 250                 |
| Tuesday   | 22               | 280                 |
| Wednesday | 25               | 320                 |
| Thursday  | 28               | 380                 |
| Friday    | 30               | 420                 |
| Saturday  | 32               | 450                 |
| Sunday    | 26               | 350                 |

If you calculate the Pearson correlation coefficient for this data, you would get a value of approximately **r = 0.98**.

This is very close to 1, which indicates a **strong positive linear relationship**. As the temperature goes up, your ice cream sales also go up in a very predictable, linear way.

---

## When to use it:

-   When you want to measure the strength and direction of a *linear* relationship between two *continuous* variables.
-   Examples:
    -   Height and weight
    -   Years of experience and salary
    -   Advertising spend and revenue

---

## Cautions:

-   **Correlation is not causation!** This is the most important rule. Just because two variables are correlated, it doesn't mean one causes the other. In our example, the hot weather *likely* causes an increase in sales, but the correlation itself doesn't prove it. There could be another factor (a "lurking variable"), like a summer festival happening that week, that is driving both temperature (people are outside) and sales.
-   **Only measures linear relationships.** If the relationship is curved (e.g., performance vs. stress, where performance is high at moderate stress but low at very low or very high stress), Pearson correlation will be close to 0, even though there is a clear relationship.
-   **Sensitive to outliers.** Just like the mean, a single outlier can significantly affect the correlation coefficient.

---

## Summary:

Pearson correlation is a powerful tool to quantify the linear relationship between two continuous variables. Always remember to visualize your data with a scatter plot to check for linearity and outliers, and never assume causation from correlation.
