def arrayMaker(string,row,col):
    arr = []
    k = 0
    tmp = []
    for i in range(len(string)):
        if(len(tmp)+1>=row):
            tmp.append(string[k])
            arr.append(tmp)
            tmp = []
            k+=1
        else:
            tmp.append(string[k])
            k+=1
        if(i == len(string)-1 and len(tmp)> 0):
            arr.append(tmp)
            
    return arr

def stringFinder(string,row,col,fString):
    twoDarray = arrayMaker(string,row,col)
    for i,index in enumerate(twoDarray):
        str = "".join(index)
        
        
        
            
 
def main():
    string = "WELCOMETOZOHOCORPORATION"
    fString = "TOO"
    row = 5
    col = 5
    stringFinder(string,row,col,fString)
    

main()
