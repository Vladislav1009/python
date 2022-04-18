from typing import Union
import requests
import enum

# Класс Units, хранит в себе атрибуты, которые отвечают за еденицы измерения погоды. Данные брали из API сайта. Библиотека enum отвечает за перечесление. Так же атрибуты будут
# не изменными, потому что используем библиотеку Units
class Units(str, enum.Enum):
    Metric = "M"
    Scientific = "S"
    Fahrenheit = "I"

class WeartherbitIO:
    def __init__(self, api_key: str, version: str='v2.0'):
        self.api_key = api_key
        self.base_url = f"https://api.weatherbit.io/{version}"
        self.print_weather = "{} | {} | {} - {}/{}" # Форма для заполнения данных.
    
    def get_current(self, city: str, lang: str='ru', units: str=Units.Metric.value, include: str='minutely'):
        if not city: return { # Если пользователь не указал название города, то выводится надпись.
            'error': 'Not valid city param'
        }
        params = {'city': city, 'lang': lang, 'units': units, 'include': include, 'key': self.api_key } # Словарь в котором хранятся значения из атрибутов __init__ и get_current 
        response = requests.request("GET", f"{self.base_url}/current", params=params) # Метод request отправляет запросы HTTP в Python. GET - получать. вторым парамметром указываем ссылку
        # и трутьим параметром передаем атрибут(params) функции get_current. 
        if response.status_code == 200: # Если пользователь указал город, и питон нашел его, тогда код страницы будет 200 и  
            return response.json().get('data')
        return {
            'error': response.text # Не понимаю эту строку.
        }
    
    def print_result_from_list(self, weather_list):
        for weather in weather_list:
            print(self.print_weather.format(
                weather.get('city_name'),
                weather.get('datetime'),
                weather.get('weather', {}).get('description'), # 'weather': {'icon': 'c03d', 'code': 803, 'description': 'Облачно с прояснениями'}; ключ словаря имеет значение словарь
                weather.get('temp'),
                weather.get('app_temp'),
            ))
# "46b4ae04160a4a2086aa15a0a537e736"  
key_user = input('Введите ключ: ')
citi_user = input('Введите город(ENG): ')

API_KEY = key_user # Ключ пользователя
ACTIVE_UNITS = Units.Metric.value # Вызов значения атрибута metric класса Units
      
weatherIO = WeartherbitIO(api_key=API_KEY) # Передаем в класс WeartherbitIO в атрибут (функция __inint__) параметр api_key с значением API_KEY. Теперь в переменной weatherIO хранится 
# экземпляр класса.
current_list = weatherIO.get_current(citi_user) # переменная current_list хранит в себе город, в котором надо найти погоду, в дальнейшем надо, что бы она была не постоянна, а пользователь 
# задавал значение. Данная переменная передает значение 'Moscow' в класс WeartherbitIO атрибут get_current через экземпляр класса wearherIO. get_current имеет значение функции get_current
weatherIO.print_result_from_list(current_list)


# key_user = '46b4ae04160a4a2086aa15a0a537e736'

# def get_current(city: str, lang: str='ru', units: str=Units.Metric.value, include: str='minutely'):
#         if not city: return { # Если пользователь не указал название города, то выводится надпись.
#             'error': 'Not valid city param'
#         }
#         params = {'city': city, 'lang': lang, 'units': units, 'include': include, 'key': key_user } # Словарь в котором хранятся значения из атрибутов __init__ и get_current 
#         response = requests.request("GET", f"https://api.weatherbit.io/v2.0/current", params=params) # Метод request отправляет запросы HTTP в Python. GET - получать. вторым парамметром указываем ссылку
#         # и трутьим параметром передаем атрибут(params) функции get_current. 
#         if response.status_code == 200: # Если пользователь указал город, и питон нашел его, тогда код страницы будет 200 и  
#             return response.json().get('data')
#         return {
#             'error': response.text # Не понимаю эту строку.
#         }
# print(get_current('Moscow'))