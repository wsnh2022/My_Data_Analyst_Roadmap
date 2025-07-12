# Statistics: Mean, Median, and Mode

These three are called "measures of central tendency." They all try to describe the "center" or "typical" value of a dataset in different ways.

---

## 1. Mean (The Average)

*   **What it is:** The most common type of "average." You calculate it by adding up all the values in a dataset and then dividing by the number of values.

*   **Formula:** `Mean = (Sum of all values) / (Number of values)`

*   **Realistic Example: Customer Spending**
    Imagine you run a small online store. In the last hour, five customers spent the following amounts:
    `$10, $15, $20, $25, $100`

    To find the mean spending, you add them up:
    `10 + 15 + 20 + 25 + 100 = $170`

    Then divide by the number of customers (5):
    `$170 / 5 = $34`

    The **mean** customer spending is **$34**.

*   **When to use it:** Use the mean when your data is reasonably symmetrical and doesn't have extreme outliers (like the `$100` purchase in our example).

*   **Caution:** The mean is sensitive to outliers. The `$100` purchase pulled the average up. Without it, the mean would be `(10 + 15 + 20 + 25) / 4 = $17.50`. This is a big difference!

---

## 2. Median (The Middle Value)

*   **What it is:** The value that is exactly in the middle of a dataset when it is sorted from smallest to largest.

*   **How to find it:**
    1.  Sort your data.
    2.  If there's an odd number of values, the median is the one in the middle.
    3.  If there's an even number of values, the median is the average of the two middle values.

*   **Realistic Example: Household Income**
    Let's look at the annual income for five households on a street:
    `$45,000, $50,000, $55,000, $65,000, $1,000,000`

    The **mean** income is `$243,000`, which is misleading because of the one very high-income household.

    Let's find the **median**. The data is already sorted. The middle value is:
    `$55,000`

    The **median** income is **$55,000**. This is a much better representation of the "typical" household on that street than the mean.

*   **When to use it:** The median is your best friend when you have skewed data or outliers (very high or very low values). It gives a more realistic "center" in these cases.

---

## 3. Mode (The Most Frequent Value for non- numerical data)

*   **What it is:** The value that appears most often in a dataset. A dataset can have one mode, more than one mode (multimodal), or no mode at all.

*   **How to find it:** Count the occurrences of each value. The one that appears most is the mode.

*   **Realistic Example: T-Shirt Sizes**
    You're ordering t-shirts for a company event. You survey 10 employees and get the following sizes:
    `M, L, S, M, L, XL, L, M, L, M`

    Let's count them:
    *   S: 1
    *   M: 4
    *   L: 4
    *   XL: 1

    Both **M** and **L** appear 4 times. So, this dataset has two modes: **M** and **L**. This is "bimodal".

*   **When to use it:** The mode is most useful for categorical data (data that falls into categories, like sizes, colors, or names). It's the only measure of central tendency you can use for non-numerical data.

---

## Summary: Which one to use?

*   **Mean:** Good for symmetrical data, but watch out for outliers.
*   **Median:** Best for skewed data or when there are outliers.
*   **Mode:** Use for categorical data or to find the most popular item.

A good data analyst reports more than one of these to give a fuller picture of the data. For example, "The mean income was high due to a few high earners, but the median income was a more representative $55,000."
