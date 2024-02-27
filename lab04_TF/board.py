# FILL THIS FILE
def new_board():
    board = []
    for _ in range(3):
        a = []
        for _ in range(3):
            a.append('-')
        board.append(a)
    return board

def get(board, row, column):
    return board[row][column]

def is_empty(board, row, column):
    if board[row][column] == '-':
        return True 
    else:
        return False

def print_board(board):
    for r in board:
        for c in r:
            print(c,end = ' ')
        print()

def place(board,marker,row,column):
    if not is_empty(board,row,column): return False
    board[row][column] = marker
    return True

def is_full(board):
    return '-' not in sum(board,[])

def is_winner(board,marker):
    lines = [
        # rows
        (0,0, 0,1, 0,2),
        (1,0, 1,1, 1,2),
        (2,0, 2,1, 2,2),
        # columns
        (0,0, 1,0, 2,0),
        (0,1, 1,1, 2,1),
        (0,2, 1,2, 2,2),
        # diagonals
        (0,0, 1,1, 2,2),
        (0,2, 1,1, 2,0)  
        ]
    for r1,c1, r2,c2, r3,c3 in lines:
        if board[r1][c1] + board[r2][c2] + board[r3][c3] == marker * 3: return True
    return False


if __name__ == ’__main__’:
    b = new_board()
    print(get(b,1,1))
    print(is_empty(b,1,1))
    print_board(b)

    place(b,'X',1,1)
    place(b,'X',0,0)
    place(b,'X',2,2)
    print_board(b)
    print(is_full(b))
    print(is_winner(b,"X"))