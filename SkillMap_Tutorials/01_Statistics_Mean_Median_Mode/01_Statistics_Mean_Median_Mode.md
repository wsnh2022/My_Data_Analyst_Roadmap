# Statistics Tutorial: Mean, Median, and Mode

This tutorial breaks down the concepts of Mean, Median, and Mode into different proficiency levels. Your goal is to reach a **Strong (🟢)** level of understanding.

---

## 🔵 Basic Proficiency: Understanding the Definitions

At this level, the goal is to memorize the definitions and be able to calculate each measure for a simple list of numbers.

### 1. Mean (The Average)

*   **Concept:** The sum of all values divided by the count of values.
*   **Calculation:**
    *   **Dataset:** `[2, 3, 5, 6, 9]`
    *   **Sum:** `2 + 3 + 5 + 6 + 9 = 25`
    *   **Count:** `5`
    *   **Mean:** `25 / 5 = 5`

### 2. Median (The Middle Value)

*   **Concept:** The value that separates the higher half from the lower half of a data sample. To find it, you must sort the data first.
*   **Calculation (Odd Number of Values):**
    *   **Dataset:** `[9, 2, 5, 3, 6]`
    *   **Sorted:** `[2, 3, 5, 6, 9]`
    *   **Median:** `5` (the middle number)
*   **Calculation (Even Number of Values):**
    *   **Dataset:** `[8, 1, 4, 7]`
    *   **Sorted:** `[1, 4, 7, 8]`
    *   **Median:** `(4 + 7) / 2 = 5.5` (the average of the two middle numbers)

### 3. Mode (The Most Frequent Value)

*   **Concept:** The value that appears most often in a dataset.
*   **Calculation:**
    *   **Dataset:** `[1, 2, 2, 3, 4, 4, 4, 5]`
    *   **Mode:** `4` (it appears 3 times, more than any other number)
    *   A dataset can have more than one mode (e.g., `[1, 1, 2, 2, 3]` has modes of 1 and 2) or no mode if all values appear with the same frequency.

---

## ✅ Why it matters

* **Understand the center of your data**: Mean, median, and mode are quick summaries of where your data clusters ([Medium][1]).
* **Choose your measure wisely**: Mean is great for symmetric distributions, but it gets distorted by outliers—median is more robust ([Statistics By Jim][2]). Mode shines when you're dealing with categorical or discrete values ([Scribbr][3]).
* **Detect patterns and anomalies**: A gap between mean and median hints at skewed data or outliers . Mode tells you what's most common—useful in business (like best-selling products) .

---

## 🛠 Practical workflow

1. **Load and clean your data**

   * Excel: remove blanks, ensure numeric formats
   * SQL: filter NULLs, ensure proper data types
   * Python/Pandas: use `.dropna()`, convert columns to numeric

2. **Visualize first**

   * Histograms/boxplots to see distribution shape
   * Skewed? Bimodal? Outliers?

3. **Calculate central measures**

   * Apply mean, median, mode depending on distribution type
   * Compare: if mean ≠ median, check for outliers or skewness

4. **Interpret and act**

   * Use median for skewed data (like income) ([The Official Blog of Edvotek®][4], [Medium][1], [Investopedia][5], [Statistics By Jim][2], [Data Science Stack Exchange][6], [Medium][7], [LinkedIn][8])
   * Use mode for categories (most common), e.g. survey responses&#x20;
   * Use mean for normally distributed metrics

5. **Supplement with variability**

   * Compute range, IQR, std dev to understand spread ([upchieve.org][9], [Investopedia][5])

6. **Report clearly**

   * Include visuals + central measures + spread measures
   * Note which measure best reflects your dataset and why

---

Below are the updated code snippets with comments for Excel, MySQL, Python, and Pandas.

---

### 📊 Excel (2025)

```text
=AVERAGE(A1:A100)      // mean—ignores text/blanks
=MEDIAN(A1:A100)       // median—sorts automatically
=MODE.SNGL(A1:A100)    // most frequent single value
=MODE.MULT(A1:A100)    // all modes if multiple tie
```

---

### 🐬 MySQL

