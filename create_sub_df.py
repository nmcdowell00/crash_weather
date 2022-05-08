#creating a sub data frame from weather code and possibly other indicators
import pandas as pd
from matching_weather_codes import *
#call = match_codes()
target = call['weather_id']
df = pd.read_csv("crash_clean.csv")

def gen_sub_df(dataframe, target_number):
	sub_df = dataframe.loc[dataframe['weather'] == target_number]
	sub_df.to_csv('sub_df.csv')
	print('sub dataframe created')
	return sub_df
#gen_sub_df(df,target)
