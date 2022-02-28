arr1 = [1,2,4,5,6,7,8]
map = {}
target = 3
lis = []

for i in arr1:
    map[target-i] = i
    lis.append(target-i)
count = 0
for j,l in zip(arr1,lis):
    if(l+j==target):
        print(j,map[l])
    else:
        print("no element found")
