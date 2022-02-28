# there is a list of elements need to be go from start of list to end
# we can take either 1 step or 2 step but we can also go 1 step backwards
# while taking the step we have to calculate the path cost and we have to find the cost of the path to be less

path = [2,3,4,8,100,200,30] 
path.append(0)
var = 0
for i in range(len(path)-1,-1,-2):
    var += min(var+path[i],var+path[i-1])


print(var)
