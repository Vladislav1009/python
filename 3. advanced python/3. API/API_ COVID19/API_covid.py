# Задачи:
# - Получить ключ для работы с api
# - Изучить предметную область
# - Создать функции для получения всех данных по 3 методам запросов (Countries, Statistics, History)
# - Создать возможность сохранения полученных данных в виде excel (Используя pandas)

#  Ключ --> c784b67935mshd9a7f3cab6995ebp190aafjsnacc724b616ce

<<<<<<< HEAD

=======
>>>>>>> fc049e853f90196442bffa8081f42433b4599bf8
import requests
import datetime
import pandas as pd

class Covid():

<<<<<<< HEAD
    def __init__(self, api_key: str, rapidapi: str):
=======
    def __init__(self, api_key: str):
>>>>>>> fc049e853f90196442bffa8081f42433b4599bf8
        """
        Конструктор класса, который автоматически выводится при создании объектов

        Args:
            api_key([str], обязательный параметр) - ключ. Берем на apiRapid;
            rapidapi([str]), обязательный параметр) - ссылка на сайт, надо для использования headers при запросе.
        """
        self.api_key = api_key
        self.url_covid = f'https://covid-193.p.rapidapi.com'
<<<<<<< HEAD
        self.rapidapi = rapidapi
        self.headers = {
            'x-rapidapi-host': self.rapidapi,
=======
        self.headers = {
            'x-rapidapi-host': 'covid-193.p.rapidapi.com',
>>>>>>> fc049e853f90196442bffa8081f42433b4599bf8
            'x-rapidapi-key': self.api_key
        }

    def get_countries(self, country: str = None):
        """
        Выводит список стран затронутых covid_19. Есть возможность не выводить список, а запросить конкретную строку.

        Args:
            country([country], не обязательный параметр) - если None, то выводится список стран, если не None, тогда проверка конкретной страны
        """
<<<<<<< HEAD
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
            


=======
        if country:
            params = {'search': country}
            response = requests.request('GET', f'{self.url_covid}/countries', headers = self.headers, params = params)
        else: 
            response = requests.request('GET', f'{self.url_covid}/countries', headers = self.headers)
        return response.json()
        
>>>>>>> fc049e853f90196442bffa8081f42433b4599bf8
    def get_statistics(self, country:str = None):
        """
        Отражает текущий статус распространения коронавируса во всех странах. Можно фильтровать country, чтобы получить его текущий статус.

        Args:
            country([country], не обязательный параметр) - если None, то выводится список стран, если не None, тогда проверка конкретной страны
        """
<<<<<<< HEAD
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
=======
        if country:
            params = {'country': country}
            response = requests.request('GET', f'{self.url_covid}/statistics', headers = self.headers, params = params)
        else:
            response = requests.request('GET', f'{self.url_covid}/statistics', headers = self.headers)
        return response.json()

    def get_history(self, country: str, date: datetime = None): # Надо обработать случай, если country будет не указан, сейчас это просто исключение
>>>>>>> fc049e853f90196442bffa8081f42433b4599bf8
        """
        Запрос всей истории статистики для страны. 

        Args:
            country([country], обязательный параметр) - название страны;
<<<<<<< HEAD
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
=======
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

>>>>>>> fc049e853f90196442bffa8081f42433b4599bf8
