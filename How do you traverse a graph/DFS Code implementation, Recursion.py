def breadth_first_search(graph,starting_node):
    # Create a recursive function that takes in the graph and the starting node.
    print(starting_node)
    for neighbor in graph[starting_node]: 
        # Create your base cases. In this case my base is when the for loop contains zero elements.
        # When that is the case I do not call the breadth_first_search function
        # Traverse all the neighbor nodes and call the recursive function with the index of the neighbor node.
        breadth_first_search(graph, neighbor)

graph = {
    1: [2, 3],
    2: [4],
    3: [5, 6],
    4: [],
    5: [],
    6: [],
}
breadth_first_search(graph, 1)
# 1 3 6 5 2 4 