def has_path(graph, starting_node, destination):
    # The first think we do is to ask if the starting node and destination are the same
    if starting_node == destination: 
        return True
    for neighbor in graph[starting_node]:
        # Here we call the same function, has_path, for all of the neighbors of a given node
        # This function return true or false if we find such node.
        if has_path(graph, neighbor, destination):
            return True

    # If we couldn't find the destination node from the starting node 
    # we return false
    return False
    
graph = {
    1: [2, 3],
    2: [4],
    3: [5, 6],
    4: [],
    5: [],
    6: [],
    7: [8, 9, 10],
    8: [],
    9: [6],
    10: [],
}
print(has_path(graph, starting_node = 7, destination = 6))
# True