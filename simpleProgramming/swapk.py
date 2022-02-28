def swapper(arr,k):
    i = 0
    l = len(arr)-1
    if(k*2 > l+1):
        return "Swap not possible"
    for i in range(k):
        arr[i], arr[l] = arr[l],arr[i] 
        i+=1
        l-=1
    return arr



print(swapper([1,2,3,4,5,6],3))
