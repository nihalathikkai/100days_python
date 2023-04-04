import smtplib
import datetime as dt 
from random import choice, randint
import csv

#gmail = "mfreeman287p@gmail.com"
#yahoo = "mfreeman287p@yahoo.com"


QUOTES = "D:/python/100days/day32_intermediate+_emailer/quotes.txt"

def send_mail(to_address, message):
    my_email = "mfreeman287p@gmail.com"
    password = "rsbhslpmkjcktwyn"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=to_address, msg=message)

def monday_motivation():
    now = dt.datetime.now()
    print(now)
    weekday = now.weekday()
    if weekday == 0:
        with open(QUOTES, 'r') as file:
            all_quotes = file.readlines()
            quote = choice(all_quotes)
        print(quote)
        send_mail(to_address="mfreeman287p@gmail.com",
                message=f"Subject:Monday Motivation\n\n{quote}")
        
        
        

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)

BIRTHDAYS_DATA = "D:/python/100days/day32_intermediate+_emailer/birthdays.csv"
LETTER_TEMPLATES = "D:/python/100days/day32_intermediate+_emailer/letter_templates"

def get_template():
    with open(f"{LETTER_TEMPLATES}/letter_{randint(1,3)}.txt") as file:
        template = "".join(file.readlines())
    return template


# with open(BIRTHDAYS_DATA, 'r') as file:
#     data = csv.reader(file)
#     next(data)
#     for row in data:
#         print(row)
#         if int(row[3])==now.month and int(row[4])==now.day:
#             letter = template.replace("[NAME]", row[0])
#             print(letter)
#             send_mail(to_address=row[1], message=f"Subject:Happy Birthday {row[0]}\n\n{letter}")

birthdays_dict = {}

with open(BIRTHDAYS_DATA, 'r') as file:
    data = csv.reader(file)
    next(data)
    for row in data:
        month = int(row[3])
        day = int(row[4])
        # birthdays_dict[(month, day)] = birthdays_dict.get((month, day), [])+[row]
        birthdays_dict.setdefault((month, day), []).append(row)

now = dt.datetime.now()
        
today = birthdays_dict.get((now.month, now.day), [])\

for row in today:
    name = row[0]
    to_address = row[1]
    template = get_template()
    letter = f"Subject:Happy Birthday {name}\n\n"+template.replace("[NAME]", name)
    print(letter)
    send_mail(to_address=to_address, message=letter)
    print("Email send")