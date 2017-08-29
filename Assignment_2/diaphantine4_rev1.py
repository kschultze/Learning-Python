# -*- coding: utf-8 -*-
"""
07/26/16

@Schultze

Script to calculate chicken nuggets combinations
Using an iterated version of diaphantine2_rev1.py, this code finds the largest
value for n for which no combination of A, B, and C exist.

update for diaphantine4_rev1.py:  Code generalized to any values of A, B and C.
i.e. it looks for a number of solutions in a row equal to the smallest value of
the 'package' size.
Also updated A, B, and C to be a single tuple called 'packages' per instruction
"""
packages = (9,6,20)
packages = tuple(sorted(packages)) #accounts for any order, keeps as tuple

A = packages[0]
B = packages[1]
C = packages[2]
maxTest = 200

isPossible = ()

for n in range(1,maxTest+1):
    maxA = n//A
    maxB = n//B
    maxC = n//C
    match = False
    
    for numA in range(0,maxA + 1):
    
        for numB in range(0,maxB + 1):
            
            for numC in range(0,maxC + 1):
                total = numA*A + numB*B + numC*C
                if total == n:
                    match = True
    
    if match:
        isPossible += (1,)
    else:
        isPossible += (0,)  
        
    if sum(isPossible[-A:]) == A: #if you find combos for 'A' tests in a row, all remaining values can be made
        print ('Largest number of McNuggets that cannot be bought in exact quantity: ' + str(n-A))
        break
    if n == maxTest:
        print('No result found up to ' + str(maxTest) + ' McNuggets, try increasing maxTest')