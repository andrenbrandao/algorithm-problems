"""
Given a list of words, find the maximum common prefix between
any 2 words in the input list.

Problem stated at this video: https://youtu.be/am3fa6otsE8?t=1186
"""


class TrieNode:
    def __init__(self):
        self.children = dict()


def findLongestCommonPrefix(words):
    max_prefix = ""

    root = TrieNode()

    for word in words:
        current_node = root
        current_prefix = ""

        for char in word:
            if char in current_node.children:
                current_prefix += char

                if len(current_prefix) > len(max_prefix):
                    max_prefix = current_prefix

                current_node = current_node.children[char]
            else:
                new_node = TrieNode()
                current_node.children[char] = new_node
                current_node = current_node.children[char]

    return max_prefix


def validate(words, expected_answer):
    answer = findLongestCommonPrefix(words)

    if answer != expected_answer:
        raise Exception(
            f"Wrong answer '{answer}'. Expected answer is: '{expected_answer}'"
        )


if __name__ == "__main__":
    validate(["electronics"], "")
    validate(["electronics", "electronicz"], "electronic")
    validate([], "")
    validate(
        [
            "electronics",
            "compact disc",
            "alphabet",
            "compass",
            "giraffe",
            "electricity",
        ],
        "electr",
    )

    print("All tests passed!")
