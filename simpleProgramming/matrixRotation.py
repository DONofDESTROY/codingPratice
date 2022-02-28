def matrixRotation(mat):
    l = 0
    r = len(mat)-1
    while l < r:
        for i in range(r-1):
            top, bottom = l,r
            topLeft = mat[top][l]
            mat[top][l]= mat[top][l]
            r-=1
            l+=1
    return mat



def main():
    mat = [[1,2,3],[4,5,6],[7,8,9]]
    for i in mat:
        print(i)
    print("doing rotation ")
    print()
    matt = matrixRotation(mat)
    for i in matt:
        print(i)


main()


