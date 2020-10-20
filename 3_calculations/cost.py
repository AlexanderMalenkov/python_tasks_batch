# -*- coding: utf-8 -*-

""" 
The program calculates cost of purchase
"""


# Entering data and checking for correctness
rub = int(input('Rub: '))
cent = int(input('Cents: '))
count = int(input('Count of product: '))
if rub <= 0 or cent <= 0 or count <= 0:
    raise Exception('Incorrect data')

# Calculating the response
print (f'{rub * count + (cent * count) // 100} Rub {(cent * count) % 100} c')
