# -*- coding: utf-8 -*-
"""
Program calculates number of desks for schoolboys from 3 classes
"""


# Identify variables for all classes
class1 = 0
class2 = 0
class3 = 0
# Entering number of schoolboys
class1 = int(input('Enter number of students in the first class: '))
class2 = int(input('Enter number of students in the second class: '))
class3 = int(input('Enter number of students in the third class: '))
# Checking for correctness and finding result
if class1 and class2 and class3 > 0:
    if (class1 + class2 + class3) % 2 == 0:
        print('You need', (class1 + class2 + class3) // 2, 'desks')
    else:
        print('You need', ((class1 + class2 + class3) // 2)+1,'desks')
else:
    print('Uncorrectly data.Try again')


