# -*- coding: utf-8 -*-

"""
Program determines whether the year is a leap year
"""


# Identify variable num_year
num_year = int(input("Enter the year number: "))

# Checking for correctness and find the result and output it
if num_year > 0:
    if num_year % 4 == 0 or num_year % 400:
        if num_year % 100 != 0:
            print(f'The year with number {num_year} is leap')
        else:
            print(f'The year with number {num_year} is not leap')
else: 
    print('Uncorrectly data. Try again')
