# -*- coding: utf-8 -*-
"""
Created on Wed Jan 23 08:27:17 2019

@author: Stanley
"""

print('Imported my_module...')

test = 'Test String'

def find_index(to_search, target):
    '''Find the index of a value in a sequence'''
    for i, value in enumerate(to_search):
        if value == target:
            return i

    return -1