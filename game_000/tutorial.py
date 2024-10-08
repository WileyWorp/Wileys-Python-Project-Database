from game_data import full_board
import time as t

def tutorial():
    print("This is the game board")
    print(full_board)
    t.sleep(1)
    print("In every game, the board will contain a few pieces: _, <, and X.")
    t.sleep(1)
    print("'_' will be a normal board piece.")
    t.sleep(1)
    print("'<' will send you back two board pieces.")
    t.sleep(1)
    print("'X' will send you back to the beginning of the board.")
    t.sleep(1)
    print("On each player's board there will be 1 of each special board piece set randomly per game.")
    print('''
_ _ _ _ X _ _ _ _ _ < _ _ _ _
_ _ _ _ _ _ < _ _ _ _ _ _ X _
          ''')
    
tutorial()