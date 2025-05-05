#!/usr/bin/python3
"""
factorial_recursive.py

A simple Python script that calculates the factorial of a non-negative integer
using a recursive function.

Usage:
    ./factorial_recursive.py <non_negative_integer>

Example:
    ./factorial_recursive.py 4
    Output: 24
"""

import sys

def factorial(n):
    """
    Recursively computes the factorial of a non-negative integer.

    Parameters:
        n (int): The number to compute the factorial of. Must be >= 0.

    Returns:
        int: The factorial of n.

    Raises:
        RecursionError: If the recursion limit is exceeded.
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Entry point of the program
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <non_negative_integer>")
        sys.exit(1)
    try:
        number = int(sys.argv[1])
        print(factorial(number))
    except ValueError:
        print("Error: Argument must be a non-negative integer.")
        sys.exit(1)
