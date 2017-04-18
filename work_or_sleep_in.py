#!/usr/bin/env python3

while True:
    try:
        day = int(input("Day (0-6)? "))
        if day > 0 and day < 6:
            print("Go to work")
            break
        elif day == 0 or day == 6:
            print("Sleep in")
            break
        else:
            print("Enter a valid number")
    except ValueError:
        print("Enter a valid number")
