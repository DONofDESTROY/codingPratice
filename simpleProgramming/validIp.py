# ip = '172.16.254.1'

# ip = '125.512.100.1'
ip = '125.512.100.abc'  

arr = ip.split('.')
validity = True

for i in arr:
    for j in i:
        if j.isalpha():
            validity = False
            
    if validity and (not (int(i)>=0 and int(i)<=255)):
        validity = False

print(validity)

