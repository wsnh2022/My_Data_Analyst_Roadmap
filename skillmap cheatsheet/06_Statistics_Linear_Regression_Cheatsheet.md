# Cheatsheet: Linear Regression

## Core Concept
*   **Purpose:** To model the **linear relationship** between a **dependent variable (Y)** and one or more **independent variables (X)**.
*   **Goal:** Find the "line of best fit" that minimizes the distance between the line and data points.

## Simple Linear Regression
*   **Equation:** `Y = mX + c`
    *   `Y`: Predicted dependent variable.
    *   `X`: Independent variable.
    *   `m` (slope): Change in Y for a one-unit increase in X.
    *   `c` (intercept): Predicted Y when X is 0.

## Multiple Linear Regression
*   **Equation:** `Y = m1X1 + m2X2 + ... + mnXn + c`
*   **Concept:** Uses two or more independent variables to predict Y.
*   **Interpretation:** Each `m` represents the change in Y for a one-unit change in its corresponding X, *holding all other X variables constant*.

## Model Fit
*   **R-squared (R²):** Proportion of variance in Y explained by X(s). Ranges from 0 to 1 (or 0% to 100%). Higher is generally better, but context is key.

## Key Assumptions
*   **Linearity:** Linear relationship between X and Y.
*   **Independence of Errors:** Errors are not correlated.
*   **Homoscedasticity:** Constant variance of errors.
*   **Normality of Errors:** Errors are normally distributed.
*   **No Multicollinearity:** Independent variables are not highly correlated with each other (for multiple regression).

## Proficiency Levels Summary

### 🔵 Basic
*   Understand what linear regression aims to do (predict Y from X).
*   Know the simple linear regression equation (`Y = mX + c`).
*   Visually interpret a line of best fit on a scatter plot.

### 🟡 Intermediate
*   Interpret the meaning of the slope (`m`) and intercept (`c`) in a real-world context.
*   Understand R-squared (R²) as a measure of model fit and its basic interpretation.
*   Apply simple linear regression to realistic prediction problems (e.g., customer spending based on website visits).

### 🟢 Strong
*   Work with and interpret results from **multiple linear regression**.
*   Understand and conceptually check the key assumptions of linear regression.
*   Use linear regression to derive **actionable business insights**.
*   Communicate model findings, including coefficients, R², and assumptions, to stakeholders.
*   Understand the limitations (e.g., correlation vs. causation, extrapolation).
