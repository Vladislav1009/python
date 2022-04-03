# Задачи:
# - Получить ключ для работы с api
# - Изучить предметную область
# - Создать функции для получения всех данных по 3 методам запросов (Countries, Statistics, History)
# - Создать возможность сохранения полученных данных в виде excel (Используя pandas)

#  Ключ --> c784b67935mshd9a7f3cab6995ebp190aafjsnacc724b616ce



from wsgiref import headers
import requests


class Covid():

    def __init__(self, api_key: str, ):
        self.api_key = api_key
        self.url = f"https://covid-193.p.rapidapi.com"

    def get_countries(self):
        headers = {
            'x-rapidapi-host': self.url,
            'x-rapidapi-key': self.api_key
        }
        response = requests.request('GET', f'{self.url}/countries', headers=headers)
        return print(response.json())


API_KEY = 'c784b67935mshd9a7f3cab6995ebp190aafjsnacc724b616ce'
covid_19 = Covid(api_key = API_KEY)
countries = covid_19.get_countries()
