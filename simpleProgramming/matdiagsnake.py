# mat = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
mat = [
    [1,4,7],
    [2,5,8],
    [3,6,9]
]
ans = {}
res = []
for i in range(len(mat)):
    for j in range(len(mat[0])):
        tmp = []
        if(ans.get(i+j)):
            tmp = ans[i+j]
            tmp.sort()
            tmp.append(mat[i][j])
        else:
            tmp = []
            tmp.append(mat[i][j])
            tmp.sort()
            ans[i+j] = tmp
for i in ans.items():
    for j in i[1]:
        res.append(j)
print(res)
