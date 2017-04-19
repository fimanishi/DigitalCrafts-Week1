#!/usr/bin/env python3

def number_factors(number):
    factors = []
    for i in range(1, number//2+1):
        if number%i == 0:
            factors.append(i)
    factors.append(number)
    return factors

print(number_factors(999))
