#!/usr/bin/env

more_coins = "y"
coins = 0
while more_coins == "y":
    print("You have {} coins".format(coins))
    while True:
        more_coins = input("Do you want another? (y/n) ").lower()
        if more_coins == "y" or more_coins == "n":
            break
    coins += 1
print("Bye")
