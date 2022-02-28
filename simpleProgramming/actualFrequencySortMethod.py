def frequencySort(d,key,reverse,r):
    di = list(d.items())
    if(reverse):
        for indi, i in enumerate(di):
            for indj, j in enumerate(di):
                if i[key] > j[key]:
                    di[indi], di[indj] = di[indj], di[indi]
    else:
        for indi, i in enumerate(di):
            for indj, j in enumerate(di):
                if i[key] < j[key]:
                    di[indi], di[indj] = di[indj], di[indi]

    return di


string = "sortwithoutanyinbuilt"
d = {}
for i in string:
    if(i not in d):
        d[i] = 1
    else:
        d[i]+=1

        
for i in frequencySort(d,1,True,0):
    print(i[0]*i[1],end="")

