#!/usr/bin/env python
# coding: utf-8



##For API calls
import requests
##Looking at tables/data/analytics 
import pandas as pd
##unix timestamp converter
from datetime import datetime
import os
from API_keys import crash_weather_key

key = crash_weather_key

def call_weather_api():
    
    prefix = 'https://api.openweathermap.org/data/2.5/weather?q=Pittsburgh,us&APPID='
    link = (prefix + key)
    
    response = requests.get(link)
    update = response.json()  

    #naming the variables
    weather = update['weather'][0]['main']
    temp = update['main']['temp']
    temperature = int(((temp- 273.15)*9/5)+32)
    weather_id = update['weather'][0]['id']
    visibility = update['visibility']
    dt = update['dt']

    date_time = datetime.utcfromtimestamp(dt).strftime('%m-%d-%Y %H:%M:%S')
    month = datetime.utcfromtimestamp(dt).strftime('%m')
    year = datetime.utcfromtimestamp(dt).strftime('%Y')
    day = datetime.utcfromtimestamp(dt).strftime('%d')
    hour = datetime.utcfromtimestamp(dt).strftime('%H')
    
    wind_speed = update['wind']['speed']
    description = update['weather'][0]['description']

    #creating the dict
    call = {'weather_id':weather_id,'weather':weather, 'temperature':temperature, 'visibility':visibility,'wind_speed':wind_speed,'description':description,'date_time': date_time,'month':month,'day':day,'year':year,'hour':hour}
    print("API called")
    #print(call)
    return call

#call_weather_api()




