def has_path(graph, starting_node, destination):
    # The first think we do is to ask if the starting node and destination are the same
    if starting_node == destination: 
        return True
    queue = [starting_node]
    while len(queue) > 0:
        current_node = queue.pop(0) 
        if current_node == destination:
            # We keep asking if they are the same with every new node in the queue
            return True
        for neighbor in graph[current_node]:
            queue.append(neighbor)

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