#master
import requests
import os
import numpy as np
import pandas as pd
from datetime import datetime
from six.moves import urllib
#%matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sns
color = sns.color_palette()
sns.set_style('darkgrid')
import geopandas
from shapely.geometry import *
#local imports
from API_keys import crash_weather_key
from APICalls_2 import call_weather_api
from weather_codes import weather_dict
from create_sub_df import gen_sub_df
from matching_weather_codes import match_codes
from visualize import make_map, count_streets, description
from trim_sub_df_hour import trim_df
call = call_weather_api()
#print('call:', call)

weather_dict = match_codes(call, weather_dict)
target = call['weather_id']
#print('target:', target)
df = pd.read_csv("crash_clean.csv")
#print('df:', df.head())

sub_df = gen_sub_df(df, target)
#trimming the sub_df based on the current time
current_time = int(call['hour'])
time_list = [current_time - 1, current_time, current_time +1]
print(time_list)
sub_df_trim = trim_df(sub_df, time_list)
#print('sub_df:', sub_df.head())
#print('weatherdict:', weather_dict)

#body 
#call the weather api
#call_weather_api()

#match_codes(call, weather_dict)

#gen_sub_df(df,target)

count_streets(sub_df_trim)

make_map(sub_df_trim)

description(weather_dict)
