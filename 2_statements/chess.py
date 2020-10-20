# -*- coding: utf-8 -*-

"""
Program determines whether the chessboard cells are the same color
"""


# Entering an array for coordinates and variables
cells = [] 
coord = 0

# Enter a number and check it for belonging to the interval
for i in range(4):
    coord = int(input('Enter your coordinates: ')) 
    if coord not in range(1,9):
          raise Exception('Incorrect data')
    cells.append(coord)

# Finding and output result
if sum(cells) % 2 == 0:
    print('Yes')
else:
    print('No')
