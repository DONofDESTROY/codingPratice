def printEmptyDiamond(n):
    '''
    Info: prints empty diamond 
    '''
    for row in range(2*n-1):
        for col in range(n*2-1):
            if(col+row==n-1)or (col-row==n-1) or (row-col ==n-1) or (row+col == n+(n*2)-3):
                print("*",end="")
            else:
                print("",end=" ")


        print()

def main():
    size = int(input())
    printEmptyDiamond(size)

main()
