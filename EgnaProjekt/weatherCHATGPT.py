import requests
import json
from datetime import datetime

print("""
      
      ######### ____ Weather in Gothenburg ____ #########
                (powered by open-meteo.com)
      
      """)

url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 57.71,
    "longitude": 11.97,
    "hourly": ["temperature_2m", "precipitation_probability", "precipitation", "cloudcover", "windspeed_10m"],
    "forecast_days": 1,
    "timezone": "Europe/Berlin"
}

response = requests.get(url, params=params)

if response.status_code == 200:
    print("""Connected to open-meteo.com (200 OK)
          
          """)
else:
    print("Something went wrong, check response.")
    print("Response code: "+str(response.status_code))
    print("""
    200: Everything went okay, and the result has been returned (if any).
    301: The server is redirecting you to a different endpoint.
         This can happen when a company switches domain names, or an endpoint name is changed.
    400: The server thinks you made a bad request. This can happen when you don’t send along the right data, among other things.
    401: The server thinks you’re not authenticated.
         Many APIs require login credentials, so this happens when you don’t send the right credentials to access an API.
    403: The resource you’re trying to access is forbidden: you don’t have the right perlessons to see it.
    404: The resource you tried to access wasn’t found on the server.
    503: The server is not ready to handle the request.
    """)

data = response.json()['hourly']

now = datetime.now()
current_hour = int(now.strftime("%H"))

def get_data(h, key):
    if response.status_code == 200:
        return str(data[h][key])
    else:
        return "NO DATA"

print("""What would you like to know?
      1. Temperature for a given hour today.
      2. Temperature right now.
      3. Tell me what the current weather is like.
      4. Tell me what the weather will be like at a given hour today.""")

in1 = int(input())

if 1 <= in1 <= 4:
    if in1 == 1:
        in2 = int(input)
