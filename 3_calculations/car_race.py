# -*- coding: utf-8 -*-

import math


"""
The program calculates the time in the road. User have to enter speed  day and path lenth
"""


# Entering speed and path lenth
speed = int(input('Enter speed: '))
lenth = int(input('Enter lenth: '))

# Cheking for correctness and finding result
if speed <= 0 or lenth <= 0:
    raise Exception('Incorrect data')

print(f'You need {math.ceil(lenth / speed)} days')
