#!/usr/bin/python3

import sys
import math

def factor(line):
    number = int(line)
    if number < 4:
        print(f"{number}={number}*1")
        return
    for i in range(2, int(math.sqrt(number)) + 1):  # Loop only up to sqrt(number)
        if number % i == 0:
            value = number // i
            print(f"{number}={i}*{value}")
            return
    print(f"{number}={number}*1")  # Fallback if no factor is found

if len(sys.argv) != 2:
    print("Usage: factors <file>")
    sys.exit(1)

filename = sys.argv[1]

try:
    with open(filename, "r") as file:  # Use 'with' for file handling
        for line in file:
            factor(line.strip())  # Factorize each line (each number)
except FileNotFoundError:
    print(f"Error: Can't open file {filename}")
    sys.exit(1)

