def canConstruct(target,tmp, arr):
    if(tmp==target):
        return True
    elif(len(tmp)>len(target)):
        return False
    else:
        for i in arr:
            if(canConstruct(target,tmp+i, arr)):
                return True
        return False



print(canConstruct('helo','', ['he', 'ee', 'll', 'oo', 'o']))
