def removeChars(s1,s2):
    exist = {}
    for i in s2:
        if i not in exist:
            exist[i] = True
    
    for i in s1:
        if(i in exist):
            s1 =  s1.replace(i,'')         
    return s1

string1 = "geeksforgeeks"
string2 = "mask"
print(removeChars(string1, string2))
print("there is some thing changed as well")
print("whooo whoo")
