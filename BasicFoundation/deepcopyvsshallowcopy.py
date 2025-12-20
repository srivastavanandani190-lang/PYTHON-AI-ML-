#DEEPCOPY SHALLOW COPY, DECORATOR
L1=[1,2,3,4]
L2=L1
print(L1,L2)
print(id(L1))
print(id(L2))
L2[1]=100
print(L1,L2)
L1[2]=200
print(L1,L2)
#same memory location

l3=[1,2,3,4]
l4=l3.copy()#shallow copy
print(id(l3))#different id 
print(id(l4))
l3[1]=500#no mutual change
print(l3)
print(l4)

#nested list
l5=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
l6=l5.copy()
print(id(l5))
print(id(l6))
l5[1][0]=45
print(l5)
print(l6)
print(id(l5[1][0]))#same address in nested list->shallow copy works for simple list but not for nested list.
print(id(l6[1][0]))