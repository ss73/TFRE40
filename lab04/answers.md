# Excercise 1

The full source code is available in [board.py](board.py)

# Excercise 2

Create the function `new_board`, which takes no parameter, and create a 3 × 3 matrix, with
only empty cells.

> The following code snippet creates a 3 × 3 matrix filled with dashes (`-`), where 
> a dash is defined as the empty state  
```python
def new_board():
    board = [['-' for _ in range(3)] for _ in range(3)]
    return board

```

# Excercise 3
Implement the function `get` which takes three arguments, the board, the row number and
the column number, and returns the value at that position in the provided board.

>The `get` function is defined in [board.py](board.py) simply be the following:
```python
def get(board, row, col):
    return board[row][col]
```    

# Excercise 4

Implement the function `is_empty`, which returns True if all cells are empty (contain `-`).

> The following code implements the described functionality. Please note that this is
> not what is required by the GUI implementation in [window_tk.py](window_tk.py).
```python
def is_empty(board):
    for row in board:
        for col in row:
            if col != '-':
                return False
    return True
```    

> The GUI application requires `is_empty` to accept three arguments; board, row
> and column and return if the individual cell is empty. The updated function
> in [board.py](board.py) is defined by:

```python
def is_empty(board, row, col):
    return board[row][col] == '-'

```

# Excercise 5
Implement the function `print_board`, which prints the board.

> The following function in [board.py](board.py) prints the board:

```python
def print_board(board):
    for row in board:
        print(' '.join(row))

```

# Excercise 6
Implement the function `place`, which takes a board, a marker, a row and a column, and
places the marker at the right position on board.

> The following function in [board.py](board.py) places the marker 'in place',
> i.e. no return is required as the matrix is passed by reference:

```python
def place(board, marker, row, col):
    board[row][col] = marker
```    

# Excercise 7
Implement the function `is_full`, which returns true if the board is full (no empty cells),
and false otherwise.

> The following code in [board.py](board.py) implements the function:

```python
def is_full(board):
    for row in board:
        for col in row:
            if col == '-':
                return False
    return True
```

# Excercise 8
Implement the function `is_winner`. The
function takes a board as input, and a marker, and returns true if the player with that
marker has won. To check that, we need to check if the player has positioned the markers
on three cell in a row, in a column, or in a diagonal.

> The `is_winner` function in [board.py](board.py) is defined by the following source code:

```python
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
```

> A nested function is used to avoid duplication as the  checks for winning *columns* is
> performed in the same way as winning *rows* but with a *transposed matrix*. The calculation
> of the matrix transpose is very pythonesque: `list(zip(*matrix))`.

# Excercise 9

Run the `window_tk.py` file and test that it works.

> After updating the `is_empty` function in in [board.py](board.py), the file
> [window_tk.py](window_tk.py) runs as expected

# Excercise 10
Add some tests to the end of the `board.py` file.

> The smoke tests added to the [board.py](board.py) are
> collected in the scope where a check is done to see if
> this file was passed directly to the python interpreter.

```python
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
```

# Excercise 11
Take a look in the window_tk.py. The window class calls functions to update the
board, when buttons are pressed. Try to understand roughly what happens in the methods
`clicked`, `restart_clicked` and `update` methods.

> `clicked` and `restart_clicked` are both callbacks added
> to the GUI components, so they are called when a mouse click
> is detected in one of those buttons.
>
> When `clicked` is called, validation is performed to
> determine if the move is allowed and, if so, updating the
> board.
>
> When `restart_clicked` is called, the game is re-initialized
> with a clean board and player X being set to make the next move.
>
> When `update` is called, during game initialization or after
> one of the `clicked` functions, the main game logic is performed
> e.g: 
> * Updating the GUI elements to reflect the current board
> * Checking for a winner
> * Checking for a draw