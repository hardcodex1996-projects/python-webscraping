from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
import os

# Set up Selenium with Chrome
options = webdriver.ChromeOptions()
#options.add_argument("--headless")  # Run headless (no browser UI)


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Open the apartments.com search page
driver.get("https://www.apartments.com/san-francisco-ca/")

# Wait until at least one listing is loaded
WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "li.mortar-wrapper"))
)

# Parse the page source with BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')

# Find listings
listings = soup.select("li.mortar-wrapper")

# Create listing data to export to csv.
listings_data = []

# Loop over the listings and extract needed information.
for apt in listings:
    title = apt.select_one("div.property-title")
    price = apt.select_one("p.property-pricing")
    property_beds = apt.select_one("p.property-beds")
    property_specials = apt.select("p.property-specials > span")
    property_amenities = apt.select("p.property-amenities > span")  # Adjusted selector to match amenity items

    amenities = []
    specials = []

    # Process amenities
    for amenity in property_amenities:
        # Check if amenity has text and append it
        if amenity.text.strip():
            amenities.append(amenity.text.strip())

    # Process specials
    for special in property_specials:
        # Check if special has text and append it
        if special.text.strip():
            specials.append(special.text.strip())

    # Append the data to listings_data
    listings_data.append({
        "Title": title.text.strip() if title else "N/A",
        "Price": price.text.strip() if price else "N/A",
        "Beds": property_beds.text.strip() if property_beds else "N/A",
        "Amenities": "\n".join(amenities) if amenities else "N/A",
        "Specials": "\n".join(specials) if specials else "N/A",
    })

driver.quit()


# Define the path to the 'media' folder
media_folder = os.path.join(os.path.dirname(__file__), 'media')

# Ensure the directory exists (create if not)
os.makedirs(media_folder, exist_ok=True)

# Define the file path for saving the CSV under 'media'
file_path = os.path.join(media_folder, 'listing.csv')

df = pd.DataFrame(listings_data)
df.to_csv(file_path, index=False)
print("Data exported to listing.csv")