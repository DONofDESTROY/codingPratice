# def alternateSort(arr):
#     i = 1
#     resArr = []
#     while(len(arr)>0):
#         if(not i%2==0):
#             maximum = max(arr)
#             arr.remove(maximum)
#             resArr.append(maximum)
#         else:
#             minimum = min(arr)
#             arr.remove(minimum)
#             resArr.append(minimum)
#         i+=1
#     return resArr

def alternateSort(arr):
    pass
        

def main():
    arr = [1, 2, 3, 4, 5, 6, 7]
    print("before Sorting")
    print(arr)
    alternateSorted = alternateSort(arr)
    print("sorting")
    print(alternateSorted)

main()
