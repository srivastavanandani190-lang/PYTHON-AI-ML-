#Loops in Python
i=1
while i<=10:
    print(i)
    i=i+1

j=10
while j>=1:
    print(j)
    j-=1
       
num=1
while(num<=50):
    if(num%2==0):
        print(num)
    num=num+1

n=int(input("Enter the number:"))
i,sum=0,0
while i<=n:
    sum=sum+i
    i=i+1
print("Sum:",sum)

m=int(input("Enter the number:"))
k=1
while(k<=m):
    print("*"*k)
    k=k+1

num2=int(input("Enter the number:"))
i=1
while(i<=10):
    print(f"{num2}*{i}={num2*i}")
    i=i+1

foodlist=['cake','ice-cream','pizza']
for i in foodlist:
    print(i)

for j in range(2,21,2):
    print(j)

for k in range(1,10):
    if i==5:
        break
    print(k)
