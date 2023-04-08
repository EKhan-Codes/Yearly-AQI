import requests, json
from geopy.geocoders import Nominatim
import datetime
import time
import sys
import matplotlib  
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
geolocator = Nominatim(user_agent="Your_Name")


#Taking Input Variables 
City = input("Enter City Name:")
Country = input("Enter Country Name:")
Year = input("Enter Year:")
#Converting City & Country Name To Latitude & Longitude
loc = geolocator.geocode(City+','+ Country)
lat = loc.latitude
lon = loc.longitude
numbers = [1]
#Taking TimeStamps For Whole Year & Converting Them TO Unix Time
for x in range(1,13) :
   date_example1 = str(x)+"/1"+"/"+ Year
   date_format1 = datetime.datetime.strptime(date_example1,"%m/%d/%Y")
   unix_time1 = datetime.datetime.timestamp(date_format1)
   numbers.append(str(int(unix_time1)))


listAqi = []
months = ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec')
#API Call
for i in range(1,len(numbers)):
  api_key = "803c2ff59b62f6866fbd3e351094671e"
  base_url = "http://api.openweathermap.org/data/2.5/air_pollution/history?"
  complete_url = base_url + "lat=" + str(lat) + "&lon=" + str(lon) + "&start=" + str(int(numbers[i])) + "&end=" + str(int(numbers[i])) + "&appid=" + api_key

  response = requests.get(complete_url)

  a = response.json()



  y = a["list"]
  z = y[0]
  a = z["main"]
  aqi = a["aqi"]


  
  listAqi.append(aqi)
#Creating Graph
xpoints = np.array(months)  
ypoints = np.array(listAqi)
plt.plot(xpoints, ypoints)
plt.show()


