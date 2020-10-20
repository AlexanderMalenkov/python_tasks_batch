# -*- coding: utf-8 -*-

"""
Program compare two entered numbers and output the smaller
"""


# Identify  variables and array and entering count of nnumbers
minimum = []
count = int(input('Input count of mubers: '))

# Filling in the array
for i in range(count):
    minimum.append(int(input('Enter your numbers: ')))

# Output the result
if len(set(minimum)) == 1:
    print('Numbers are equal')
else:
    print (f'Minimum is: {min(minimum)}')



    
