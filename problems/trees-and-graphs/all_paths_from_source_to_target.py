"""
LeetCode 797. All Paths From Source to Target
https://leetcode.com/problems/all-paths-from-source-to-target/
"""


"""

0 -> 1
|    |
v    v
2 -> 3 x

result = [[0, 1, 3], [0,2,3]]

Base case:
- current_node == dest: append current_path, return

Recursive step:
- Use DFS starting from node 0
- We accumulate the nodes we have passed on each function call
- If we reach the destination, we append the current path to the result


"""

from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        src = 0
        dst = len(graph) - 1
        result = []

        self.dfs(graph, src, dst, result, [src])
        return result

    def dfs(self, graph, current_node, dst, result, current_path):
        if current_node == dst:
            result.append(current_path.copy())
            return

        for neighbor in graph[current_node]:
            current_path.append(neighbor)
            self.dfs(graph, neighbor, dst, result, current_path)
            current_path.pop()
