import requests
import pandas as pd
from bs4 import BeautifulSoup, Tag

url = 'https://scrapingclub.com/exercise/list_basic/'
request = requests.get(url)
bs = BeautifulSoup(request.text, 'lxml')

# Поиск карточек товара должне происходить по осмысленным классам. 
# В твоем случае класс 'col-lg-4 col-md-6 mb-4' не имеет никакого смысла,
# В тоже время класс 'card' несет за собой конкретный смысл "карточка товара".
# ----
# Название item говорит о том, что переменная хранит в себе только 1 значение. 
# Но де факто у тебя там хранится массив значений.
items: list[Tag] = bs.find_all('div', class_ = "card")

# Твой вариант решения задачи с словарем так же вполне рабочий, но более лаконичный вариант создания нужных тебе колонок заранее.
# Так же проверять параметры на наличии намного прощее будет, если ты уже знаешь что и куда будешь записывать 
dict_items = {
    'Name': [],
    'Price': []
}

for item in items:
    item_name: Tag = item.find('h4', class_ = 'card-title')
    
    # Дополнительные проверки и только после модификация значений
    if not item_name: item_price = None
    if isinstance(item_name, Tag): item_name = item_name.text.strip()
    
    item_price: Tag = item.find('h5')

    # Дополнительные проверки и только после модификация значений
    if not item_price: item_price = None
    if isinstance(item_price, Tag): item_price = item_price.text.strip()
    
    if not item_name and not item_price:
        continue


    # Добавление в нужные тебе колонки полученных данных
    dict_items.get('Name').append(item_name)
    dict_items.get('Price').append(item_price)
    
df_dict_items = pd.DataFrame(dict_items)
df_dict_items.to_excel('./price_items.xlsx')