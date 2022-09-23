def depth_first_search(graph, starting_node):
    queue = [starting_node]  # Declare a stack and insert the starting node.
    # While the stack is not empty you remove the last node of the stack.
    while len(queue) > 0:
        current_node = queue.pop()
        print(current_node)
        for neighbor in graph[current_node]:
            # Insert all the neighbors of the node into the queue.
            queue.append(neighbor)


graph = {
    1: [2, 3],
    2: [4],
    3: [5, 6],
    4: [],
    5: [],
    6: [],
}
depth_first_search(graph, 1)
# 1 3 6 5 2 4  # It does not matter if you start with the right neighbor or with the left one
