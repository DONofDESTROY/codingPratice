list1 = [2,4,5,6,7,9,10,13]
list2 = [2,3,4,5,6,7,8,9,11,15]
s = set()
i=j=0
while(i<len(list1)and j<len(list2)):
    s.add(list1[i])
    s.add(list2[j])
    i+=1
    j+=1
while(i<len(list1)):
    s.add(list1[i])
    i+=1

while(j<len(list2)):
    s.add(list2[j])
    j+=1
print(s)
