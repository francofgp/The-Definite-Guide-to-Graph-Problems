WATER = "W"
LAND = "L"
def largest_island(grid):
    visited = set()
    max_size = float("-inf")
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            current_size = explore_land(grid, row, col, visited)
            if current_size > 0:
                max_size = max(max_size, current_size)
    return max_size

def explore_land(grid, row, col, visited):
    is_row_in_bounds = row >= 0 and row < len(grid)
    is_col_in_bounds = col >= 0 and col < len(grid[0])
    if is_row_in_bounds is not True or is_col_in_bounds is not True:
        return 0
    if grid[row][col] ==  WATER:
        return 0

    position = (row, col)
    if position in visited:
        return 0
    visited.add(position)

    size = 1
    # Here we start with a size of 1 for the first piece of land, 
    # then add 1 if the recursive function calls return 1 for its neigbors, 
    # then return total size
    size += explore_land(grid, row - 1, col, visited)
    size += explore_land(grid, row + 1, col, visited)
    size += explore_land(grid, row, col - 1, visited)
    size += explore_land(grid, row, col + 1, visited)

    return size


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