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

def remove(board,row,column):
    if is_empty(board,row,column): return False
    board[row][column] = '-'
    return True

def is_full(board):
    return '-' not in sum(board,[])

def possible_lines():
    return [
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

def is_winner(board,marker):
    for r1,c1, r2,c2, r3,c3 in possible_lines():
        if board[r1][c1] + board[r2][c2] + board[r3][c3] == marker * 3: return True
    return False

def eval(board,marker):
    if marker == 'X':
        opponent = 'O'
    else:
        opponent = 'X'
    value = 0
    for r1,c1, r2,c2, r3,c3 in possible_lines():
        line = board[r1][c1] + board[r2][c2] + board[r3][c3]
        if (marker in line and opponent in line) or line == '---':
            # Line value = 0
            pass
        else:
            if marker in line:
                sign = 1
            else:
                sign = -1
            value += sign * 10 ** (2-line.count('-'))
    return value


if __name__ == '__main__':
    b = new_board()
    print(get(b,1,1))
    print(is_empty(b,1,1))
    print_board(b)
    print()

    place(b,'X',1,1)
    place(b,'O',1,0)
    place(b,'X',2,2)
    place(b,'O',2,0)
    
    print_board(b)
    print(is_full(b))
    print(is_winner(b,"X"))

    print(eval(b,'O'))