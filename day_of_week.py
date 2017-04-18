#!/usr/bin/env

while True:
    try:
        day = int(input("Day (0-6)? "))
        if day >= 0 and day <= 7:
            break
    except ValueError:
        print("Please enter a valid number.")

week_days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
print(week_days[day])
