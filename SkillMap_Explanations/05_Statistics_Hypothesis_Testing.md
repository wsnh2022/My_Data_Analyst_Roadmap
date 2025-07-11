# Statistics: Hypothesis Testing

Hypothesis testing is a formal procedure for investigating our ideas about the world using statistics. It is most often used by scientists to test specific predictions, called hypotheses, that arise from theories.

At its core, hypothesis testing is a way to determine if a result is **statistically significant**—that is, if it's unlikely to have occurred by random chance.

---

## The Two Hypotheses

Every hypothesis test involves two competing statements:

1.  **Null Hypothesis (H₀):** This is the default assumption or the status quo. It states that there is **no effect** or **no difference**. It's the idea that nothing interesting is going on.

2.  **Alternative Hypothesis (H₁ or Ha):** This is the claim you want to test. It states that there **is an effect** or **a difference**. It's the reason you are conducting the test.

**The Goal:** To collect enough evidence to **reject the null hypothesis** in favor of the alternative hypothesis.

---

## Realistic Example: A/B Testing a Website Button

Imagine you work for an e-commerce company. The current "Buy Now" button on your website is blue. A designer suggests that a green button might lead to more clicks.

You decide to run an A/B test to find out.

*   **Null Hypothesis (H₀):** There is no difference in the click-through rate (CTR) between the blue button and the green button. (The change has no effect).
*   **Alternative Hypothesis (H₁):** The green button has a different click-through rate than the blue button. (The change has an effect).

You show the blue button (Control) to a random sample of 1,000 visitors and the green button (Variant) to another random sample of 1,000 visitors. Here are the results:

*   **Blue Button (Control):** 100 clicks out of 1000 visitors (10% CTR)
*   **Green Button (Variant):** 125 clicks out of 1000 visitors (12.5% CTR)

The green button performed better. But is this result **statistically significant**, or could it just be due to random luck? This is where hypothesis testing comes in.

---

## The P-value

*   **What it is:** The p-value is the probability of observing your data (or something more extreme) if the **null hypothesis were true**.

*   **How to interpret it:**
    -   A **small p-value** (typically ≤ 0.05) indicates that your data is unlikely to have occurred if the null hypothesis were true. Therefore, you **reject the null hypothesis**.
    -   A **large p-value** (> 0.05) indicates that your data is consistent with the null hypothesis. Therefore, you **fail to reject the null hypothesis**.

In our A/B test example, you would run a statistical test (like a chi-squared test) on your results. Let's say the test gives you a **p-value of 0.04**.

This means there is only a 4% chance that you would see a difference this large (or larger) if the green button actually had no effect. Since 0.04 is less than our common threshold of 0.05, we can say the result is **statistically significant**.

**Conclusion:** You **reject the null hypothesis** and conclude that the green button likely does have a higher click-through rate.

---

## Cautions:

-   **Statistical significance does not equal practical significance.** A result can be statistically significant but the effect size might be too small to be useful in a real-world scenario. In our example, the 2.5% increase in CTR is likely practically significant for a business.
-   **Failing to reject the null hypothesis doesn't prove it's true.** It just means you don't have enough evidence to reject it.
-   The 0.05 threshold is a convention, not a hard rule.

---

## Summary:

Hypothesis testing is a structured way to make decisions based on data.

1.  You start with a **null hypothesis** (no effect) and an **alternative hypothesis** (an effect).
2.  You collect data.
3.  You calculate a **p-value** to determine the likelihood of your data if the null hypothesis were true.
4.  If the p-value is small enough, you **reject the null hypothesis** and conclude that your finding is **statistically significant**.
