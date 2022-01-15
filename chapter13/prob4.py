l1=[5,10,22,15,25,36,42,45,50,60]
b = lambda x: x%5==0
a = filter(b,l1)
print(list(a))