WATER = "W"
LAND = "L"
def island_count(grid):
    visited = set()
    island = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            # We iterate the grid with a double 
            # for loop and call the explore_land 
            # function with each node.
            # This function returns true or false, 
            # true means it found an island and 
            # we can add it to our variable "island".
             if explore_land(grid, row, col, visited):
                island += 1
    return island

def explore_land(grid, row, col, visited):
    # we check if the node is out of bounds or not, 
    # if true, we return true
    is_row_in_bounds = row >= 0 and row < len(grid)
    is_col_in_bounds = col >= 0 and col < len(grid[0])
    if is_row_in_bounds is not True or is_col_in_bounds is not True:
        return False
    #If the current node is water we return false
    if grid[row][col] ==  WATER:
        return False

    # we grab the current position and check if the node
    # has been visited
    position = (row, col)
    if position in visited:
        return False
    visited.add(position)

    # We call the recursive function, 
    # passing as parameter the possible positions of the neighboring nodes.
    explore_land(grid, row - 1, col, visited)
    explore_land(grid, row + 1, col, visited)
    explore_land(grid, row, col - 1, visited)
    explore_land(grid, row, col + 1, visited)

    # when we reach this statement, it means we found an island
    return True

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