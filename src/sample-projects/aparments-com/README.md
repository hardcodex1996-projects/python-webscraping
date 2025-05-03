# 🏠 Apartment Listings Scraper

This project scrapes apartment listings from [apartments.com](https://www.apartments.com/) using Python, Selenium, and BeautifulSoup. It extracts key details such as property title, price, number of beds, amenities, and specials, and saves the data into a structured format.

---

## 📌 Features

- Uses **Selenium WebDriver** to load dynamic content rendered via JavaScript.
- Parses HTML content with **BeautifulSoup**.
- Collects:
  - Property title
  - Price
  - Beds
  - Specials
  - Amenities
- Outputs results into a list of dictionaries (can easily be exported to CSV or JSON).

---

## 🚀 Technologies Used

- Python 3.x
- [Selenium](https://pypi.org/project/selenium/)
- [BeautifulSoup (bs4)](https://pypi.org/project/beautifulsoup4/)
- [webdriver-manager](https://pypi.org/project/webdriver-manager/)

---

## 📦 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/apartment-scraper.git
   cd apartment-scraper
