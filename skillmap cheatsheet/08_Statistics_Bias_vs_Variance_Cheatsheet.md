# Cheatsheet: Bias vs. Variance

## Bias
*   **Concept:** Error from incorrect assumptions in the learning algorithm. How far off target your model is *on average*.
*   **Symptom:** **Underfitting** (model is too simple, performs poorly on both training and new data).
*   **Analogy:** Archer's arrows are tightly grouped but consistently off the bullseye.

## Variance
*   **Concept:** Error from sensitivity to small fluctuations in the training data. How spread out your model's predictions are.
*   **Symptom:** **Overfitting** (model learns noise in training data, performs well on training but poorly on new data).
*   **Analogy:** Archer's arrows are scattered all over the target, even if centered around the bullseye.

## The Bias-Variance Tradeoff
*   **Tension:** Reducing bias often increases variance, and vice-versa.
*   **Goal:** Find the "sweet spot" – a model complex enough to capture true patterns (low bias) but not so complex it learns noise (low variance).

## Diagnosing
*   **High Bias (Underfitting):** High training error, high validation/test error (similar).
*   **High Variance (Overfitting):** Low training error, high validation/test error (much higher).

## Strategies to Manage
*   **To Reduce Bias (Underfitting):** Increase model complexity, add more features, decrease regularization.
*   **To Reduce Variance (Overfitting):** Get more training data, reduce model complexity, increase regularization, feature selection, cross-validation.

## Proficiency Levels Summary

### 🔵 Basic
*   Understand bias and variance conceptually (e.g., using the archer analogy).
*   Differentiate between high bias (consistently wrong) and high variance (inconsistent).

### 🟡 Intermediate
*   Connect high bias to **underfitting** and high variance to **overfitting**.
*   Understand how model complexity influences the bias-variance tradeoff.
*   Explain the implications of underfitting and overfitting in realistic scenarios (e.g., customer churn prediction).

### 🟢 Strong
*   Diagnose whether a model is suffering from high bias or high variance by analyzing training and validation/test errors.
*   Apply specific strategies to mitigate high bias (e.g., using more complex models) or high variance (e.g., adding more data, regularization).
*   Communicate the bias-variance tradeoff and its implications for model performance and reliability to stakeholders.
*   Optimize models by balancing bias and variance for better generalization to unseen data.
