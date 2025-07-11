# Cheatsheet: Confidence Intervals

## Core Concept
*   **Purpose:** A range of values that is likely to contain the true value of an unknown population parameter (e.g., true mean, true proportion).
*   **Why:** Because sample statistics are only estimates and have inherent uncertainty.

## Key Components
*   **Point Estimate:** Your best single guess (e.g., sample mean).
*   **Margin of Error:** The "plus or minus" amount that creates the range.
*   **Confidence Level:** The probability that the interval contains the true parameter (e.g., 95%, 99%).

## Interpretation (e.g., 95% CI for mean is (10, 20))
*   "I am 95% confident that the true population mean is between 10 and 20."
*   **NOT:** 95% chance the true mean is in *this specific* interval.
*   **Means:** If you repeat the sampling process many times, 95% of the intervals constructed would contain the true population mean.

## Factors Affecting Interval Width
*   **Confidence Level:** Higher confidence (e.g., 99%) -> Wider interval.
*   **Sample Size:** Larger sample size -> Narrower interval (more precise estimate).
*   **Variability (Standard Deviation):** Higher variability -> Wider interval.

## Proficiency Levels Summary

### 🔵 Basic
*   Understand what a confidence interval is (a range of likely values).
*   Know its purpose (quantifying uncertainty of an estimate).
*   Interpret a given confidence interval (e.g., "I am 95% confident that...").

### 🟡 Intermediate
*   Understand the factors that make a confidence interval wider or narrower (confidence level, sample size, variability).
*   Use confidence intervals in basic practical decision-making (e.g., comparing two products, monitoring a KPI).

### 🟢 Strong
*   Calculate confidence intervals using statistical software (e.g., Python's SciPy).
*   Understand the underlying statistical assumptions for different types of confidence intervals.
*   Effectively communicate the meaning, implications, and limitations of confidence intervals to non-technical stakeholders.
*   Use confidence intervals to provide robust and actionable insights (e.g., estimating Average Order Value with precision).
