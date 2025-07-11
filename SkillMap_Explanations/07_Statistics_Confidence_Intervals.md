# Statistics: Confidence Intervals

A confidence interval is a range of values that you are fairly sure contains the true value of a population parameter. It's a way of quantifying the uncertainty of a sample statistic.

When you take a sample and calculate a statistic (like a mean or proportion), you know that the statistic is just an estimate of the true population parameter. A confidence interval gives you a range around that estimate.

---

## Key Components of a Confidence Interval

1.  **Point Estimate:** The sample statistic you are using to estimate the population parameter (e.g., the sample mean).
2.  **Margin of Error:** The "plus or minus" part that you add to and subtract from the point estimate. It represents the uncertainty of your estimate.
3.  **Confidence Level:** The probability that the confidence interval contains the true population parameter. This is usually expressed as a percentage, with 95% being the most common.

**Confidence Interval = Point Estimate ± Margin of Error**

---

## Realistic Example: Average Customer Age

Imagine you want to know the average age of all customers who shop at your online store. Your entire customer base is the **population**. It's too difficult to get the age of every single customer, so you take a **sample** of 100 customers.

You calculate the average age of your sample:

*   **Sample Mean (Point Estimate):** 35 years old

This is your best guess for the average age of all your customers, but it's unlikely to be exactly right. To account for the uncertainty, you calculate a **95% confidence interval**.

Let's say the calculation gives you a **margin of error** of **± 2 years**.

Your 95% confidence interval is:

`35 ± 2 years`

This means your confidence interval is **(33, 37)**.

**How to interpret this:**

You can say, "I am 95% confident that the true average age of all my customers is between 33 and 37 years old."

**What does "95% confident" really mean?**

This is a subtle but important point. It means that if you were to repeat this process many times (take many samples and calculate a confidence interval for each), 95% of those intervals would contain the true population mean. It does *not* mean there is a 95% probability that the true mean is in your specific interval.

---

## Factors Affecting the Margin of Error (and the width of the interval)

-   **Confidence Level:** A higher confidence level (e.g., 99%) will result in a wider interval. To be more confident, you need to give a wider range of plausible values.
-   **Sample Size:** A larger sample size will result in a smaller margin of error and a narrower interval. More data gives you a more precise estimate.
-   **Variability in the data (Standard Deviation):** More variability in the data will lead to a larger margin of error and a wider interval.

---

## Summary

-   A **confidence interval** provides a range of plausible values for a population parameter.
-   It helps you understand the **uncertainty** associated with a sample statistic.
-   It is expressed as a **point estimate ± margin of error**.
-   The **confidence level** (e.g., 95%) tells you how often this method will capture the true population parameter in the long run.
-   Confidence intervals are crucial for making sound decisions based on sample data.
