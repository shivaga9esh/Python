# Import the whisky_web_scraping class
from Helper import whisky_web_scraping

# Create a scraper object
scraper = whisky_web_scraping()

# Scrape Data
data = scraper.scrape_whisky(number_of_pages=5)

# Sample Output
print(data)