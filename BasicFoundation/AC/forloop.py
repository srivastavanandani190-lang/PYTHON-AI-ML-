str="nandani"
for i in str:
    print(i)
else:
    print("end")


list=[1,4,9,16,25,36,49,64,81,100]
for el in list:
    print(el)    


list1=(1,4,9,16,25,36,49,64,81,100,49,49)
xy=49
index=0
for ele in list1:
    if(ele == xy):
        print("yes found at index:",index)
        break
    index=index+1
    
#range 
for t in range(2,10,2):
    print(t)

#print 1 to 100
for j in range(1,101):
    print(j)

#print 100 to 1
for k in range(100,0,-1):
    print(k)

#table
num=int(input("enter num:"))
for l in range(1,11):
    print(num*l)

#sum of n natural number
m=int(input("enter m:"))
sum=0
for r in range(1,m+1):
    sum=sum+r
print("SUM OF m NATURAL NUMBER:",sum)

#factorial
z=int(input("enter z:"))
product=1
for p in range(1,z+1):
    product=product*p
print("FACTORIAL OF z:",product)   

#pass use
for x in range(10):
    pass
#in future you may use this loop.
print("useful work")
