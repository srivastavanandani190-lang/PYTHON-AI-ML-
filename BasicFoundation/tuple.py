#tuble is an immutable,duplicate element are allowed ,slicing ,sequence , hetrogeneous, indexing oredered
# t=(1,) # to create single value tuple
# x=1,2,3,4
# print(x) # by default it create a tuple
# z=(1,) #z=(1) type is int
# y=("hello",)  #y=("hello")
# print(type(z))
# print(type(y))
#wap to unpack elemnet in tuple
#unpacking is called when the multiple variable is assigned to a tuple then variable take the corresponding value
#print(a,*b,c=x)
t=(1,2,3,5,5,8,9,5)
t1=(11,12,15)
a=t.count(5)
b=t.index(5)
print(a)
print(b)
print(t+t1)
#create a tuple of weekdays and print those with len greater than three.
t3=("mon","tue","wed","thus","fri","sat")
for i in t3:
    if(len(i)==4):
        res=i
print(res)        
#create a tuple of different data type members and check the frequency of each member
t4=(4.1,12,"hello","hii","hello",4.1,52,56,52,58,52,4.1)
for i in t4:
    count=t4.count(i)
    print(count)
print("\n")    
#wap to join two input tuple ikf their first element is common
t5=(1,2,5)
t6=(1,8,9)
if(t5[0]==t6[0]):
    print(t5+t6)
else:
    print("no")    