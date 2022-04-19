import requests
import pandas as pd
from typing import List
from bs4 import BeautifulSoup, Tag

url = 'https://scrapingclub.com/exercise/list_basic/'
request = requests.get(url)
request_BeautifulSoup = BeautifulSoup(request.text, 'lxml')

information_products = {
    'Name product': [],
    'Price product': []
}

tag_card: List[Tag] = request_BeautifulSoup.find_all('div', class_ = 'card') 

for info_product in tag_card:
    name_product: Tag = info_product.find('h4', class_ = 'card-title') 
   
    if not name_product: price_product = None
    if isinstance(name_product, Tag): name_product = name_product.text.strip()

    price_product: Tag = info_product.find('h5')

    if not price_product: price_product = None
    if isinstance(price_product, Tag): price_product = price_product.text.strip()

    if not name_product and not price_product:
        continue

    information_products.get('Name product').append(name_product)
    information_products.get('Price product').append(price_product)

df_information_products = pd.DataFrame(information_products)

df_information_products.to_excel('./parsing_product_name_and_price.xlsx', index = False)




