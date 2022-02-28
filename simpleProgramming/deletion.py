s1 = 'heat'
s2 = 'hit'
s1map = {}
s2map = {}
for i in s1:
    if i in s1map:
        s1map[i] += 1
    else:
        s1map[i] = 0


for i in s2:
    if i in s2map:
        s2map[i] += 1
    else:
        s2map[i] = 0




print(s1map, s2map)
