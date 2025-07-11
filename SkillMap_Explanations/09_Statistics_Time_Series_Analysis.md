# Statistics: Time Series Analysis

Time series analysis is a statistical method that deals with time-ordered data points. In other words, it's the analysis of data that is collected over a period of time.

The goal of time series analysis is to understand the underlying structure and patterns in the data to make forecasts.

---

## Components of a Time Series

A time series can be decomposed into several components:

1.  **Trend:** The overall long-term direction of the data (e.g., increasing, decreasing, or flat).

2.  **Seasonality:** A repeating pattern or cycle that occurs at a fixed and known frequency (e.g., daily, weekly, monthly, yearly).

3.  **Cyclical Component:** A pattern that is not of a fixed period, usually associated with business cycles. These cycles are longer than seasonal patterns.

4.  **Irregular or Random Component:** The unpredictable, random fluctuations in the data. This is the noise that is left over after you have accounted for the other components.

---

## Realistic Example: Monthly Sales Data

Imagine you are analyzing the monthly sales of a retail store over the past three years.

*   **Trend:** You might see a general upward trend in sales over the three years as the business grows.

*   **Seasonality:** You would likely see a spike in sales every December due to the holidays. This is a seasonal pattern that repeats every 12 months.

*   **Cyclical Component:** You might notice that sales were higher for a period of 18 months and then lower for the next 18 months, corresponding to a broader economic cycle.

*   **Irregular Component:** A sudden, one-time spike in sales in one month could be due to a promotion that you didn't run in other months. This is an irregular fluctuation.

By decomposing the time series, you can understand the different forces that are driving your sales.

---

## Key Concepts and Techniques

### a) Stationarity

A time series is **stationary** if its statistical properties (like mean, variance, and autocorrelation) are constant over time. Many time series models require the data to be stationary. If it's not, you may need to transform it (e.g., by **differencing**, which means subtracting the previous value from the current value) to make it stationary.

### b) Autocorrelation

**Autocorrelation** is the correlation of a time series with a delayed copy of itself. For example, the autocorrelation at lag 1 is the correlation between the time series and the same time series shifted by one time period. This is useful for finding repeating patterns in the data.

### c) Forecasting

The ultimate goal of time series analysis is often to make forecasts about the future.

*   **Rolling Trends / Moving Averages:** A simple forecasting technique is to calculate the average of the last *n* time periods. This is called a moving average. It helps to smooth out short-term fluctuations and highlight longer-term trends.

*   **Forecasting Models:** There are many statistical models used for time series forecasting, such as:
    -   **ARIMA (AutoRegressive Integrated Moving Average):** A very common and powerful class of models.
    -   **Exponential Smoothing:** A method that gives more weight to recent observations.
    -   **Prophet:** A forecasting tool developed by Facebook that is designed to be easy to use and robust to missing data and outliers.

---

## Summary

-   **Time Series Analysis** is the analysis of data collected over time.
-   The data can be decomposed into **trend, seasonality, cyclical, and irregular** components.
-   Understanding these components is key to building a good forecasting model.
-   Techniques like **moving averages** can be used for simple forecasting.
-   More advanced models like **ARIMA** and **Prophet** can be used for more sophisticated forecasting.
-   Time series analysis is used in many fields, including finance, economics, and weather forecasting.
