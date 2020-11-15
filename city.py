import pprint
import requests
from datetime import date


class YahooWeatherForecast:

    def get(city):
        url = f'http://api.openweathermap.org/data/2.5/find?q={city}&units=metric&appid=dded191e9c87fc0c60a897aedfcd37fc'
        data = requests.get(url).json()
        weather = data["list"][0]["main"]
        return weather


class CityInfo:
    def __init__(self, city):
        self.city = city

 #   def weather_forecast(self):
 #       return YahooWeatherForecast.get(self.city)


def _main():
    city = "Rostov-on-Don"
    weather = YahooWeatherForecast.get(city)
    pprint.pprint(f'Сегодня {date.today()} температура воздуха {weather["temp"]} градус. Ощущается как {int(weather["feels_like"])}')


if __name__ == "__main__":
    _main()
