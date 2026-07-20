#made api request from paid open weather api key
from dotenv import load_dotenv
import os
load_dotenv()
import requests
OWN_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.getenv("api_key")
weather_params = {
    "lat": 22.891010,
    "lon": 77.419281,
    "appid": api_key,
}
response = requests.get(url=OWN_endpoint, params=weather_params )
response.raise_for_status()
print(response.json())
