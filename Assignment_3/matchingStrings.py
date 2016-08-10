# -*- coding: utf-8 -*-
"""
Created on Mon Aug 08 21:37:52 2016
@author: kschultze

Functions to find all instances of a substring in a string.
One is iterative, one is recursive.
"""

def findAll(target, key, start = 0):
    """
    Returns list of indeces of substring locations in a string.
    Returns None if no instances found.
    Will only return the first instance of overlapping substrings    
    """
    import string
    
    index = string.find(target,key,start)
    if index == -1:
        return None
    indexList = []
    while index != -1:
        indexList += [index]
        index = string.find(target,key,index + len(key))
    return indexList

def findAllRecursive(target, key, start = 0):
    """
    Returns list of indeces of substring locations in a string.
    Returns None if no instances found.
    Will only return the first instance of overlapping substrings
    """
    import string
    
    if string.find(target, key,start) == -1:  #base case
         return None
         
    else:                               #recursive step
        index = string.find(target,key,start)
        indexList = findAllRecursive(target, key,index + len(key))  #recursion     
        
        if indexList == None:  #gets rid of the 'None' passed in the base case
               indexList = []
        return [index] + indexList

#Test code

str1 = 'tgacatgcacaagtatgcatcatcatcat'
key1 = 'atgc'
key2 = 'catcat'
key3 = 'xyz'

print('[4,14]')
print(findAll(str1,key1))
print('[17,23]')
print(findAll(str1,key2))
print('[14]')
print(findAll(str1,key1,5))
print('None')
print(findAll(str1,key3))

print('[4,14]')
print(findAllRecursive(str1,key1))
print('[17,23]')
print(findAllRecursive(str1,key2))
print('[14]')
print(findAllRecursive(str1,key1,5))
print('None')
print(findAllRecursive(str1,key3))