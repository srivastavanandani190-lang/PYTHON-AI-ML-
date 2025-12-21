dictionary={"cat":"animal","table":{"wooden","fibre","steel"}}
print(dictionary)
#mutable elements ke case me koi bhi ayasakta hai either tuple,list or set

marks={}
x=int(input("enter dsa:"))
marks.update({"dsa":x})
x=int(input("enter coa:"))
marks.update({"coa":x})
x=int(input("enter python :"))
marks.update({"python":x})
x=int(input("enter dstl:"))
marks.update({"dstl":x})
print(marks)

sub={"python","c++","python","c++","c","java","c++","java","c++","c","python"}
print(sub)

values={9,9.0,9.25,8}
print(values)

value={("float",9.0),("int",9)}
print(value)
