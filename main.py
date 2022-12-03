##################### Birthday Wish ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

# -----------Code-----------
import pandas as pd
import random
import smtplib
import datetime as dt

my_email = "@gmail.com"
my_pass = "password"

dt_now = dt.datetime.now()
c_month = dt_now.month
c_date = dt_now.day

df = pd.read_csv("birthdays.csv")

if c_month in df.values and c_date in df.values:
    per_df = df[(df['month']==c_month) & (df['day']==c_date)]
    per_detail = per_df.to_dict('records')

    for n in range(0, len(per_detail)):
        txt_n = random.randint(1, 3)
        with open(f"letter_templates/letter_{txt_n}.txt") as txt:
            letter = txt.read()
            e_letter = letter.replace('[NAME]', per_detail[n]['name'])


        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(my_email, my_pass)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=f"{per_detail[n]['email']}",
                msg=f"Subject:Happy Birthday Dear\n\n{e_letter}"
            )





