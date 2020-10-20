# -*-   coding: utf-8 -*-

"""
The program finds the fractional part of the number(first symbol after the dot)
"""


# Entering data and finding the result
print('The first symbol after dot is', abs(int(float(input('Enter your number: '))* 10) % 10))

