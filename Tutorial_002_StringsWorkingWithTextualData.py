# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 11:01:29 2019

@author: Stanley
"""

message = "Hello World"
message2 = "Bobby's World"
message3 = 'Bobby\'s World'
message4 = """Bobby's World was a
good cartoon in the 1990's """
print(message)
print(message2)
print(message3)
print(message4)
print(len(message))
print(message[0])
print(message[10])
print(message[0:5])
print(message[:5])
print(message[6:])
print(message.lower())
print(message.count('Hello'))
print(message.count('l'))
print(message.find('World'))

message.replace('World','universe')
print(message)

message = message.replace('World','universe')
print(message)

greeting = "Hello"
name = "Michael"
message =  greeting + ", "+ name + ". Welcome!"
print(message)

message = "{}, {}. Welcome!".format(greeting, name)
print(message)

message = f"{greeting}, {name}. Welcome!"
print(message)


message = f"{greeting}, {name.upper()}. Welcome!"
print(message)

# to display all methods of a variable

print(dir(name))

print(help(str))
print(help(str.lower))
