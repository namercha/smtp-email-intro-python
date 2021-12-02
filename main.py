# import smtplib
#
# my_email = "from@gmail.com"
# password = ""
# to_email = "to@gmail.com"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs=to_email,
#                         msg="Subject:Hi from Nabil\n\nHello, this is a test email using python I wrote.")
# FYI Gmail requires modifying security settings of the account to enable less secure access.

##
# import datetime as dt
# now = dt.datetime.now()
# print(now)
# print(now.year)
# if now.year == 2020 or now.year == 2021:
#     print("Wear a face mask.")
# print(now.month)
#
# date_of_birth = dt.datetime(year=1995, month=12, day=12)
# print(date_of_birth)

##
# Sending a monday motivational email:
import datetime as dt
import smtplib
import random

MY_EMAIL = "from@gmail.com"
PASSWORD = ""
TO_EMAIL = "to@gmail.com"

now = dt.datetime.now()
weekday = now.weekday()
# Monday is 0, Tuesday is 1 ...
if weekday == 1:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs=TO_EMAIL,
                            msg=f"Subject:Monday Motivation\n\n{quote}")
