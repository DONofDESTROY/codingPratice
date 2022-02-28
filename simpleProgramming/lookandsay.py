def lookAndSay(n):
    lis = []
    lis.append(1)
    lis.append(11)
    for _ in range(n):
        ans = ""
        for j in str(lis[-1]):
            print("on this",str(lis[-1]))
            c = str(lis[-1]).count(j)
            # j = (j)
            # ans += f"{c}{j}"
            ans = f"{c}{j}"
        lis.append(ans)
        print(ans)

            






lookAndSay(5)
