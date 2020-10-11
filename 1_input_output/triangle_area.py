# -*- coding: utf-8 -*-
"""
User has to enter length of triangle legs and program will substitute input data in the formula and output the result
"""


# Input lenth
leg1 = int(input('Enter lenth of the first leg: '))
leg2 = int(input('Enter lenth of the second leg: '))
# Cheking for correctness and substitute input data in formula and output result
if leg1 > 0 and leg2 > 0:
    area = (leg1 * leg2)/2
    print('Area of triangle: ', area)
else:
    print('Uncorrectly data.Try again')






