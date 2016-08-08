# -*- coding: utf-8 -*-
"""
Created on Sat Jul 23 21:50:33 2016

@author: Schultze


rev3 at computing the nth prime number
now it saves each found prime number in a tuple and only uses those numbers to
test for future primes.  Not sure however if this is faster that rev2 for large
primes as it might be more computationally expensive to store the large tuple?
"""
import time

startTime = time.time()

numPrime = 100000  #enter in the nth prime you want to find
guess = 1
testTuple = (2,)  #generate tuple of known primes to use as test divisors

while len(testTuple) < numPrime:
    guess += 2
    
    test = 2
    i = 0
    primeFlag = 0
    
    while guess%test != 0 and primeFlag == 0:   #first condition fails if guess is evenly divisible (not prime)
        test = testTuple[i]
        primeFlag = guess/test < test           #if it makes it this far without a divisor, it must be prime
        i += 1
        
    if primeFlag:
        testTuple = testTuple + (guess,)        #adds new prime to tuple
        
print(str(numPrime) + 'th prime = ' + str(testTuple[-1]))

endTime = time.time()

print('Runtime = ' +str(endTime - startTime))