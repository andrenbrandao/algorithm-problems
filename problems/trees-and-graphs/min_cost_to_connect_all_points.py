"""
LeetCode 1584: Min Cost to Connect All Points
https://leetcode.com/problems/min-cost-to-connect-all-points/

## SOLUTION ##

- Calculate the manhattan distance between points: |x1 - x2| + |y1 - y2|
- Return the minimum cost to make all points connected

This looks analogous to a spanning tree algorithm.
We want to connect all points and only have one path between any of them.

This is a possible example:
  B
 /
A---C
 \
  D

This is a wrong one:
  B
 / \  <--- we have two posible ways to get from A to C
A---C
 \
  D

Kruskals Algorithm:
- Create all edges
- Sort them by weight
- Start by picking the edge with the lowest weight
- Add the vertices of the edge to a Union Find data structure, so they will be in the same set
- If the vertices are already in the same set, we ignore the edge and go to the next


To add the points to the UnionFind, lets use their position in the array
as the identifier for the UnionFind DS.

Time Complexity: O(N²*logN²) where N is the number of edges
Space ComplexitY: O(N²)


TODO: Implement Prims Algorithm
"""

from typing import List


class Solution:
    # Kruskals Algorithm
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = self.create_edges(points)
        sorted_edges = self.sort_edges(edges)
        union_find = UnionFind(len(points))

        cost = 0

        for edge in sorted_edges:
            if union_find.find(edge.pos1) == union_find.find(edge.pos2):
                continue

            cost += edge.weight
            union_find.union(edge.pos1, edge.pos2)

        return cost

    def create_edges(self, points):
        n = len(points)
        edges = []

        for i in range(n):
            for j in range(i + 1, n):
                edges.append(Edge(points, i, j))
        return edges

    def sort_edges(self, edges):
        return sorted(edges, key=lambda x: x.weight)


class Edge:
    def __init__(self, points, pos1, pos2):
        self.pos1 = pos1
        self.pos2 = pos2
        point1 = points[pos1]
        point2 = points[pos2]
        self.weight = abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])


class UnionFind:
    def __init__(self, n):
        self.parents = list(range(n))
        self.ranks = [1] * n

    # Union by Rank
    def union(self, pos1, pos2):
        first_root = self.find(pos1)
        second_root = self.find(pos2)

        if first_root == second_root:
            return

        if self.ranks[first_root] < self.ranks[second_root]:
            self.parents[first_root] = second_root
        elif self.ranks[second_root] < self.ranks[first_root]:
            self.parents[second_root] = first_root
        else:
            self.parents[second_root] = first_root
            self.ranks[first_root] += 1

    # Find with Path Compression
    def find(self, pos):
        if self.parents[pos] == pos:
            return pos

        self.parents[pos] = self.find(self.parents[pos])
        return self.parents[pos]
