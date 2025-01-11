# Web Scraper Project
## Description
This project is a modular web scraper designed to crawl and extract product URLs from various e-commerce websites.
It follows the MVC (Model-View-Controller) architecture, with separate components for fetching pages,
parsing the content, logging errors, and handling utility functions like retries and rate limiting.

The scraper is built using Python and the following libraries:
``
httpx for making asynchronous HTTP requests.
BeautifulSoup for parsing HTML content.
logging for tracking errors and events.
asyncio for concurrent tasks and rate-limiting.
``
## Features
Rate Limiting: Adds a delay between requests to prevent overloading the server.
Shallow Scraping: Only fetches data from the landing page without following internal links.
Error Handling: Includes retries and logging to handle failures gracefully.
Modular Structure: Organized into MVC-like components for easier maintenance and extension.

### Project Structure
```
web-scraper/
│
├── app/                # Core scraper logic
│   ├── __init__.py        
│   ├── app.py        
│   ├── controller.py       
│   ├── models.py           
│   ├── scraper.py           
│   ├── fetcher.py          # Responsible for fetching pages 
│   ├── parser.py           # Responsible for parsing and extracting URLs
│   ├── logger.py           # Logging setup
│   └── utils.py            # Helper functions for retries, error handling, etc.
│
├── data/                   # Where the output data (JSON) will be saved
│   └── product_urls.json  
│
├── tests/                  # Unit tests for the project
│
├── requirements.txt        # Project dependencies
├── README.md               # Project overview and setup instructions
```

## Folder Descriptions

* app/: Contains the core scraping logic following the MVC architecture.
* crawler.py: The controller that manages the overall crawling process, handles URL lists, and calls fetch and parse methods.
* fetcher.py: Fetches the HTML content of pages asynchronously.
* parser.py: Parses the HTML content and extracts necessary data such as product URLs or product details.
* logger.py: Configures logging to handle errors, warnings, and info messages.
* utils.py: Contains helper functions for retries, rate limiting, error handling, etc.
* data/: Stores the output data (in JSON format).

* product_urls.json: The JSON file where scraped product URLs are saved.
* tests/: Contains unit tests to ensure the functionality of individual components.

requirements.txt: Lists the dependencies required for the project.

Current Behavior
Fetch Page: The scraper fetches the HTML content from the provided URLs asynchronously using httpx.
Parse Page: The scraper uses BeautifulSoup to parse the HTML and extract product-related information.
Rate Limiting: A delay of 2 seconds is added between requests to avoid overwhelming the server.
Shallow Scraping: Currently, the scraper only collects data from the landing page of each URL.
Error Handling: The scraper handles errors with retries, ensuring reliability when fetching pages.
Example Output
The scraper will output logs and results similar to:
```
INFO:root:Page loaded successfully: https://myntra.com
INFO:root:Page loaded successfully: https://amazon.com
INFO:root:Scraping finished: [{'domain': 'https://myntra.com', 'error': 'Failed to fetch page'}, {'domain': 'https://amazon.com', 'content': {'title': 'Sample Product', 'price': '$19.99'}}]
```

## Future Scope
* Deep Scraping: Expand the scraper to follow internal links and collect additional product details, have more than 1 layer of extraction
* Anti-Bot Handling: Integrate techniques to bypass common anti-bot mechanisms like CAPTCHAs.
* API routing: Dynamic api routing to prevent ip tracking
* Honouring robots.txt
* Data Persistence: Integrate a database (e.g., MongoDB, SQLite) to store scraped data persistently.
* Advanced Rate Limiting: Implement dynamic rate-limiting based on server response headers
* Distributed Scraping: Scale the scraping process across multiple machines or processes for large datasets.

## Installation
Clone the repository:

````
git clone <repo_url>
cd web-scraper
````

Install the required dependencies:

```
pip install -r requirements.txt
```

Usage
To run the scraper, execute the following command:
````
uvicorn app.app:app --reload --host 0.0.0.0 --port 4000
````
or
```
docker-compose up --build
```
## Curl to test
```
curl --location 'http://127.0.0.1:4000/scrape' \
--header 'Content-Type: application/json' \
--data '{
    "domains": [
        "https://myntra.com",
        "https://amazon.com"
    ]
}'
```