def main():
    postLis = {}
    i = 0
    while True:
        post = input()
        if(i<10):
            postLis[i] = post
        else:
            postLis[i] = post
            postLis.pop(i-10)
        i+=1
        print("length is",len(postLis.keys()))
        print(list(postLis.values()))


main()

