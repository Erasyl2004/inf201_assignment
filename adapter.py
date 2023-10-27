from gpt_api import GPT_API
from weather_api_conection import Weather
class Adapter(GPT_API,Weather):
    def getCity(self):
        city = eval(GPT_API.get_city(self=self))
        return city["city"]
    def printWeather(self,city: str):
        res = Weather.get_weather(self=self,city=city)
        print("city:",city,"\nregion:",res["region"],"\ncountry:",res["country"],"\ntemperature:",res["temperature"],"\nlast_update:",res["last_up"])
