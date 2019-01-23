# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 08:07:21 2019

@author: Stanley
"""
import Tutorial_009_MyModule as myMod

from Tutorial_009_MyModule import find_index
import sys
import random
import math
import datetime
import calendar
import os

courses = ['History', 'Math', 'Physics', 'CompSci']


index = find_index(courses,'Math')

if index >= 0:
    print("Course found at index ", index)
else:
    print("Course not found ")

index = myMod.find_index(courses,'Math2')

if index >= 0:
    print("Course found at index ", index)
else:
    print("Course not found")
    
print(sys.path)

random_course = random.choice(courses)
print(random_course)

rads = math.radians(90)
print(rads)
print(math.sin(rads))

today = datetime.date.today();
print(today)
print(calendar.isleap(2018))
print(calendar.isleap(2020))


print(os.getcwd())
print(os.__file__)