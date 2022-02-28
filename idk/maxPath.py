def maxPath(row,col,grid,count):
    if(row == len(grid)-1 and col == len(grid[0])-1):
        return grid[row][col]
    elif(row > len(grid)-1 or col > len(grid[0])-1):
        return 0
    else:
        down = maxPath(row+1,col,grid,count)
        right = maxPath(row,col+1,grid,count)
        count = grid[row][col]+max(down,right)
        return count

grid = [
  [1, 2, 8, 1],
  [3, 10, 12, 10],
  [4, 0, 6, 3],
]
print(maxPath(0,0,grid, 0))
