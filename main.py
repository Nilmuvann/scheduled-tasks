import datetime as dt
import pandas as pd
import random
import smtplib

MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

now = dt.datetime.now()
today_month = now.month
today_day = now.day
today = (today_month, today_day)

dt = pd.read_csv("birthday-wisher-normal-start/birthdays.csv")

birthdays_dict = {(data_row["month"], data_row["day"]) : data_row for (index, data_row) in dt.iterrows()}

if (today_month, today_day) in birthdays_dict:
    entry = birthdays_dict[today]
    file_path = f"birthday-wisher-normal-start/letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as mail:
        content = mail.read()
        content = content.replace("[NAME]", entry["name"])
    
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls() #making connection secure
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(
           from_addr=MY_EMAIL, 
           to_addrs=MY_EMAIL, 
           msg=f"Subject: Happy Birthday\n\n{content}")



