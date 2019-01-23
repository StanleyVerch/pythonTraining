# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 13:20:32 2019

@author: Stanley
"""

import os
from datetime import datetime

print(dir(os))
print("\n\n current working directory: ", os.getcwd())  # get current working directory

currWorkingDir = os.getcwd()
print("\n\n current working directory: ", currWorkingDir)

os.chdir("C:/Users/Stanley/Projects")
print("\n\n current working directory: ", os.getcwd())

os.chdir(currWorkingDir)
print("\n\n current working directory: ", os.getcwd())

print("\n\n list files in directory: ", os.listdir())

"""
make directories
"""
os.mkdir("make_directory")
os.rmdir("make_directory")
os.makedirs("make_directory1/sub1")
os.removedirs("make_directory1/sub1")

#  os.rename('junk.txt', 'newJunk.txt')

print(os.stat('junk.txt').st_size)

modtime = os.stat('junk.txt').st_mtime
print(datetime.fromtimestamp(modtime))


for dirpath, dirname, filename in os.walk(currWorkingDir):
    print("\ncurrent path: ", dirpath)
    print("directory name: ",dirname)
    print("file name: ", filename)
    
print(os.environ.get('HOMEPATH'))

"""
for a in os.environ:
    print('Var: ', a, 'Value: ', os.getenv(a))
print("all done")
"""

filepath = os.environ.get('HOMEPATH') + '\\test.txt'
print(filepath)

filepath = os.path.join(os.environ.get('HOMEPATH'), 'test.txt')
print(filepath)

print(os.path.basename('/tmp/text.txt'))
print(os.path.dirname('/tmp/text.txt'))
print(os.path.split('/tmp/text.txt'))
print(os.path.exists('/tmp/text.txt'))
print(os.path.isdir(os.environ.get('HOMEPATH')))
print(os.path.splitext('/tmp/text.txt'))
print(dir(os.path))

