#Expense Tracker
expenses=[]
print("Welcome to Expense Tracker")
while True:
    print("===Menu===")
    print("1.Add Expenses!")
    print("2.View All Expenses!")
    print("3.View Total Expenses!")
    print("4.Exit!")
    choice=int(input("Enter Your Choice:"))

    if(choice==1):
        date=input("Enter Date:")
        Category=input("Type of Expense:")
        description=input("About items:")
        amount=int(input("Enter the Amount:"))
        expense={'date':date,'category':Category,'description':description,'amount':amount}
        expenses.append(expense)
        print("\nExpenses added successfully")

    elif(choice==2):
        if(len(expenses)==0):
            print("Please add your expenses!")
        else:
            print("Your expenses are:")
            count=1
            for item in expenses:
                print(f"{count}:{item['date']},{item['category']},{item['description']},{item['amount']}")        
            count=count+1 

    elif(choice==3):
        total=0
        for items in expenses:
            total=total+items['amount']
        print("\nTotal Expenses=",total)

    elif(choice==4):
        print("Thank You!")
        break

    else:
        print("Invalid Choice")                