def permutations(arr):
    res = []
    s = len(arr)
    def backtracking(tmp,arr):
        if(len(tmp) == s):
            print(tmp)
            res.append(tmp)
            return
        else:
            for ind,i in enumerate(arr):
                tmp.append(i)
                val = arr.pop(ind)
                print()
                backtracking(tmp,arr)
                tmp.pop()
                arr.append(val)
    backtracking([],arr)

    return res





print(permutations([1,2,3]))
