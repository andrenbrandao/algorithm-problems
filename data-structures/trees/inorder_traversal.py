"""
Implement a inorder traversal of a tree both recursively and iteratively.
"""


class Node:
    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


def inorder_rec(node):
    result = []

    def helper(node):
        if node is None:
            return result

        helper(node.left)
        result.append(node.val)
        helper(node.right)

    helper(node)
    return result


def inorder_ite(node):
    result = []
    stack = []

    stack.append(("call", node))
    while stack:
        command, node = stack.pop()
        if command == "call":
            if node is None:
                pass
            else:
                # we want to execute node.left first, then resume at the current_node
                # and then node.right, so we have to append these commands in reverse order to the stack
                stack.append(("call", node.right))
                stack.append(("resume", node))
                stack.append(("call", node.left))
        else:
            result.append(node.val)

    return result


def test(node, expected_answer):
    answer = inorder_ite(node)

    if answer != expected_answer:
        raise Exception(
            f"Answer {answer} is incorrect. Expected answer was {expected_answer}"
        )


if __name__ == "__main__":
    tree = Node(4)
    test(tree, [4])
    tree = Node(4, Node(2, Node(1), Node(3)), Node(5))
    test(tree, [1, 2, 3, 4, 5])
    print("All tests passed!")
