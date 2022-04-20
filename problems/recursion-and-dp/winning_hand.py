"""
Google Interview Question

Game where you receive 14 tiles.
Want to know if you can win the game by making hands with the following possibilities.

pair: [11, 22...]
set: [111, 222, 333]
street: [123, 456, 789]

To win, you need 1 pair and 4 sets and/or streets.
And have to use all 14 tiles.

[1 1 1 1 2 2 3 3 4 4 4 5 5 5 ] → [11, 123, 123, 444, 555]

Return if the game was won or not.

Found a variation of the problem: [https://leetcode.com/discuss/interview-question/1740425/indeed-phone-interview-mini-game](https://leetcode.com/discuss/interview-question/1740425/indeed-phone-interview-mini-game)

"""


"""
        [1 1 1 1 2 2 3 3 4 4 4 5 5 5 ]
           /        \
          1 1       2 2
          /         /
         123        111
         /         /
       123       345
         /      /
        444    345
       /         /
     555        x
       /
	Winner

The array is sorted.

Base case:
- count_pair == 1 and count_sets + count_streets == 4: return True

Recursive step:
- Iterate over the array
- Choose one of the numbers and look for a pair
- Mark the values as visited
- If a pair is found, call the function recursively
- Else, unmark the values and keep trying to find a pair
- Try to find a set or a street
- If found, keep going down the tree


[1 1 1 1 2 2 3 3 4 4 4 5 5 5 ] → [11, 123, 123, 444, 555]
"""

# Refactored
def find_winner(tiles):
    n = len(tiles)

    def rec_helper(count_pairs, count_sets, count_streets, hands):
        if count_pairs == 1 and count_sets + count_streets == 4:
            return True

        has_won = False
        for i, val in enumerate(tiles):
            if val != -1:
                has_won = (
                    has_won
                    or find_pair(
                        count_pairs, count_sets, count_streets, hands, has_won, i, val
                    )
                    or find_set(
                        count_pairs, count_sets, count_streets, hands, has_won, i
                    )
                    or find_street(
                        count_pairs, count_sets, count_streets, hands, has_won, i, val
                    )
                )

        return has_won

    def find_street(count_pairs, count_sets, count_streets, hands, has_won, i, val):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if val + 1 == tiles[j] and tiles[j] + 1 == tiles[k]:
                    tmps = [val, tiles[j], tiles[k]]
                    tiles[i], tiles[j], tiles[k] = [-1, -1, -1]
                    hands.append(tmps)
                    has_won = has_won or rec_helper(
                        count_pairs, count_sets, count_streets + 1, hands
                    )
                    hands.pop()
                    tiles[i], tiles[j], tiles[k] = tmps
        return has_won

    def find_set(count_pairs, count_sets, count_streets, hands, has_won, i):
        if i + 2 < n and tiles[i] == tiles[i + 1] == tiles[i + 2]:
            tmps = [tiles[i], tiles[i + 1], tiles[i + 2]]
            tiles[i], tiles[i + 1], tiles[i + 2] = [-1, -1, -1]
            hands.append(tmps)
            has_won = has_won or rec_helper(
                count_pairs, count_sets + 1, count_streets, hands
            )
            hands.pop()
            tiles[i], tiles[i + 1], tiles[i + 2] = tmps
        return has_won

    def find_pair(count_pairs, count_sets, count_streets, hands, has_won, i, val):
        if count_pairs == 0 and i + 1 < n and tiles[i + 1] == val:
            tmp1 = tiles[i]
            tmp2 = tiles[i + 1]
            tiles[i] = -1
            tiles[i + 1] = -1
            hands.append([tmp1, tmp2])
            has_won = has_won or rec_helper(
                count_pairs + 1, count_sets, count_streets, hands
            )
            hands.pop()
            tiles[i] = tmp1
            tiles[i + 1] = tmp2
        return has_won

    return rec_helper(0, 0, 0, [])


def find_winner_1(tiles):
    n = len(tiles)

    def rec_helper(count_pairs, count_sets, count_streets, hands):
        if count_pairs == 1 and count_sets + count_streets == 4:
            return True

        has_won = False
        for i, val in enumerate(tiles):
            if val != -1:
                if count_pairs == 0 and i + 1 < n and tiles[i + 1] == val:
                    tmp1 = tiles[i]
                    tmp2 = tiles[i + 1]
                    tiles[i] = -1
                    tiles[i + 1] = -1
                    hands.append([tmp1, tmp2])
                    has_won = has_won or rec_helper(
                        count_pairs + 1, count_sets, count_streets, hands
                    )
                    hands.pop()
                    tiles[i] = tmp1
                    tiles[i + 1] = tmp2

                if i + 2 < n and tiles[i] == tiles[i + 1] == tiles[i + 2]:
                    tmps = [tiles[i], tiles[i + 1], tiles[i + 2]]
                    tiles[i], tiles[i + 1], tiles[i + 2] = [-1, -1, -1]
                    hands.append(tmps)
                    has_won = has_won or rec_helper(
                        count_pairs, count_sets + 1, count_streets, hands
                    )
                    hands.pop()
                    tiles[i], tiles[i + 1], tiles[i + 2] = tmps

                for j in range(i + 1, n):
                    for k in range(j + 1, n):
                        if val + 1 == tiles[j] and tiles[j] + 1 == tiles[k]:
                            tmps = [val, tiles[j], tiles[k]]
                            tiles[i], tiles[j], tiles[k] = [-1, -1, -1]
                            hands.append(tmps)
                            has_won = has_won or rec_helper(
                                count_pairs, count_sets, count_streets + 1, hands
                            )
                            hands.pop()
                            tiles[i], tiles[j], tiles[k] = tmps

        return has_won

    return rec_helper(0, 0, 0, [])


def test(tiles, expected_answer):
    answer = find_winner(tiles)

    if answer != expected_answer:
        raise Exception(
            f"Answer {answer} is incorrect. Expected answer was {expected_answer}"
        )


test([1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5], True)
test(
    [1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 9, 9], True
)  # [1,2,3] [2,3,4] [4,5,6] [5,6,7] [9,9]
test([1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 9], False)
test([1, 2, 3, 3, 4, 4, 5, 6, 6, 6, 7, 8, 8, 9], False)
print("All tests passed!")
