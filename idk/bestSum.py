def bestSum(target,arr):
    if target == 0:
        return []
    elif target < 0:
        return None
    else:
        tmp = None
        for i in arr:
            rem = target - i
            res = bestSum(rem,arr)
            if(res != None):
                combo = [*res, i]
                if( tmp == None or len(tmp) > len(res)):
                    tmp = combo


    return tmp



print(bestSum(10,[1,3,4,7]))
