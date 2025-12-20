#ARITHMETIC OPERATOR
a=256
b=5
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)#just int value
print(a**b)
print(a%b)
c="hello"
d="honey"
print(c+d)
print("c"*5)#replicate the string.
print(3*5)
print("30"*2)
e=input("enter e:")
f=input("enter f:")
print(e+f)#concatinate
g=int(input("enter g:"))
h=int(input("enter h:"))
print(g+h)

#COMPARISON OPERATOR
i=56
j=89
print(i>j)
print(i<j)
print(i==j)#compares the value
print(i!=j)
print(i>=j)
print(i<=j)

#bitwise operator
m=9
n=3
print(m&n)
print(m|n)
print(m^n)
print(m<<1)
print(m>>1)
print(m!=n)


#logical operator
k=234
l=562
print(k>l or k==l)
print(k<l and k!=l)

#assignment operator(=(is-to compare memory address),==(to check values))
#identity(is operator ,is not operator) and membership operator(in operator ,not in operator)

list=[1,2,5,7,9]
print(4 in list)
print(7 in list)
print(4 not in list)
print(9 not in list)

o=5
p=o
print(p is o)
print(p is not o)

#PRECEDENCE(priority of operator) AND ASSOCIATIVITY(L-R)
#(),**,*/,+-,<< >>,!=,< > <= 