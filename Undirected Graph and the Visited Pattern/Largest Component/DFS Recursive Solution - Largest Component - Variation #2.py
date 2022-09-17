def get_largests_component(graph):
    visited = set()
    max_size = float("-inf")
    for node, edges in graph.items():
        size = traverse(node, graph, visited)
        # we compare the size of the recursive call, with the max_size,
        # and then we return it
        max_size = max(max_size, size)
    return max_size
def traverse(node, graph,visited):
    # If the node es visited it means we counted already
    if node in visited:
        return 0
    visited.add(node)
    # if the node is not visited it means at least the size is one
    size = 1

    for neighbor in graph[node]:
        # we sume +1 to the sum for every new non visited node
        size +=  traverse(neighbor, graph,visited)
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