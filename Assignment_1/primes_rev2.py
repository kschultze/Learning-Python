# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 21:50:33 2016

@author: Schultze

rev2 at computing the nth prime number
now iterates every odd number and only goes up to the highest logically necessary
"""
import time
startTime = time.time()

guess = 1

i = 1
while i < 500000:
    guess = guess + 2
    test = 1
    
    rem = 1
    primeFlag = 0
    while rem != 0 and primeFlag == 0:
        test = test + 2
        rem = guess%test
        primeFlag = guess/test < test #no reason to test further, it's a prime
        
    if primeFlag:
        prime = guess
        i = i + 1
        
print(prime)

endTime = time.time()
print('Runtime = ' +str(endTime - startTime))