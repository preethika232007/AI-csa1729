grid = [[0, 1, 1, 1],
        [0, 0, 1, 0],
        [1, 0, 0, 1],
        [1, 1, 1, 0]]

def vacuum_cleaner(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                grid[i][j] = 0

    return grid

vacuum_cleaner(grid)

print("Cleaned Room:")
for row in grid:
    print(row)

print("The room can be cleaned.")