# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 21:50:33 2016

@author: Schultze


rev3 at computing the nth prime number
now it saves each found prime number in a tuple and only uses those numbers to
test for future primes.  Not sure however if this is faster that rev2 for large
primes as it might be more computationally expensive to store the large tuple?
fixed above speed issue by preallocating memory
"""
import time

startTime = time.time()

numPrime = 500000  #enter in the nth prime you want to find
guess = 1
testList = [None]*numPrime #preallocate memory
testList[0] = 2
primeIndex = 1

while testList[-1] == None:
    guess += 2
    
    test = 2
    i = 0
    primeFlag = 0
    
    while guess%test != 0 and primeFlag == 0:   #first condition fails if guess is evenly divisible (not prime)
        test = testList[i]
        primeFlag = guess/test < test           #if it makes it this far without a divisor, it must be prime
        i += 1
        
    if primeFlag:
        testList[primeIndex] = guess     #adds new prime to tuple
        primeIndex += 1
        
print(str(numPrime) + 'th prime = ' + str(testList[-1]))

endTime = time.time()

print('Runtime = ' +str(endTime - startTime))