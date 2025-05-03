import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

base_url = "http://books.toscrape.com/catalogue/page-{}.html"
book_data = []

for page in range(1, 4):  # scrape first 3 pages
    url = base_url.format(page)
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")

    books = soup.select(".product_pod")
    for book in books:
        title = book.h3.a["title"]
        price = book.select_one(".price_color").text.strip()
        rating = book.p["class"][1]
        availability = book.select_one(".instock.availability").text.strip()
        
        book_data.append({
            "Title": title,
            "Price": price,
            "Rating": rating,
            "Availability": availability
        })

# Define the path to the 'media' folder
media_folder = os.path.join(os.path.dirname(__file__), 'media')

# Ensure the directory exists (create if not)
os.makedirs(media_folder, exist_ok=True)

# Define the file path for saving the CSV under 'media'
file_path = os.path.join(media_folder, 'books.csv')

df = pd.DataFrame(book_data)
df.to_csv(file_path, index=False)
print("Data exported to books.csv")
