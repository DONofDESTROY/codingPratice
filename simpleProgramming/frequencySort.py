def frequencySort(arr):
    map= {}
    ans = []
    for i in arr:
        if(i not in map):
            map[i] = arr.count(i)
    table = []
    for i in map.items():     
        table.append(list(i[::-1]))
    # print("table 1 ", table)    
    table.sort()
    for i in table:
        for j in range(i[0]):
            ans.append(i[1])
    # print("ans is",ans)    
    return ans



def main():
    arr = [1,3,1,3,1,4,5,2,2,4,5,3,1,3,1,1]
    print("before")
    print(arr)
    arr = frequencySort(arr)
    print("after")
    print(arr)

main()
