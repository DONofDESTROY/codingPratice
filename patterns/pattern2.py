number = int(input())
size = 2*number -1
for row in range(size):
    for col in range(size):
            print(number-min(row,col,size-1-row,size-1-col),end=" ")
    print()
