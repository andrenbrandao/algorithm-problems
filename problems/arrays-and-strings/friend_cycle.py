"""

Given employees and friendships, find all adjacencies that denote the friendship
A friendship is bi-directional/mutual so if 1 is friends with 2, 2 is also friends with 1.

Sample Input:
employees = [
  "1, Bill, Engineer",
  "2, Joe, HR",
  "3, Sally, Engineer",
  "4, Richard, Business",
  "6, Tom, Engineer"
]

friendships = [
  "1, 2",
  "1, 3",
  "3, 4"
]

Sample Output:
Output: [
"1: 2, 3",
"2: 1",
"3: 1, 4",
"4: 3",
"6: None"
]


-- Algorithm --

- Go through all employees and get their ids, so that we can generate
a result with all ids
- Add them to a hashmap
- Go through the friendships and add the bidirectional relations to the
keys in the hashmap
- In the end, go through the employees ids, lookup their friends in the
hashmap and write the friends to a string
Note: we cannot use the ordering of hashmaps because it can be different

{
    1: [2, 3],
    2: [1],
    3: [1, 4],
    4: [3],
    6: []
}

result = [
    "1: 2, 3",
    "2: 1",
    "3: 1, 4",
    "4: 3",
    "6: None"
]

"""


def friend_cycle(employees, friendships):
    friends_hashmap = dict()
    ids = []

    for employee in employees:
        employee_id = employee[0]
        ids.append(employee_id)
        friends_hashmap[employee_id] = []

    for friendship in friendships:
        id1, id2 = friendship[0], friendship[3]
        friends_hashmap[id1].append(id2)
        friends_hashmap[id2].append(id1)

    result = []
    for id in ids:
        if len(friends_hashmap[id]) > 0:
            friends = ", ".join(friends_hashmap[id])
            result.append(f"{id}: {friends}")
        else:
            result.append(f"{id}: None")

    return result


def test(employees, friendships, expected_answer):
    answer = friend_cycle(employees, friendships)

    if answer != expected_answer:
        raise Exception(
            f"Answer {answer} is incorrect. Expected answer was {expected_answer}"
        )


test(
    [
        "1, Bill, Engineer",
        "2, Joe, HR",
        "3, Sally, Engineer",
        "4, Richard, Business",
        "6, Tom, Engineer",
    ],
    ["1, 2", "1, 3", "3, 4"],
    ["1: 2, 3", "2: 1", "3: 1, 4", "4: 3", "6: None"],
)
print("All tests passed!")
