"""

Given a list of weights and a max capacity of a knapsack, find all possible
combinations of items that can fit in the knapsack.

The answer should include the indexes of the items and not the items themselves.

Examples:

weights: [3, 5]
maxWeight: 8

answer:
[[0,1],[0], [1], []]


weights: [4, 7, 2, 1]
maxWeight: 7

answer:
[[0,2,3], [0,2], [0,3], [0], [1], [2,3], [2], [3], []]


-----
Algorithm:


               []
            /      \
           []       [4]
          /   \     /   \
        []     [7] [4]    [4,7]
      /   \     / \
     []   [2]  [7] [7,2] <-- overweight, return
    /  \
   []   [1] <- do not have any elements left, add to the combinations
   /
  do not have any elements left, add the combination

We choose to add an item or not. If we find a combination that is
over maxWeight we stop the recursive calls.

If the combination is valid, we add to our list of combinations.

Base case:
- maxWeight < 0: return (we added a number that made it over the weight)
- position == len(weights): save current combination

Recursive step:
- Start from the first element, we can choose to add it or not.
- If we add it, we subtract it from the maxWeight and go to the next element
- Else, we do not subtract it and go to the next element
- Repeat until we are over weight or have gone through all elements

Time Complexity: O(2^n) - we have to go through all combinations
Space Complexity: O(maxWeight) - it is the deepest height of the tree we can go.





weights: [3, 5]
maxWeight: 8
len(weights) = 2

current_combination = []
position = 2
max_weight = 8

           []
       /       \
      [3]      []
     /   \     / \
    [3,5] [3] [5] []
"""


def knapsack_combinations(weights, max_weight):
    result = []

    def rec_helper(weights, max_weight, position, current_combination):
        if max_weight < 0:
            return
        if position == len(weights):
            result.append(current_combination)
            return

        rec_helper(
            weights,
            max_weight - weights[position],
            position + 1,
            current_combination + [position],
        )
        rec_helper(
            weights,
            max_weight,
            position + 1,
            current_combination,
        )

    rec_helper(weights, max_weight, 0, [])
    return result


def test(weights, max_weight, expected_answer):
    answer = knapsack_combinations(weights, max_weight)

    if answer != expected_answer:
        raise Exception(
            f"Answer {answer} is incorrect. Expected answer was {expected_answer}"
        )


if __name__ == "__main__":
    test([3, 5], 8, [[0, 1], [0], [1], []])
    test([4, 7, 2, 1], 7, [[0, 2, 3], [0, 2], [0, 3], [0], [1], [2, 3], [2], [3], []])
    print("All tests passed!")
