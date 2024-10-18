from game_data import full_board
import time as t

def tutorial():
    print("This is the game board")
    print(full_board)
    t.sleep(1.5)
    print("In every game, the board will contain a few pieces: _, <, and X.")
    t.sleep(1.5)
    print("'_' will be a normal board piece.")
    t.sleep(1.5)
    print("'<' will send you back two board pieces.")
    t.sleep(1.5)
    print("'X' will send you back to the beginning of the board.")
    t.sleep(1.5)
    print("On each player's board there will be 1 of each special board piece set randomly per game.")
    t.sleep(1.5)
    print("Your player, 'O', will start at the first board piece and your goal is to send it to the 'W'")
    t.sleep(1.5)
    print(''' Example:
O _ _ _ X _ _ _ _ _ < _ _ _ _ W
O _ _ _ _ _ _ < _ _ _ _ _ X _ W
          ''')
    print("You will roll dice to figure out how many moves you make.")
    t.sleep(1.5)
    print("Now go my children, have fun playing my game.")