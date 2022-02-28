def mirroImage(s):
    for r in range(s):
        for _ in range(s-r):
            print(" ",end=" ")
        for c in range(r,-1,-1):
            print(c,end=" ")
        for ac in range(1,r+1):
            print(ac,end=" ")
        print()

size = int(input())
mirroImage(size)
