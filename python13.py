#working with requests
import requests
response = requests.get(url="http://api.open-notify.org/iss-now.json")
print(response)
print(response.status_code)
response.raise_for_status()
data = response.json()
print(data)
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]
iss_position = longitude, latitude
print(iss_position)

#requesting sunrise & sunset

from datetime import datetime
my_lat = 22.891010
my_lon = 88.419281
parameters = {
    "lat": my_lat,
    "lng": my_lon,
}
response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
print(data)
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
print(sunrise, sunset)
time_now = datetime.now()
print(time_now)