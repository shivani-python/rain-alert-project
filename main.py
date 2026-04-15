import smtplib

import requests
MY_LATITUDE = 16.898001
MY_LONGITUDE = 81.674698
API_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = input("Enter API key: ")
weather_params ={
    "lat":MY_LATITUDE,
    "lon":MY_LONGITUDE,
    "appid":API_KEY,
    "cnt":4,
}
response = requests.get(url=API_ENDPOINT, params=weather_params)
print(response.status_code)
response.raise_for_status()
weather_data = response.json()
# view in jsonviewer.stack.hu
print(weather_data)
# print(weather_data["list"][0]["weather"][0]["id"]
# for hour_data in weather_data["list"]:
#     print(hour_data["weather"][0]["id"])
will_rain = False
for num in range(0,3):
    weather_id = weather_data["list"][num]["weather"][0]["id"]
    if weather_id < 700:
        will_rain = True
if will_rain:
    MY_EMAIL = input("Enter email: ")
    MY_PASSWORD = input("Enter password: ")
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(MY_EMAIL,MY_PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=MY_EMAIL,
        msg="subject:Rain Alert\n\nHey it's going to rain"
    )
