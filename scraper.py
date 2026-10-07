import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import pandas as pd


url = "https://books.toscrape.com/"

headers = {
    "User-Agent": "Mozilla/5.0"
}

data = []
page_number = 1


while url:

    print(f"Scraping page {page_number}...")

    response = requests.get(
        url,
        headers=headers,
        timeout=10
    )

    if response.status_code != 200:
        print("Error while loading the page.")
        break

    response.encoding = "utf-8"

    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )

    books = soup.find_all(
        "article",
        class_="product_pod"
    )

    for book in books:

        title = book.h3.a["title"]

        price = book.find(
            "p",
            class_="price_color"
        ).get_text(strip=True)

        availability = book.find(
            "p",
            class_="instock availability"
        ).get_text(strip=True)

        rating = book.find(
            "p",
            class_="star-rating"
        )["class"][1]

        product_link = urljoin(
            url,
            book.h3.a["href"]
        )

        data.append({
            "Title": title,
            "Price": price,
            "Availability": availability,
            "Rating": rating,
            "Product URL": product_link
        })

    next_button = soup.find(
        "li",
        class_="next"
    )

    if next_button:

        next_link = next_button.find("a")["href"]

        url = urljoin(
            url,
            next_link
        )

        page_number += 1

    else:
        url = None


print("\nScraping finished.")
print("Total pages:", page_number)
print("Total books:", len(data))


# Convert data to a Pandas DataFrame
df = pd.DataFrame(data)


# Save the data to a CSV file
df.to_csv(
    "books.csv",
    index=False,
    encoding="utf-8-sig"
)


print("\nCSV file created successfully!")
print("Rows:", len(df))
print("Columns:", len(df.columns))


# Display first 5 rows
print("\nFirst 5 rows:")
print(df.head())