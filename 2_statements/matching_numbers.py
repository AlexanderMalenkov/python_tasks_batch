# -*- coding: utf-8 -*-

"""
The program finds matching numbers among the given numbers
"""


# Enter variables 
first_number = int(input('Enter the first number: '))
second_number = int(input('Enter the second number: '))
third_number = int(input('Enter the third number: '))

# Comparing numbers and output the result
if first_number ==  second_number ==  third_number:
    print(3)
elif first_number == second_number or first_number == third_number or second_number == third_number:
    print(2)
else:
    print(0)


