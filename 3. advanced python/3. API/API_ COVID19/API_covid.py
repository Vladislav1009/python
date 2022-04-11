# Задачи:
# - Получить ключ для работы с api
# - Изучить предметную область
# - Создать функции для получения всех данных по 3 методам запросов (Countries, Statistics, History)
# - Создать возможность сохранения полученных данных в виде excel (Используя pandas)

#  Ключ --> c784b67935mshd9a7f3cab6995ebp190aafjsnacc724b616ce

import requests
import datetime
import pandas as pd

class Covid():

    def __init__(self, api_key: str, rapidapi: str):
        """
        Конструктор класса, который автоматически выводится при создании объектов

        Args:
            api_key([str], обязательный параметр) - ключ. Берем на apiRapid;
            rapidapi([str]), обязательный параметр) - ссылка на сайт, надо для использования headers при запросе.
        """
        self.api_key = api_key
        self.url_covid = f'https://covid-193.p.rapidapi.com'
        self.rapidapi = rapidapi
        self.headers = {
            'x-rapidapi-host': self.rapidapi,
            'x-rapidapi-key': self.api_key
        }

    def get_countries(self, country: str = None):
        """
        Выводит список стран затронутых covid_19. Есть возможность не выводить список, а запросить конкретную строку.

        Args:
            country([country], не обязательный параметр) - если None, то выводится список стран, если не None, тогда проверка конкретной страны
        """
        params = {'search': country}
        response = requests.request('GET', f'{self.url_covid}/countries', headers = self.headers, params = params)
        return response.json()
        
    def get_statistics(self, country:str = None):
        """
        Отражает текущий статус распространения коронавируса во всех странах. Можно фильтровать country, чтобы получить его текущий статус.

        Args:
            country([country], не обязательный параметр) - если None, то выводится список стран, если не None, тогда проверка конкретной страны
        """
        params = {'country': country}
        response = requests.request('GET', f'{self.url_covid}/statistics', headers = self.headers, params = params)
        return response.json()

    def get_history(self, country: str, date: str = None): # Надо обработать случай, если country будет не указан, сейчас это просто исключение
        """
        Запрос всей истории статистики для страны. 

        Args:
            country([country], обязательный параметр) - название страны;
            date([], не обязательный) - Дата и время
        """
        params = {
            'country': country,
            'day': date
        }
        response = requests.request('GET', f'{self.url_covid}/history', headers = self.headers, params = params)
        return response.json()

    def df_func(self, func):
        """
        Преобразует результаты функций запроса в Data Frame

        Args:
            func([Any], oбязательный) - объект class Covid()
        """  
        return pd.DataFrame(func.get('response'))
             

rapidapi_host = 'covid-193.p.rapidapi.com'
API_KEY = "c784b67935mshd9a7f3cab6995ebp190aafjsnacc724b616ce"
country = 'USA'
date = datetime.date(2022, 1, 1).strftime('%Y-%m-%d')

covid_19 = Covid(api_key = API_KEY, rapidapi = rapidapi_host)
countries_obj = covid_19.get_countries()
statistics_obj = covid_19.get_statistics()
history_obj = covid_19.get_history(country)
df_obj = covid_19.df_func(statistics_obj)

df_obj.to_excel('./draft_api.xlsx', index = False)

