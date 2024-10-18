import random as r

#            0    1    2    3    4    5    6    7    8    9   10   11   12   13   14
board_p1 = ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', 'W']
board_p2 = ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', 'W']
full_board = ' '.join(board_p1) + "\n" + ' '.join(board_p2)
b_indexes = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14']

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
    # Final product
    full_board = ' '.join(board_p1) + "\n" + ' '.join(board_p2)
    print(full_board)