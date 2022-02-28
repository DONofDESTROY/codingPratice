def removeUnwantedParan(string):
    lCount = 0
    rCount = 0
    for i in string:
        if(i=="("):
            lCount+=1
        elif(i==")"):
            rCount+=1
    print(f"Lcount is {lCount} and rightcount {rCount}")



removeUnwantedParan("(((a)")