```sql
-- Mean: arithmetic average
SELECT AVG(col) AS mean_val
FROM your_table;

-- Median: handles even/odd row counts
SELECT AVG(mid_vals) AS median_val FROM (
  SELECT col AS mid_vals
  FROM your_table
  ORDER BY col
  LIMIT 2 - (SELECT COUNT(*) FROM your_table) % 2
  OFFSET (SELECT (COUNT(*) - 1) / 2 FROM your_table)
) AS sub;

-- Mode: most common value
SELECT col AS mode_val
FROM your_table
GROUP BY col
ORDER BY COUNT(*) DESC
LIMIT 1;
```

---

### 🐍 Python + SciPy/NumPy

```python
import numpy as np               # efficient numeric ops
from scipy import stats          # for mode

data = [99,86,87,88,111,86,103,87,94,78,77,85,86]

mean = np.mean(data)               # arithmetic mean
median = np.median(data)           # middle value
mode = stats.mode(data).mode[0]    # most frequent value

print(mean, median, mode)
```

---

### 🐍 Python Standard Library

```python
import statistics

data = [99,86,87,88,111,86,103,87,94,78,77,85,86]

mean = statistics.mean(data)     # arithmetic average
median = statistics.median(data) # middle value
mode = statistics.mode(data)     # most frequent (unique)

print(mean, median, mode)
```

---

### 🐼 Python + Pandas

```python
import pandas as pd

df = pd.DataFrame({
    'Group': ['A','A','B','B','A'], 
    'Value': [10,12,12,15,12]
})

# ensure numeric values, drop missing
df = df[df['Value'].notna()]
df['Value'] = df['Value'].astype(float)

def first_mode(x):
    return x.mode().iloc[0]        # pick first if multiple

result = df.groupby('Group')['Value'].agg(
    mean='mean', 
    median='median', 
    mode=first_mode
)

print(result)
```

---

### 📌 Quick Pandas Shortcut

```python
import pandas as pd
df = pd.DataFrame({'x': data})
print(df['x'].mean(), df['x'].median(), df['x'].mode()[0])
```

---

### 📊 Summary Table

| Tool   | Mean                              | Median                                | Mode                                            |
| ------ | --------------------------------- | ------------------------------------- | ----------------------------------------------- |
| Excel  | `=AVERAGE(...)`                   | `=MEDIAN(...)`                        | `=MODE.SNGL(...)` / `MODE.MULT(...)`            |
| MySQL  | `AVG(col)`                        | `ORDER BY… LIMIT… OFFSET…`            | `GROUP BY… ORDER BY COUNT DESC…`                |
| Python | `np.mean()` / `statistics.mean()` | `np.median()` / `statistics.median()` | `stats.mode(...).mode[0]` / `statistics.mode()` |
| Pandas | `df['col'].mean()`                | `df['col'].median()`                  | `df['col'].mode()[0]`                           |

---

Let me know if you want to walk through a real dataset or need help choosing visuals or interpreting results.

[1]: https://medium.com/%40femiloyeseun/understand-the-reason-why-we-calculate-mean-median-and-mode-in-statistics-a8d225a3c1fa?utm_source=chatgpt.com "Understand the reason why we calculate Mean, Median and Mode ..."
[2]: https://statisticsbyjim.com/basics/measures-central-tendency-mean-median-mode/?utm_source=chatgpt.com "Mean, Median, and Mode: Measures of Central Tendency"
[3]: https://www.scribbr.com/statistics/central-tendency/?utm_source=chatgpt.com "Central Tendency | Understanding the Mean, Median & Mode - Scribbr"
[4]: https://blog.edvotek.com/2022/07/21/data-analysis-range-mean-median-and-mode/?utm_source=chatgpt.com "Data analysis: range, mean, median, and mode"
[5]: https://www.investopedia.com/terms/d/descriptive_statistics.asp?utm_source=chatgpt.com "Descriptive Statistics: Definition, Overview, Types, and Examples"
[6]: https://datascience.stackexchange.com/questions/46744/when-to-use-mean-vs-median?utm_source=chatgpt.com "When to use mean vs median - Data Science Stack Exchange"
[7]: https://medium.com/%40vishal.im/unveiling-the-basics-mean-median-mode-and-standard-deviation-in-statistics-and-machine-learning-c9c54782efd2?utm_source=chatgpt.com "Unveiling the Basics: Mean, Median, Mode, and Standard Deviation ..."
[8]: https://www.linkedin.com/advice/0/how-can-understanding-mean-median-mode-improve-your-5sapc?utm_source=chatgpt.com "Boost Data Analysis with Mean, Median, and Mode - LinkedIn"
[9]: https://upchieve.org/blog/what-are-mean-median-mode-and-range?utm_source=chatgpt.com "What are Mean, Median, Mode and Range? - UPchieve"


