#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculate the factorial of a non-negative integer using recursion.

    Parameters:
    n (int): A non-negative integer for which to compute the factorial.

    Returns:
    int: The factorial of the input number.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Read the number from command-line arguments, compute its factorial, and print it
f = factorial(int(sys.argv[1]))
print(f)
