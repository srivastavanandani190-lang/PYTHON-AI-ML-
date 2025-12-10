#class creation
class Vehicle:
    color="black"#attributes variables inside class
    petrolOrDiesel="petrol"
    mileage="10"
    #functions in classes is called methods
    def start(self):
        print("Vehicle started!")
#object creation
car=Vehicle()
print(car.color)
car.start()
bike=Vehicle()
print(bike.petrolOrDiesel)
aeroplane=Vehicle()
print(aeroplane.mileage)#access common attributes for all objects!

class car:
    brand="scorpio"
obj=car()
print(obj.brand)    

class laptop:
    brand="ASUS"
    RAM="8GB"
    price=74000
lap1=laptop()#object attributes>class attributes!
lap1.brand="victus"
lap2=laptop()
lap2.price=80000
print("laptop1 brand:",lap1.brand)
print("laptop1 price:",lap1.price)    
print("laptop2 brand:",lap2.brand)
print("laptop2 price:",lap2.price)    

#constructor
class student:
    schoolname="GEMS"
    def __init__(self, name,course):
        #self->object's location(whichever object you pass)
        self.name=name#linking with object!
        self.course=course
        print("Constructor is called automatically!")
        print(self.name)
        print(self.course)
student1=student("honey","M.Tech")
# print(student1.schoolname)
student2=student("anjali","B.Tech")   

class Student:
    # @staticmethod
    def __init__(self,name ,listofmarks):
        self.name=name
        self.listofmarks=listofmarks
    def average(self):
        sum=0
        for eachvalue in self.listofmarks:
            sum+=eachvalue
        average=sum/3
        print("Average is:",average)
stu1=Student("Aditya",[99,98,96])
stu1.average()
        
#four pillar of oops->1.Encapsulation(data+methods) 2.Abstraction(shows essential) 
#3.Polymorphism(same function different action) 4.Inheritance(property of parent class used by child)
class Account:
     def __init__(self, acc_no, balance):
       self.acc_no = acc_no
       self.balance = balance
     def credit(self, amount):
       self.balance += amount
       print("Amount credited:", amount)
     def debit(self, amount):
      if amount <= self.balance:
       self.balance -= amount
       print("Amount debited:", amount)
      else:
       print("Insufficient funds")
     def show_balance(self):
      print("Account:", self.acc_no, "| Balance:", self.balance)

a1 = Account("SAU123", 5000)
a1.credit(2000)
a1.debit(1500)
a1.show_balance()

class payment:
   @staticmethod
   def __init__():
      print("successful payment!")
transaction=payment()   
