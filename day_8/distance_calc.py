import geocoder, requests
from math import acos, cos, sin, radians, degrees
from decouple import config

def get_coordinates(address, api_key):
    url = "https://trueway-geocoding.p.rapidapi.com/Geocode"

    querystring = {"address":address,"language":"en"}

    headers = {
        'x-rapidapi-key': api_key,
        'x-rapidapi-host': "trueway-geocoding.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    res = response.json()
    lat = res['results'][0]['location']['lat']
    lng = res['results'][0]['location']['lng']

    return lat, lng

def get_distance(lat1, lat2, lng1, lng2):
    distance = degrees(acos(cos(radians(90-lat1))*cos(radians(90-lat2)) + sin(radians(90-lat1))*sin(radians(90-lat2))*cos(radians(lng1-lng1))))*111.1
    return distance

def main():
    
    localization = input ("Localization: ")

    API_KEY = config('KEY')

    g = geocoder.ip('me')
    lat1 = g.latlng[0]
    lng1 =  g.latlng[1]

    lat2,lng2 = get_coordinates(localization, API_KEY)

    distance = get_distance(lat1, lat2, lng1, lng2);

    print("Distance : {:.0f} km".format(distance))
    

if __name__ == "__main__":
    main()