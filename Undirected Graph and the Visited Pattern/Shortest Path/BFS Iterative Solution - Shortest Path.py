def shortest_path(graph, source, destination):
    visited = set()
    queue = [(source, 0)]

    while len(queue) > 0:
        current_node, distance = queue.pop(0)
        if current_node == destination:
            return distance
        if current_node in visited:
            continue
        visited.add(current_node)
        
        for neighbor in graph[current_node]:
            queue.append((neighbor, distance + 1))

    return -1
    
graph = {
    1: [2, 3],
    2: [1, 4],
    3: [1, 5, 6],
    4: [2, 5],
    5: [3, 4, 6],
    6: [3, 5],
}

print(shortest_path(graph, 1, 6))
# 2