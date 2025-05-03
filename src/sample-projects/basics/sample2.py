#Example 1: Scraping News Headlines (from BBC News)

import requests
from bs4 import BeautifulSoup

url = "https://www.bbc.com/news"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Find headline tags (BBC often uses <h3> for headlines)
headlines = soup.find_all("h2", attrs={"data-testid": "card-headline"})

for h in headlines:
    text = h.get_text().strip()
    if text:
        print("📰", text)
