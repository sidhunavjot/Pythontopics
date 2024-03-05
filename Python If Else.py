"""
Given an integer, n , perform the following conditional actions:
If  n is odd, print Weird
If  n is even and in the inclusive range of  to , print Not Weird
If  n is even and in the inclusive range of  to , print Weird
If  n is even and greater than , print Not Weird
"""

import math
import os
import random
import re
import sys


# Function to perform conditional actions
def check_number(n):
    if n % 2 != 0:
        print("Weird")
    elif n % 2 == 0 and 2 < n < 5:
        print("Not Weird")
    elif n % 2 == 0 and 6 <= n <= 20:
        print("Weird")
    elif n % 2 == 0 and n > 20:
        print("Not Weird")


# Main function
if __name__ == '__main__':
    # Reading input integer
    n = int(input("Enter number: ").strip())

    # Checking the numbers
    check_number(n)