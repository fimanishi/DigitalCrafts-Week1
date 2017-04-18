#!/usr/bin/env python3

from math import ceil

while True:
    try:
        amount = float(input("Total bill amount? "))
        if amount > 0:
            break
    except ValueError:
        print("Please enter a valid bill value.")

service = ""

while not (service == "good" or service == "fair" or service == "bad"):
    service = input("Level of service? ").lower()

while True:
    try:
        people = int(input("Split how many ways? "))
        if people > 0:
            break
    except ValueError:
        print("Enter a valid number of people.")

if service == "good":
    tip_percentage = 0.2;
elif service == "fair":
    tip_percentage = 0.15;
elif service == "bad":
    tip_percentage = 0.1;

tip_amount = round(amount*tip_percentage,2)

total_amount = round(amount + tip_amount,2)

per_person = ceil(total_amount/people)

print("Tip amount: ${:.2f}".format(tip_amount))
print("Total amount: ${:.2f}".format(total_amount))
print("Amount per person: ${:.2f}".format(per_person))
