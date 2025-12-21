#works in pair
info={
    "name":"apna college","subjects":["python","c","java"],
    "topics":("dict","set"),
    "age":35,
    "is_adult":True,
    15:23.2
}
print(info)
print(type(info))
print(info["name"])
info["name"]="nandani"
#print(info)
info["age"]="twenty"
print(info)

student={"name":"honey","subjects":{
    "phy":89,"chem":99,"math":98
}}
#nested dictionary
print(student["subjects"]["chem"])
print((student.keys()))
print(list(student.keys()))
print((student.values()))
print(list(student.values()))
print(tuple(student.values()))