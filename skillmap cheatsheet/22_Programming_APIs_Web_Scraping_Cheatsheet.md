# Cheatsheet: APIs & Web Scraping

## APIs (Application Programming Interfaces)
*   **Purpose:** Programmatic way to request structured data from a service/website.
*   **Advantages:** Structured data (JSON/XML), reliable, official method.
*   **`requests` library:** Standard Python library for HTTP requests.
    *   `requests.get(url, params=...)`: Make a GET request.
    *   `response.status_code`: HTTP status (200 for success).
    *   `response.json()`: Parse JSON response into Python dict/list.
*   **Parameters:** Used to filter/customize API responses.
*   **Authentication:** API keys, tokens (often in headers or params).
*   **Pagination:** Looping through multiple requests to get all data.

## Web Scraping
*   **Purpose:** Extract data from websites when no API is available.
*   **Method:** Parse HTML content to pull desired information.
*   **`BeautifulSoup` library:** For parsing HTML/XML documents.
    *   `BeautifulSoup(html_content, 'html.parser')`: Parse HTML.
    *   `soup.find_all('tag', class_='class_name')`: Find elements.
    *   `element.text.strip()`: Extract text.

## Ethical Considerations
*   **Prefer APIs:** Always use API if available.
*   **Be Respectful:** Don't overload servers (use `time.sleep()`).
*   **Check `robots.txt`:** See website's scraping rules.
*   **Terms of Service:** Review website's terms.
*   **Dynamic Content:** May require `Selenium` or `Playwright` for JavaScript-rendered pages.

## Proficiency Levels Summary

### 🔵 Basic
*   Understand the difference between APIs and Web Scraping.
*   Make simple `GET` requests to public APIs using the `requests` library.
*   Understand that data is often returned in JSON format.

### 🟡 Intermediate
*   Parse JSON responses from APIs into Pandas DataFrames.
*   Use API parameters to filter or customize requests.
*   Perform basic web scraping using `requests` to get HTML and `BeautifulSoup` to parse and extract data.
*   Understand when to use web scraping vs. APIs.

### 🟢 Strong
*   Work with authenticated APIs (API keys, tokens).
*   Handle API **pagination** to retrieve large datasets.
*   Build more robust web scrapers, including error handling and respecting rate limits.
*   Understand and apply ethical considerations for web scraping.
*   Conceptualize handling dynamic web content (e.g., using `Selenium`).
*   Integrate API/scraped data into a data analysis workflow.
