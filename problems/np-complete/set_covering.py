"""
The set-covering problem
Book: Grokking Algorithms
Chapter 8: Greedy Algorithms

Suppose you're starting a radio show. You want to reach listeners in all 50 states.
You have to decide what stations to play on to reach all those listeners.
It costs money to be on each station, so you're trying to minimize the number of stations you play on.
You have a list of stations.
Each station covers a region, and there's overlap.

station | states
kone -> id, nv, ut
ktwo -> wa, id, mt
kthree -> or, nv, ca
kfour -> nv, ut
kfive -> ca, az

How do you figure out the smallest set of stations you can play on to cover all 50 states?

--
### SOLUTION ####

Naive Solution
- Create a set of states
- Create all possible subsets of stations
- For each subset, check if it contains all states and pick the smallest

How to find the time complexity? For each station, I can add it to the set, or not add it.

        {}
   /         \
  {}        {kone}
 / \         /  \
{} {ktwo} {kone} {kone, ktwo}
/\...

2^0 + 2^1+ 2^2... 2^n => Sum(2^k) from 0 to n. => 2^(n+1) - 1

Time Complexity: O(2^n)

--
Greedy Solution (Approximation Algorithm)
- Pick the station with the most states that have not been covered yet.
It is ok if some states have already been covered.
- Repeat the process until all states are covered.

So, we have to go through all stations and check how many states it can cover. Compare this to the
next stations and get the one with the max amount of states covered.
Do this until all states are covered.

Since we might go through the entire list N times for each of the states, this is O(n²).

Time Complexity: O(n²)
"""


def set_cover_greedy(stations, states_needed):
    final_stations = set()

    while states_needed:
        best_station = None
        covered = set()

        for station, states_for_station in stations.items():
            covered_states_of_stations = states_for_station & states_needed
            if len(covered_states_of_stations) > len(covered):
                covered = covered_states_of_stations
                best_station = station

        states_needed -= covered
        final_stations.add(best_station)

    return final_stations


def set_cover_naive(stations, states_needed):
    subsets = generate_subsets(stations)

    subsets_with_all_states = get_subsets_with_all_states(
        stations, subsets, states_needed
    )

    return min(subsets_with_all_states, key=lambda subset: len(subset))


def generate_subsets(stations):
    keys = list(stations.keys())
    subsets = []

    def rec_gen_subset(stations, index, current_subset):
        if index >= len(stations):
            subsets.append(current_subset)
            return

        rec_gen_subset(stations, index + 1, current_subset | set([stations[index]]))
        rec_gen_subset(stations, index + 1, current_subset)

    rec_gen_subset(keys, 0, set())
    return subsets


def get_subsets_with_all_states(states_for_station, subsets, states_needed):
    subsets_with_all_states = []
    for subset in subsets:
        covered_states = set()
        for station in subset:
            covered_states = covered_states | states_for_station[station]
        if covered_states == states_needed:
            subsets_with_all_states.append(subset)

    return subsets_with_all_states


def test(stations, states_needed, expected_answer):
    answer = set_cover_greedy(stations, states_needed)

    if answer != expected_answer:
        raise Exception(
            f"Answer {answer} is incorrect. Expected answer was {expected_answer}"
        )


if __name__ == "__main__":
    stations = {
        "kone": set(["id", "nv", "ut"]),
        "ktwo": set(["wa", "id", "mt"]),
        "kthree": set(["or", "nv", "ca"]),
        "kfour": set(["nv", "ut"]),
        "kfive": set(["ca", "az"]),
    }
    states_needed = set(["id", "nv", "ut", "wa", "mt", "or", "ca", "az"])
    test(stations, states_needed, set(["ktwo", "kthree", "kone", "kfive"]))
    print("All tests passed!")
