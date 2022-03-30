"""
Implement a Union Find data structure.

Also, use the following heuristics:
- Union by Rank
- Path Compression

Start with a simple array of integers, then
generalize to be used with any type of elements.


-- Solution

To use Union By Rank, we get the shortest subtree and
point to the root of the other with higher rank.
If they have the same height, we increase the rank of the root.

For Path Compression, when we call Find, we want to recursively
go up the tree and point all elements to the root.


    2
  / |
 1  3
    |
    4

Find(4)


    2
  / | \
 1  3  4


-- With any type of element

Map the elements to an index in the array.
We can use a hashmap for this.

{
    a: 0
    b: 1
    c: 2
    d: 3
}

Now, when we want to find an element, we get the index
from the hashmap.
"""


class UnionFind:
    def __init__(self, elements):
        self.elements = elements
        self.parents = list(range(len(elements)))
        self.ranks = [1] * len(elements)
        self.val_to_int = {elements[i]: i for i in range(len(elements))}

    # Union by Rank
    def union(self, first_val, second_val):
        first_root = self._find_integer(self.val_to_int[first_val])
        second_root = self._find_integer(self.val_to_int[second_val])

        if self.ranks[first_root] < self.ranks[second_root]:
            self.parents[first_root] = second_root
        else:
            self.parents[second_root] = first_root
            if self.ranks[first_root] == self.ranks[second_root]:
                self.ranks[first_root] += 1

    # Get the original value of the union root
    def find(self, value):
        val_integer = self.val_to_int[value]
        parent_integer = self._find_integer(val_integer)
        return self.elements[parent_integer]

    # Path Compression Find
    def _find_integer(self, value):
        if self.parents[value] != value:
            self.parents[value] = self._find_integer(self.parents[value])

        return self.parents[value]


"""
Commands:
union 1 2
find 2
"""


def union_find_query(elements, queries):
    answer = []
    union_find = UnionFind(elements)

    for query in queries:
        command, *values = query.split()

        if command == "union":
            first_val = to_integer_if_digit(values[0])
            second_val = to_integer_if_digit(values[1])
            union_find.union(first_val, second_val)
        elif command == "find":
            val = to_integer_if_digit(values[0])
            answer.append(union_find.find(val))
        else:
            raise Exception("Invalid command!")

    return answer


def to_integer_if_digit(val):
    if val.isdigit():
        return int(val)
    return val


def test(elements, queries, expected_answer):
    answer = union_find_query(elements, queries)

    if answer != expected_answer:
        raise Exception(
            f"Answer {answer} is incorrect. Expected answer was {expected_answer}"
        )


if __name__ == "__main__":
    test([1, 2], ["find 1", "find 2"], [1, 2])
    test([1, 2], ["union 1 2", "find 1", "find 2"], [1, 1])
    test(
        [1, 2, 3, 4, 5, 6],
        [
            "union 1 2",
            "union 2 3",
            "union 4 5",
            "find 1",
            "find 2",
            "find 3",
            "find 4",
            "find 5",
            "find 6",
        ],
        [1, 1, 1, 4, 4, 6],
    )
    test(
        ["a", "b", "c", "d", "e", "f"],
        [
            "union a b",
            "union b c",
            "union d e",
            "find a",
            "find b",
            "find c",
            "find d",
            "find e",
            "find f",
        ],
        ["a", "a", "a", "d", "d", "f"],
    )
    print("All tests passed!")
