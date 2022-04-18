from typing import Union
import requests
import enum


class Units(str, enum.Enum):
    Metric = "M"
    Scientific = "S"
    Fahrenheit = "I"

class WeartherbitIO:
    def __init__(self, api_key: str, version: str='v2.0'):
        self.api_key = api_key
        self.base_url = f"https://api.weatherbit.io/{version}"
        self.print_weather = "{} | {} | {} - {}/{}"
    
    def get_current(self, city: str, lang: str='ru', units: str=Units.Metric.value, include: str='minutely'): # -> Union[dict[str, str], list[dict]]: # "Union[dict[str, str], list[dict]]" из-за этого выдал ошибку
        if not city: return {
            'error': 'Not valid city param' # "не действительный параметр города"
        }
        params = {'city': city, 'lang': lang, 'units': units, 'include': include, 'key': self.api_key } # units - еденица измерения; include - временной диапазон
        response = requests.request("GET", f"{self.base_url}/current", params=params)
        if response.status_code == 200:
            return response.json().get('data') 
        return {
            'error': response.text
        }
    
    # def forecast_five(self, city^)

    def print_result_from_list(self, weather_list):
        for weather in weather_list:
            print(self.print_weather.format( # из функции __init__
                weather.get('city_name'), #вызываем значение ключа 'city_name'
                weather.get('datetime'),
                weather.get('weather', {}).get('description'),
                weather.get('temp'),
                weather.get('app_temp'),
            ))
     
API_KEY = input('User key: ') # "46b4ae04160a4a2086aa15a0a537e736"  
User_citi = input('Enter_citi: ')
ACTIVE_UNITS = Units.Metric.value
      
weatherIO = WeartherbitIO(api_key=API_KEY)
current_list = weatherIO.get_current(User_citi) # хранит в себе то, что вернет функция get_current
weatherIO.print_result_from_list(current_list)