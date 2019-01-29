# -*- coding: utf-8 -*-
"""
Created on Tue Jan 29 10:37:12 2019

@author: 612383423
"""

### Task 3 

def is_prime(number):
    """returns True if *number* is prime"""
    for element in range(number):
        if number % element == 0:
            return False
    return True

def print_next_prime(number):
    """prints the closest prime number larger than *number* """
    index = number
    while True:
        index +=1
        if is_prime(index):
            print(index)