import requests
import json

api_key = "API_KEY"  # replace with your own API key from OpenWeatherMap

def get_weather(city):
    # make a request to the OpenWeatherMap API
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city, api_key)
    response = requests.get(url)

    # parse the JSON response
    data = json.loads(response.text)
    weather = data["weather"][0]["main"]
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]

    # format and print the weather information
    print("Weather in {}:".format(city))
    print(" - Condition: {}".format(weather))
    print(" - Temperature: {}°F".format(round(temp * 9/5 - 459.67, 2)))
    print(" - Humidity: {}%".format(humidity))

# test the function with a city name
get_weather("Delhi")


