# Overview
 This project matches current weather data historical crash data to create visualization of where crashes usually occur during both the weather event and current time. 
 
### Data
The weather data is drawn from [Open Weather Data API]("https://openweathermap.org/api). The crash data is taken from the [WPRDC](https://data.wprdc.org/dataset/allegheny-county-crash-data)

### Process 
The first step in this project was cleaning the crash data. I used Jupytr notebooks to create visualizations that allowed me to make educated decisions on how to clean the data. I also used [this similiar project]() to help me make data cleaning decisions. After cleaning the crash data, I had to manipulate the data from the API to match the features of the Crash Data. The most important change I made was mathching the weather codes from the API to the codes in the Crash Data. To do this, I went through all of the codes in the API, manually, and matched them to the best fit code in the crash data. This allowed me to query the crash data 

### Further Implementations 
The next steps for this project would be scraping current crash data to create more accuarate predictions. This could be done by writign a script to draw the data from the PennDot live crash feed. This would be a difficult task would be difficult becuase the data on this feed is very unstructerd. To use this data in a meanigful way a lot of preperatory work would have to be completed. 


