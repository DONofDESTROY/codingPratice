cache = {}
def fib(n):
    if(n in cache):
        return cache[n]
    else:
        if(n<1):
            return 1;
        else:
            cache[n-1]= fib(n-1)
            cache[n-2]= fib(n-2)
            return cache[n-1]+cache[n-2]



print(fib(100))

