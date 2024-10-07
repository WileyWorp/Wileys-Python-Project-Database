import random as rand
import time as t
from game_data import full_board
import tutorial as tutorial_py

print("Welcome to my first python terminal game project!")
'''start = input("Press [ENTER] to start: ")
while start != "":
    start = input("Press [ENTER] to start: ")'''

while True:
    tut_q = input('Would you like the tutorial? (y/n): ').lower()  # Convert input to lowercase
    if tut_q == 'y':
        tutorial_py.tutorial()  # Call tutorial function
        break
    elif tut_q == 'n':
        break
    else:
        print('Invalid input. Please enter y or n.')

print('finished')