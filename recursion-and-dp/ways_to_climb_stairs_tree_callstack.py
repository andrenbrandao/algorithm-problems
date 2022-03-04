"""
There are n stairs, a person standing at the bottom wants to reach the top.
The person can climb an array of possible steps at a time.
Count the number of ways, the person can reach the top.

      10
    /  |  \
   8   5   9
 / | \
0 -> one way


"""


class Tree:
    def __init__(self) -> None:
        self.call = ""
        self.returned = None
        self.children = []


def staircase(n, possible_steps, tree):
    tree.call = f"staircase({n})"

    if n == 0:
        tree.returned = 1
        return 1

    ways = 0
    for steps in possible_steps:
        if n - steps >= 0:
            child = Tree()
            tree.children.append(child)
            ways += staircase(n - steps, possible_steps, child)

    tree.returned = ways
    return ways


def printTree(tree, indent=""):
    if tree is None or len(tree.children) == 0:
        print(tree.call + " returned " + str(tree.returned))
    else:
        print(tree.call + " returned " + str(tree.returned))
        for child in tree.children[:-1]:
            print(indent + "|" + "-" * 4, end="")
            printTree(child, indent + "|" + " " * 4)
        child = tree.children[-1]
        print(indent + "└" + "-" * 4, end="")
        printTree(child, indent + "  " * 4)


def test(n, possible_steps, expected_answer):
    tree = Tree()
    answer = staircase(n, possible_steps, tree)
    printTree(tree)
    if answer != expected_answer:
        raise Exception(
            f"Answer {answer} is incorrect! Expected answer was {expected_answer}"
        )


if __name__ == "__main__":
    # test(0, [1, 2, 3], 1)
    test(10, [2, 4, 5, 8], 11)
    print("All tests passed!")
