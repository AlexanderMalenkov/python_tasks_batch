# -*- coding: utf-8 -*-

"""
The program finds the last digit of the number
"""


# Identify a variable and checking for correctness
num = int(input('Enter your number: '))
if insistance(num, str):
  raise Exception('Your entered the letter')
  
# Finding result and output it
print(f'Last digit of the number {num} is {abs(num % 10)}')


