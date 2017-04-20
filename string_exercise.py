#!/usr/bin/env python3

string = "test"

#  string uppercased
print(string.upper())

# string capitalized
print(string.capitalize())

# string reversed
new_string = ""
# runs through the string from end to beginning
for i in range(len(string)-1, -1, -1):
    # adds the item to the new string
    new_string += string[i]
print(new_string)

# replaces the letters in the paragraph that match list_letters with numbers
paragraph = "I want to test this"

list_letters = ["A", "E", "G", "I", "O", "S", "T"]
list_numbers = ["4", "3", "6", "1", "0", "5", "7"]
length = range(len(list_letters))
new_paragraph = ""
# gets each letter in the paragraph
for i in paragraph:
    check = 0
    # iterates through the list of letters and
    # compare the letter from the paragraph
    for j in length:
        # if they match, add the corresponding number to
        # the string and changes check to 1
        if i.upper() == list_letters[j]:
            new_paragraph += list_numbers[j]
            check = 1
    # if check is not 1, means that the letter is not
    # in the list and then the original letter is added to the string
    if check != 1:
        new_paragraph += i

print(new_paragraph)

# if the word has long vowels, extends it to length of five
word = "Ooze"
# defines a previous letter value
previous = ""
vowels = ["a", "e", "i", "o", "u"]
output = ""
# iterates throug the word
for i in word:
    check = 0
    # iterates through the vowels list
    for j in vowels:
        # if the letter in word is a vowel and matches the previous letter
        if i.lower() == j and i.lower() == previous.lower():
            # adds 4 of the same letter to the new string
            output += i*4
            check = 1
    # if it wasn't a vowel or if didn't match the previous letter
    if check == 0:
        # appends to the new string the original value
        output += i
    # updates the previous letter with the current letter
    previous = i
print(output)
