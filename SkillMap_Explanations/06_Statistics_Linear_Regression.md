# Statistics: Linear Regression

Linear regression is a statistical method used to model the relationship between a dependent variable and one or more independent variables. It's one of the most fundamental and widely used predictive modeling techniques.

The goal of linear regression is to find the **line of best fit** that describes the relationship between the variables.

---

## Simple Linear Regression

This involves only two variables:

-   **Independent Variable (X):** The variable we believe influences the other. Also called the predictor or explanatory variable.
-   **Dependent Variable (Y):** The variable we are trying to predict or explain. Also called the response variable.

The relationship is modeled by the equation of a straight line:

`Y = mX + c`

-   `Y` is the predicted value of the dependent variable.
-   `X` is the value of the independent variable.
-   `m` is the **slope** of the line. It represents the change in Y for a one-unit change in X.
-   `c` is the **intercept**. It's the value of Y when X is 0.

---

## Realistic Example: Predicting House Prices

Imagine you are a real estate agent and you want to predict the price of a house based on its size. You have data on recent house sales:

| House Size (sq. ft.) (X) | House Price ($) (Y) |
|--------------------------|---------------------|
| 1400                     | 245,000             |
| 1600                     | 312,000             |
| 1700                     | 279,000             |
| 1875                     | 308,000             |
| 2100                     | 405,000             |
| 2350                     | 450,000             |

You can use linear regression to find the line of best fit for this data. The algorithm will find the optimal values for the slope (`m`) and intercept (`c`) that minimize the overall error between the predicted prices and the actual prices.

Let's say the linear regression model gives you the following equation:

`Price = 200 * Size - 50000`

This means:

-   **Slope (m = 200):** For each additional square foot of size, the model predicts that the house price will increase by $200.
-   **Intercept (c = -50000):** A house with 0 square feet would be predicted to have a price of -$50,000. This doesn't make sense in the real world, which highlights that the intercept is often just a mathematical necessity for the line and may not be interpretable.

Now you can use this model to make predictions. If you have a new house on the market that is 2,000 sq. ft., you can predict its price:

`Price = 200 * 2000 - 50000 = $350,000`

---

## Multiple Linear Regression

This is an extension of simple linear regression that uses **multiple independent variables** to predict a single dependent variable.

For example, to get a more accurate house price prediction, you could include other variables:

-   Number of bedrooms
-   Number of bathrooms
-   Age of the house
-   Distance to the city center

The equation would look like:

`Price = m1*Size + m2*Bedrooms + m3*Bathrooms + m4*Age + c`

---

## Cautions and Key Concepts

-   **Assumptions:** Linear regression has several assumptions, such as a linear relationship between the variables, and that the errors (residuals) are normally distributed. It's important to check these assumptions.
-   **Overfitting:** If you use too many independent variables, your model might fit the training data perfectly but fail to generalize to new, unseen data. This is called overfitting.
-   **Correlation vs. Causation:** Like with correlation, regression models describe relationships, but they don't prove causation.

---

## Summary

-   **Linear Regression** is used to model the relationship between variables and make predictions.
-   It finds the **line of best fit** that minimizes the errors.
-   **Simple linear regression** uses one independent variable, while **multiple linear regression** uses more than one.
-   It's a powerful and interpretable tool, but you need to be aware of its assumptions and limitations.
