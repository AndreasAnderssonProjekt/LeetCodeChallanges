def numberOfIslands(grid):
    m = len(grid)
    n = len(grid[0])
    count = 0

    for i in range(m):
        for j in range(n):
            if grid[i][j] == "1":
                count += 1
                dfs(grid, i, j)
    return count

def dfs(grid, x, y):
    if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
        return
    if grid[x][y] != "1":
        return

    grid[x][y] = "X"
    dfs(grid, x-1, y)
    dfs(grid, x, y-1)
    dfs(grid, x+1, y)
    dfs(grid, x, y+1)
