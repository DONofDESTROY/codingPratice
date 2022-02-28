memo = {}
def howSum(target,arr, memo):
    if target in memo:
        return memo[target]
    elif target == 0:
        return []
    elif target < 0:
        return None
    else:
        for i in arr:
            rem = target - i
            res = howSum(rem,arr, memo)
            if(res != None):
                memo[target] = [*res, i]
                return [*res, i]
    return None

                 



print(howSum(1000,[3,4,7], memo))
