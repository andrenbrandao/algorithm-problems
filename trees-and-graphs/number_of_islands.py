"""
LeetCode 200. Number of Islands
https://leetcode.com/problems/number-of-islands/

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water),
return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands
horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
"""

"""
 [0,    1,    0,    1,    0]
 [0,    0,    1,    1,    1]
 [1,    0,    0,    1,    0]
 [0,    1,    1,    0,    0]
 [1,    0,    1,    0,    1]

count = 1

- Iterate over the matrix
- When we find a 1, we do a DFS to find its neighbors
- Mark each 1 as visited
- When return from the DFS, we add 1 to a count

base case:
- element != 1: return
- overbound: return

Time Complexity: O(mn)
Space Complexity: O(mn)

We can also solve it with BFS.
The advantages of BFS is that we don't risk having a stack overflow, like
it could happen with DFS.

"""

from collections import deque


def get_number_of_islands(grid):
    count = 0
    width = len(grid[0])
    height = len(grid)

    for i in range(height):
        for j in range(width):
            if grid[i][j] == 1:
                dfs(grid, i, j)
                count += 1

    return count


def dfs(grid, i, j):
    if is_overbound(grid, i, j) or grid[i][j] != 1:
        return

    if grid[i][j] == 1:
        grid[i][j] = "#"

    # up
    dfs(grid, i - 1, j)

    # down
    dfs(grid, i + 1, j)

    # right
    dfs(grid, i, j + 1)

    # left
    dfs(grid, i, j - 1)


def is_overbound(grid, i, j):
    width = len(grid[0])
    height = len(grid)

    return i < 0 or i >= height or j < 0 or j >= width


def bfs(grid, i, j):
    queue = deque()
    queue.append((i, j))

    while queue:
        i, j = queue.popleft()

        if grid[i][j] == 1:
            grid[i][j] = "#"

            for row, col in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if not is_overbound(grid, row, col):
                    queue.append((row, col))


print(
    get_number_of_islands(
        [
            [0, 1, 0, 1, 0],
            [0, 0, 1, 1, 1],
            [1, 0, 0, 1, 0],
            [0, 1, 1, 0, 0],
            [1, 0, 1, 0, 1],
        ]
    )
)
print(get_number_of_islands([[0]]))
