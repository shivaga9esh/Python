# Create a scraper object

from Helper import whisky_web_scraping
from IPython.display import display

scraper = whisky_web_scraping()

# Generate a BeautifulSoup object
soup = scraper.scrape_html(base_url = 'https://www.thewhiskyexchange.com/c/40/single-malt-scotch-whisky?pg='
                           ,page = 1)

# Collecting the div objects from the first page
proudcts_info_content = scraper.get_page_content(soup)
proudcts_info_price = scraper.get_page_price(soup)

# Extracting from the div objects the name, alcohol percent, alcohol amount and price of each product
product_name = scraper.get_product_name(proudcts_info_content)
product_al_percent = scraper.get_product_alcohol_percent(proudcts_info_content)
product_al_amount = scraper.get_product_alcohol_amount(proudcts_info_content)
product_price = scraper.get_product_price(proudcts_info_price)

# Creating a DataFrame from the first page
df = scraper.create_df(names=product_name, alcohol_amount=product_al_amount,
                       alcohol_percent=product_al_percent, price= product_price )
display(df)