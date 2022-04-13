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

    def __init__(self, api_key: str):
        """
        Конструктор класса, который автоматически выводится при создании объектов

        Args:
            api_key([str], обязательный параметр) - ключ. Берем на apiRapid;
            rapidapi([str]), обязательный параметр) - ссылка на сайт, надо для использования headers при запросе.
        """
        self.api_key = api_key
        self.url_covid = f'https://covid-193.p.rapidapi.com'
        self.headers = {
            'x-rapidapi-host': 'covid-193.p.rapidapi.com',
            'x-rapidapi-key': self.api_key
        }

    def get_countries(self, country: str = None):
        """
        Выводит список стран затронутых covid_19. Есть возможность не выводить список, а запросить конкретную строку.

        Args:
            country([country], не обязательный параметр) - если None, то выводится список стран, если не None, тогда проверка конкретной страны
        """
        if country:
            params = {'search': country}
            response = requests.request('GET', f'{self.url_covid}/countries', headers = self.headers, params = params)
        else: 
            response = requests.request('GET', f'{self.url_covid}/countries', headers = self.headers)
        return response.json()
        
    def get_statistics(self, country:str = None):
        """
        Отражает текущий статус распространения коронавируса во всех странах. Можно фильтровать country, чтобы получить его текущий статус.

        Args:
            country([country], не обязательный параметр) - если None, то выводится список стран, если не None, тогда проверка конкретной страны
        """
        if country:
            params = {'country': country}
            response = requests.request('GET', f'{self.url_covid}/statistics', headers = self.headers, params = params)
        else:
            response = requests.request('GET', f'{self.url_covid}/statistics', headers = self.headers)
        return response.json()

    def get_history(self, country: str, date: datetime = None): # Надо обработать случай, если country будет не указан, сейчас это просто исключение
        """
        Запрос всей истории статистики для страны. 

        Args:
            country([country], обязательный параметр) - название страны;
            date([], не обязательный) - Дата и время, за которое надо вывети данные по covid
        """
        if date: date.strftime('%Y-%m-%d')
        if country:
            params = {
                'country': country,
                'day': date
            }
        else:
            params = {'country': country,}
        response = requests.request('GET', f'{self.url_covid}/history', headers = self.headers, params = params)
        return response.json()

    def new_dict(self, func):
        new_dict_df = {}
        response = func.get('response')
        for dict_array in response:
            if isinstance(dict_array, str): 
                new_dict_df['response'] = [response]
            elif isinstance(dict_array, dict):
                for key_response, value_response in dict_array.items():
                    if isinstance(value_response, dict):
                        for key_value_response, value_value_response in value_response.items():
                            new_dict_df[key_value_response +'_' + key_response] = [value_value_response]
                    else:
                        new_dict_df[key_response] = [value_response]
        return new_dict_df

    def result(self, func, convert_to_df: bool = False):
        """
        Преобразует результаты функций запроса в Data Frame

        Args:
            func([Any], oбязательный) - def class Covid()
        """  
        if convert_to_df:
            convert_df = pd.DataFrame(func)
            return convert_df.to_excel('./draft_api.xlsx', index = False)
        else:
            return func
            
       
             

API_KEY = "c784b67935mshd9a7f3cab6995ebp190aafjsnacc724b616ce"
country = 'USA'
date = datetime.date(2022, 1, 1)

covid_19 = Covid(api_key = API_KEY)
countries = covid_19.get_countries()
statistics = covid_19.get_statistics()
history = covid_19.get_history(country)
dict_in_df = covid_19.new_dict(statistics)
result = covid_19.result(dict_in_df, convert_to_df = True)

print(dict_in_df)

