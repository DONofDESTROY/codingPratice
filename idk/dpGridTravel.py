cache = {}
def gridTraveler(m,n):
    global cache
    if(f"{m},{n}" in cache):
        return cache[f"{m},{n}"]
    elif(m==1 and n==1):
        return 1
    elif(m==0 or n==0):
        return 0
    else:
        cache[f"{m},{n}"] = gridTraveler(m-1,n) + gridTraveler(m,n-1)
        return cache[f"{m},{n}"]


# print(gridTraveler(3,3))
# print(gridTraveler(18,18))
print(gridTraveler(41,50))
print(cache)
