"""
Write the function `sudokuSolve` that checks whether a given sudoku board (i.e. sudoku puzzle) is solvable. If so, the function will returns `true`. Otherwise (i.e. there is no valid solution to the given sudoku board), returns `false`.

In sudoku, the objective is to fill a **9x9** board with digits so that each column, each row, and each of the nine **3x3** sub-boards that compose the board contains all of the digits from 1 to 9. The board setter provides a partially completed board, which for a well-posed board has a unique solution. **As explained above, for this problem, it suffices to calculate whether a given sudoku board has a solution. No need to return the actual numbers that make up a solution**.

A sudoku board is represented as a two-dimensional **9x9** array of the characters ‘1’,‘2’,…,‘9’ and the `'.'` character, which represents a blank space. The function should fill the blank spaces with characters such that the following rules apply:

1. In every row of the array, all characters ‘1’,‘2’,…,‘9’ appear exactly once.
2. In every column of the array, all characters ‘1’,‘2’,…,‘9’ appear exactly once.
3. In every 3x3 sub-board that is illustrated below, all characters ‘1’,‘2’,…,‘9’ appear exactly once.

A solved sudoku is a board with no blank spaces, i.e. all blank spaces are filled with characters that abide to the constraints above. If the function succeeds in solving the sudoku board, it’ll return true (false, otherwise).


##### SOLUTION #####

Check if sudoku board is solvable.

Each 3x3 board needs to have all digits from 1-9
Also, each column, each row have to have digits from 1-9

Do not need to return the solution. Only if it is True or False (solvable).

1. In every row of the array, all characters '1','2',…,'9' appear exactly once.
2. In every column of the array, all characters '1','2',…,'9' appear exactly once.
3. In every 3x3 sub-board that is illustrated below, all characters '1','2',…,'9' appear exactly once.

Fill the characters '.' with a digit.

[1,2,4]

[5 3 .][. . .][...]
[6 . .][1 9 5][...]
[. 9 8][. . .][...]x <--- reached the column after the last, so it is solvable

- Recursively add possible digits 1-9 to the next empty cell. We have to check the row and column
to know which digits we can add.
- Iterate over the board from left to right and top to bottom. Keeping the row, column indexes
of where we are.
- If we reach row == n - 1 and column == n, we have reached the end and it is a valid solution. Otherwise, return false.
"""


def sudoku_solve(board):
    def rec_sudoku_solve(board, row, column):
        height = len(board)
        width = len(board[0])
        is_solvable = False

        # it is solvable if we have filled the last column of the last row
        if row == height - 1 and column == width:
            return True

        # when we reach the last column, go to the next row
        if column == width:
            column = 0
            row = row + 1

        # keep iterating if it is not empty
        if not is_empty_space(board, row, column):
            return rec_sudoku_solve(board, row, column + 1)

        # found an empty space, try to insert numbers
        for number in map(str, list(range(1, 10))):
            if can_add_number(board, row, column, number):
                board[row][column] = number
                is_solvable = is_solvable or rec_sudoku_solve(board, row, column + 1)
                board[row][column] = "."  # put it back to try another possible digit

        # could not insert any number
        return is_solvable

    return rec_sudoku_solve(board, 0, 0)


def is_empty_space(board, row, column):
    return board[row][column] == "."


def can_add_number(board, row, column, number):
    return (
        not is_number_in_row(board, row, number)
        and not is_number_in_column(board, column, number)
        and not is_number_in_small_board(board, row, column, number)
    )


def is_number_in_row(board, row, number):
    width = len(board[0])
    for column in range(width):
        if board[row][column] == number:
            return True
    return False


def is_number_in_column(board, column, number):
    height = len(board)
    for row in range(height):
        if board[row][column] == number:
            return True
    return False


"""
[5,3,4]
[6,x,2] <-- (1,1) have to check from 0 to 2
[1,9,8] <-- (2,2) have to check from 0 to 2. Well, we have already cchecked for other numbers, so we do not need to.
We only need to check the next numbers inside the board.

position (4,1) has to be checked from (4,2), (5,0), (5,1) and (5,2) 

rows
3 -> 0 + 3 -> 3 - 3 % 3 = 3 
4 -> 1 + 3 -> 4 - 4 % 3 = 3
5 -> 2 + 3 -> 5 - 5 % 3 = 3

another board
6 ->

columns
0 1 2

How to get the possible range we can search in a board given a row and column?
We have to get the beginning point of a small board. To do this we have to "translate" a point
to the beginning of a small board.
So if we have (4,2), we would need to start checking from (3,0)
3 = 4 - 1 = 4 - 4 % 3 = 3
To translate it we have to subtract the number % 3.
"""


def is_number_in_small_board(board, row, column, number):
    start_row = row - row % 3
    start_column = column - column % 3

    for i in range(start_row, start_row + 3):
        for j in range(start_column, start_column + 3):
            if board[i][j] == number:
                return True

    return False


board = [
    [".", "8", "9", ".", "4", ".", "6", ".", "5"],
    [".", "7", ".", ".", ".", "8", ".", "4", "1"],
    ["5", "6", ".", "9", ".", ".", ".", ".", "8"],
    [".", ".", ".", "7", ".", "5", ".", "9", "."],
    [".", "9", ".", "4", ".", "1", ".", "5", "."],
    [".", "3", ".", "9", ".", "6", ".", "1", "."],
    ["8", ".", ".", ".", ".", ".", ".", ".", "7"],
    [".", "2", ".", "8", ".", ".", ".", "6", "."],
    [".", ".", "6", ".", "7", ".", ".", "8", "."],
]

print(sudoku_solve(board))
