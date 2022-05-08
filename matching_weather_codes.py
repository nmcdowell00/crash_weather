#fucntion to match the weather codes to be ready to query
from APICalls_2 import *
from weather_codes import weather_dict

call = call_weather_api()
#inputs are teh output of the weather API and the dict to match both weather codes 
def match_codes(dictionary, codes): 
	code = dictionary['weather_id']
	for x in codes: 
		if code in codes[x]:
			on_match = x
			dictionary['weather_id'] = int(on_match)
	print('weather_codes mathched')
	#print(call)
	return dictionary
#match_codes(call, weather_dict)