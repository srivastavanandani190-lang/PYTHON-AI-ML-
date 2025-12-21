count=1
while count<=5:
    print("HELLO")
    count=count+1

#1 to 100 number
i=1
while i<=100:
     print(i)
     i=i+1

# 100 to 1 number
j=100
while j>=0:
     print(j)
     j=j-1

#table of n
num=int(input("Enter num:"))
k=1
while k<=10:
     print(k*num)
     k=k+1     

#list in loop
list=[1,4,9,16,25,36,49,64,81,100]
m=0
while m<=9:
     print(list[m])
     m=m+1

heroes=["batman","superman","thor","siperman"]
idx=0
while idx<len(heroes):
     print(heroes[idx])
     idx=idx+1

 #searching element
tup=(1,4,9,16,25,36,49,64,81,100)
search=25
idx1=0
while idx1<len(tup):
     if(tup[idx1] == search):
          print("found at ",idx1)
          break
     else:
          print("not found")
     idx1=idx1+1

#continue
u=0
while u<=9:
     if(u==6):
          u=u+1
          continue
     print(u)
     u=u+1

#sum a natural number
a=int(input("enter a:"))
v=0
sum=0
while(v<=a):
     sum=sum+v
     v=v+1
print(sum)

#factorial 
b=int(input("enter b:"))
product=1
q=1
while(q<=b):
     product=product*q
     q=q+1
print(product)     



