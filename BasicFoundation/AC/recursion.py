#recursive function.
def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)
    #print("end")
show(5)
show(2)    
#factorial
def fac(num):
    if(num==0 or num==1):
        return 1
    else:
        return num*fac(num-1)
print(fac(6))
#sum of natural number
def sum(n):
    if(n==1):
        return 1
    else:
        return n+sum(n-1)
print(sum(5))        

#lists using recursion
fruits=["mango","apple","guava","orange","litchi","strawberry"]
def printlist(list,index):
    if(index==len(list)):
        return 
    else:
        print(list[index])
printlist(fruits,1)