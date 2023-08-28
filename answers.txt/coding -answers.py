
4)
array=[1, 1, 1, 2, 2, 3, 4, 5, 5]

b=set(array)
array=list(b)

print(array)




6)

a,b=[1, 3, 5], [2, 4]

array=a+b
n=len(array)


for i in range(0,n-1):
    if (array[i] > array[i+1]):
         array[i+1],array[i]=array[i],array[i+1]
         

for i in range(0,n):
     print(array[i])




or

array=sorted(array)
print(array)

