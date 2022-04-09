"""
LeetCode 79: Word Search
https://leetcode.com/problems/word-search/

Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells,
where adjacent cells are horizontally or vertically neighboring.

The same letter cell may not be used more than once.

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
"""

"""

K I N T
B I N S
G N Y I
U O E D
D I B V
H I R T

- Iterate over the matrix
- If we match the first letter of word, do a DFS
- On the DFS, we start from the first letter and if
pos == len(word) - 1 and matrix[i][j] == word[pos], we return True
- If the letter in matrix does not match the word, we backtrack

TC: O(m*n*w)
SC: O(w)

-- FORGOT THAT THE SAME CELL CAN BE USED ONlY ONCE
Have to mark the cells as used

"""


def exist(board, word):
    width = len(board[0])
    height = len(board)

    for i in range(height):
        for j in range(width):
            if dfs(board, word, i, j, 0):
                return True

    return False


def dfs(board, word, i, j, pos):
    width = len(board[0])
    height = len(board)

    if i < 0 or j < 0 or i >= height or j >= width or word[pos] != board[i][j]:
        return False

    if word[pos] == board[i][j] and pos == len(word) - 1:
        return True

    # mark word position as used
    tmp = board[i][j]
    board[i][j] = "#"

    up = dfs(board, word, i - 1, j, pos + 1)
    right = dfs(board, word, i, j + 1, pos + 1)
    left = dfs(board, word, i, j - 1, pos + 1)
    down = dfs(board, word, i + 1, j, pos + 1)

    # unmark visited word
    board[i][j] = tmp
    return up or right or left or down
