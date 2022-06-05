"""
1020. Number of Enclaves
https://leetcode.com/problems/number-of-enclaves/
"""

"""
Get the number of land cells that cannot reach a border of the grid.

Brute Force:
For each land cell, we run BFS or DFS and try to reach a border. However,
this algiorithm would be slow.
TC: O((m*n)^2)

Another Approach:
- Go through each cell and when we reach a land on the border, run BFS and mark the neighbors
as visited (make them become water).
- Then, go through the whole grid and count the number of 1s left.

Time Complexity: O(m*n)
Space Complexity: O(m*n) because of the queue
"""

from collections import deque
from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        width = len(grid[0])
        height = len(grid)

        for i in range(height):
            if grid[i][0] == 1:
                self.bfs(i, 0, grid)

            if grid[i][width - 1] == 1:
                self.bfs(i, width - 1, grid)

        for j in range(width):
            if grid[0][j] == 1:
                self.bfs(0, j, grid)

            if grid[height - 1][j] == 1:
                self.bfs(height - 1, j, grid)

        count = 0
        for i in range(height):
            for j in range(width):
                if grid[i][j] == 1:
                    count += 1

        return count

    def bfs(self, i, j, grid):
        width = len(grid[0])
        height = len(grid)

        queue = deque()
        queue.append((i, j))
        grid[i][j] = 0

        def add_neighbor(i, j):
            if i < 0 or i == height or j < 0 or j == width or grid[i][j] == 0:
                return

            queue.append((i, j))
            grid[i][j] = 0

        while queue:
            i, j = queue.popleft()

            add_neighbor(i + 1, j)
            add_neighbor(i - 1, j)
            add_neighbor(i, j - 1)
            add_neighbor(i, j + 1)
