#Dictionary(key-value pair,complex datatype)
student={
    'name':'Nandani','degree':'B.Tech','age':20
}
print(type(student))
print(len(student))
print("NAME:",student['name'])
print("AGE:",student.get('age'))
student['CGPA']=9.59
print(student)
#tuple(list)
print("KEYS:",student.keys())
print("Values:",student.values())
print("Key-Value pair:",student.items())
print("\n")

marks={}
print(type(marks))
marks['Maths']=99
marks['Physic']=98
marks['Chemistry']=97
marks['Biology']=96
marks['computer']=95
print("Marks of respective subjects:",marks)
print("\n")

#Sets(immutable(frozen-set),unordered,unique,no repetition)
language={'C++','C','PYTHON','JAVASCRIPT','C','C++','C'}
print(type(language))
print("Languages:",language)
print("Number of languages:",len(language))
language.add('MongoDB')
language.remove('C')
print("Modified Languages:",language)
print("\n")

#List to Set
List1=[12,13,14,15]
Set1=set(List1)
print(type(List1))
print(type(Set1))
print("SETS:",Set1)
print("Number of element in set:",len(Set1))