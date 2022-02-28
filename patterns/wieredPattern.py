def printpattern(size, word):
    count = 0
    if size%2 ==0:
        word = word[:size//2]+'*'+word[size//2:]
        size+=1
    for i in range(size):
        for j in range(size):
            if(i==size//2):
                print(word[count],end=" ")
                count+=1
            elif(i==j or i+j==size-1 or j==size//2):
                print(word[i],end=" ")
            else:
                print(" ",end=" ")
        print(" ")



def main():
    word = input("better enter a odd size word:== ")
    size = len(word)
    printpattern(size, word)

main()
