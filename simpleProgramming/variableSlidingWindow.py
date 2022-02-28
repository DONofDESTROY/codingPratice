arr = [1,2,3,4,5,6,7]

for i in range(1,len(arr)+1):
    for j in range(len(arr)):
        window = arr[j:j+i]
        if(len(window)==i):
            print(window)

