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
    400: The server thinks you made a bad request. This can happen when you don’t send along the right data, among other things.
    401: The server thinks you’re not authenticated.
    403: The resource you’re trying to access is forbidden: you don’t have the right perlessons to see it.
    404: The resource you tried to access wasn’t found on the server.
    503: The server is not ready to handle the request.
    """)

data = response.json()
now = datetime.now()
current_hour = now.strftime("%H")

def get_data(hour, variable):
    return str(data['hourly'][variable][hour])

def print_menu():
    print("""
    What would you like to know?
    1. Temperature for a given hour today.
    2. Temperature right now.
    3. Tell me what the current weather is like.
    4. Tell me what the weather will be like at a given hour today.
    """)

def get_user_input(prompt, valid_range):
    while True:
        try:
            user_input = int(input(prompt))
            if user_input in valid_range:
                return user_input
            else:
                print(f"Not a valid option. Enter a number from {min(valid_range)} - {max(valid_range)}.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    print_menu()
    choice = get_user_input("Enter your choice (1-4): ", range(1, 5))

    if choice == 1:
        hour = get_user_input("Input what hour you wish to know the temp for today (0-23): ", range(0, 24))
        print(f"Temperature for {hour}.00 is {get_data(hour, 'temperature_2m')} C.")
    elif choice == 2:
        print(f"Current temperature is {get_data(int(current_hour), 'temperature_2m')} C.")
    elif choice == 3:
        print(f"\nRight now you can expect a temperature of {get_data(int(current_hour), 'temperature_2m')} C, "
            f"a {get_data(int(current_hour), 'precipitation_probability')}% chance of {get_data(int(current_hour), 'precipitation')}mm precipitation, "
            f"with a cloud cover of {get_data(int(current_hour), 'cloudcover')}%, "
            f"and a windspeed of {get_data(int(current_hour), 'windspeed_10m')}km/h.\n")
    elif choice == 4:
        hour = get_user_input("Input what hour of today you're interested in. (0-23): ", range(0, 24))
        print(f"\nAt {hour}.00 you can expect a temperature of {get_data(hour, 'temperature_2m')} C, "
            f"a {get_data(hour, 'precipitation_probability')}% chance of {get_data(hour, 'precipitation')}mm precipitation, "
            f"with a cloud cover of {get_data(hour, 'cloudcover')}%, "
            f"and a windspeed of {get_data(hour, 'windspeed_10m')}km/h.\n")

if __name__ == "__main__":
    main()

