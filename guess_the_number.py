#!/usr/bin/env

from random import randint

choice = "Y"

while choice == "Y":
    print("I am thinking of a number between 1 and 10.")
    turns = 0
    guesses = 5
    random_number = randint(1,10)
    print(random_number)
    while True:
        if turns == guesses:
            print("You ran out of guesses!")
            break
        print("You have {} guesses left".format(5-turns))
        while True:
            try:
                number = int(input("What's the number? "))
                if number >= 1 and number <= 10:
                    break
                else:
                    print("Enter a valid number.")
            except ValueError:
                print("Enter a valid number.")
        if number == random_number:
            continue_guessing = False
            print("Yes! You win!")
            break
        elif number < random_number:
            print("{} is too low".format(number))
        elif number > random_number:
            print("{} is too high".format(number))
        turns += 1
    while True:
        choice = input("Do you want to play again (Y or N)? ").upper()
        if choice == "Y" or choice == "N":
            break
print("Bye!")
