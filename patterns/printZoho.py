def printz(size):
    for row in range(size):
        for col in range(size):
            if(row ==0 or row == size-1 or row+col == size-1):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()

def printo(size):
    for row in range(size):
        for col in range(size):
            if(row ==0 or row == size-1 or col == 0 or col == size-1):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()

def printh(size):
    for row in range(size):
        for col in range(size):
            if(col ==0 or col == size-1 or  row == size//2):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()

def printzoho(size):
    printz(size)
    print()
    printo(size)
    print()
    printh(size)
    print()
    printo(size)
    print()


size = int(input("enter font size:--- "))
printzoho(size)
