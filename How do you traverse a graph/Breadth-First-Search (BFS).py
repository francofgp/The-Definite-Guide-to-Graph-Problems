def breadth_first_search(graph,starting_node):
    queue = [starting_node] # Declare a queue and insert the starting node.
    while len(queue) > 0: # While the queue is not empty you remove the first node of the queue.
        current_node = queue.pop(0) 
        print(current_node)
        for neighbor in graph[current_node]:
            queue.append(neighbor) # Insert all the neighbors of the node into the queue.

graph = {
    1: [2, 3],
    2: [4],
    3: [5, 6],
    4: [],
    5: [],
    6: [],
}
breadth_first_search(graph, 1)
# 1 2 3 4 5 6