def searcher(t,s):
    nr = len(t)
    nc = len(t[0])
    def helper(r,c,i,s):
        print(i,r,c)
        print(s[i]==t[r][c])
        if(s[i]==t[r][c]):
            i+=1
            if(i == len(s)-1):
                print(f"End index: <{r},{c}>")
            return True
        if(  not(r==0 and c==0) and ( r<0 or c <0 or  r>nr or c > nc )):
            return False
        else:
            for k in range(len(t)):
                for j in range(len(t[0])):
                    val = helper(k,j,0,i)
                    print(val)
                    if (val):
                        print(f"Starting index: <{k},{j}>")
        
    helper(0,0,0,s)

        

    

wordTable = [
    ['w','e','l','c','o'],
    ['m','e','t','o','z'],
    ['o','h','o','c','o'],
    ['r','p','o','r','a'],
    ['t','i','o','n','']
]
search = "too"
searcher(wordTable, search)
# w	e	L	C	O
# M	E	T	O	Z
# O	H	O	C	O
# R	P	O	R	A
# T	I	O	n	  
