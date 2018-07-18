# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 18:42:27 2018
monte carlo simulation of pi

area of circle = pi*r^2
area of square = 4r^2

circle/square = pi/4

y^2 + x^2 = r^2  (unit circle)


@author: kschultze
"""

import random
import numpy

def simulatePi(num):
    inCircle = 0
    for i in range(num):
        x = random.random()
        y = random.random()
        if (x**2 + y**2) < 1: #only operating in first quadrant
            inCircle += 1
            
    print inCircle*4.0/num
    return inCircle*4.0/num

piList = []    
for i in range(10):
    piList.append(simulatePi(10000000))
print ''
print numpy.average(piList)
print numpy.std(piList)