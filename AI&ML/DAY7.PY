#functions(block of reusable code)

def greet():
    print("Hello! Honey")
greet()

def sum():
    a=8
    b=9
    sum=a+b
    print("sum:",sum)
sum()

def welcomemssg():
    print("Welcome to Python Programming!")
welcomemssg()

def inspire():
    print("You are the master of Your Destiny")
inspire()

def average(a,b):
    averagevalue=(a+b)/2
    print("Average:",averagevalue)
average(5,12)
average(56,5)
average(4,4)

def show_age(name="Nandani",age=20):
    print(f"{name} is {age} years old")
show_age("Honey",20)
show_age()
show_age("Muskan",20)

def multiply(a=10,b=30):
    return a*b
result=multiply(5,10)
print("multiplication of two number:",result)

def square(num=10):
    return num**2
print("Square:",square(6))

def countfunc(userinput):
    vowels="aeiouAEIOU"
    countvowel=0
    countconsonant=0
    for eachchar in userinput:
        if(eachchar.isalpha()):
            if(eachchar in vowels):
                countvowel+=1
            else:
                countconsonant+=1
    return countvowel , countconsonant
vowels,consonants=countfunc("Nandani Srivastava")
print(vowels,consonants)                