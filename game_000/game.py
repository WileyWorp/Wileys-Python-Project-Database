import random as rand
import time as t
import tutorial as tutorial_py

print("Welcome to my first python terminal game project!")
'''start = input("Press [ENTER] to start: ")
while start != "":
    start = input("Press [ENTER] to start: ")'''

#            0    1    2    3    4    5    6    7    8    9   10   11   12   13   14    15
board_p1 = ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_']
board_p2 = ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_']
full_board = ' '.join(board_p1) + "\n" + ' '.join(board_p2)

tut_q = input('Would you like the tutorial? (y/n): ')

if tut_q == 'y':
    tutorial_py.tutorial()

while tut_q != 'y':
    if tut_q == 'n':
        break
    tut_q = input('Please enter y/n: ')
    if tut_q == 'y':
        print('tutorial')
        break
    elif tut_q == 'n':
        break