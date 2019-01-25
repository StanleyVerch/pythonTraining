# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 16:27:49 2019

@author: Stanley
"""

import csv

with open('Tutorial_013_names.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)
    print(csv_reader)
    for line in csv_reader:
        print(line)

print("\n\nlist2")
with open('Tutorial_013_names.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    for line in csv_reader:
        print(line)
        
print("\n\nlist3")
with open('Tutorial_013_names.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file)
    with open('Tutorial_013_new_names.csv','w',newline='') as new_file:
        csv_writer = csv.writer(new_file, delimiter='\t')
        for line in csv_reader:
            csv_writer.writerow(line)

print("\n\nlist4")
with open('Tutorial_013_new_names.csv','r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')
    print(csv_reader)
    for line in csv_reader:
        print(line)

print("\n\nlist5")
with open('Tutorial_013_new_names.csv','r') as csv_file:
    csv_reader = csv.DictReader(csv_file,   delimiter='\t')
    for line in csv_reader:
        print(line)
        print(line['email'])
        
print("\n\nlist6")
with open('Tutorial_013_names.csv','r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    with open('Tutorial_013_new_names.csv','w',newline='') as new_file:
        fieldnames =['first_name','last_name', 'email']
        csv_writer = csv.DictWriter(new_file,fieldnames=fieldnames)
        csv_writer.writeheader()
        for line in csv_reader:
            csv_writer.writerow(line)

print("\n\nlist7")
with open('Tutorial_013_names.csv','r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    with open('Tutorial_013_new_names2.csv','w',newline='') as new_file:
        fieldnames =['first_name','last_name']
        csv_writer = csv.DictWriter(new_file,fieldnames=fieldnames)
        csv_writer.writeheader()
        for line in csv_reader:
            del line['email']
            csv_writer.writerow(line)
