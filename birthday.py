"""
birthday.py
Author: Daniel M
Credit: Dad, internet, myself
Assignment:

Your program will ask the user the following questions, in this order:

1. Their name.
2. The name of the month they were born in (e.g. "September").
3. The year they were born in (e.g. "1962").
4. The day they were born on (e.g. "11").

If the user's birthday fell on October 31, then respond with:

  You were born on Halloween!

If the user's birthday fell on today's date, then respond with:

  Happy birthday!

Otherwise respond with a statement like this:

  Peter, you are a winter baby of the nineties.

Example Session

  Hello, what is your name? Eric
  Hi Eric, what was the name of the month you were born in? September
  And what year were you born in, Eric? 1972
  And the day? 11
  Eric, you are a fall baby of the stone age.
"""
from datetime import datetime
from calendar import month_name
todaymonth = datetime.today().month
todaydate = datetime.today().day
todaymonth = month_name[todaymonth].lower()
name=input("Hello, what is your name? ")
month=input(("Hi "+name+", what was the name of the month you were born in? "))
year=int(input("And what year were you born in, "+name+"? "))
day=int(input("And the day? "))

month=month.lower()

#Seasons
winter=["december","january","february"]
spring=["march","april","may"]
summer=["june","july","august"]
fall=["september","october","november"]
season=""

message=""

if month in winter:
    season="winter"
elif month in spring:
    season="spring"
elif month in summer:
    season="summer"
elif month in fall:
    season="fall"
    
if year<=1989 and year>=1980:
    group="eighties"
elif year<=1999 and year>=1990:
    group="nineties"
elif year>=2000:
    group="two thousands"
elif year<1980:
    group="Stone Age"
    
message=(name+", you are a "+season+" baby of the "+group+".")

if month==todaymonth and day==todaydate:
    message="Happy birthday!"
elif month=="october" and day==31:
    message="You were born on Halloween!"
    
print(message)









