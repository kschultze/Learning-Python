# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 20:11:31 2017

@author: kschultze
"""

import string

#for i in range(1,len(a)+1):
#    print a[-1*i]
    
def countChars(string,char):
    count = 0
    for i in string:
        if i == char:
            count += 1
    return count

def isLower(ch): 
    return string.find(string.lowercase, ch) != -1 


def threeLines(): 
  newLine() 
  newLine() 
  newLine() 

def newLine(): 
  print 
  return None

print "First Line." 
threeLines() 
print "Second Line." 

def compare(x,y):
    if x > y:
        return 1
    if x < y:
        return -1
    else:
        return 0

def slope(x1,x2,y1,y2):
    return (y1 - y2)/(x1 - x2)
    # 2,2 3,1 ans -1, and 5
def yIntercept(x1,x2,y1,y2):
    return y1-x1*slope(x1,x2,y1,y2)
    # y = slope*x + i
        
def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
#write a program to figure out the pattern of trailing zeros with increasing n

def fibbonaci(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fibbonaci(n-1) + fibbonaci(n-2)
 
calcd = {0:1,1:1}
def fibbonaci2(n, calcd):
    """faster version of fibbonaci utilizing dictionaries"""
    if calcd.has_key(n):
        return calcd[n]
    else:
        newFib = fibbonaci2(n-1,calcd) + fibbonaci2(n-2,calcd)
        calcd[n] = newFib
        return newFib

storedFibs = [1,1]  #first 2 fibbonaci numbers
def fibbonaci3(n, storedFibs):
    """tweaked version of fibbonaci2 to use lists, probably slightly more 
       straightforward since data is naturally ordered"""
    if len(storedFibs) > n:
        return storedFibs[n]
    else:
        newFib = fibbonaci3(n-1,storedFibs) + fibbonaci3(n-2,storedFibs)
        storedFibs.append(newFib)
        return newFib
        

def fibbonaci4(n):
    """trying to make it so it only takes a single argument n, currently still
        have to make a global variable which I don't like"""
    if 'storedFibs' not in globals():
        global storedFibs
        storedFibs = [1,1]
    if len(storedFibs) > n:
        return storedFibs[n]
    else:
        newFib = fibbonaci4(n-1) + fibbonaci4(n-2)
        storedFibs.append(newFib)
        print storedFibs[-1]
        return newFib
#What about having the function return a set of all values?  Is a set ordered?
        
def fibbonaci5(n):
    fibs = [1,1]
    while len(fibs) <= n:
        newFib = fibs[-1] + fibs[-2]
        fibs.append(newFib)
    return fibs[-1]
        
#import matplotlib.pyplot as plt
#n = 20
#fibList = []
#for i in range(1,n+1):
#    fibList = fibList + [fibbonaci(i)]
#plt.plot(fibList)

def swap0(s1, s2):
    assert type(s1) == list and type(s2) == list
    tmp = s1[:]
    s1 = s2[:]
    s2 = tmp
    return s1, s2
s1 = [1]
s2 = [2]
s1, s2 = swap0(s1, s2)
print s1, s2

def rev(s):
    assert type(s) == list
    for i in range(len(s)/2):
        tmp = s[i]
        s[i] = s[-(i+1)]
        s[-(i+1)] = tmp
s = [1,2,3]
rev(s)
print s