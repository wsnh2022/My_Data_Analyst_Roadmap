# Cheatsheet: Time Series Analysis

## Core Concept
*   **Definition:** A sequence of data points collected at successive, equally spaced points in time. Order matters.
*   **Purpose:** Understand underlying patterns to make forecasts.

## Components of a Time Series
*   **Trend:** Long-term increase or decrease (general direction).
*   **Seasonality:** Repeating pattern over a fixed, known period (e.g., daily, weekly, yearly).
*   **Irregular/Random (Noise):** Unpredictable fluctuations after accounting for trend and seasonality.

## Key Concepts
*   **Stationarity:** Statistical properties (mean, variance, autocorrelation) remain constant over time. Many models require this.
    *   **Differencing:** Subtracting previous value to remove trend/seasonality and achieve stationarity.
*   **Autocorrelation:** Correlation of a time series with a lagged version of itself. Helps identify patterns (e.g., seasonality).

## Simple Forecasting Techniques
*   **Moving Averages:** Smooths out short-term fluctuations by averaging data points over a specified window.

## Advanced Forecasting Models (Conceptual)
*   **ARIMA (AutoRegressive Integrated Moving Average):** Combines AR (past values), I (differencing), MA (past errors).
*   **Exponential Smoothing:** Gives more weight to recent observations.
*   **Prophet (by Facebook):** Handles seasonality, holidays, missing data well; user-friendly.

## Proficiency Levels Summary

### 🔵 Basic
*   Define what a time series is.
*   Identify the basic components: Trend, Seasonality, Irregular/Random.
*   Provide simple examples of time series data.

### 🟡 Intermediate
*   Visually identify trend, seasonality, and irregular components in a time series plot.
*   Apply simple forecasting techniques like moving averages to smooth data and make short-term forecasts.
*   Understand the concept of smoothing and its purpose.

### 🟢 Strong
*   Understand the concept of **stationarity** and its importance for time series modeling.
*   Use **autocorrelation** to identify patterns and model components.
*   Be aware of and conceptually understand advanced forecasting models (ARIMA, Exponential Smoothing, Prophet).
*   Apply time series analysis to real-world forecasting problems (e.g., product demand, website traffic) and evaluate model accuracy.
*   Communicate forecasts and their associated uncertainties to stakeholders.
