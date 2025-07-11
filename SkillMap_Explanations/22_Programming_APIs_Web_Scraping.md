# Programming (Python): APIs & Web Scraping

Often, the data you need is not in a neat CSV file or a database. It might be on a website or available through a service. APIs and web scraping are two techniques for programmatically gathering this kind_of data using Python.

---

## 1. APIs (Application Programming Interfaces)

*   **What it is:** An API is a set of rules and protocols that allows different software applications to communicate with each other. In the context of data analysis, it's a way for you to **request data from a service in a structured, predictable way**.

*   **The Analogy:** Think of an API as a waiter in a restaurant.
    -   You (your Python script) are the customer.
    -   The kitchen is the server with the data.
    -   You don't go into the kitchen yourself. You give your order (a **request**) to the waiter (the **API**).
    -   The waiter brings you your food (the **data**) in a nicely formatted way (usually **JSON**).

*   **Why use APIs?**
    -   **Structured Data:** The data you get back is almost always in a clean, machine-readable format like JSON, which is very easy to parse and load into a Pandas DataFrame.
    -   **Reliable:** APIs are designed for programmatic access, so they are generally stable and reliable.
    -   **Official:** It's the intended way to get data from the service.

### Realistic Example: Getting Weather Data from an API

Imagine you want to get the current weather for London. You could use a weather API like OpenWeatherMap.

```python
import requests
import pandas as pd

# The API endpoint (the URL you make the request to)
# You would need to sign up for an API key from the service
api_key = "YOUR_API_KEY"
city = "London"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

# Make the request to the API
response = requests.get(url)

# The API returns data in JSON format. We can convert it to a Python dictionary.
data = response.json()

# Now you can extract the information you need
temperature = data['main']['temp']
weather_description = data['weather'][0]['description']

print(f"The temperature in London is {temperature}°C.")
print(f"The weather is: {weather_description}")

# You can also easily load JSON data into a Pandas DataFrame
# (This is more useful when the API returns a list of objects)
df = pd.json_normalize(data)
print(df.head())
```

---

## 2. Web Scraping

*   **What it is:** Web scraping is the process of automatically extracting data from websites. You use a program to browse a website, just like a human, and pull out the information you need from the HTML code.

*   **When to use it:** When the data you want is on a website but there is **no API** available.

*   **The Tools:** The two most common Python libraries for web scraping are:
    -   **`requests`**: To download the HTML content of a web page.
    -   **`BeautifulSoup`**: To parse the HTML and navigate its structure to find the data you want.

### Realistic Example: Scraping Book Titles from a Website

Imagine you want to get a list of all the book titles from a website like `books.toscrape.com` (a website designed for scraping practice).

```python
import requests
from bs4 import BeautifulSoup
import pandas as pd

# 1. Get the HTML
url = "http://books.toscrape.com/"
response = requests.get(url)
html = response.content

# 2. Parse the HTML with BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# 3. Find the elements you want
# By inspecting the website's HTML, we find that each book title
# is inside an <h3> tag, which is inside an <article> tag with the class 'product_pod'
book_elements = soup.find_all('article', class_='product_pod')

# 4. Extract the text
book_titles = []
for book in book_elements:
    title = book.h3.a['title']
    book_titles.append(title)

# 5. Put it in a DataFrame
df = pd.DataFrame({'Title': book_titles})
print(df)
```

---

## Cautions and Ethics

-   **APIs are always preferred.** If a website has an API, use it. It's more reliable and respectful.
-   **Be respectful when scraping.** Don't send too many requests in a short amount of time, as you could overload the website's server. Check the website's `robots.txt` file (e.g., `www.example.com/robots.txt`) to see which parts of the site they ask you not to scrape.
-   **Websites change.** A web scraper can break if the website it's scraping changes its HTML structure.

---

## Summary

-   **APIs** are for getting data from a service in a **structured** way.
-   **Web Scraping** is for extracting data from a website when **no API is available**.
-   The `requests` library is used for both.
-   For APIs, you typically work with **JSON** data.
-   For web scraping, you use a library like **BeautifulSoup** to parse **HTML**.
-   These skills allow you to acquire a vast amount of data that would otherwise be inaccessible.
