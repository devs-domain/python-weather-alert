import requests
import smtplib
import os


my_email = os.environ.get("MY_EMAIL")
my_password = os.environ.get("MY_PASSWORD")
api_key = os.environ.get("API_KEY")
recepient_email = os.environ.get("MY_RECEPIENT")

MY_LAT = 14.346370
MY_LONG = 120.882347

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "cnt":4
    }
will_rain = False
response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True


if will_rain:
    print("Bring an umbrella!")
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs=recepient_email,
                            msg="Subject:Alert!\n\nBring an umbrella!")
