import requests
from twilio.rest import Client

MY_LAT = 52.199910
MY_LNG = 20.888070
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = "<API_KEY>"
account_sid = "<ACCOUNT_SID>"
auth_token = "<AUTH_TOKEN>"

parameters = {
    "lat": MY_LAT,
    "lon": MY_LNG,
    "cnt": 4,
    "appid": API_KEY,
}

response = requests.get(OWM_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()

will_rain = False
weather_description = ""
for item in weather_data["list"]:
    weather = item["weather"][0]
    weather_id = weather["id"]
    if int(weather_id) < 700:
        will_rain = True
        weather_description = weather["description"]

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=f"Today's weather is: {weather_description}. Remember to bring an umbrella☂️",
        from_="+12565789358",
        to="<MY_PHONE>",
    )
    print(message.status)
