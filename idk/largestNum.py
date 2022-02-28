def largestNum(arr):
    arr = [str(n) for n in arr]
    size = len(arr)
    def helper(tmp, arr):
        if(len(arr)==0):
            print(''.join(tmp))
            return ''.join(tmp)
        else:
            for i in range(len(arr)):
                val = arr[i]
                tmp.append(val)
                arr.pop(i)
                print(arr)
                helper(tmp,arr)     
                arr.append(val)
                print(tmp,arr)


    return helper([],arr)

print(largestNum([10,2]))
