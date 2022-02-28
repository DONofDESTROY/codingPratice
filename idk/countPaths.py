memo = {}
def count_paths(row, col,grid, count, memo):
  if(f"{row},{col}" in memo):
        return memo[f"{row},{col}"]
  elif(row > len(grid)-1 or col > len(grid[0])-1 or grid[row][col]=='X'):
    return 0
  elif(row == len(grid)-1 and col== len(grid[0])-1):
    count+=1
    return True
  else:
    memo[f"{row},{col}"] = count_paths(row+1,col,grid,count, memo) + count_paths(row,col+1,grid, count, memo)
    return memo[f"{row},{col}"]

grid = [
  ["O", "O", "X", "O", "O", "O"],
  ["O", "O", "O", "O", "O", "X"],
  ["X", "O", "O", "O", "O", "O"],
  ["X", "X", "X", "O", "O", "O"],
  ["O", "O", "O", "O", "O", "X"],
]

print(count_paths(0,0,grid,0, memo))
