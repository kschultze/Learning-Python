# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 21:50:33 2016

@author: Schultze

first crack at computing the nth prime number
optimized for simplest code, not fastest run time
"""
import time
millis1 = int(round(time.time() * 1000))

guess = 2

i = 1
while i < 10000:
    guess = guess + 1
    test = 1
    
    rem = 1
    while rem != 0:
        test = test + 1
        rem = guess%test
                
    if test == guess:
        prime = guess
        i = i + 1
        
print(prime)

millis2 = int(round(time.time() * 1000))
print('time = ' + str(millis2-millis1))
