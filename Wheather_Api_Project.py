import os
import requests
from dotenv import load_dotenv

# Load variables from the .env file
load_dotenv()

# Read the API key
API_KEY = os.getenv("API_KEY")

# Check if API key exists
if not API_KEY:
    print("Error: API_KEY not found in .env file")
    exit()

url = "https://api.openweathermap.org/data/2.5/weather"


def response_get(response):
    if response.status_code == 200:
        data = response.json()

        print("\n------ Weather Report ------")
        print("City:", data["name"])
        print("Temperature:", data["main"]["temp"], "°C")
        print("Humidity:", data["main"]["humidity"], "%")
        print("Weather:", data["weather"][0]["description"])
        print("----------------------------\n")

    else:
        print("Error:", response.status_code)
        print(response.json())


while True:
    city = input("Enter City (or 'E' to exit): ")

    if city.lower() == "e":
        print("Program Ended.")
        break

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(url, params=params)

    response_get(response)