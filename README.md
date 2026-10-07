# TP01 - Python Web Scraping Case Study

## Project Description

This project is a practical case study in Web Scraping using Python.

The objective is to collect data from an educational website, parse HTML pages, automatically navigate through all available pages, and save the extracted information into a CSV file.

The website used in this project is:

**Books to Scrape**

This website is specifically designed for practicing Web Scraping.

It contains 1,000 books distributed across 50 pages, which makes it suitable for the requirement of producing at least 1,000 rows of extracted data.

---

## Technologies and Libraries Used

- Python 3
- Requests
- BeautifulSoup4
- Pandas
- urllib.parse

---

## How the Program Works

The program performs the following steps:

1. Sends an HTTP request to the website using the `requests` library.
2. Downloads the HTML source code of each page.
3. Parses the HTML using `BeautifulSoup`.
4. Finds all book elements available on the current page.
5. Extracts information from each book.
6. Detects the `Next` page button automatically.
7. Navigates through all available pages.
8. Stores the extracted data in a Python list.
9. Converts the collected data into a Pandas DataFrame.
10. Saves the final dataset into a CSV file.

---

## Extracted Data

The following information is extracted for each book:

- Title
- Price
- Availability
- Rating
- Product URL

---

## Dataset Size

The website contains:

- 50 pages
- 20 books per page
- 1,000 books in total

Expected final result:

```text
Total pages: 50
Total books: 1000
Rows: 1000