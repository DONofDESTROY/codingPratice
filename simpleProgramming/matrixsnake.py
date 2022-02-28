def matrixsnake(mat):
    ans = []
    for ind, i in enumerate(mat):
        sub = i
        if(ind%2 != 0):
            sub = i[::-1]
        for j in sub:
            ans.append(j)
        
    return ans


matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(matrixsnake(matrix))
