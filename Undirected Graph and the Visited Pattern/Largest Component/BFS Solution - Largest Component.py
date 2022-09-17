def get_largests_component(graph):
    visited = set()
    # We use the this variale to store the size of the maximum component
    # its first value es - infinity.
    max_size = float("-inf")
    for node in graph:
        queue = [node]
        size = 0
        while len(queue) > 0:
            current_node = queue.pop(0)
            if current_node in visited:
                continue
            size += 1
            visited.add(current_node)
            for neighbor in graph[current_node]:
                queue.append(neighbor)
        # when we stop iterating throug a component
        # we need to compare its maximum value with the
        # max_size variable.
        max_size = max(max_size, size)
    return max_size


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