from math import sqrt, ceil, floor
arr = [10,36,3,49,12]
ans = []
weit = {}
for i in arr:
    sum = 0
    if(i%2 == 0):
        sum+=3
    root = sqrt(i)
    if (floor(root)==ceil(root)):
        sum+=5
    if(i%4==0 and i%6==0):
        sum+=4
    weit[i]=sum

print(weit)
weit = sorted(weit.items(),key=lambda x: x[1],reverse=True) 
for i in weit:
    ans.append(i[0])
print(ans)
