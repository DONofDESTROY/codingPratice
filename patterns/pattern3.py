size = int(input())
if(not size%2 ==0):
    for row in range(size*2-1):
        for col in range(size*2-1):
            print("*",end=" ")
        print()
else:
    raise Exception("This program works for odd")
