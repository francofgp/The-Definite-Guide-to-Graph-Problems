WATER = "W"
LAND = "L"
def largest_island(grid):
    visited = set()
    # Variable to keep track of the largest island
    max_island = float("-inf")
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == WATER:
                continue
            if (row, col) in visited:
                continue
            # Iterate the grid and call the explore_land function,
            # which will return the size of the island found, 
            # and then compare it with our max_island variable.
            max_island = max(max_island, explore_land(grid, row, col, visited))

    return max_island

def explore_land(grid, row, col, visited):
    max_island = 0
    queue = [(row, col)]
    while len(queue) > 0:
        row, col = queue.pop(0)
        if (row, col) in visited:
            continue
        visited.add((row, col))
        if grid[row][col] == WATER:
            continue
        # We add 1 to our variable for each land node we find, 
        # then look for the neighbours of the current land node.
        max_island +=1
        neighbors = get_neigbors(grid, row, col)
        for neighbor in neighbors:
            queue.append(neighbor)
    return max_island
    
def get_neigbors(grid, row, col):
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
    ["W", "L", "W", "W", "W"],
    ["W", "L", "W", "W", "W"],
    ["W", "W", "W", "L", "W"],
    ["W", "W", "L", "L", "W"],
    ["L", "W", "W", "L", "L"],
    ["L", "L", "W", "W", "W"],
]
print(largest_island(grid))
# 5