import time
import requests
from pprint import pprint

'''
Open Weather Map API
https://openweathermap.org/api

requests module documentation

install - pip install requests

Docs and API reference - https://docs.python-requests.org/en/master/

https://openweathermap.org/api

"http://api.covid19india.org/csv/latest/cowin_vaccine_data_statewise.csv"

'''

url_config = {
    'api_key':'274bb94a6186ecdd6d674d2ecf479878',
    'zip_code':'452009',
    'country_code':'',
    'city_name':'indore',
    'temp_unit':'imperial'} #unit can be metric, imperial, or kelvin

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?q={1}&appid={0}"

while True:
    final_url = BASE_URL.format(url_config["api_key"], url_config["city_name"])
    
    weather_data = requests.get(final_url)

    #pprint(weather_data)
    
    time.sleep(20) #get new data every 20 seconds
