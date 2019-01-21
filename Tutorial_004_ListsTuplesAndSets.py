# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 08:09:51 2019

@author: Stanley
"""

# Mutable
list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1

print(list_1)
print(list_2)

list_1[0] = 'Art'

print(list_1[0])
print(list_1[-1])  # use -1 to find  last item in list

# :2 is the stopping point of the list stops at physucs but does not include it
print(list_1[0:2]) 
print(list_2)

list_2.append( 'Art')
print(list_2)

list_2.insert( 0,'Art History')
print(list_2)

list_3 = ['History', 'Math', 'Physics', 'CompSci']
list_4 = ['art', 'Education']
list_3.insert(0, list_4)
print("list3 insert", list_3)

list_3 = ['History', 'Math', 'Physics', 'CompSci']
list_4 = ['Art', 'Education']
list_3.extend( list_4)
print("list3 extend", list_3)

popped = list_3.pop()
print("popped", popped)
print("list3 pop", list_3)

list_3.reverse()
print("list3 reversed", list_3)

list_3.sort()
print("list3 sorted", list_3)

list_3.sort(reverse=True)
print("list3 Descending ", list_3)

sorted_list = sorted(list_1)
print("sorted_list ", sorted_list)

nums =[1,5,2,4,3]
print("Minimum ", min(nums))
print("Maximum ", max(nums))
print("sum ", sum(nums))

print("index of" ,list_3.index("CompSci"))
print("Find in list", 'Art1' in list_1)

for item in list_3:
    print("list value is ", item)

for index, item in enumerate(list_3):
    print("list value is at ", index, " for ", item)
    
for index, item in enumerate(list_3, start=1):
    print("list value is at ", index, " for ", item)

list_3str = ','.join(list_3)
print("comma Delimite",list_3str )

list_3split = list_3str.split(',')
print("string split into list   ",list_3split )


# Immutable
tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1

print("TUPLES")
print(tuple_1)
print(tuple_2)


# Sets  no duplicates in a set (does not conatain duplicates)
print("SETS")
cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
art_courses = {'History', 'Math', 'Art', 'Design'}


print(cs_courses)
print("intersection ", cs_courses.intersection(art_courses))
print("difference ", cs_courses.difference(art_courses))
print("union ", cs_courses.union(art_courses))



# Empty Lists
empty_list = []
empty_list = list()

# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

# Empty Sets
empty_set = {} # This isn't right! It's a dict
empty_set = set()