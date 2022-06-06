"""
LeetCode 542. 01 Matrix
https://leetcode.com/problems/01-matrix/
"""

"""
We want to find the distance of the nearest 0 for each cell.

0 cells always have a distance of 0 to the nearest zero.
1 cells will have at least a distance of 1.

What if we have a matrix with all 1s?
- The contraints tell us there is a least one zero in the matrix.

With all zeroes?
- All have a zero distance

[1 1 1]
[1 1 1]
[1 1 0]

Output:
[4 3 2]
[3 2 1]
[2 1 0]


Brute Force:
- Iterate over the matrix
- When we find a 1, we run a BFS to find the nearest 0 and calculate the distance

TC: O((m*n)^2)

Better Approach:

We could add all zeroes to a queue and run a BFS to calculate the distance
to the neighbors.
This could be optimized by only adding the 1s neighbors to zeroes and start them
with distance equal to 1. Then, run a BFS.

Algorithm:
- Initialize a result matrix with zero as the distances.
- Iterate over the matrix and when we find a zero, add the neighbors that are 1 to
a queue. Mark them as already visited to make sure they are not also added by other zeroes.
- Run BFS with these added 1s and increase the distance.
- Store this distances in the result matrix.

Time Complexity: O(m*n)
Space Complexity: O(m*n)

"""

from typing import List
from collections import deque


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        height = len(mat)
        width = len(mat[0])
        result = [[0 for _ in range(width)] for _ in range(height)]

        queue = deque()

        def add_neighbor_to_queue(i, j, distance):
            if i < 0 or i == height or j < 0 or j == width or mat[i][j] != 1:
                return

            queue.append((i, j, distance))
            mat[i][j] = -1  # mark as visited

        for i in range(height):
            for j in range(width):
                if mat[i][j] == 0:
                    add_neighbor_to_queue(i + 1, j, 1)
                    add_neighbor_to_queue(i - 1, j, 1)
                    add_neighbor_to_queue(i, j + 1, 1)
                    add_neighbor_to_queue(i, j - 1, 1)

        while queue:
            i, j, distance = queue.popleft()

            result[i][j] = distance

            add_neighbor_to_queue(i + 1, j, distance + 1)
            add_neighbor_to_queue(i - 1, j, distance + 1)
            add_neighbor_to_queue(i, j + 1, distance + 1)
            add_neighbor_to_queue(i, j - 1, distance + 1)

        return result
