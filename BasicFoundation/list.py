# list->[],empty list->[]orlist(),heterogeneous element's collection,concatinate,
# class type:list,ordered sequence(EOL),mutable(modification allowed),indexing(+,-),
# slicing,duplicacy.

li1=['hello',12.5,True,None]
l=list([1,2,3,'hii'])
print(l[0:2])
print(li1[-3:-1])

li=['Apple','Name',12.5,13,None,True,2+3j]
print(li[:])
print(li[0:3])#first three elements 
print(li[::-1])#reverse
li[0]='hello'#updation
print(li[:])

x=['xy','yz']
for i in x:
    i.upper()#no change function of string.
    #not saved hence no change observed.
print(x)#original form 

x=['xy','yz']
for i in x:
    x=i.upper()
    print(x,end=" ")#original form 


lis=list(input("\nenter list:"))
for i in lis:
    print(i,end="")


# method for particular object type
# function is independent of class type

l1=["h","g","k","l","m"]
l1.insert(2,9) #insert(index,element)
l1.append("q")# add at last position
l1[2]=10 #overwrite data loss
del l1[2]# index
l1.remove("g")# element
del l1
print(l1)


# wap to find maximum and second maximum member in list.
list=[12,21,56,56,23,21,15,14,15,96,59]
max=list[0]
sec=list[0]
for i in list:
    if max<i:
        max=i
for j in list:
    if sec>i and sec<max:
        sec=i        
print(max)  
print(sec)      
# functions-> len(l1),max(l2),min(l1),list(tuple)
# method->l1.pop(),l1.count(),l1.sort(),l1.sort(reverse=True)
print(max(list))
print(min(list))
print(len(list))
list.pop(2)
print(list)
list.sort()
print(list)
for i in list:
   print(list.count(i),end=" ")
list.sort (reverse=True)
print("\n",list)

l3=[1,2,3,4,5]
l4=[6,9,7,8]
l3=l3+l4
print(l3)
print(l4*3)
#write thr difference between append ()and insert()
#write a program to swap elements in the list
n=int(input("Enter the index first"))
m=int(input("enter the index"))
temp=l3[n]
l3[n]=l3[m]
l3[m]=temp
print(l3)
numbers = input("Enter a list of integers separated by spaces: ")
num_list = [int(x) for x in numbers.split()]
total = 0
for num in num_list:
    total = total + num
print("The sum of the numbers is:", total)
print("Average of the numbers is : ",total/len(num_list))

#wap to remove duplicate from the list.
numbers = input("Enter a list of integers separated by spaces: ")
num_list = [int(x) for x in numbers.split()]
total = 0
l2=[]
for i in num_list:
    if i not in l2:
        l2.append(i)
print(l2)        
#wap to print all positive number in list.
numbers = input("Enter a list of integers separated by spaces: ")
num_list = [int(x) for x in numbers.split()]
total = 0
l2=[]
for i in num_list:
    if i>0:
        l2.append(i)
print(l2)        
#wap to count positive ,negative and string type element.

numbers = input("Enter a list of integers separated by spaces: ")
num_list = [int(x) for x in numbers.split()]
total = 0
t1=0
s=0
for i in num_list:
    if i>0:
        total=total+1
    elif i<0: 
           
         t1=t1+1
    else:
        
        s=s+1    
    

