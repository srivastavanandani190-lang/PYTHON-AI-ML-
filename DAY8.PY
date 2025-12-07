#FILE HANDLING IN PYTHON!
import os
file=open("python.txt","r")
data=file.read()
print("Data of file:",data)
data=data.lower()
if "honey" in data:
    print("Yes honey is present in file.")
else:
    print("Not present")
file.close()    

file=open("report.txt","w")
file.write("Hello world.")
file=open("report.txt","a")
file.write("\nlet's learn python!")
file.close()

with open("report.txt","r") as f:
    line1=f.readline()
    line2=f.readline()#sequentially every line at last returns empty.

    print("line1:",line1)
    print("line2:",line2)

with open("report.txt","r") as f:
    lines=f.readlines()#list of all lines.
    print("line1:",lines)
    print(len(lines))

os.rename("python.txt","language.txt")
#os.remove("report.txt")
#try and except