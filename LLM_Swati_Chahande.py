from typing import re

import requests
from bs4 import BeautifulSoup
import pandas as pd

# SEC 10-K URL for Apple
url = "https://www.sec.gov/Archives/edgar/data/320193/000032019321000105/aapl-20210925.htm"

# Fetch the webpage content
headers = {
    "User-Agent": "Mozilla/5.0"
}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, "html.parser")
text = soup.get_text(separator=' ', strip=True).lower()

# Define product categories and descriptions
product_categories = [
    ("iPhone 12", "Apple’s smartphone line powered by iOS."),
    ("mac", "Mac® is the Company’s line of personal computers based on its macOS® operating system."),
    ("iPad", "Apple’s line of tablets."),
    ("wearables, home and accessories", "Products like Apple Watch, Apple TV, HomePod, and accessories."),
    ("services", "Apple’s services including iCloud, Apple Music, and the App Store.")
]


products = []

# Search for each product category
for category, description in product_categories:
    if category in text:
        products.append({
            "Company Name": "Apple Inc.",
            "Stock Name": "AAPL",
            "Filing Time": "11/01/2020",
            "Product Category": category.title(),
            "Product Description": description,
            #"URL for Filing": url
        })

# Convert to DataFrame and CSV
df = pd.DataFrame(products)
csv_file = "apple_product_categories1.csv"
df.to_csv(csv_file, index=False)

# Show results
if not df.empty:
    print(f"✅ Extracted {len(df)} product categories. Saved to '{csv_file}'")
    print(df)
else:
    print("⚠️ No product categories found.")

