X=["hello","12", 456]
X[0]*=3
#X[2][1]="bye"
print(X[0])
print(X[2])

a=3
b=5
c=10
x= int(a&b<<2//5**2+c^b)
y= int(b>>a**2<<2 >> b**2^c**3)
print(x)
print(y)
print(5>>9<<2>>25^1000)


m,n,o,p=[eval(x) for x in input("Enter 4 values:").split(":")]
print("values of m,n,o,p:",m,n,o,p)