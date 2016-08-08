# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 21:50:33 2016

@author: Schultze

rev2 at computing the nth prime number
now iterates every odd number and only goes up to the highest logically necessary
could only try dividing by odds as well which should roughly double the speed
but using only the list of primes itself will be even faster for rev3
"""
import time
millis1 = int(round(time.time() * 1000))

guess = 1

i = 1
while i < 100000:
    guess = guess + 2
    test = 1
    
    rem = 1
    primeFlag = 0
    while rem != 0 and primeFlag == 0:
        test = test + 1
        rem = guess%test
        primeFlag = guess/test < test #no reason to test further, it's a prime
        
    if primeFlag:
        prime = guess
        i = i + 1
        
print(prime)

millis2 = int(round(time.time() * 1000))
print('time = ' + str(millis2-millis1))
