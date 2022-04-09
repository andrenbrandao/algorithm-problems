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

# Tabular
def staircase_tabular(n, possible_steps):
    T = [0] * (n + 1)
    T[0] = 1

    for i in range(1, n + 1):
        for step in possible_steps:
            if i - step >= 0:
                T[i] += T[i - step]

    return T[n]


# Memoization
memo = dict()


def staircase_memo(n, possible_steps):
    if n == 0:
        memo[n] = 1
        return 1

    if memo.get(n):
        return memo[n]

    ways = 0
    for steps in possible_steps:
        if n - steps >= 0:
            ways += staircase_memo(n - steps, possible_steps)

    memo[n] = ways
    return ways


# Recursive
def staircase_recursive(n, possible_steps):
    if n == 0:
        return 1

    ways = 0
    for steps in possible_steps:
        if n - steps >= 0:
            ways += staircase_recursive(n - steps, possible_steps)

    return ways


def test(n, possible_steps, expected_answer):
    answer = staircase_tabular(n, possible_steps)
    if answer != expected_answer:
        raise Exception(
            f"Answer {answer} is incorrect! Expected answer was {expected_answer}"
        )


if __name__ == "__main__":
    test(0, [1, 2, 3], 1)
    test(10, [2, 4, 5, 8], 11)
    test(100, [2, 4, 5, 8], 239633692743365)
    print("All tests passed!")
