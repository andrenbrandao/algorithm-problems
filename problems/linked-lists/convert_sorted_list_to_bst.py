
"""
LeetCode 109. Convert Sorted List to Binary Search Tree
https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/
"""

"""
Let's look at an example:

                  m
-10 -> -3 -> 0 -> 5 -> 9

    0
 /     \
-10     9
  \     /
   -3  5

or

   0
  /  \
 -3   9
 /    /
-10  5


By the way above, we can get the middle element and choose it as the root.
Then, we take the left part of the linked list and recursively get the root of the part
as the left child of the root.
Do the same for the right part of the linked list

                                   f
                    s
-15 -> -10 -> -3 -> 0 -> 5 -> 7 -> 9


     0
   /    \
  -10    7
 /  \    /  \
-15 -3  5    9


We do the same for the example above.

The problem, however is how to do this efficiently? Because it is a singly linked list,
we cannot keep traversing it all the time to divide the parts.

We can use a slow and fast pointers approach to get the middle element.
But, it would be easier if we could convert the linked list into an array.


## 1st option ##

Convert the linked list to array and use it to generate the BST.

Time Complexity: O(n)
Space Complexity: O(n) because of the new array


## 2nd option ##

Can we decrease the space complexity?

If we use fast and slow pointers to always get the middle of each part, how would the time
complexity change?

I believe it would be like this:

     n
   /  \
 n/2  n/2
/   \...
n/4 n/4...

So, it would be like a merge sort.

TC: O(nlgn)
SC: O(lgn) because the depth is being divided by 2, which becomes lgn

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    # Option 2 #
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def createBst(head):
            if not head:
                return None

            if not head.next:
                return TreeNode(head.val)

            mid = self.findMid(head)

            leftChild = createBst(head)
            rightChild = createBst(mid.next)

            return TreeNode(mid.val, leftChild, rightChild)


        bst = createBst(head)

        return bst

    def findMid(self, head):
        prev = ListNode(float('-inf'))
        prev.next = head
        slow = head
        fast = head

        while fast and fast.next:
            prev = prev.next
            slow = slow.next
            fast = fast.next.next

        prev.next = None
        mid = slow

        return mid

    # Option 1 #
    def sortedListToBSTArray(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        current = head
        elements = []

        while current:
            elements.append(current.val)
            current = current.next


        bst = self.create_bst(elements, 0, len(elements) - 1)

        return bst

    def create_bst(self, elements, left, right):
        if left > right:
            return None

        mid = (right - left) // 2 + left

        root = TreeNode(elements[mid], self.create_bst(elements, left, mid-1), self.create_bst(elements, mid+1, right))

        return root
