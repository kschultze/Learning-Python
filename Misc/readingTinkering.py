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
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fibbonaci(n-1) + fibbonaci(n-2)
 
calcd = {0:1,1:1}
def fibbonaci2(n, calcd):
    """faster version of fibbonaci utilizing libraries"""
    if calcd.has_key(n):
        return calcd[n]
    else:
        newFib = fibbonaci2(n-1,calcd) + fibbonaci2(n-2,calcd)
        calcd[n] = newFib
        return newFib

previous = [1,1]  #first 2 fibbonaci numbers
def fibbonaci3(n, previous):
    """tweaked version of fibbonaci2 to use lists, probably slightly more 
       straightforward since data is naturally ordered"""
    if len(previous) > n:
        return previous[n]
    else:
        newFib = fibbonaci3(n-1,previous) + fibbonaci3(n-2,previous)
        previous.append(newFib)
        return newFib
        
#import matplotlib.pyplot as plt
#n = 20
#fibList = []
#for i in range(1,n+1):
#    fibList = fibList + [fibbonaci(i)]
#plt.plot(fibList)

for i in 'abcd':
    print i
    