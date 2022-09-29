import requests
from datetime import datetime
import smtplib
import time

MY_EMAIL = "abc@gamil.com"
PASSWORD = "password"
MY_LAT = 0  # Your latitude
MY_LONG = 0  # Your longitude


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG -5  <= iss_longitude <= MY_LONG + 5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()
    time_in_hour = time_now.hour

    #If the ISS is close to my current position
    # and it is currently dark
    if sunset < time_in_hour < sunrise:
        return True

# Then send me an email to tell me to look up.


while True:
    # Run the code every 60 seconds.
    time.sleep(60)
    if is_iss_overhead() and is_night():

        with smtplib.SMTP("smpt.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg="Subject:Look up!\n\nThe ISS is above you in the sky"
            )
