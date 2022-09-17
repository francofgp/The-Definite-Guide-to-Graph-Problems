def connected_components_counts(graph):
    visited = set()
    count = 0 # we use this variable to counts our components

    # This new for loop is important, because we need to make sure that we traverse through the entire graph
    # to ensure that we visit all nodes.
    for node, neighbors in graph.items():
        queue = [node]
        if node in visited:
            continue
        while len(queue) > 0:
            currentNode = queue.pop(0)
            if currentNode in visited:
                continue
            visited.add(currentNode)
            for neighbor in graph[currentNode]:
                queue.append(neighbor)

        # We count as + 1 component, when our queue is empty, 
        #because when we're traversing on the first node of a component 
        # and we add an element to the queue, and when our queue happened
        #  to be empty that means that we have visited all the nodes 
        # related to the first node of our for loop, on the next element 
        # of our for loop, if that element has been visited we skip it, 
        # if the next element of our for loop is a node that has not 
        # been visited, that means that we found a new component and  
        # we need to search for its neighbors and add them to the queue.
        count += 1
    return count

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
    11: [12],
    12: [11]
}
print(connected_components_counts(graph))
# 3