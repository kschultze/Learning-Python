# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 21:50:33 2016

@author: Schultze

first crack at computing the nth prime number
optimized for simplest code, not fastest run time
"""

#guess = 2
#
#n = 1
#while n < 1000:
#    guess = guess + 1
#    test = 1
#    
#    rem = 1
#    while rem != 0:
#        rem = guess%test
#        test = test + 1
#        
#    if test == guess:
#        prime = guess
#        n = n + 1
#        
#print(prime)

#second part of assignment: prove that the product of primes < n is always e**n
#and this ratio converges on 1 as n increases

import math

n = 2
primeSum = math.log(2)

i = 1
while i < 1000:
    n = n + 1
    test = 1
    
    rem = 1
    while rem != 0:
        test = test + 1
        rem = n%test
        
    if test == n:
        prime = n
        primeSum = primeSum + math.log(prime)
        i = i + 1

print('n = ' + str(n))
print('primeSum = ' +str(primeSum))
print('ratio = ' +str(primeSum/n))

#Ideas for building on code
#    loop to run through lots of n's then store and plot the results of the
#    ratio to see it approach 1