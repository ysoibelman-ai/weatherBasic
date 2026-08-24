from dotenv import load_dotenv
import os
from requests import get
import csv
from datetime import datetime

def main ():
   
    city = get_city()
    if not check_city(city):
        invalid_city()

    country_code = get_country_code()
    if not check_country_or_state_code(country_code):
        invalid_country_code()

    state_code=""
    if check_usa(country_code):
        state_code = get_state_code()
        if not check_country_or_state_code(state_code):
            invalid_state_code()

    location = get_location (city,country_code,state_code)
    check_location(location)
    latitude = get_latitude(location)
    longitude = get_longitude(location)
    print (latitude)
    print (longitude)

    

    
def get_latitude(location):
    return location["lat"]

def get_longitude(location):
    return location["lon"]
    

def check_location(location):
    if not location:
        exit("Location not found")

def get_location(city, country, state):
    basic_url = "http://api.openweathermap.org/geo/1.0/direct?"
    query_parameters = f"q={city},{state},{country}&"
    appid = f"appid={get_key()}"

    result = get(f"{basic_url}{query_parameters}{appid}")
    result = result.json()
    if result == []:
        return None
    else:
        return result[0]
    

def get_key () -> str:
    load_dotenv()
    api_key = os.getenv("API_KEY")
    return api_key

def get_city() -> str:
    city = input("enter city name: ").strip()
    return city

def check_city(city):
    if isinstance(city,str) and city.strip():
        return True

def invalid_city():
    exit("you enterned an invalid city name. exiting program...")

def get_country_code():
    country_code = input("enter country code: ").upper().strip()
    return country_code

def check_country_or_state_code (code) -> bool:
    if code.isalpha() and len (code) == 2:
        return True

def invalid_country_code():
    exit("invalid country code. exiting program...")

def check_usa(country_code):
    if country_code == "US":
        return True

def invalid_state_code():
    exit("invalid state code. exiting program...")

def get_state_code():
    state_code = input("enter state code: ").upper().strip()
    return state_code






main ()