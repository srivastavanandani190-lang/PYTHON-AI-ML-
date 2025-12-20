# str1="helloworld"
# for i in range(len(str1)):
#     print(str1[i],end="")
# #empty string.
# #string slicing.
# #start,stop,step.
# print("\n")
# print(str1[:5])

# str2="ABES ENGINEERING COLLEGE"
# print(str2[5:16])
# print(str2[: :-1])
# print(str2[3:5])
# print(str2[1:len(str2):2])
# print(str2[10:2:-1])
# print(str2[-11:-7])
# #try except 
# mssg="welcome to mysore"
# word=mssg[-7:]
# if(word=="mysore"):
#     print("got it")
# else:
#     mssg=mssg[3:14]
#     print(mssg)    
# print("abes">"aktu")
# print("aktu"<"abes")       

# s1="hellohow"
# for i in range(len(s1)):#total iteratrion=8 a will be printed 7 times
#     print(s1,end="")
#     s1="a"

# #concatination+
# #repetition*
# #in operator(member present or not)

#vowels 
# s=input("enter string:")
#if('a' in s or 'e' in s or 'i' in s or 'o' in s or 'u' in s):
#     print("yes")
# else :
#     print("no")  

#pallindrome
# s1=input("enter pallindrome:")
# if(s1==s1[::-1]):
#         print("yes")
# else:
#         print("no") 

#class vs object
#methods of string
#del s1
# functionlen(s1) 
# s1.method(dot operator)   
# s1=s1.capitalize()just 1 letter of first word
# s1=s1.title()1 letter of every word
# s1=s1.casefold()lowercase each letter
#s1=s1.count('o') counts the letter or substrings
#s2.endswith('h') startswith

# s1="helloWorld is first"
# print(s1)
# s1=s1.capitalize()
# print(s1)
# s1=s1.title()
# print(s1)
# s1=s1.casefold()
# print(s1)
# s1=s1.count('o')
# print(s1)

# s2=input("enter email:")
# print(s2.endswith('com'))
# print(s2.endswith('edu'))


# s2=input("enter name:")
# if(s2.startswith('ms')):
#     print(s2)
# else:
#     print('ms'+s2)    

#val=10.8934
# print("In Float {0:f}".format(val))
# print("Two decimal point {0:.2f}".format(val))
# val=10
# print("In Binary {0:b}".format(val))
# print("{0} and {1}")
# print("{fname} and {sname}  play football".format(fname="Bob",sname="Ram"))
# fname="Bob"
# sname="RAM"
# print(f"{fname} and {sname} play football")
# t="twinkel twinkel little "
# s="*"
# print(f"{t}{s}")
# s="-"

# print(f"Good morning maddam {s} how are you")
# line="Hello How are you"
# L=line.split('a')
# for i in L:
#print(i,end='')

# example="ABES Engineering college" 
# print(example[::-1].startswith("A"))
# s="2bcs3ed"
# count=0
# for i in range(7):

n=input("enter password:")
def check_password(password):
    has_upper = False
    has_special = False
    special_chars = "!@#$%^&*()_+=-[]{};:,.<>?/|"

    for ch in password:
        if ch.isupper():
            has_upper = True
        if ch in special_chars:
            has_special = True
    if has_upper and has_special:
       
        print("Password is valid")
    else:
        print("Password is invalid")
check_password(n)


#string ->sequence,heterogeneous(any datatype),slicing,ordered,immutable,indexing,duplicacy is allowed,no modification/updation,empty string'',"",str().




 