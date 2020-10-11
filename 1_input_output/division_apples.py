# -*- coding: utf-8 -*-

"""
User has to insert number of schoolboys and number of apples
"""


# Identify variables num_students and num_apples
num_students = 0
num_apples = 0

# Enter number of students and number of apples
num_students = int(input('Enter number of students: '))
num_apples = int(input('Enter number of apples: '))

# Cheking for correctness and find and output result of division
if num_students > 0 and num_apples > 0:
    print('Each of the students will recieve: ', num_apples // num_students)
    print('Will remain:', num_apples % num_students)
else:
    print('Uncorrectly data. Try again')
