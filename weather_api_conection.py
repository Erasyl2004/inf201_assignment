import requests
import os
from dotenv import load_dotenv
load_dotenv()
appid = os.getenv("weather_key")
class Weather:
    def get_weather(self,city: str):
        try:
            res = requests.get("http://api.weatherapi.com/v1/current.json",params={"key": appid,"q": city})
            data = res.json()
            my_result = {
                "temperature": data["current"]["temp_c"],
                "region": data["location"]["region"],
                "country": data["location"]["country"],
                "last_up": data["current"]["last_updated"]
            }
            return my_result
        except Exception as e:
            print("Exception (weather):", e)
            pass