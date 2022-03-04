"""
Implement a preorder traversal of a tree both recursively and iteratively.
"""


class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def preorder_rec(node):
    result = []

    def helper(node):
        if node is None:
            return

        result.append(node.val)
        helper(node.left)
        helper(node.right)

    helper(node)
    return result


def preorder_ite(node):
    result = []
    stack = []

    stack.append(("call", node))
    while stack:
        command, node = stack.pop()
        if command == "call":
            if node is None:
                pass
            else:
                # We want to first append the node, then go left, then right.
                # So we have to append these calls to the stack in reverse order.
                stack.append(("call", node.right))
                stack.append(("call", node.left))
                stack.append(("resume", node))
        else:
            result.append(node.val)

    return result


def test(node, expected_answer):
    answer = preorder_ite(node)

    if answer != expected_answer:
        raise Exception(
            f"Answer {answer} is incorrect. Expected answer was {expected_answer}"
        )


if __name__ == "__main__":
    tree = Node(4)
    test(tree, [4])
    tree = Node(4, Node(2, Node(1), Node(3)), Node(5))
    test(tree, [4, 2, 1, 3, 5])
    print("All tests passed!")
