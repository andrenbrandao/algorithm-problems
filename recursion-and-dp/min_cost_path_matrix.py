"""
Given a matrix of integers matrix of size n*m, where each element matrix[i][j]
represents the cost of passing from that cell, create a function that returns
the cost of the minimum cost path to go from the top left cell to the bottom right cell,
knowing that you can only move to the right or to the bottom.

"""


def minimumCostPath(matrix):
    memo = dict()

    def helper(matrix, i, j):
        if i == 0 and j == 0:
            return matrix[0][0]

        if (i, j) in memo:
            return memo[(i, j)]

        cost = float("inf")
        if i > 0:
            cost = min(cost, helper(matrix, i - 1, j))
        if j > 0:
            cost = min(cost, helper(matrix, i, j - 1))

        memo[(i, j)] = cost + matrix[i][j]
        return cost + matrix[i][j]

    width = len(matrix[0])
    height = len(matrix)
    return helper(matrix, height - 1, width - 1)
