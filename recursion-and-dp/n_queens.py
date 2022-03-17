"""
To find all the solutions, we just have to make a small modification to the Algorithm to
find the Number of Solutions below.
----


Given a board, we want to find the number of possible ways we can get
the n queens on a nxn board so that no two queens attack each other.

We have to recursively go through all possible ways and count them.

[. . . .]
[. . . .]
[. . . .]
[. . . .]

[. Q . .]
[Q . . .] <- attacked
[. . . .]
[. . . .]

We have to check the rows above it in the following way:
- Column
- Diagonal to the left
- Diagonal to the right

[. Q . .]
[. . . Q]
[. Q . .] <- attacked
[. . . .]
 0 1 2 3

When we have places all the queens in the board and they were not attacked,
we have found a solution, so return 1.

We want to return the sum of the ways we have found.

- Start at the first row
- Place the queen on the next position
- Check if it is being attacked: if yes, return, else continue
- Go to the row below, repeat
- If we are over the height of the board, we have places all queens, return 1

            [. . . .]
            [. . . .]
            [. . . .]
            [. . . .]
        /        |      \ ....
    [Q . . .] [. Q . .]
    [. . . .] [. . . .]
    [. . . .] [. . . .]
    [. . . .] [. . . .]
    /     \
[Q . . .] ...
[Q . . .]
[. . . .]
[. . . .]
(attacked)

Since we don't go down the paths the queens were attacked, we have a shorter tree.
What is the Time Complexity?





--Checking for attackers--

[Q . . .]
[l c r Q]
[. Q . .]
[. . . .]

- Check board[row-1][col]: always same column
- Check board[row-1][leftDiag]
- Check board[row-1][rightDiag]

leftDiag = col-1
rightDiag = col+1

- Decrement leftDiag
- Increment rightDiag
on every iteration

- Also, check if leftDiag and rightDiag are still inside the board. Look for the edges.

"""
from typing import List


def solveNQueens(n: int) -> List[List[str]]:
    board = create_board(n)
    solutions = []

    def recQueens(board, row):
        if row == n:
            solutions.append(copy_board(board))
            return

        for col in range(n):
            if not is_attacked(board, row, col):
                board[row][col] = "Q"
                recQueens(board, row + 1)
                board[row][col] = "."

    recQueens(board, 0)
    return solutions


# Check to the rows above if there is a queen attacking it
# Column above
# Diagonal to the left
# Diagonal to the right
def is_attacked(board, row, col):
    n = len(board)
    leftDiag = col - 1
    rightDiag = col + 1

    while row - 1 >= 0:
        is_queen_above = board[row - 1][col] == "Q"
        is_queen_diag_left = board[row - 1][leftDiag] == "Q" if leftDiag >= 0 else False
        is_queen_diag_right = (
            board[row - 1][rightDiag] == "Q" if rightDiag < n else False
        )

        if is_queen_above or is_queen_diag_left or is_queen_diag_right:
            return True

        row -= 1
        leftDiag -= 1
        rightDiag += 1

    return False


def create_board(n):
    return [["."] * n for _ in range(n)]


def copy_board(board):
    return ["".join(row.copy()) for row in board]


def test(size, expected_answer):
    answer = solveNQueens(size)

    if answer != expected_answer:
        raise Exception(
            f"Answer {answer} is incorrect. Expected answer was {expected_answer}"
        )


if __name__ == "__main__":
    test(1, [["Q"]])
    test(4, [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]])
    print("All tests passed!")
