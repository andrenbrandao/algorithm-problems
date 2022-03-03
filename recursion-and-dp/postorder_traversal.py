"""
Implement a postorder traversal of a tree both recursively and iteratively.
"""


class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def postorder_rec(node):
    result = []

    def helper(node):
        if node is None:
            return

        helper(node.left)
        helper(node.right)
        result.append(node.val)

    helper(node)
    return result


def postorder_ite(node):
    result = []
    stack = []

    # here we simulate the execution of a recursive function
    # with "call" and "resume" commands
    stack.append(("call", node))
    while stack:
        command, node = stack.pop()

        if command == "call":
            # if we reach an empty node, we dont call the function anymore
            if node is None:
                pass
            else:
                # we have to append the stack in the reverse order
                # because we will be popping them from the stack
                stack.append(("resume", node))
                stack.append(("call", node.right))
                stack.append(("call", node.left))
        else:
            # we have resuming the call on the node, so we append its value
            result.append(node.val)

    return result


def test(node, expected_answer):
    answer = postorder_ite(node)

    if answer != expected_answer:
        raise Exception(
            f"Answer {answer} is incorrect. Expected answer was {expected_answer}"
        )


if __name__ == "__main__":
    tree = Node(4)
    test(tree, [4])
    tree = Node(4, Node(2, Node(1), Node(3)), Node(5))
    test(tree, [1, 3, 2, 5, 4])
    print("All tests passed!")
