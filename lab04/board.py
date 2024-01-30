def new_board():
    board = [['-' for _ in range(3)] for _ in range(3)]
    return board

def get(board, row, col):
    return board[row][col]

#def is_empty(board):
#    for row in board:
#        for col in row:
#            if col != '-':
#                return False
#    return True
def is_empty(board, row, col):
    return board[row][col] == '-'

def print_board(board):
    for row in board:
        print(' '.join(row))

def place(board, marker, row, col):
    board[row][col] = marker

def is_full(board):
    for row in board:
        for col in row:
            if col == '-':
                return False
    return True

def is_winner(board, marker):
    def has_winner_row(board, marker):
        for row in board:
            if len(set(row)) == 1 and marker in set(row):
                return True
    if has_winner_row(board, marker) or has_winner_row(list(zip(*board)), marker):
        return True
    if board[0][0] == marker and board[1][1] == marker and board[2][2] == marker:
        return True
    if board[0][2] == marker and board[1][1] == marker and board[2][0] == marker:
        return True
    return False

if __name__ == '__main__': 
    board = new_board()
    place(board,'X',0,2)
    place(board,'X',1,1)
    place(board,'X',1,0)
    print_board(board)
    assert(not is_winner(board, 'X'))
    transpose = list(zip(*board))
    print_board(transpose)
    assert(not is_winner(transpose, 'X'))
    place(board, 'X', 2, 0)
    assert(is_winner(board, 'X'))
    place(board, 'O', 2, 0)
    assert(not is_winner(board, 'X'))
    place(board, 'X', 1, 2)
    assert(is_winner(board, 'X'))
