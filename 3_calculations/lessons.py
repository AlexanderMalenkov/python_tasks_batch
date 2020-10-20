# -*- coding: utf-8 -*-
"""
The program determines the end time of the lesson the number of which was entered by the user
"""


# Entering number of lesson
num_lesson = int(input('Enter number of lesson: '))
time = 540

# Checking for correctness and finding result
if num_lesson not in range(1,11):
    raise Exception('Incorrect data')

time += num_lesson * 45
num_lesson -= 1

while num_lesson > 0:
    if num_lesson % 2 == 0:
        time += 10
    else:
        time += 5
    num_lesson -= 1
print(f'{time // 60} H {time % 60} Min')

