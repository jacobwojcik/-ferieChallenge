import requests
from datetime import datetime
import random
from decouple import config

API_KEY = config('KEY')

weather_url = "https://community-open-weather-map.p.rapidapi.com/weather"
city="Cracow"

querystring = {"q":city,"lat":"0","lon":"0","id":"2172797","lang":"eng","units":"metric"}
headers = {
    'x-rapidapi-key': API_KEY,
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
    }
response = requests.request("GET", weather_url, headers=headers, params=querystring)

if response.status_code == 200:
    res = response.json()

    print("City: ",city)
    print("Date: ", datetime.now().strftime('%d-%m-%Y %H:%M:%S'))

    print('Weather :', res['weather'][0]['description'])
    print('Temperature:', res['main']['temp'], '°C')
    print('Pressure:', res['main']['pressure'], ' hPa \n')

else:
    print("Something went wrong with weather ;<")
#random quote

quotes_url = "https://type.fit/api/quotes"
response = requests.request("GET", quotes_url)

if response.status_code == 200:
    res = response.json()
    quote = random.choice(res)
    print(f'"{quote["text"]}"',' - ',quote['author'])
    print('\n')

else:
    print("Something went wrong with quote ;<")