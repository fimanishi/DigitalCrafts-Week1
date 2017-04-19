#!/usr/bin/env python3

def guess_game(lower_limit, upper_limit):
    user_input = ""
    guesses = 1
    while user_input.lower() != "correct":
        number = (upper_limit + lower_limit) // 2
        print("Is your number {}?".format(number))
        user_input = input("Is this number (too high), (too low) or (correct)? ")
        if user_input.lower() == "correct":
            print("I guessed your number in {} guesses!".format(guesses))
        elif user_input.lower() == "too low":
            lower_limit = number
        elif user_input.lower() == "too high":
            upper_limit = number
        else:
            print("Please enter a valid input")
            guesses -= 1
        guesses += 1

guess_game(0,100)
