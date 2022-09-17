def connected_components_counts(graph):
    visited = set()
    count = 0

    for node, neighbors in graph.items():
        stack = [node]
        if node in visited:
            continue
        while len(stack) > 0:
            currentNode = stack.pop()
            if currentNode in visited:
                continue
            visited.add(currentNode)
            for neighbor in graph[currentNode]:
                stack.append(neighbor)
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