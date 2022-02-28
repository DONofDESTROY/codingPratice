def lookandSay(n):
    str = "1"
    print(str)
    count = 0
    while count < n:
        ans = ""
        for index,i in enumerate(str):
            c = str.count(i)
            if(i != str[index-1]):
                print(f"{c}{i}",end="")
                ans+=f"{c}{i}"
                str = ans
                c=0
        print()
        count+=1

def main():
    size = int(input("enter the size "))
    lookandSay(size)

main()
