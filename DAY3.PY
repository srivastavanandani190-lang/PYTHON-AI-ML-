#Assi-3
#SMART TEMPERATURE CONVERTER
celcius=float(input("Enter temperature in degree celcius:"))
kelvin=celcius+273.15
fahrenheit=((celcius*9.0)/5)+32
print("Temperature in Kelvin:",kelvin)
print("Temperature in Fahrenheit:",fahrenheit)
#lecture->3
str1='Hello'
str2="World"
str3='''Welcome to Python Coding'''
print(str1)
print(str2)
print(str3)
#concatenation
print(str1+" "+str2+" "+str3)
#length of string
print(len(str2)) 

name=input("Enter name:")
print("First character of name->",name[0])
print("Last character of name->",name[6])
print("Length of name string->",len(name))

#slicing
a='Honey'
print(a[0:5])
print(a[-1:-6:-1])

color=input("Enter color:")
mid=len(color)//2
print(color[mid-1:mid+2])
#method
sen=input("Enter Statement:")
print(sen.lower())
print(sen.replace(" ","_"))
#formatted string
n="Nandani"
age=20
print(f"My name is {n} and I am {age} year old")

print("Goodmorning")
print("Good \n morning")
print("Good \t morning")