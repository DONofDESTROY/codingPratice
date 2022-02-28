# can go 2 step forward
# can go 1 step backward
# find max robery
def planner(arr,s):
    dp = arr.copy()
    dp.append(float('inf')) 
    dp.append(float('inf')) 
    dp.append(float('inf')) 
    for i in range(len(arr),-1,-1):
       print(dp[i])
       dp[i]+=min(dp[i+2],dp[i-1])
    return dp

# houseList = [9,4,6,8,5]
houseList = [5, 1, 2, 10, 100]
print(planner(houseList,0))
