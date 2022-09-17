def cycle_in_graph(graph):
    visited = set()
    currently_in_stack = set()

    for node in graph:
        # If the node was visited, we can skip it.
        if node in visited:
            continue
        # We call the function below, 
        # to determine if the node we are scanning has a cycle, 
        # if true, we return True.
        contains_cycle = is_node_in_cycle(graph, node, visited, currently_in_stack)
        if contains_cycle:
            return True
    return False

    
def is_node_in_cycle(graph, node, visited, currently_in_stack):
    visited.add(node)
    # We add the current node to our stack, 
    # if we explore it again and it is in the stack, it means we found a cycle.
    currently_in_stack.add(node)

    neighbors = graph[node]
    # We explore the neighbours of our current node
    for neighbor in neighbors:
        if neighbor not in visited:
            # For each of the neighbouring nodes we call the function below again, 
            # to continue exploring,
            # and return True if a cycle is found.
            contains_cycle = is_node_in_cycle(graph, neighbor, visited, currently_in_stack)
            if contains_cycle:
                return True
        # If the node we are exploring has been visited and is in the stack, 
        # it means that there is a cycle.
        elif neighbor in currently_in_stack:
            return True
    currently_in_stack.remove(node)

    return False

graph = {
    1: [2, 4],
    2: [3],
    3: [3],
    4: [5],
    5: [2]
}
print(cycle_in_graph(graph))
# True