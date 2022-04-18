import requests
import pandas as pd
from bs4 import BeautifulSoup

url = 'https://scrapingclub.com/exercise/list_basic/'
request = requests.get(url)
bs = BeautifulSoup(request.text, 'lxml')
item = bs.find_all('div', class_ = "col-lg-4 col-md-6 mb-4")
dict_items = {}
for items in item:
    item_name = items.find('h4', class_ = 'card-title').text.strip()
    item_price = items.find('h5').text
    dict_items[item_name] = [item_price] 
df_dict_items = pd.DataFrame({'Name': dict_items.keys(), 'Price': dict_items.values()})
df_dict_items.to_excel('./price_items.xlsx', index = False)



