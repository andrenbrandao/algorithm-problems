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


def staircase(n, possible_steps, callstack):
    callstack.append(f"staircase({n}, {possible_steps})")
    print(callstack)

    if n == 0:
        callstack.pop()
        print(callstack)
        return 1

    ways = 0
    for steps in possible_steps:
        if n - steps >= 0:
            ways += staircase(n - steps, possible_steps, callstack)

    callstack.pop()
    print(callstack)
    return ways


def test(n, possible_steps, expected_answer):
    answer = staircase(n, possible_steps, [])

    if answer != expected_answer:
        raise Exception(
            f"Answer {answer} is incorrect! Expected answer was {expected_answer}"
        )


if __name__ == "__main__":
    test(0, [1, 2, 3], 1)
    test(10, [2, 4, 5, 8], 11)
    print("All tests passed!")
