# -*- coding: utf-8 -*-
"""
Created on Thu Jan 24 07:46:49 2019

@author: Stanley
"""

"""
bad way to open file  need to explicitly close files else you can end
up with leaks that cause you to run over the maximum allowable file
descriptor on your system. program will throw an exception

"""
f = open('Tutorial_011_text.txt','r')
print(f.name, f.mode)
f.close()

""" 
open file with context manager best way to open files
once control exits with block file is automattically closed.
"""

with open('Tutorial_011_text.txt','r') as f:
    print(f.name, f.mode)
    f_contents = f.read()
    print(f_contents)
    
with open('Tutorial_011_text.txt','r') as f:
    print("\n", f.name, f.mode)
    f_contents = f.readlines()
    print(f_contents)
    
with open('Tutorial_011_text.txt','r') as f:
    print("\n", f.name, f.mode)
    f_contents = f.readline()
    print(f_contents,end="")
    f_contents = f.readline()
    print(f_contents)
    
    
    
with open('Tutorial_011_text.txt','r') as f:
    print("\n", f.name, f.mode)
    for line in f:
        print(line,end="")
        
with open('Tutorial_011_text.txt','r') as f:
    print("\n", f.name, f.mode)
    f_contents = f.read(100)
    print(f_contents,end='')
    f_contents = f.read(100)
    print(f_contents)


with open('Tutorial_011_text.txt','r') as f:
    print("\n", f.name, f.mode)
    size_to_read = 10
    
    f_contents = f.read(size_to_read)
    while (len(f_contents) >0):
        print(f_contents,end='')
        f_contents = f.read(size_to_read)
        
with open('Tutorial_011_text.txt','r') as f:
    print("\n", f.name, f.mode)
    size_to_read = 10
    f_contents = f.read(size_to_read)
    print(f_contents,end='')
    f_contents = f.read(size_to_read)
    print(f_contents,end='')
    print(f.tell())
    
    
with open('Tutorial_011_text.txt','r') as f:
    print("\n", f.name, f.mode)
    size_to_read = 10
    f_contents = f.read(size_to_read)
    print(f_contents,end='')
    f.seek(0)
    f_contents = f.read(size_to_read)
    print(f_contents,end='')


with open('Tutorial_011_text2.txt','w') as f:
    f.write('some junk')
    
with open('Tutorial_011_text2.txt','w') as f:
    f.write('some junk')
    f.write('more junk')
    
with open('Tutorial_011_text2.txt','w') as f:
    f.write('some junk')
    f.seek(0)
    f.write('more junk')
    
with open('Tutorial_011_text.txt','r') as rf:
    with open('Tutorial_011_text_copy.txt','w') as wf:
        for line in rf:
            wf.write(line)

# open jpg in binary mode using the b
with open('Tutorial_011_FrankSinatra.jpg','rb') as rf:
    with open('Tutorial_011_FrankSinatra_c.jpg','wb') as wf:
        for line in rf:
            wf.write(line)


with open('Tutorial_011_FrankSinatra.jpg','rb') as rf:
    with open('Tutorial_011_FrankSinatra_c.jpg','wb') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while (len(rf_chunk) >0):
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)
