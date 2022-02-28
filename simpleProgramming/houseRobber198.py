def houseRobber(arr):
    def helper(arr):
        if(len(arr)==0):
            return 1
        else:
           return max(arr[0]+helper(arr[2:]),arr[1]+helper(arr[3:]))


    return max(arr[0]+helper(arr[2:]),arr[1]+helper(arr[3:]))




print(houseRobber([1,2,3,1]))
