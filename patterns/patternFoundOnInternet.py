# https://rizwan94.blogspot.com/2013/10/maventic-technical-round-question.html
def printPattern(num):
    h = num//2
    for r in range(num):
        for c in range(num):
            if(r == 0 or c == 0 or r == num-1 or c == num-1 or ((r+c== num-1)and (r!=h)) or ((r-c == 0)and c!=h)):
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()



def main():
    size = int(input())
    printPattern(size)


main()
