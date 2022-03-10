"""
HackerRank Problem:
https://www.hackerrank.com/challenges/swap-nodes-algo/problem

"""


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'swapNodes' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY indexes
#  2. INTEGER_ARRAY queries
#

"""

- Create a tree using a Node class to make things easier O(n)
- For each query, do a BFS and swap the nodes at the depths multiple of K O(n)
- Call a InOrderTraversal function to get the result O(n)

Time Complexity: O(n) * number queries
"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""

 [1,2,3,-1,-1,-1,-1]
  0 1 2 3   4  5  6

parent = (pos - 1) // 2
"""

from collections import deque


def create_tree(indexes):
    if len(indexes) == 0:
        return Node(1)

    root = Node(1)
    queue = deque()
    queue.append(root)
    for left, right in indexes:
        node = queue.popleft()

        if left != -1:
            leftNode = Node(left)
            queue.append(leftNode)
        else:
            leftNode = None

        if right != -1:
            rightNode = Node(right)
            queue.append(rightNode)
        else:
            rightNode = None

        node.left = leftNode
        node.right = rightNode

    return root


def inorder_traversal(root):
    result = []

    queue = []
    queue.append((root, "call"))
    while queue:
        node, command = queue.pop()

        if command == "call":
            if node is None:
                pass
            else:
                queue.append((node.right, "call"))
                queue.append((node, "resume"))
                queue.append((node.left, "call"))
        else:
            result.append(node.val)

    return result


def swap_nodes(root, target_depth):
    queue = deque()
    queue.append((root, 1))

    while queue:
        node, depth = queue.popleft()

        if depth % target_depth == 0:
            node.left, node.right = node.right, node.left

        if node.left is not None:
            queue.append((node.left, depth + 1))
        if node.right is not None:
            queue.append((node.right, depth + 1))


def swapNodes(indexes, queries):
    root = create_tree(indexes)
    result = []

    for depth in queries:
        swap_nodes(root, depth)
        result.append(inorder_traversal(root))

    return result


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    fptr.write("\n".join([" ".join(map(str, x)) for x in result]))
    fptr.write("\n")

    fptr.close()
