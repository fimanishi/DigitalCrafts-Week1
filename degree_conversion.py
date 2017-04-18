#!/usr/bin/env

def to_farenheit(degc):
    degf = degc*1.8 + 32
    return degf

def main():
    temp = int(input("Temperature in C? "))
    print("{} F".format(to_farenheit(temp)))

if __name__ == "__main__":
    main()
