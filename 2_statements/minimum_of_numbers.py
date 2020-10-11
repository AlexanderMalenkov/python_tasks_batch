# -*- coding: utf-8 -*-

"""
Program compare two entered numbers and output the smaller
"""


# Entering variables
first_num = int(input('Enter your number: '))
second_num = int(input('Enter your number: '))

# Comparing and output result
if first_num > second_num:
    print(second_num)
elif first_num < second_num:
    print(first_num)
else:
    print('Numbers are equal')


    
