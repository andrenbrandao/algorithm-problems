"""
547. Number of Provinces
https://leetcode.com/problems/number-of-provinces/
"""

"""
To know how many provinces we have, we can connect
the cities in a UnionFind data structure.

Then, we look at the parents and check how many are different.

One optimization is to consider each city as a province and then
decrement 1 at each union operation.

Time Complexity: O(n*n) since we have to go through all connections
Space Complexity: O(n) because of the UnionFind data structure

"""
from typing import List


class UnionFind:
    def __init__(self, n):
        self.parents = list(range(n))
        self.ranks = [1] * n

    def find(self, city):
        if self.parents[city] == city:
            return city

        self.parents[city] = self.find(self.parents[city])
        return self.parents[city]

    def union(self, city1, city2):
        root1 = self.find(city1)
        root2 = self.find(city2)

        if root1 == root2:
            return False

        if self.ranks[root1] > self.ranks[root2]:
            self.parents[root2] = root1
        elif self.ranks[root1] < self.ranks[root2]:
            self.parents[root1] = root2
        else:
            self.parents[root2] = root1
            self.ranks[root1] += 1

        return True


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        uf = UnionFind(n)
        provinces = n

        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1 and uf.union(i, j):
                    provinces -= 1

        return provinces
