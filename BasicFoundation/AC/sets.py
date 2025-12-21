collection=set()
collection.add(1)
collection.add(2)
collection.add(2)
collection.add(8)
collection.add(9)
print(collection)

set1={(1,2,3),12,6,5}
'''just tuple because sets elements are immutable and set 
is mutable you can add value later using add function.'''
print(set1)
set2={23,24,25,26,27}
set3={26,27,28,29}
print(set2.union(set3))
print(set2.intersection(set3))
