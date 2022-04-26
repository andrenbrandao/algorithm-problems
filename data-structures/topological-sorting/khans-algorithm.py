"""
## Topological Sorting ##

It provides a way to find a path using all nodes in a directed acyclic
graph.

   B
 / | \
A  |  D
 \ | /
   v
   C

Let's consider the above graph as having the following paths:
A -> B
A -> C
B -> C
B -> D
C -> D

A valid answer would be: A -> B -> C -> D.

The algorithm to do this would be:

- Calculate the in-degree and out-degree of all nodes
- Get the nodes that have an in-degree of zero and add them to a queue
- Pop the next element from the queue and add it to our path
- Remove this current node from the graph. That is, take all the neighbors of
the current_node and decrease their in-degrees by one.
- Add the next nodes with in-degree zero to the queue
- Repeat until we do not have any more nodes to visit

Notes:
- If we have a cycle, we will have nodes with in-degree greater than zero
that were not visited.

Time Complexity: O(V + E)
Space Complexity: O(V + E)
"""
from collections import deque, defaultdict


def topological_sort(nodes):
    adjacency_hashmap = create_adjacency_hashmap(nodes)
    indegrees = create_indegree_hashmap(nodes)
    visited = set()
    queue = deque()

    for key in indegrees:
        if indegrees[key] == 0:
            queue.append(key)
            visited.add(key)

    result = []
    while queue:
        key = queue.popleft()
        result.append(key)

        for neighbor in adjacency_hashmap[key]:
            if neighbor in visited:
                continue

            indegrees[neighbor] -= 1
            if indegrees[neighbor] == 0:
                queue.append(neighbor)
                visited.add(neighbor)

    for key in indegrees:
        if indegrees[key] != 0:
            raise Exception("Cycle detected!")

    return result


def create_adjacency_hashmap(nodes):
    hashmap = defaultdict(list)

    for node in nodes:
        for neighbor in node.neighbors:
            hashmap[node.name].append(neighbor.name)

    return hashmap


def create_indegree_hashmap(nodes):
    hashmap = dict()

    for node in nodes:
        hashmap[node.name] = hashmap.get(node.name, 0)
        for neighbor in node.neighbors:
            hashmap[neighbor.name] = hashmap.get(neighbor.name, 0) + 1

    return hashmap


class Node:
    def __init__(self, name, neighbors=[]):
        self.name = name
        self.neighbors = neighbors


def create_graph():
    node_a = Node("A")
    node_b = Node("B")
    node_c = Node("C")
    node_d = Node("D")

    node_a.neighbors = [node_b, node_c]
    node_b.neighbors = [node_c, node_d]
    node_c.neighbors = [node_d]

    return [node_a, node_b, node_c, node_d]


def create_cyclic_graph():
    node_a = Node("A")
    node_b = Node("B")
    node_c = Node("C")
    node_d = Node("D")

    node_a.neighbors = [node_b, node_c]
    node_b.neighbors = [node_c, node_d]
    node_c.neighbors = [node_d]
    node_d.neighbors = [node_c]

    return [node_a, node_b, node_c, node_d]


def create_cyclic_graph_2():
    node_a = Node("A")
    node_b = Node("B")
    node_c = Node("C")
    node_d = Node("D")

    node_a.neighbors = [node_b, node_c]
    node_b.neighbors = [node_c, node_d]
    node_c.neighbors = [node_d]
    node_d.neighbors = [node_a]

    return [node_a, node_b, node_c, node_d]


def test(nodes, expected_answer):
    answer = topological_sort(nodes)

    if answer != expected_answer:
        raise Exception(
            f"Answer {answer} is incorrect. Expected answer was {expected_answer}"
        )


def test_exception(nodes, message):
    try:
        topological_sort(nodes)
    except Exception as error:
        if message != str(error):
            raise error


if __name__ == "__main__":
    test(create_graph(), ["A", "B", "C", "D"])
    test([], [])
    test_exception(create_cyclic_graph(), "Cycle detected!")
    test_exception(create_cyclic_graph_2(), "Cycle detected!")
    print("All tests passed!")
