cache = {}
def canSum(target, array):
    global cache
    if target in cache:
        return cache[target]
    elif target == 0:
        return True
    elif target <0:
        return False
    else:
        for i in range(len(array)):
            cache[target-array[i]] = canSum(target-array[i],array)
            if(cache[target-array[i]]):
                return True
    return False




print(canSum(7,[2,4,7,10,30,40]))
print(cache)
