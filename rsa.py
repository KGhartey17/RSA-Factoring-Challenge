#!/usr/bin/python3

import sys
import math

# Helper function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Function to factorize a number into two prime factors
def factor_rsa(line):
    number = int(line)
    if number < 4:
        print(f"{number}={number}*1")
        return
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            value = number // i
            if is_prime(i) and is_prime(value):
                print(f"{number}={i}*{value}")
                return
    print(f"{number}={number}*1")  # Fallback if no prime factorization is found

if len(sys.argv) != 2:
    print("Usage: rsa <file>")
    sys.exit(1)

filename = sys.argv[1]

try:
    with open(filename, "r") as file:
        for line in file:
            factor_rsa(line.strip())  # Factorize each number as RSA requires
except FileNotFoundError:
    print(f"Error: Can't open file {filename}")
    sys.exit(1)

