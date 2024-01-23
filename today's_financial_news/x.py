# scrape ft.com for main news headlines (world, us, companies, tech, markets) and print out as bullet points

# import
from bs4 import BeautifulSoup
import requests

# WORLD: url, page, soup and output
url_world = "https://www.ft.com/world"
page_world = requests.get(url_world)
soup_world = BeautifulSoup(page_world.text, "html.parser")
category_world = soup_world.find(class_="o-teaser__tag").text
headline_world = soup_world.find(class_="o-teaser__heading").text
print("WORLD:", category_world.upper())
print(headline_world)

# # US: url, page, soup and output
url_us = "https://www.ft.com/us"
page_us = requests.get(url_us)
soup_us = BeautifulSoup(page_us.text, "html.parser")
category_us = soup_us.find(class_="o-teaser__tag").text
headline_us = soup_us.find(class_="o-teaser__heading").text
print("US:", category_us.upper())
print(headline_us)

# # COMPANIES: url, page, soup and output
url_companies = "https://www.ft.com/companies"
page_companies = requests.get(url_companies)
soup_companies = BeautifulSoup(page_companies.text, "html.parser")
category_companies = soup_companies.find(class_="o-teaser__tag").text
headline_companies = soup_companies.find(class_="o-teaser__heading").text
print("COMPANIES:", category_companies.upper())
print(headline_companies)

# TECH: url, page, soup and output
url_tech = "https://www.ft.com/technology"
page_tech = requests.get(url_tech)
soup_tech = BeautifulSoup(page_tech.text, "html.parser")
category_tech = soup_tech.find(class_="o-teaser__tag").text
headline_tech = soup_tech.find(class_="o-teaser__heading").text
print("TECH:", category_tech.upper())
print(headline_tech)

# MARKETS: url, page, soup and output
url_markets = "https://www.ft.com/markets"
page_markets = requests.get(url_markets)
soup_markets = BeautifulSoup(page_markets.text, "html.parser")
category_markets = soup_markets.find(class_="o-teaser__tag").text
headline_markets = soup_markets.find(class_="o-teaser__heading").text
print("MARKETS:", category_markets.upper())
print(headline_markets)



