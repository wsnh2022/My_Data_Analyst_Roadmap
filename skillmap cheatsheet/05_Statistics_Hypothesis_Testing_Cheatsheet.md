# Cheatsheet: Hypothesis Testing

## Core Concept
*   **Purpose:** A formal procedure to make decisions about a population based on sample data. Determines if an observed effect is likely real or due to chance.
*   **Analogy:** Court trial (assume innocence, gather evidence to prove guilt).

## The Two Hypotheses
*   **Null Hypothesis (H₀):** The default assumption; states no effect, no difference, no relationship (e.g., "New campaign has no effect on sales.").
*   **Alternative Hypothesis (H₁ or Ha):** The claim to test; states there is an effect, difference, or relationship (e.g., "New campaign increases sales.").
*   **Goal:** Collect enough evidence to **reject H₀** in favor of H₁.

## P-value
*   **Definition:** The probability of observing your data (or more extreme data) *if the null hypothesis were true*.
*   **Interpretation:**
    *   **Small p-value (≤ α):** Unlikely if H₀ true. **Reject H₀.** (Statistically significant).
    *   **Large p-value (> α):** Likely if H₀ true. **Fail to reject H₀.** (Not statistically significant).

## Significance Level (Alpha, α)
*   **Definition:** A pre-set threshold (commonly 0.05 or 5%) for deciding statistical significance.
*   **Type I Error:** Rejecting H₀ when it is true (False Positive). Probability = α.
*   **Type II Error:** Failing to reject H₀ when it is false (False Negative). Probability = β.

## Proficiency Levels Summary

### 🔵 Basic
*   Understand the core idea of testing a claim against a default assumption.
*   Define Null (H₀) and Alternative (H₁) Hypotheses.
*   Grasp the goal: to reject H₀.

### 🟡 Intermediate
*   Understand the concept and interpretation of a p-value.
*   Know how to use the significance level (α) to make a decision (reject/fail to reject H₀).
*   Identify and explain Type I and Type II errors.
*   Apply to simple A/B testing scenarios (e.g., website headline conversion).

### 🟢 Strong
*   Choose the appropriate statistical test based on data type, number of groups, and assumptions (e.g., t-test, chi-squared).
*   Differentiate between **statistical significance** (p-value) and **practical significance** (effect size).
*   Communicate the implications of findings, including limitations of statistical significance, to non-technical stakeholders.
*   Design and interpret results from real-world experiments (e.g., evaluating training programs).
