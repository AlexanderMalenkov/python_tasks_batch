# -*- coding: utf-8 -*-

"""
Program determines whether the chessboard cells are the same color
"""



# Entering cells' coordinates
cell_x1 = int(input('Enter X: '))
cell_y1 = int(input('Enter Y: '))
cell_x2 = int(input('Enter X: '))
cell_y2 = int(input('Enter Y: '))

# Checking for correctness and checking for a neibor's location and ouput the result
if cell_x1 in range(1,9) and cell_x1 in range(1,9):
    if cell_y1 in range(1,9) and cell_y1 in range(1,9):
        if cell_x2 in range(1,9) and cell_x2 in range(1,9):
            if cell_y2 in range(1,9) and cell_y2 in range(1,9):
                if (cell_x1 + cell_x2 + cell_y1 + cell_y2) % 2 == 0:
                    print('Yes')
                else:
                    print('No')

            else:
                print('Uncorrectly data. Try again')
        else:
             print('Uncorrectly data. Try again')
    else:
        print('Uncorrectly data. Try again')
else:
    print('Uncorrectly data. Try again')


