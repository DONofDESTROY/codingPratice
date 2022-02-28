def segregate(arr):
    count1 = 0
    count0 = 0
    for i in arr:
        if(i==0):
            count0+=1
        elif(i==1):
            count1+=1
    return [0]*count0+[1]*count1



def main():
    print(segregate([0, 1, 0, 1, 0, 0, 1, 1, 1, 0]))
    


main()
