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
        response_json = response.json()
        if country == None:
            return response_json 
        elif country != None:
            if country in response_json.get('response'):
                return {country: 'есть в списке стран, зараженных covid'}
            if country not in response_json:
                return {country: 'не найдена в списке стран зараженных covid'}
            


    def get_statistics(self, country:str = None):
        """
        Отражает текущий статус распространения коронавируса во всех странах. Можно фильтровать country, чтобы получить его текущий статус.

        Args:
            country([country], не обязательный параметр) - если None, то выводится список стран, если не None, тогда проверка конкретной страны
        """
        params = {'country': country}
        response = requests.request('GET', f'{self.url_covid}/statistics', headers = self.headers, params = params)
        response_json = response.json()
        if country == None:
            return response_json 
        elif country != None:
            if response_json.get('response') == None:
                return 'Вы ввели неправельные данные, либо такого города нет'
            elif response_json.get('response') != None:
                return response_json

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

    def print_result(self, func = None):
        """
        Выводит результат работы функций. Если никакой запрос не выполняется, то print "Функция не выбранна".

        Args:
            func[(Any), не обязательный) - объект с функцией class Covid()
        """
        if func == None:
            print('Функция не выбранна')
        elif func != None:
            print(func)
            

rapidapi_host = 'covid-193.p.rapidapi.com'
API_KEY = "c784b67935mshd9a7f3cab6995ebp190aafjsnacc724b616ce"
country = 'dfadsfa'
date = datetime.date(2022, 1, 1).strftime('%Y-%m-%d')

covid_19 = Covid(api_key = API_KEY, rapidapi = rapidapi_host)
countries_obj = covid_19.get_countries()
statistics_obj = covid_19.get_statistics(country)
history_obj = covid_19.get_history(country, date)
result_obj = covid_19.print_result(statistics_obj)

# df_country = pd.DataFrame({'Страны с ковидом': countries_obj.get('response')})

# dict_cases_1 = {}
# for response_s in statistics_obj.get('response'):
#     response_cases = response_s.get('cases')
#     for key_s, value_s in response_cases.items():
#         dict_cases_1[key_s] = value_s
# df_statistics = pd.DataFrame({'Наименование': dict_cases_1.keys(), 'Значения': dict_cases_1.values()})

# dict_cases_2 = {}
# for response_h in statistics_obj.get('response'):
#     response_cases = response_h.get('cases')
#     for key_h, value_h in response_cases.items():
#         dict_cases_2[key_h] = value_h
# df_history = pd.DataFrame({'Наименование': dict_cases_2.keys(), 'Значения': dict_cases_2.values()})

# df = {'country': df_country, 'statistics': df_statistics, 'history': df_history}
# writer = pd.ExcelWriter('./Covid19.xlsx', engine = 'xlsxwriter')
# for key_df in df.keys():
#     df[key_df].to_excel(writer, sheet_name = key_df,  index = False)

# writer.save()