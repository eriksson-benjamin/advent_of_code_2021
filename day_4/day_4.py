import numpy as np

# Import input
draw_order = np.loadtxt('draw_order.txt', delimiter=',', dtype='int')
b = np.loadtxt('boards.txt', dtype='int')
n_boards = int(b.shape[0]/b.shape[1])

# Reshape boards to (5x5x100) array
boards = b.reshape([n_boards, 5, 5])
bool_boards = np.zeros(np.shape(boards), dtype='int')

'''
Part 1
'''

# Apply draws
for draw in draw_order:
    print(f'Drawing number: {draw}')
    bool_boards[boards==draw] = 1

    '''
    row_sum is a 5x100 array where each column corresponds to a board. For 
    board 0 (column 0 in row_sum), each row in row_sum correspond to the sum 
    of the rows in bool_boards. When this reaches 5, the board has reached
    "bingo" along a row. Same goes for col_sum but for "bingo" along a column.
    '''
    row_sum = np.sum(bool_boards, axis=2) 
    col_sum = np.sum(bool_boards, axis=1)

    # Check if bingo on board
    if np.any(row_sum==5):
        board_index = np.where(row_sum==5)
        print(f'Bingo! (on row {board_index[1]} on board {board_index[0]})')
        break
    elif np.any(col_sum==5):
        board_index = np.where(col_sum==5)    
        print(f'Bingo! (on column {board_index[1]} on board {board_index[0]})')
        break

# Find sum of unmarked numbers on first winning board
winning_board = boards[board_index[0], :, :]
unmarked_bool = bool_boards[board_index[0], :, :]==0
unmarked = winning_board[unmarked_bool]


print(f'Final score: {unmarked.sum()*draw}')

# '''
# Part 2 - Unfinished
# '''
# # We know that after all numbers are drawn, all boards are fully marked, so 
# # we can apply the draw orders backwards to save time
# bool_boards = np.ones(np.shape(boards))

# for draw in np.flip(draw_order):
#     # Unmark boards
#     bool_boards[boards==draw] = 0
    
#     # Sum of marked numbers on each row/column
#     row_sum = np.sum(bool_boards, axis=2) 
#     col_sum = np.sum(bool_boards, axis=1)

#     # Check rows/column which are fully marked
#     bool_row = row_sum==5
#     bool_col = col_sum==5

#     # When a row/col in bool_row/col has a sum of 1 it has just won
#     bool_row_sum = np.sum(bool_row, axis=1)
#     bool_col_sum = np.sum(bool_col, axis=1)

#     # Index where the sum is 1
#     row_index = np.where(bool_row_sum==1)[0]
#     col_index = np.where(bool_col_sum==1)[0] 
    
#     # Check if only one row/column is fully marked
#     if len(row_index):
#         print(f'Last bingo! (on board {row_index[0]})')
#         break
#     elif len(col_index):
#         print(f'Last bingo! (on board {col_index[0]})')
#         break
    
# # Find sum of unmarked numbers on last winning board
# winning_board = boards[board_index[0], :, :]
# unmarked_bool = bool_boards[board_index[0], :, :]==0
# unmarked = winning_board[unmarked_bool]  














