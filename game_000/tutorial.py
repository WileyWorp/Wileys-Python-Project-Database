import game as main
import time as t

def tutorial():
    print("This is the game board")
    print(main.full_board)
    t.sleep(1)
    print("In every game, the board will contain a few pieces: _, <, and X.")
    t.sleep(1)
    print("'_' will be a normal board piece.")
    t.sleep(1)
    print("'<' will send you back two board pieces.")
    t.sleep(1)
    print("'X' will send you back to the beginning of the board.")