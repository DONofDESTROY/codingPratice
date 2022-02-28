from itertools import permutations
def largest(l):
    lst = []
    for i in permutations(l, len(l)):
        lst.append("".join(map(str,i))) 
    return max(lst)
  
print(largest([1, 34, 3, 98, 9, 76, 45, 4]))
