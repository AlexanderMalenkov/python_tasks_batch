# -*- coding: utf-8 -*-

"""Programm calculates the number of hours in a given number of minutes"""

#enter number of minutes and identify final hours and minutes

hours = 0
minutes = 0
num_min = int(input('Enter number of minutes: '))

#calculating the number of minutes and hours in the entered minutes and checking for correctness and cheking for the number of days in the entered minutes

if num_min > 0:
     hours = num_min // 60
     minutes = num_min % 60
     if num_min < 1440:
         print (hours, 'H', minutes, 'Min')
     else:
         print (hours % 24, 'H', minutes, 'Min')
else:
    print ('Uncorrectly data. Try again')


