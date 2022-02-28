arr = [4,5,2,25]
for i in arr:
    k = 0
    ans = i
    print(f"i --> ",end = "")
    while i+k <= len(arr)-1 and  i < arr[i+k]:
        ans = arr[i+k]
        if(i+k == len(arr)-1):
            ans = -1
        k+=1
    print(k)

