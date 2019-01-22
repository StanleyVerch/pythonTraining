# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 08:11:57 2019

@author: Stanley
"""

# Comparisons:
# Equal:            ==
# Not Equal:        !=
# Greater Than:     >
# Less Than:        <
# Greater or Equal: >=
# Less or Equal:    <=
# Object Identity:  is


# False Values:
    # False
    # None
    # Zero of any numeric type
    # Any empty sequence. For example, '', (), [].
# Any empty mapping. For example, {}.



if True:
    print('Evaluated to True')
else:
    print('Evaluated to False')
    
language = 'Python'

if language == 'Python':
    print("language is Python")
else:
    print('language is not Python')
    
language = 'Java'

if language == 'Python':
    print("language is Python")
else:
    print('language is not Python')
    
    
language = 'Java'

if language == 'Python':
    print("language is Python")
elif language == 'Java':
    print('language is Java')
else:
    print('no matches')
    
user = 'Admin'
logged_in = True

if user == 'Admin'  and logged_in :
    print("Administrators Page ")
else:
    print("Bad creditials")


user = 'Admin'
logged_in = True

if not logged_in :
    print("Please log in")
else:
    print("welcome")

a = [1,2,3]
b = [1,2,3]

print("list a " , a, " list id ", id(a))
print("list b " , b, " list id ", id(b))
print ("a == b gives ", a == b)
print ("a is b gives ", a is b)


a = [1,2,3]
b = a

print("list a " , a, " list id ", id(a))
print("list b " , b, " list id ", id(b))
print ("a == b gives ", a == b)
print ("a is b gives ", a is b)