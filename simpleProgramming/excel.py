def colnum_string(n):
    string = ""
    while n > 0:
        n, remainder = divmod(n - 1, 26)
        print(divmod(n-1,26))
        string = chr(65 + remainder) + string
    return string

while True:
    num = int(input())
    print(colnum_string(num))
