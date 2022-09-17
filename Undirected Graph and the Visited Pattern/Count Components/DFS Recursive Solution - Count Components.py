def connected_components_counts(graph):
    visited = set()
    count = 0
    # we iterate through our graph and calling the traverse function
    # on each element
    for node, neighbors in graph.items():
        if traverse_graph(node, visited, graph):
            count += 1 
    return count

def traverse_graph(currentNode, visited, graph):
    if currentNode in visited:
        return False
    visited.add(currentNode)

    for neighbor in graph[currentNode]:
        traverse_graph(neighbor, visited, graph)

    # When the recursive function reach this statement it means that it has found out component
    # and all its nodes have been marked as visited, so that we don't count them in the next
    # recursion call
    return True

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