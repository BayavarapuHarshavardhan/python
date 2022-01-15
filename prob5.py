from functools import reduce
def max(m,n):
    if m>n:
        return m
    else :
        return n    
a = [1,525,6,8,9,10,18,56,93]
maxnum = reduce(max,a)
print(maxnum)