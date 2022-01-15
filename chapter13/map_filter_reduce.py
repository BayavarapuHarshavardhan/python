from functools import reduce
double=lambda y: 2*y
list1 = [4,6,9,3,6,69,3,45,6,5,2,5]
h = map(double,list1)
print(list(h))
even = lambda y: y%2==0
j = filter(even,list1)
print(list(j))
sum = lambda x,y:x+y
list2 =[1,6,4,3]
k =reduce(sum,list2)
print(k)