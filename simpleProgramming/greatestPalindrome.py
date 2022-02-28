def isPalindrome(arr):
    size = len(arr)
    flag = True
    for i in range(size//2):
        if(abs(arr[i])!=abs(arr[-(i+1)])):
            flag = False
    return flag


def mainWindowMaker(arr):
    maxSoFar = [arr[0]]
    for i in range(len(arr)+1):
        for j in range(len(arr)+1):
            window = arr[i:j]
            if(len(window)>0):
                if(isPalindrome(window)):
                    if(len(window)> len(maxSoFar)):
                        maxSoFar = window
    return maxSoFar

print(mainWindowMaker([1,-2,4,-5,-6,3,3,6]))
