##################### Extra Hard Starting Project ######################
import pandas
import datetime as dt
import random
import smtplib


email = "alexleetest123@gmail.com"
password = "testpassword@123"
# 1. Update the birthdays.csv
# done
def send_letter(name):
    letter_number = random.randint(1, 3)
    letters = ""
    with open(f"letter_templates/letter_{letter_number}.txt") as letter:
        for lines in letter:
            letters += lines.replace("[NAME]", name)
        print(letters)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(from_addr= email, to_addrs="alexleetest123@yahoo.com", msg=f"Subject:Happy Birthday \n\n {letters}")


# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
birthdays = pandas.read_csv("birthdays.csv")
for index, row in birthdays.iterrows():
    if row.month == now.month and row.day == now.day:
        send_letter(row["name"])
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
