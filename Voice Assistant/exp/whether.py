import requests
import os


user_api = '34699a951b05e5cc4472544b2cc74a01'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q=" + \
    location+"&appid="+user_api
api_link = requests.get(complete_api_link)
api_data = api_link.json()
print(api_data)

# create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
#date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print("Current temperature is: {:.2f} deg C".format(temp_city))
print("Current weather desc  :", weather_desc)
print("Current Humidity      :", hmdt, '%')
print("Current wind speed    :", wind_spd, 'kmph')
