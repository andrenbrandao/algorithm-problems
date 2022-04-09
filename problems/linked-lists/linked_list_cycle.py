"""
LeetCode 141. Linked List Cycle
https://leetcode.com/problems/linked-list-cycle/
"""

# O(n) time
# O(n) memory

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        currentNode = head
        visitedNodes = {}

        while currentNode is not None:
            if visitedNodes.get(currentNode) is not None:
                return True

            visitedNodes[currentNode] = True
            currentNode = currentNode.next

        return False
