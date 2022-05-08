#creating a sub data frame from weather code and possibly other indicators
import pandas as pd
from matching_weather_codes import *
call = match_codes()
target = call['weather_id']

def gen_sub_df():
	df = pd.read_csv("crash_clean.csv")
	sub_df = df.loc[df['weather'] == target]
	sub_df.to_csv('sub_df.csv')
	#return(sub_df)
gen_sub_df()
