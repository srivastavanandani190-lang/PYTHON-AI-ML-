students=["muskan","anjali","nilakshi","nandani","navya"]
print(students)
print(type(students))
print(id(students))
print(len(students))

#mutable
students[3]="honey"
print(students)
print(len(students))

#slicing
print(students[1:3])
print(students[:3])
print(students[:])
print(students[1:])
print(students[:-1])

#list methods
list=[94,99,91,93,88,90]
list.append(99) # add at end.
print(list)
list.sort() #arranged  in ascending order
print(list)
list.sort(reverse=True) #descending
print(list)
list.reverse()
print(list)
list.insert(2,93) # add elements
print(list)
list.remove(91) #remove elements
print(list)
list.pop(3)  #remove element at that index
print(list)
#for strings
fruits=["mango","apple","litchi","guava","strawberry","banana"]
fruits.sort()
print(fruits)
fruits.reverse()
print(fruits)
