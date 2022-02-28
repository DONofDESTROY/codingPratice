def sum(num):
    sum = 0
    while (num>0):
        sum+= num%10
        num = num//10
    return sum
def sumSort(arr):
    # print("given array: ", arr)
    map = {}
    lis = []
    for i in arr:
        if(i not in map):
            map[i] = sum(i) 
    lis = list(map.items())
    # print("each element sum: ",lis)
    lis2 = []
    for index,i in enumerate(lis):
        for indexj,j in enumerate(lis):
            if(i[0] == j[0]):
                if(i[1] > j[1]):
                    lis[index],lis[indexj] = lis[indexj],lis[index]
            if(i[0] < j[0]):
                lis[index],lis[indexj] = lis[indexj],lis[index]
    # print("sorted: ",lis)
    for i in lis:
       lis2.append(i[0]) 
    # print("return this",end=" ")
    print(lis2)


def main():
    arr = [21,12,43,34]
    sumSort(arr)
main()

