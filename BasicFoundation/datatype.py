#python2 vs python3
#(3/2=1 vs 3/2=1.5)
#collection , collection+list compression
#print"",print("")
#xrange(),range()
# 2000 ,2008
#raw_input(),input()

#datatypes
x=4
y=4.5
z="hello"
v=True
b=3+4j
n='y'
print(type(x))
print(type(y))
print(type(z))
print(type(v))
print(type(b))
print(type(n))
print(id(x))
print(id(y))
print(id(z))
print(id(v))
print(id(b))
print(id(n))
#type conversion
#implicit indirect conversion interpreter itself convert one type of data to another once operation is performed(higher datatype)
x=16.6
y=8
z=x+y
print(z)
#explicit conversion user convert it into required datatype.(valid number should be their in string for conversion.)
a="25"
b=5
c=int(a)
print(b+c)
m=13
n=3
o=int(m/n)
print(o)
#question 
q=12.4
w=20
e='123.45'
print(int(q),complex(w),float(e))

#basic input(string by default) output function(sum)
#print(value, sep='character',end='\n')
h=89.65
g=55
print("sum of g and h:",h+g)
r=float(input("enter r:"))
t=int(input("enter t:"))
print("sum of r and t:",r+t)

#question
z=12
s=23.5
f='ABSEC'
print(z,s,f,sep='\n')
#print(f,sep='\n')
