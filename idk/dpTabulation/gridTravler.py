def gridTravler(row,col):
    dp = [[0 for _ in range(col+2)] for _ in range(row+2)]
    dp[1][1] = 1


    for i in range(row+1):
        for j in range(col+1):
            current = dp[i][j]
            dp[i][j+1] += current
            dp[i+1][j] += current
    
    for i in range(row+2):
        for j in range(col+2):
            print(dp[i][j], end=" ")
        print()
    print(dp[row][col])



gridTravler(4,4)
