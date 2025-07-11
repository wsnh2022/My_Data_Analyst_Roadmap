# Statistics: Probability and Sampling

## 1. Probability

*   **What it is:** The measure of the likelihood that an event will occur. It is expressed as a number between 0 and 1 (or 0% and 100%).
    -   A probability of 1 means the event is certain to happen.
    -   A probability of 0 means the event is certain not to happen.
    -   A probability of 0.5 means the event has a 50% chance of happening.

*   **Formula for a single event:** `P(event) = (Number of favorable outcomes) / (Total number of possible outcomes)`

*   **Realistic Example: Customer Churn**
    Imagine you have a dataset of 1,000 customers from last year. You know that 50 of them churned (cancelled their subscription).

    The probability of a randomly selected customer churning is:
    `P(churn) = 50 / 1000 = 0.05` or `5%`

    This simple probability is a powerful metric. You can now say, "Based on historical data, our customers have a 5% probability of churning."

---

## 2. Sampling

*   **What it is:** The process of selecting a subset of individuals from a larger population to estimate the characteristics of the whole population. It's a fundamental concept in data analysis because it's often impractical or impossible to collect data from everyone.

*   **Why do we sample?**
    -   **Cost and Time:** It's cheaper and faster to collect data from a sample than from the entire population.
    -   **Feasibility:** Sometimes, the population is too large to study in its entirety (e.g., all the voters in a country).

*   **The Goal of Sampling:** To get a **representative sample** that accurately reflects the characteristics of the population.

---

## Key Sampling Techniques

### a) Simple Random Sampling

*   **What it is:** Every individual in the population has an equal chance of being selected.
*   **Realistic Example: Employee Satisfaction Survey**
    Your company has 5,000 employees. You want to survey 500 of them about their job satisfaction. Using a simple random sample, you would assign a number to every employee and then use a random number generator to pick 500 names. This ensures that every employee has an equal chance of being asked.

### b) Stratified Sampling

*   **What it is:** The population is divided into subgroups (strata) based on a shared characteristic (e.g., age, gender, location). Then, a random sample is taken from each subgroup.
*   **Realistic Example: Marketing Campaign Survey**
    You want to know how different age groups are responding to a new marketing campaign. Your customer base is 60% aged 18-34, 30% aged 35-54, and 10% aged 55+. 

    If you just took a simple random sample, you might get very few people from the 55+ group by chance. With stratified sampling, you would divide your customers into these three age groups and then take a random sample from each group, perhaps in proportion to their representation. This guarantees you get enough responses from each age group to draw meaningful conclusions.

---

## Cautions and Key Concepts

*   **Sampling Bias:** This occurs when your sample is not representative of the population. For example, if you only survey people who are available during the day on a weekday, you are likely to miss out on people who work traditional 9-to-5 jobs. This would lead to biased results.
*   **Sample Size:** The size of your sample affects the reliability of your findings. A larger sample size generally leads to more accurate estimates, but there are diminishing returns.

---

## Summary

-   **Probability** quantifies the chance of an event happening.
-   **Sampling** is the practical way we collect data to make inferences about a larger population.
-   The quality of your sample is crucial. A **biased sample** will lead to **incorrect conclusions**, no matter how sophisticated your analysis is.
-   Techniques like **simple random sampling** and **stratified sampling** help you get a more representative sample.
