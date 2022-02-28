def reverseString(string):
    if(len(string)<1):
        return ''
    else:
        return string[-1] + reverseString(string[:len(string)-1])




print(reverseString("hello There"))
