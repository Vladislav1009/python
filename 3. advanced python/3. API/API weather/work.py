from typing import Union
import requests
import enum

# Создание класса Units
class Units(str, enum.Enum):
    Metric = "M"
    Scientific = "S"
    Fahrenheit = "I"

class WeartherbitIO:
    def __init__(self, api_key: str, version: str='v2.0'):
        self.api_key = api_key
        self.base_url = f"https://api.weatherbit.io/{version}"
        self.print_weather = "{} | {} | {} - {}/{}"
    
    def get_current(self, city: str, lang: str='ru', units: str=Units.Metric.value, include: str='minutely') -> Union[dict[str, str], list[dict]]:
        if not city: return {
            'error': 'Not valid city param'
        }
        params_current = {'city': city, 'lang': lang, 'units': units, 'include': include, 'key': self.api_key }
        response = requests.request("GET", f"{self.base_url}/current", params=params_current)
        if response.status_code == 200:
            return response.json().get('data')
        return {
            'error': response.text
        }

    def get_forecast_hour(self, city: str, lang: str='ru', units: str=Units.Metric.value, hour: int = 48):
        if not city: return {
            'error': 'Not valid city param'
        }
        params_hour = {'city': city,'lang': lang, 'units': units, 'hour': hour, 'key': self.api_key }
        response = requests.request("GET", f"{self.base_url}/forecast/hourly", params=params_hour) # https://api.weatherbit.io/v2.0/forecast/3hourly/46b4ae04160a4a2086aa15a0a537e736/hours=48
        if response.status_code == 200:
            return response.json().get('data')
        return {
            'error': response.text
         }

    def get_hour_minutely(self, city: str, lang: str='ru', units: str=Units.Metric.value, include: str='minutely' ):
        if not city: return {
            'error': 'Not valid city param'
        }
        params_hour_minutely = {'city': city,'lang': lang, 'units': units, 'include': include, 'key': self.api_key }
        response = requests.request("GET", f"{self.base_url}/forecast/minutely", params=params_hour_minutely) # https://api.weatherbit.io/v2.0/forecast/3hourly/46b4ae04160a4a2086aa15a0a537e736/hours=48
        if response.status_code == 200:
            return response.json().get('data')
        return {
            'error': response.text
         }
    
    def print_result_from_list(self, weather_list):
        for weather in weather_list:
            print(self.print_weather.format(
                weather.get('city_name'),
                weather.get('datetime'),
                weather.get('weather', {}).get('description'),
                weather.get('temp'),
                weather.get('app_temp'),
            ))

def_user = input('Whay def? ')    
API_KEY = input('User key: ') # 46b4ae04160a4a2086aa15a0a537e736
user_citi = input('User citi: ')
hour_user = int(input('Forecast(hour): '))
ACTIVE_UNITS = Units.Metric.value
      
weatherIO = WeartherbitIO(api_key=API_KEY)
current_list = weatherIO.get_current(user_citi)
hour_list = weatherIO.get_forecast_hour(user_citi, hour_user)
hour_minutely_list = weatherIO.get_hour_minutely(user_citi)


if def_user == 'get_current':
    weatherIO.print_result_from_list(current_list)
elif def_user == 'get_forecast_hour':
    weatherIO.print_result_from_list(hour_list)
elif def_user == 'get_hour_minutely':
    weatherIO.print_result_from_list(hour_minutely_list)
else:
    print('Такой функции нет!')
