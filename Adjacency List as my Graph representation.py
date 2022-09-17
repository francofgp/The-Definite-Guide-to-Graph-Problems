edges = [
    ["1", "2"],
    ["2", "3"],
    ["5", "3"],
    ["5", "4"],
    ["1", "4"]
]
def create_graph(edges):
    graph = {}
    for edge in edges:
        node_a, node_b = edge
        if node_a not in graph:
            graph[node_a] = []
        if node_b not in graph:
            graph[node_b] = []
        graph[node_a].append(node_b)
        graph[node_b].append(node_a)
    return graph

print(create_graph(edges))