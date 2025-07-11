# Programming (Python) Tutorial: APIs & Web Scraping

This tutorial breaks down API and Web Scraping skills into different proficiency levels. Your goal is to reach a **Basic (🔵)** level of understanding.

---

## 🔵 Basic Proficiency: Understanding Concepts and Making Simple API Requests

At this level, you understand what APIs and web scraping are, and can make basic requests to public APIs to retrieve data.

### 1. What is an API?

*   **Concept:** API stands for Application Programming Interface. It's a set of rules and protocols that allows different software applications to communicate with each other. In data analysis, it's a way to programmatically request data from a service or website in a structured format.
*   **Why use APIs?**
    *   **Structured Data:** Data is usually returned in a clean, machine-readable format (like JSON or XML).
    *   **Reliable:** APIs are designed for programmatic access, so they are generally stable.
    *   **Official:** It's the intended way to get data from a service.

### 2. What is Web Scraping?

*   **Concept:** Web scraping is the process of automatically extracting data from websites. It involves writing code to browse a web page, parse its HTML content, and pull out the desired information.
*   **When to use it:** When there is **no API available** for the data you need on a website.

### 3. Making Simple API Requests with `requests`

*   **`requests` library:** The standard Python library for making HTTP requests.
*   **`GET` Request:** Used to retrieve data from a specified resource.

```python
import requests

# Example: Fetching data from a public API (e.g., JSONPlaceholder for fake data)
url = "https://jsonplaceholder.typicode.com/posts/1"

# Make a GET request
response = requests.get(url)

# Check if the request was successful (status code 200 means OK)
if response.status_code == 200:
    # Get the JSON data from the response
    data = response.json()
    print("Successfully fetched data:")
    print(data)
    print(f"Title: {data['title']}")
else:
    print(f"Error: {response.status_code} - {response.text}")
```

### Realistic Example: Getting a Random Joke from an API

Many public APIs don't require authentication. Let's use a simple joke API.

```python
import requests

url = "https://official-joke-api.appspot.com/random_joke"
response = requests.get(url)

if response.status_code == 200:
    joke_data = response.json()
    print("Setup:", joke_data['setup'])
    print("Punchline:", joke_data['punchline'])
else:
    print("Could not fetch joke.")
```

---

## 🟡 Intermediate Proficiency: Handling API Responses and Basic Web Scraping

At this level, you can parse JSON responses into Pandas DataFrames, handle common API parameters, and perform basic web scraping to extract data from HTML.

### 1. Parsing JSON into Pandas DataFrames

API responses are often in JSON format, which can be easily converted to a Pandas DataFrame.

```python
import requests
import pandas as pd

url = "https://jsonplaceholder.typicode.com/users"
response = requests.get(url)

if response.status_code == 200:
    users_data = response.json()
    # Convert list of dictionaries to DataFrame
    users_df = pd.DataFrame(users_data)
    print("Users DataFrame (first 5 rows):")
    print(users_df.head())

    # If JSON is nested, use json_normalize
    # df_normalized = pd.json_normalize(users_data)
else:
    print("Error fetching users.")
```

### 2. API Parameters

Many APIs allow you to filter or customize the response using parameters in the URL.

```python
# Example: Getting posts by a specific user ID
url = "https://jsonplaceholder.typicode.com/posts"
params = {'userId': 1}

response = requests.get(url, params=params)

if response.status_code == 200:
    posts_by_user = response.json()
    print(f"Found {len(posts_by_user)} posts for userId 1.")
else:
    print("Error fetching posts.")
```

### 3. Basic Web Scraping with `BeautifulSoup`

*   **`BeautifulSoup` library:** Used for parsing HTML and XML documents.
*   **Workflow:**
    1.  Make a `GET` request to get the HTML content of the page.
    2.  Parse the HTML content with `BeautifulSoup`.
    3.  Use `BeautifulSoup` methods to find the desired elements (e.g., by tag name, class, ID).

```python
import requests
from bs4 import BeautifulSoup

# Example: Scraping a simple HTML page
url = "http://books.toscrape.com/"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all <h3> tags
    h3_tags = soup.find_all('h3')
    print("First 5 H3 tags:")
    for tag in h3_tags[:5]:
        print(tag.text.strip())

    # Find elements by class
    # (You need to inspect the website's HTML to find class names)
    product_titles = soup.find_all('h3', class_='product_title')
    print("\nFirst 5 product titles:")
    for title in product_titles[:5]:
        print(title.text.strip())
else:
    print("Error fetching page.")
```

---

## 🟢 Strong Proficiency: Authenticated APIs, Pagination, and Robust Web Scraping

At this level, you can work with APIs requiring authentication, handle pagination, build more robust web scrapers, and understand ethical considerations.

### 1. Authenticated APIs

Many real-world APIs require authentication (e.g., API keys, OAuth tokens) to access data.

*   **API Keys:** Often passed as a query parameter or in the request header.
    ```python
    # Example (conceptual): Using an API key
    api_key = "YOUR_SECRET_API_KEY"
    url = "https://api.example.com/data"
    headers = {'Authorization': f'Bearer {api_key}'}
    # Or params = {'api_key': api_key}

    response = requests.get(url, headers=headers)
    # Process response...
    ```

### 2. Handling Pagination

APIs often return data in pages (e.g., 100 records per request) to manage load. You need to loop through pages to get all data.

```python
# Example (conceptual): Fetching data with pagination
all_data = []
page = 1
while True:
    url = f"https://api.example.com/items?page={page}&limit=100"
    response = requests.get(url)
    if response.status_code != 200: break

    current_page_data = response.json()
    if not current_page_data: break # No more data

    all_data.extend(current_page_data)
    page += 1

print(f"Fetched {len(all_data)} items across all pages.")
```

### 3. Robust Web Scraping

*   **Handling Dynamic Content (JavaScript):** For websites that load content dynamically with JavaScript, `requests` and `BeautifulSoup` alone might not be enough. You might need tools like `Selenium` or `Playwright` to control a web browser programmatically.
*   **Error Handling:** Implement `try-except` blocks to handle network errors, HTTP errors, or parsing errors.
*   **Rate Limiting:** Be respectful of the website's servers. Add `time.sleep()` between requests to avoid being blocked.
*   **User-Agent:** Set a `User-Agent` header in your requests to mimic a real browser.

```python
import requests
from bs4 import BeautifulSoup
import time

# Example: More robust scraping (conceptual)
url = "http://books.toscrape.com/catalogue/page-1.html"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

book_titles = []
for i in range(1, 3): # Scrape first 2 pages
    page_url = f"http://books.toscrape.com/catalogue/page-{i}.html"
    try:
        response = requests.get(page_url, headers=headers, timeout=10)
        response.raise_for_status() # Raise HTTPError for bad responses (4xx or 5xx)
        soup = BeautifulSoup(response.content, 'html.parser')
        for title_tag in soup.find_all('h3'):
            book_titles.append(title_tag.a['title'])
        time.sleep(1) # Be polite, wait 1 second between requests
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {page_url}: {e}")
        break

print(f"Scraped {len(book_titles)} book titles.")
```

### 4. Ethical Considerations

*   **`robots.txt`:** Check the website's `robots.txt` file (e.g., `www.example.com/robots.txt`) to see which parts of the site they allow or disallow scraping.
*   **Terms of Service:** Always review the website's terms of service.
*   **Data Usage:** Be mindful of how you use the scraped data, especially if it contains personal information.

By mastering these advanced techniques, you can effectively acquire data from a wide range of online sources, which is a critical skill for any data analyst.
