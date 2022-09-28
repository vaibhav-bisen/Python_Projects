
import datetime as dt
import pandas as pd
import smtplib
import random

MY_EMAIL = "abc@gmail.com"
PASSWORD = "password"
# Check if today matches a birthday in the birthdays.csv
# Create a tuple from today's month and day using datetime. e.g. today = (today_month, today_day)
now = dt.datetime.now()
current_month = now.month
current_day = now.day
today = (current_month, current_day)
# Use pandas to read the birthdays.csv
data = pd.read_csv("birthdays.csv")
# Use dictionary comprehension to create a dictionary from birthday.csv that is formatted like this:
# birthdays_dict = {
#     (birthday_month, birthday_day): data_row
# }
# Dictionary comprehension template for pandas DataFrame looks like this:
# new_dict = {new_key: new_value for (index, data_row) in data.iterrows()}
# e.g. if the birthdays.csv looked like this:
# name,email,year,month,day
# Test,test@email.com,2000,11,12
# Then the birthdays_dict should look like this:
# birthdays_dict = {
#     (11, 12): Test,test@email.com,2000,11,12
# }
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
# Then you could compare and see if today's month/day tuple matches one of the keys in birthday_dict:
if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    # If there is a match, pick a random letter (letter_1.txt/letter_2.txt/letter_3.txt) from letter_templates and replace the [NAME] with the person's actual name from birthdays.csv
    # Use the random module to get a number between 1-3 to pick a random letter.
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    # Use the replace() method to replace [NAME] with the actual name.
    with open(file_path) as letter_file:
        contents = letter_file.read()
        letter = contents.replace("[NAME]", birthday_person["name"])
    # Send the letter generated in that person's email address.
    # Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        # Remember to call .starttls()
        connection.starttls()
        # Remember to log in to your email service with email/password. Make sure your security setting is set to allow less secure apps.
        connection.login(user=MY_EMAIL, password=PASSWORD)
        # The message should have the Subject: Happy Birthday then after \n\n The Message Body.
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=birthday_person["email"], msg=f"Subject:Happy Birthday!\n\n{letter}")
