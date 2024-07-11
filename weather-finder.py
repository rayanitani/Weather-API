# Import the necessary libraries
import requests
import json
import math
# Define the API key, base URL, and city
API_KEY = "6713b0e01b450535d5db2d1980c15a50"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
CITY = input("Enter City Name:")

# Define a function to fetch and parse weather data
def fetch_weather(city):
    # Build the URL
    url = f"{BASE_URL}?q={city}&appid={API_KEY}"

    # Send a GET request to the API
    response = requests.get(url)

    # If the request was successful, parse and print the weather data
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        wind = data['wind']
        weather_desc = data['weather'][0]['description']
        print(f"Weather in {city}:")
        print(f"Temperature: {math.floor(main['temp']-273.15)}C")
        print(f"Humidity: {main['humidity']}%")
        print(f"Pressure: {main['pressure']}hPa")
        print(f"Wind Speed: {wind['speed']}m/s")
        print(f"Weather Description: {weather_desc}")
    else:
        print(f"Error: Unable to fetch weather data for {city}. Please check the city name and try again.")

# Call the function to fetch and print the weather data
fetch_weather(CITY)

