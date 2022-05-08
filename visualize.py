#creating a map visualization from the sub_dfma
import os
import numpy as np
import pandas as pd
from six.moves import urllib
#%matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sns
color = sns.color_palette()
sns.set_style('darkgrid')
 

import geopandas
from shapely.geometry import *
from create_sub_df import *
from matching_weather_codes import *
#sub_df = gen_sub_df()
#weather_dict = match_codes()
#print(sub_df.head())
def make_map(dataframe):

	map_df = dataframe[['long','lat']].dropna()
	map_df = map_df[(map_df.long >-80.1) & (map_df.long < -79.85)]
	map_df = map_df[(map_df.lat >40.36) & (map_df.lat < 40.5)]

	fig = plt.figure(figsize=(7,7))
	ax = fig.add_subplot(1, 1, 1) # nrows, ncols, index

	ax.plot(-79.96,40.47,'ro',alpha=1) #inoccuous point so we can output the legend
	ax.legend(['severity'],fontsize = 12)
	ax.plot(map_df.long.values, map_df.lat.values,'r.',alpha=.35)
	ax.plot(-79.9959,40.4406,'ko')

	ax.annotate('Pittsburgh',(-79.9959,40.4406),xytext=(-79.994,40.445),fontsize=16)
	ax.set_aspect('equal')
	ax.set_facecolor((1,1,1))

	plt.title('A Map of Pittsburgh by Crashes', fontsize = 16)
	plt.ylabel('Latitude', fontsize=12)
	plt.xlabel('Longitude', fontsize=12)
	plt.savefig('pittsburgh.pdf', dpi=300)

#make_map(sub_df)

def count_streets(dataframe): 
	most_frequent = pd.DataFrame(dataframe['street'].astype('str').value_counts().sort_values(ascending=False).head(10))
	most_frequent.plot.bar()
	plt.savefig('most.pdf', dpi=300,bbox_inches='tight', pad_inches=1)

#count_streets(sub_df)



def description(dictionary):
	current_weather = dictionary['weather']
	current_temp = dictionary['temperature']
	current_time = dictionary['date_time']
	print('weather:',current_weather)
	print('date:',current_time)
	print('temp:', current_temp)

#description(weather_dict)





