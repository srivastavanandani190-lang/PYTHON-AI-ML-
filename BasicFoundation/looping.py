#for loop(to iterate certain block of code)
#RANGE(1,10)->ONE TO NINE SEQUENCE(start,stop,step) by default step=1
x=int(input("enter x:"))
y=int(input("enter y:"))
print("even number")
for a in range(x,y+1,2):
    print(a,end="\n")
print("odd number")    
for b in range(x+1,y,2):
    print(b,end="\n")    
print("using while loop")    
while(x<=y):
    print(x)
    x=x+2

#sum of n natural number.
num=int(input("enter num:"))
sum=0
for i in range(1,num+1):
    sum=sum+i
print(sum)

#loop over strings
for j in "hello":
    print(j,end="")

#tuple
for k in (1,2):
    print(k)

#list
for l in [1,2,3]:
    print(l)

#set
for s in {1,2,3,4}:
    print(s)

#dictionary
for d in{'A':'a','B':'b','C':'c'}:
    print(d)    

#sum using list
sum1=0
for z in[1,2,3,4]:
    sum1=sum1+z
print(sum1)    



