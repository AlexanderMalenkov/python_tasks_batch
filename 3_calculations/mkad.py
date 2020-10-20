# -*- coding: utf-8 -*-

"""
The program determines the rider's position after entered time
"""


# Entering time and speed
time = float(input("Enter rider's way time: "))
speed = float(input("Enter rider's speed: "))

# Determine rider's way and finding absolute of his time and speed if they are less than zero
print('Rider will stop on the',(109 - (abs(time) * abs(speed)) % 109),'km')
