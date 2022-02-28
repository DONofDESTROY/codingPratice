# An array of costs was given.
# You can either take two jumps forward or one jump backward. 
# If you land on a particular index, you have to add the cost to your total.
# Find the minimum cost needed to cross the array or reach the end of the array.

###############
    # Input
###############

# 5 (Number of elements in the array)
#
# [9,4,6,8,5] (Array)
#
# 1 (Index to start)

###############
   # Output
###############


def minJump(target, arr , n, count):
    print(n)
    if(n == target):
        return arr[n]
    elif(n >= target or n < 0):
        print("here")
        return 0
    else:
        twoStep = 0
        back = 0
        if(n-1 > 0):
            back = minJump(target,arr,n-1,count)
        if(n+2 < target):
            twoStep = minJump(target, arr, n+2,count)
        count = min(twoStep,back) 
        return min(twoStep,back)


print(minJump(5-1,[9,4,6,8,5],0,0))

