l1=[7]
a=[ a*i for a in l1 for i in range(1,11)]
      
str1=""
for item in a:
     str1 +=str(item)+"\n"
print(str1)