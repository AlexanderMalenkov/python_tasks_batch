# -*- coding: utf-8 -*-
"""
User has to enter length of triangle legs and program will substitute input data in the formula and output the result
"""


# Input lenth
first_leg = int(input('Enter lenth of the first leg: '))
second_leg = int(input('Enter lenth of the second leg: '))

# Cheking for correctness and substitute input data in formula and output result
if first_leg > 0 and second_leg > 0:
    print('Area of triangle: ', (first_leg * second_leg) / 2)
else:
    print('Uncorrectly data.Try again')






