def has_path(graph, starting_node, destination, visited = set()):
    # The first think we do is to ask if the starting node and destination are the same
    if starting_node == destination: 
        return True
    for neighbor in graph[starting_node]:
        # We ask if our neighboring node has been visited
        if neighbor in visited:
            continue
        # we mark our neighbor has visited, so that in the next recursion call
        # we ask if it is the node that we are looking for
        visited.add(neighbor)
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