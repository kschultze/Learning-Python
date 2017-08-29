# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 15:56:00 2017

@author: kschultze
"""

def factorial(n):
    """
    returns the factorial of an int
    """
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
    
def countEndZeros(num):
    """
    returns a count of trailing zeros given an int or string
    """
    num = str(num)
    if num[-1] != '0':
        return 0
    else:
        return 1 + countEndZeros(num[:-1])

import matplotlib.pyplot as plt
        
n = 500
factZeros = []
for i in range(1,n+1):
    factZeros = factZeros + [countEndZeros(factorial(i))]
plt.plot(range(1,n+1),factZeros)