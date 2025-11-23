#Conditional Statements(if,if-else,if-elif-else)
age=int(input("Enter Your Age:"))
if age>=18:
    print("Eligible to Vote")
else:
    print("Not Eligible to Vote")  

num=int(input("Enter number:"))
if num>0:
    print("Positive Number")
elif num==0:
    print("ZERO")
else:
    print("Negative Number")     

#Lists(heterogeneous,mutable,complex datatype)
fruits=['Mango','Apple','Guava','Strawberry','Banana','Litchi']
print(type(fruits))
print("NUMBER OF fruits:",len(fruits))
print("first fruit:",fruits[0])
print(fruits[0:4])
fruits[0]='Orange'
print(fruits)

f1=input("enter first food:")
f2=input("enter second food:")
f3=input("enter third food:")
foodlist=[]
foodlist.append(f1)
foodlist.append(f2)
foodlist.append(f3)
print(type(foodlist))
print("Number of food you like:",len(foodlist))
print("food you like:",foodlist)

#Tuple(heterogeneous,immutable,complex datatype)
marks=(90,96,98,97,96,100)
print(type(marks))
print("Marks:",marks)
print(marks[0])
print("Number of occurence of 96:",marks.count(96))
print("Index of 98:",marks.index(98))
print("Maximum marks:",max(marks))
print("Minimum marks:",min(marks))