# Cheatsheet: Matplotlib & Seaborn

## Matplotlib (Foundation)
*   **Purpose:** Comprehensive library for creating static, animated, and interactive visualizations.
*   **Key Module:** `matplotlib.pyplot` (aliased as `plt`).
*   **Core Components:** `Figure` (canvas), `Axes` (individual plot).

## Basic Matplotlib Plots
*   `plt.plot(x, y)`: Line plot.
*   `plt.scatter(x, y)`: Scatter plot.
*   `plt.bar(x, height)`: Bar chart.
*   `plt.hist(data)`: Histogram.

## Basic Matplotlib Customization
*   `plt.title("Title")`
*   `plt.xlabel("X-axis")`, `plt.ylabel("Y-axis")`
*   `plt.grid(True)`
*   `plt.show()`

## Seaborn (High-Level Interface)
*   **Purpose:** Statistical graphics library built on Matplotlib. Provides enhanced aesthetics and simplifies complex plots.
*   **Key Module:** `seaborn` (aliased as `sns`).
*   **Advantages:** Less code for complex plots, better default aesthetics, works well with Pandas DataFrames.

## Common Seaborn Plots
*   `sns.lmplot(x, y, data)`: Scatter plot with regression line.
*   `sns.barplot(x, y, data)`: Bar plot (shows mean).
*   `sns.boxplot(x, y, data)`: Box plot (distribution by category).
*   `sns.countplot(x, data)`: Count plot (frequency of categories).
*   `sns.histplot(data, x)`: Histogram (enhanced).

## Combining Matplotlib & Seaborn
*   Use Seaborn for quick, aesthetically pleasing statistical plots.
*   Use Matplotlib for fine-tuning (titles, labels, subplots, saving).

## Proficiency Levels Summary

### 🔵 Basic
*   Understand the purpose of data visualization.
*   Create simple line, scatter, bar, and histogram plots using Matplotlib.
*   Add basic titles and labels to plots.

### 🟡 Intermediate
*   Use Seaborn to create more aesthetically pleasing and statistically oriented plots (e.g., `lmplot`, `boxplot`, `countplot`).
*   Understand how Seaborn simplifies plotting compared to raw Matplotlib.
*   Combine Matplotlib functions for basic customization of Seaborn plots (e.g., `plt.title`, `plt.xlabel`).
*   Visualize relationships between variables and distributions effectively.

### 🟢 Strong
*   Create advanced Seaborn plots (e.g., `heatmap` for correlation matrices, `pairplot` for multivariate relationships, `violinplot`).
*   Master Matplotlib's `subplots()` for arranging multiple plots in a grid.
*   Fine-tune plot aesthetics and customization for publication-quality output (styles, color palettes, annotations).
*   Use visualization as a powerful tool for **data storytelling**, guiding the audience through insights.
*   Understand the strengths and weaknesses of different plot types for various data and messages.
