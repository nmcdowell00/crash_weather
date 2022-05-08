#!/usr/bin/env python
# coding: utf-8

# In[1]:


##For API calls
import requests
##Looking at tables/data/analytics 
import pandas as pd
##unix timestamp converter
from datetime import datetime
import mysql.connector
import sqlite3
import os


# In[2]:


cwDB = mysql.connector.connect( 
    host="192.168.1.198",
  user="deuser",
  password="depassword",
  database="crash_weather_odb"
)

mycursor = cwDB.cursor()

response = requests.get('https://api.openweathermap.org/data/2.5/weather?q=Pittsburgh,us&APPID=7899531bc8fd2729ed670798e7e85adb')

update = response.json()

type(update)

update

weather = update['weather'][0]['main']

temp = update['main']['temp']

temperature=int(((temp- 273.15)*9/5)+32)

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

cols = ['weather_id','weather', 'temperature', 'visibility','wind_speed','description','month','day','year','hour','date_time']

df = pd.DataFrame(columns=cols)

call = {'weather_id':weather_id,'weather':weather, 'temperature':temperature, 'visibility':visibility,'wind_speed':wind_speed,'description':description,'date_time': date_time,'month':month,'day':day,'year':year,'hour':hour}

df.to_csv('api_call.csv')
df

mycursor.execute("DROP TABLE IF EXISTS weather_data")
mycursor.execute("CREATE TABLE weather_data(id INT AUTO_INCREMENT PRIMARY KEY, weather_id INT, description VARCHAR(255),  weather VARCHAR(255), temperature INT,  visibility INT, wind_speed DECIMAL(5,2), date_time VARCHAR(255), hour INT, month INT, day INT,year INT)")
                 
                 


# In[29]:


add_weather = "INSERT INTO weather_data(weather_id , description, weather, temperature, visibility, wind_speed, date_time, hour, month, day, year) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);"


# In[30]:


weather_data =[weather_id ,description , weather ,temperature ,visibility , wind_speed, date_time , hour, month , day , year]
weather_data


# In[31]:


mycursor.execute(add_weather,weather_data)


# In[32]:


cwDB.commit()

