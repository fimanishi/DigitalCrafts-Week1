#!/usr/bin/env

print("Please fill in the blanks below:")
print("____(name)____'s favorite band is ____(band)____.")
name = input("What is name? ")
band = input("What is band? ")
print("{name}'s favorite band is {band}.".format(name=name, band=band))
