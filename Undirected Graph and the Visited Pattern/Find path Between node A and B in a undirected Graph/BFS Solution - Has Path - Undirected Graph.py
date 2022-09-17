def has_path(graph, starting_node, destination):
    visited = set() # Set to keep track our visited nodes
    if starting_node == destination:
        return True
    queue = [starting_node]
    while len(queue) > 0:
        current_node = queue.pop(0) 

        # Ask if our current node has been visited
        # if it has been visited, we skip this node
        if current_node in visited: 
            continue
        # add our current node to the visited set
        visited.add(current_node) 

        if current_node == destination:
            return True
        for neighbor in graph[current_node]:
            queue.append(neighbor)

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
print(has_path(graph, starting_node = 2, destination = 6))
# True