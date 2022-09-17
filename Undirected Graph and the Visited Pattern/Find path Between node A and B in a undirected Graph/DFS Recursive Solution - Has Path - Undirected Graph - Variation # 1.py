# We add a new parameter called visited, to keep track of our visited nodes.
# We pass an empty visited set to our function for the first time.
def has_path(graph, starting_node, destination, visited = set()):
    # The first think we do is to ask if the starting node and destination are the same
    if starting_node == destination: 
        return True
    # we checked if our starting node has been visited, if it has
    # we return False
    if starting_node in visited:
        return False
    visited.add(starting_node)
    for neighbor in graph[starting_node]:
        if has_path(graph, neighbor, destination, visited):
            return True

    return False

graph = {
    1: [2, 3],
    2: [1, 4],
    3: [1, 5, 6],
    4: [2],
    5: [3],
    6: [3],
    7: [8, 9, 10],
    8: [7],
    9: [7],
    10: [7],
}
print(has_path(graph, starting_node = 10, destination = 8))
# True