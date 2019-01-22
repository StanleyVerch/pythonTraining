# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 10:03:12 2019

@author: Stanley
"""

def hello_func():
    pass   #shell function needs to be filled in later
    
def hello_func2():
    print("Hello me")
   
def hello_func3():
    return "Hello Me"

print(hello_func)
print(hello_func())

 
hello_func2()


def hello_func4(greeting, name =""):
    return f"{greeting} {name}"

   
print("\nfunction return value")
      
for i in range(3):
    print(hello_func3())
 
print(hello_func3().upper())
print(hello_func4("Good Day!"))
print(hello_func4("Good Day!","Mate"))



def student_info(*args, **kwargs):
    print(args)
    print(kwargs)
 
student_info('math', 'art', name='John', age=22)  

courses = ['math', 'art']
info = {'name':'John', 'age':22}
print("\nStudent info")
       
student_info(courses, info)
student_info(*courses, **info)


# Number of days per month. First value placeholder for indexing purposes.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
    """Return True for leap years, False for non-leap years."""

    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    """Return number of days in that month in that year."""

    # year 2017
    # month 2
    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]

print(days_in_month(2004, 2))