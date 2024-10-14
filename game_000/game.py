import time
import game_data as game_data_py
import tutorial as tutorial_py
import ellipsis as ellipsis_py

print("Welcome to my first python terminal game project!")
'''start = input("Press [ENTER] to start: ")
while start != "":
    start = input("Press [ENTER] to start: ")'''

while True:
    tut_q = input('Would you like the tutorial? (y/n): ').lower()
    if tut_q == 'y':
        tutorial_py.tutorial()
        time.sleep(1)
        break
    elif tut_q == 'n':
        break
    else:
        print('Invalid input. Please enter y or n.')

ellipsis_py.ellipsis()

game_data_py.rand_board()