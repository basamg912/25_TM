import requests
import json
from geopy.geocoders import Nominatim

# ipstack 에서 user 의 위도 경도 얻어오기
def get_longi_latitude(key):
    url = "https://api.ipstack.com/check?access_key="+key
    r = requests.get(url)
    j = json.loads(r.text)
    return j

        
def transform_loc(loc_json):
    long = loc_json['longitude']
    lati = loc_json['latitude']

    coords = f"{lati},{long}"
    geolocator = Nominatim(user_agent='basamg')
    location = str(geolocator.reverse(coords))
    location = location.replace(" ",'')
    location = location.replace(",",' ')
    return location

