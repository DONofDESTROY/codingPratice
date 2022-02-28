lis = [[0,1,0],[1,0,1],[0,1,0]]
s = set()
for i in lis:
    tmp = ''
    for j in i:
        tmp += str(j)
    s.add(tmp)



for i in s:
    tmp = []
    for j in i:
       tmp.append(int(j)) 
    print(tmp)

