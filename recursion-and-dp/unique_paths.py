"""
LeetCode 62: https://leetcode.com/problems/unique-paths/

Base Case:
If robot is already at the bottom left for a grid 1x1. So return 1.

Recursive Step:
The way to get to the last step from any of the adjacency cells, the robot
needs to be either:
1. Up from the current cell and do one step down. -> one way
2. Left from the cell and do one step to right. -> one way

So it is the number of ways coming from up + the number of ways coming from the left.

Call the recursive function for the robot in position up from the cell and left from the cell.

--

We have to use memoization to remember the ways of cells we have already calculated.

[xxxxxxx]
[xxxxxac]
[xxxxxbd]

If the robot is at d, it can come from b or c. So we sum the number of ways from each of them.
Now, we shrink the problem to when the robot is at b and at c.
In these two places, it will look for the number of ways from a. So, we are calculating this twice.

---
Bottom Up Approach


  1 2 3 4   5 6   7
1 1 1 1 1   1 1   1
2 1 2 3 4   5 6   7
3 1 3 6 10 15 21  28

m = 3
n = 7
"""


def uniquePathsDP(m, n):
    width = n
    height = m
    matrix = [[-1 for _ in range(width)] for _ in range(height)]

    for i in range(height):
        matrix[i][0] = 1

    for j in range(width):
        matrix[0][j] = 1

    for i in range(1, height):
        for j in range(1, width):
            matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]

    return matrix[-1][-1]


def uniquePaths(m: int, n: int) -> int:
    def recUniquePaths(m, n, memo, callstack):
        callstack.append(f"recUniquePaths({m},{n},{memo})")
        print(callstack)
        if m == 1 and n == 1:
            callstack.pop()
            print(callstack)
            return 1

        if memo.get((m, n)):
            return memo[(m, n)]

        up = 0
        if m - 1 >= 1:
            up = recUniquePaths(m - 1, n, memo, callstack)

        left = 0
        if n - 1 >= 1:
            left = recUniquePaths(m, n - 1, memo, callstack)

        memo[(m, n)] = up + left
        callstack.pop()
        print(callstack)
        return up + left

    memo = dict()
    return recUniquePaths(m, n, memo, [])


print(uniquePaths(3, 7))
print(uniquePathsDP(3, 7))
