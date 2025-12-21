age=21
if(age>=18):
    print("yes can vote")
else:
    print("no")


marks=int(input("MARKS:"))
if(marks>=90):
    print("A")
elif(marks>=80 and marks<90):
    print("B")
elif(marks>=70 and marks<80):
    print("C") 
else:
    print("D")      


num=int(input("number:"))
if(num%2==0):
    print("EVEN")
else:
    print("ODD")


a=int(input("a:"))
if(a%7==0):
    print("YES DIVISIBLE BY 7")
else:
    print("NOT DIVISIBLE")


m=int(input("m:"))
n=int(input("n:"))
o=int(input("o:"))
if(m>=n and m>=o):
    print("m")
elif(n>=m and n>=o):
    print("n") 
else:
    print("o")       