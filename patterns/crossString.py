def printCross(string):
    n = len(string)
    for i in range(n):
        for j in range(n):
            # for \
            if(i==j):
                print(string[i],end=" ")
            # for /
            elif(i+j==n-1):
                print(string[j],end=" ")
            # rest not line
            else:
                print(" ",end=" ")
        print()



def main():
    string = input("enter a string \n")
    printCross(string)


main()
