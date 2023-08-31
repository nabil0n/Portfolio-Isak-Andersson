from PyQt6.QtWidgets import *
from PyQt6.QtGui import QFont
import requests
import json
from datetime import datetime

print("""
      
      ######### ____ Weather in Gothenburg ____ #########
                (powered by open-meteo.com)
      
      """)

url = "https://api.open-meteo.com/v1/forecast?latitude=57.71&longitude=11.97&hourly=temperature_2m,precipitation_probability,precipitation,cloudcover,windspeed_10m&forecast_days=1&timezone=Europe%2FBerlin"
params = {
    "latitude": 57.71,
    "longitude": 11.97,
    "hourly": ["temperature_2m", "precipitation_probability", "precipitation", "cloudcover", "windspeed_10m"],
    "forecast_days": 1,
    "timezone": "Europe/Berlin"
}

response = requests.get(url, params=params)
now = datetime.now()
current_hour = now.strftime("%H")

if response.status_code == 200:
    print("""Connected to open-metro.com (200 OK)
          
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

data=response.json()

def get_data(h, v):
    d = data['hourly'][v]
    return str(d[h])

print("""What would you like to know?
      1. Temperature for given a given hour today.
      2. Temperature right now.
      3. Tell me what the current weather is like.
      4. Tell me what the weather will be like at a given hour today.""")

in1 = int(input())

while in1<1 or in1>4:
    print("Not a valid option. Enter a number from 1 - 4.")
    in1 = int(input())
else:
    if in1 == 1:
        print("Input what hour you wish to know the temp for today (0-23)")
        in2 = int(input())
        print("Temperature for "+str(in2)+".00 is "+get_data(in2, 'temperature_2m')+" C.")
    elif in1 == 2:
        print("Current temperature is "+get_data(int(current_hour), 'temperature_2m')+" C.")
    elif in1 == 3:
        print("\nRight now you can expect a temperature of "+get_data(int(current_hour), 'temperature_2m')+" C, \na "+get_data(int(current_hour), 'precipitation_probability')+" % chance of "+get_data(int(current_hour), 'precipitation')+"mm precipitaion, \nwith a cloudcover of "+get_data(int(current_hour), 'cloudcover')+" %, \nand a windspeed of "+get_data(int(current_hour), 'windspeed_10m')+"km/h.\n")
    elif in1 == 4:
        print("Input what hour of today you're intrested in. (00-23)")
        in3 = int(input())
        print("\nAt "+str(in3)+".00 you can expect a temperature of "+get_data(in3, 'temperature_2m')+" C, \na "+get_data(in3, 'precipitation_probability')+" % chance of "+get_data(in3, 'precipitation')+"mm precipitaion, \nwith a cloudcover of "+get_data(in3, 'cloudcover')+" %, \nand a windspeed of "+get_data(in3, 'windspeed_10m')+"km/h.\n")

# def main():
#     app = QApplication([])
#     window = QWidget()
#     window.setGeometry(100, 100, 200, 300)
#     window.setWindowTitle("Weather in Gothenburg")
    
#     layout = QVBoxLayout()
    
#     label = QLabel("What would you like to know?")
#     button1 = QPushButton("Temp by hour")
#     button2 = QPushButton("Temp now")
#     button3 = QPushButton("Current weather")
#     button4 = QPushButton("weather by hour")
    
#     layout.addWidget(label)
#     layout.addWidget(button1)
#     layout.addWidget(button2)
#     layout.addWidget(button3)
#     layout.addWidget(button4)
    
#     window.setLayout(layout)
    
#     button1.clicked.connect(get_data(int(current_hour), "temperature_2m"))

    
#     # label = QLabel(window)
#     # label.setText("PLACEHOLDER")
#     # label.setFont(QFont("Arial", 16))
#     # label.move(50, 10)
    
#     window.show()
#     app.exec()

# if __name__ == "__main__":
#     main()