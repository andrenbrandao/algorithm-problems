"""
1905. Count Sub Islands
https://leetcode.com/problems/count-sub-islands/
"""

"""
We want to know if islands in grid2 are totally in grid1.

To do that, we can find a land cell in grid2 and run a BFS or DFS while checking if all
of these cells are also a land in grid1.

If all of them are there, we increment the count of sub-islands.
Notice that we have to mark them as visited. We can change them to water cells while iterating.
Also, we cannot stop the BFS if the islands do not match, because we have to keep marking
the cells as visited.

Algorithm:
- Iterate over the cells in grid2
- When a land cell is found, run BFS and check if all are a land in grid1.
If yes, increment the count. Keep marking the cells as visited until the BFS ends.
- Repeat until all cells in grid2 are visited

Time Complexity: O(m*n)
Space Complexity: O(m*n) because of the queue
"""

from collections import deque
from typing import List


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        width = len(grid1[0])
        height = len(grid1)

        subislands_count = 0
        for i in range(height):
            for j in range(width):
                if grid2[i][j] == 1:
                    if self.is_subisland(i, j, grid1, grid2):
                        subislands_count += 1

        return subislands_count

    def is_subisland(self, i, j, grid1, grid2):
        width = len(grid1[0])
        height = len(grid1)

        queue = deque()

        all_cells_match = grid1[i][j] == grid2[i][j]
        queue.append((i, j))
        grid2[i][j] = 0

        def add_neighbor_to_queue(i, j):
            if i < 0 or i == height or j < 0 or j == width or grid2[i][j] == 0:
                return

            queue.append((i, j))
            grid2[i][j] = 0

        while queue:
            i, j = queue.popleft()

            # we do not need to check if they match
            # since we are always walking on lands of grid2
            # all we need to check is if grid1 is a land
            if grid1[i][j] != 1:
                all_cells_match = False

            add_neighbor_to_queue(i + 1, j)
            add_neighbor_to_queue(i - 1, j)
            add_neighbor_to_queue(i, j + 1)
            add_neighbor_to_queue(i, j - 1)

        return all_cells_match
