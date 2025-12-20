#Decision statement
#if statement ->if, else if, elif ,nested if.

#traffic light
light = "red"
if(light== "green"):
   print("go")
elif(light=="red"):
   print("stop")
else :
   print("light is broken")

 # one can vote or not
age=int(input("Enter your age"))
if(age>=18):
    print("can cast vote")
else :
    print("can not cast vote")

# number is positive or negative
num=int(input("Enter a number"))
if(num>0):
    print("positive")
elif(num==0):
    print("number is zero")
else:
    print("Negative")

#largest number between three number
a=2
b=5
c=9
if(a>b):
    if(a>c):
        print("a is largest",a)
    else:
        print("c is largest",c)
else:
    if(b>c):
        print("b is largest",b)
    else:
        print("c is largest",c)

#wap to mention the movie ticket price as per the age
age=int(input("Enter the age :"))
price1=120
price2=300
if(age<=18):
    print("price is ",price2)
else:
    print("price is",price1)

#to check the balance from atm
balance=float(input("Enter the balance"))
if(balance>=500):
    print("the balance is",balance)
else:
    print("insufficient balance")

# print Excellent if greater then 95 marks
marks=int(input("Enter the marks"))
if (marks>95):
   print("Excellent")
else:
   print("Not excellent")

# leap year or not
year=int(input("enter a year"))
if(year % 4==0 or year % 400==0  and year % 100!=0):
    print("year is leap year")
else:
    print("year is not leap year")

#snippets    
x=3
if x>2 or x<5 and x==6:
    print("ok")
else:
    print("no output")

#grades    
marks =int(input("Enter the marks"))
if(marks>=95):
    print("EXCELLENT")
elif( 95>marks and marks<=80):
    print("good")
elif(marks<80 and marks>=60):
    print("average")
else:
    print("below average")

#snippet
y=0.1*3
if y!=0.3:
    print("Launch a missile")
else:
    print("Let's have peace")
print(y)

x=3
if(x>2):
    x=x*2
if(x>4):
    x=0
print(x)
       
                 
      


