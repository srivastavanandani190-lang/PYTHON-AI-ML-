def sum(a=7,b=9):
    s=a+b
    return s
print(sum(5,6))
print(sum())
print(sum(6))
print(sum(5))

#average of number
def avg(a,b,c):
    ave=(a+b+c)/3
    print(ave)
    return ave
avg(1,3,5)
avg(5,9,6)

#lists using functions
cities=["delhi","bombay","lucknow","hyderabad","noida","newyork"]
chocolates=["dairymilk","kitkat","munch","park","sneakers"]
def length(list):
  print(len(list))

length(cities)
length(chocolates)

def display(list):
   for i in list:
      print(i,end=" ")

display(cities)
display(chocolates)   
print("\n")
#factorial
num=int(input("enter the num:"))
def fAC(n):
   product=1
   for i in range(1,n+1):
      product=product*i
   print(product)
   return product
fAC(num)
# odd and even
numb=int(input("enter the number:"))
def nature(n):
   if(n%2==0):
      print("EVEN")
   else:
      print("ODD")
nature(numb)         
