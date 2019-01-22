# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 09:08:50 2019

@author: Stanley
"""

nums = [1,2,3,4,5]

for num in nums:
    print(num, "", end="")

print("\n\nbreak")
for num in nums:
    if num == 3:
        print("FOUND", end="")
        break
    print(num, end="")

print("\n\ncontinue")
for num in nums:
    if num == 3:
        print("FOUND ", end="")
        continue # do not print 3
    print(f"{num} ", end="")

print("\n\ninner loops")
for num in nums:
    for letter in "abc":
        message = f"{num}{letter},"
        print(message, end="" )

print("\n\nrange loop1 0-9")
for i in range(10):
    print(i, "", end="")

print("\n\nrange loop2 1-10")
for i in range(1,11):
    print(i, "", end="")    


print("\n\nwhile loops")

x = 0
while x < 10:
    print(f"{x},", end="")
    x += 1
