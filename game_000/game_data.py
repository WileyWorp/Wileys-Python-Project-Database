import random as r

#            0    1    2    3    4    5    6    7    8    9   10   11   12   13   14    15
board_p1 = ['P1', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', 'W']
board_p2 = ['P2', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', 'W']
full_board = ' '.join(board_p1) + "\n" + ' '.join(board_p2)
b_indexes = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15']
p1_pos = 0

def rand_board():
    # p1 <
    r_index = r.choice(b_indexes)
    b_indexes.remove(r_index)
    board_p1[int(r_index)] = "<"
    # p1 X
    r_index = r.choice(b_indexes)
    b_indexes.remove(r_index)
    board_p1[int(r_index)] = "X"
    # p2 <
    r_index = r.choice(b_indexes)
    b_indexes.remove(r_index)
    board_p2[int(r_index)] = "<"
    # p2 X
    r_index = r.choice(b_indexes)
    b_indexes.remove(r_index)
    board_p2[int(r_index)] = "X"
    
def move_p1(target):
    board_p1[p1_pos] = "_"
    p1_new_pos = target
    if p1_new_pos == 16:
        print("Player 1 wins!")
    elif board_p1[p1_new_pos] == "<":
        p1_new_pos -= 2
    elif board_p1[p1_new_pos] == "X":
        p1_new_pos = 0
    board_p1[p1_new_pos] = "P1"