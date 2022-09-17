def get_largests_component(graph):
    visited = set()
    max_size = float("-inf")
    for node, neighbors in graph.items():
        # Inicializamos el size en 0, y luego lo pasamos a la funcion traverse_graph
        size = 0
        max_size = max(max_size , traverse_graph(node, visited, graph, size))
    return max_size

def traverse_graph(currentNode, visited, graph, size):
    if currentNode in visited:
        return size
    visited.add(currentNode)
    # If the node has not been visited 
    # that means that the size must be at least 1 + previous size.
    size += 1
    for neighbor in graph[currentNode]:
        # calls to the neighbouring nodes may have different sizes,
        # but we are interested in the maximum, 
        # so we use the max() function to update the size variable.
        size = max(size, traverse_graph(neighbor, visited, graph, size))

    return size

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
print(get_largests_component(graph))
# 6