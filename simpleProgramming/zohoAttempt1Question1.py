def hasher(arr):
    d = {}
    for i in arr:
        if(i not in d):
            d[i]= 1
        else:
            d[i]+=1
    return d

def isS2inS1(s1,s2,ss1,ss2):
    map2 = hasher(s2)
    flag = False
    for i in range(len(s1)-ss2+1):
        window = s1[i:i+ss2]
        map1 = hasher(window)        
        if(map1 == map2):
            print(f"found element on index {i}:{window}")
            flag = True
    if(not flag):
        print("no match found")
        

def main():
    s1 = [1,2,3,4,5,6,1,2,3]
    s2 = [1,2,3,4]

    isS2inS1(s1,s2,len(s1),len(s2))

main()
