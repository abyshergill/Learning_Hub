Welcome to **Chapter 13: Interacting with the Web**!

So far, all of your Python programs have lived in isolation on your computer. In this chapter, we are going to connect Python to the internet. You will learn how to fetch live data from websites and extract information from web pages, turning the entire internet into your personal database.

---

## 🌍 Chapter 13: Interacting with the Web

### 1. The Requests Module (Talking to APIs)

Modern websites and services (like weather apps, financial tickers, or social media) often provide **APIs** (Application Programming Interfaces). An API is basically a backdoor that allows your code to talk directly to their servers and request raw data (usually in JSON format) without having to load a visual web page.

To talk to an API, we use the incredibly popular, third-party `requests` module. (You will need to install it first by running `pip install requests` in your terminal).

```python
import requests

# 1. Make a GET request to a public API (Let's fetch a random joke)
url = "https://official-joke-api.appspot.com/random_joke"
response = requests.get(url)

# 2. Check if the request was successful (Status Code 200 means OK)
if response.status_code == 200:
    print("Successfully connected to the server!\n")
    
    # 3. Convert the incoming JSON data into a Python Dictionary
    joke_data = response.json()
    
    # 4. Access the data using standard dictionary keys
    print(f"Setup: {joke_data['setup']}")
    print(f"Punchline: {joke_data['punchline']}")
else:
    print(f"Failed to connect. Status code: {response.status_code}")

```

### 2. Web Scraping Basics (BeautifulSoup)

What happens if you want data from a website, but they *don't* have an API? You have to extract the data directly from the raw HTML of the webpage. This is called **Web Scraping**.

CodeWithHarry introduces a powerful library called `BeautifulSoup` to do this. (Install it using `pip install beautifulsoup4`).

Here is the standard workflow for scraping a site:

1. Use `requests` to download the raw HTML of the webpage.
2. Hand that raw HTML to `BeautifulSoup` to parse (organize) it.
3. Search through the parsed HTML to find the specific tags or classes holding your data.

```python
import requests
from bs4 import BeautifulSoup

# 1. Download the HTML of a webpage (Using a dummy scraping site)
url = "http://quotes.toscrape.com/"
response = requests.get(url)

# 2. Parse the HTML using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# 3. Find the data!
# Let's say we inspect the webpage and see every quote is inside a <span> tag with the class "text"
quotes = soup.find_all("span", class_="text")

print("--- Top Quotes of the Day ---")
# Loop through the list of HTML elements we found
for quote in quotes:
    # .text strips away the HTML tags and just leaves the pure words
    print(quote.text)

```

*(Disclaimer: Always check a website's `robots.txt` file or terms of service before scraping them. Scraping too fast or scraping restricted data can get your IP address banned!)*

---

You now have the power to automate data collection from anywhere on the web. Whether you are pulling live stock prices via APIs or scraping news headlines, Python makes web interaction incredibly simple.

Are you ready for the grand finale, **Chapter 14: Concurrency**, where we will learn how to make your programs run multiple tasks at the exact same time to achieve blazing-fast speeds?