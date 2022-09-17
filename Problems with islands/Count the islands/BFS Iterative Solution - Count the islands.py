WATER = "W"
LAND = "L"
def island_count(grid):
    visited = set()
    islands = 0
    # With this nested for loop, we iterate through our grid
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            # We continue if the cell is watter
            if grid[row][col] == WATER:
                continue
            # we also continue if the cell has been visited
            if (row, col) in visited:
                continue
            # If we reach this line, it means that we found an island,
            # our next step is to keep exploring this island,
            # and mark of its adjancent cells as visited, so we can 
            # skip them in the next iteration of the foor loop
            islands += 1
            explore_land(grid, row, col, visited)

    return islands

def explore_land(grid, row, col, visited):

    queue = [(row, col)]
    while len(queue) > 0:
        row, col = queue.pop(0)
        #We check if the node has been visited, 
        # if so we skip it.
        if (row, col) in visited:
            continue
        # We mark the node as visited, and check if 
        # the current node is water, if so we skip it.
        visited.add((row, col))
        if grid[row][col] == WATER:
            continue
        # We get the neighboring nodes of 
        # the current node, and then add them to the queue.
        neighbors = get_neigbors(grid, row, col)
        for neighbor in neighbors:
            queue.append(neighbor)

def get_neigbors(grid, row, col):
    # We get the nodes around the current node. 
    neighbors = []
    # Up
    if row - 1 >= 0:
        neighbors.append((row - 1, col))
    # Down
    if row + 1 < len(grid):
        neighbors.append((row + 1, col))
    # Left
    if col - 1 >= 0:
        neighbors.append((row, col - 1))
    # Rigth
    if col + 1 < len(grid[0]):
        neighbors.append((row, col + 1))

    return neighbors

grid = [
    ["W", "L", "W", "W", "L", "L"],
    ["W", "W", "W", "W", "W", "W"],
    ["W", "W", "W", "W", "L", "W"],
    ["W", "L", "L", "W", "L", "L"],
    ["W", "L", "L", "W", "L", "W"],
    ["W", "W", "W", "W", "W", "W"],
]
print(island_count(grid))
# 4