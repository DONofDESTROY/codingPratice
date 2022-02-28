def diamondHole(n):
    for i in range(n*2-1):
        for j in range(n*2-1):
            print("*",end="")
        print()


def main():
    n = int(input())
    diamondHole(n)


main()

