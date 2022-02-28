#*       *
#  *   *
#    *
#  *   *
#*       *

size = int(input())
for row in range(size):
    for col in range(size):
        if((row == col) or (row+col == size-1)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