---

## 🟡 Intermediate Proficiency: Understanding the "Why" and the Impact of Outliers

At this level, you move beyond simple calculation to understand when to use each measure and how they are affected by the data's distribution.

### The Key Question: Which one should I use?

*   **Use the Mean when:** Your data is **symmetrical** (like a bell curve) and has no significant outliers. It's the most common measure but can be misleading.
*   **Use the Median when:** Your data is **skewed** or has **significant outliers**. The median is a more robust measure of the "typical" value in these cases.
*   **Use the Mode when:** You are working with **categorical data** (e.g., colors, sizes, names) or when you want to find the most popular item.

### The Impact of Outliers: A Realistic Example

Imagine you are analyzing the salaries of 5 employees at a small company:

`$50,000, $52,000, $55,000, $58,000, $60,000`

*   **Mean:** `$55,000`
*   **Median:** `$55,000`

Here, the mean and median are the same. The data is symmetrical.

Now, let's say the CEO's salary is included in the dataset:

`$50,000, $52,000, $55,000, $58,000, $60,000, $500,000`

*   **Mean:** `(825,000) / 6 = $137,500`
*   **Median:** `(55,000 + 58,000) / 2 = $56,500`

**The Insight:** The single outlier (the CEO's salary) has dramatically skewed the **mean**, making it a poor representation of the typical employee's salary. The **median**, however, is much less affected and gives a much more realistic picture.

---

## 🟢 Strong Proficiency: Applying and Communicating Insights

At this level, you can confidently choose the right measure, justify your choice, and use it to communicate a clear and honest story about the data.

### Scenario: Analyzing Customer Wait Times

You are an analyst for a bank, and you are analyzing customer wait times (in minutes) for two different branches.

*   **Branch A:** `[2, 3, 3, 4, 5, 5, 6, 7, 25]`
*   **Branch B:** `[4, 5, 5, 6, 6, 7, 7, 8, 9]`

**Your Analysis:**

1.  **Calculate all three measures for both branches:**
    *   **Branch A:**
        -   Mean: `(60 / 9) = 6.67` minutes
        -   Median: `5` minutes
        -   Mode: `3` and `5` minutes
    *   **Branch B:**
        -   Mean: `(57 / 9) = 6.33` minutes
        -   Median: `6` minutes
        -   Mode: `5`, `6`, and `7` minutes

2.  **Interpret the results:**
    *   If you only looked at the **mean**, you might conclude that Branch B is slightly more efficient than Branch A (6.33 min vs 6.67 min).
    *   However, you are a strong analyst, so you notice the **outlier** in Branch A's data: the `25`-minute wait. This outlier is pulling the mean up.
    *   You correctly identify that the **median** is a better measure of the typical customer experience in this case.

3.  **Communicate the Insight:**

    You don't just send the numbers. You tell the story.

    **To your manager:** "While the average wait time is slightly lower at Branch B, this is misleading. Branch A has a median wait time of just 5 minutes, which is a full minute faster than Branch B's median of 6 minutes. This means that on a typical day, customers at Branch A are getting served faster. However, Branch A suffers from occasional, very long wait times, like the 25-minute one we see here. My recommendation is to investigate the cause of these occasional long waits at Branch A, as they are hurting our overall average and represent a poor customer experience for those affected."

By using the right measure and communicating it effectively, you have provided a much more accurate and actionable insight than a simple comparison of the means would have allowed.
