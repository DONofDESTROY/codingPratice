def secondMaxMin(arr,leng):
    max1 = arr[0]
    max2 = arr[0]
    min1 = arr[0]
    min2 = arr[0]
    for i in arr:
        if(i > max1):
            max1,i = i, max1
            if(max2 > max1):
                max1,max2 = max2,max1
        if(i < min2):
            min1, i = min1, i
            if(min1 < min2):
                min1,min2 = min2, min1
    print(f"2nd max is {max2} and 2nd min is {min2}")
def main():
    arr = [3,2,5,2,1,7]
    secondMaxMin((arr),len(arr))


main()
