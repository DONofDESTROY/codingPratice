str1 = input()
str2 = input()
something = str1.split(str2)
if(len(something)>1):
    print(len(something[0]))
else:
    print(-1)

#balas method
# def main(str1, str2):
#     if str2 in str1:
#         return str1.index(str2[0])
#     else:
#         return -1

# print(main(str1,str2))
