arr = [-2,-3,4,-1,-2,1,5,-3]

msf = arr[0]
maxe = arr[0]
for i in arr:
    maxe = maxe+i
    if(maxe < i):
        maxe = i
    if(msf < maxe):
        msf = maxe



print(msf)
    
