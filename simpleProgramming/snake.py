# mat = [[1,2,3],[4,5,6],[7,8,9]]
mat = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
count= 0
res = []
for i in mat:
    if(count%2 == 0):
        for j in i:
            res.append(j)
    else:
        for j in i[::-1]:
            res.append(j)
    count+=1



print(res)
