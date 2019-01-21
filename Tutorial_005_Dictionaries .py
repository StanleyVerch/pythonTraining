# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 13:37:31 2019

@author: Stanley
"""

student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
print(student)

print(student['name'])
print(student['courses'])

print(student.get('name'))

print(student.get('phone'))
print(student.get('phone','students do not have a  does not exist'))

student['phone']= '555-444-6666'
print(student.get('phone','students do not have a  does not exist'))

student.update({'name':'Jane','age':26,'phone':'555-444-6661'})
print(student)

     
del student['age']
print(student)

student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
student['phone']= '555-444-6666'
print(student.get('phone','students do not have a  does not exist'))

print(student)  

age = student.pop('age')
print(student) 
print(age)

# show number of keys
print(len(student))

# show  keys
print(student.keys())

# show  student values
print(student.values())

# show  student keys and values
print(student.items())

for key,values in student.items():
    print(key, values)  