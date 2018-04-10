## -*- coding: utf-8 -*-
#"""
#Created on Mon Aug 21 20:11:31 2017
#
#@author: kschultze
#"""
#
#import string
#
##for i in range(1,len(a)+1):
##    print a[-1*i]
#    
#def countChars(string,char):
#    count = 0
#    for i in string:
#        if i == char:
#            count += 1
#    return count
#
#def isLower(ch): 
#    return string.find(string.lowercase, ch) != -1 
#
#
#def threeLines(): 
#  newLine() 
#  newLine() 
#  newLine() 
#
#def newLine(): 
#  print 
#  return None
#
#print "First Line." 
#threeLines() 
#print "Second Line." 
#
#def compare(x,y):
#    if x > y:
#        return 1
#    if x < y:
#        return -1
#    else:
#        return 0
#
#def slope(x1,x2,y1,y2):
#    return (y1 - y2)/(x1 - x2)
#    # 2,2 3,1 ans -1, and 5
#def yIntercept(x1,x2,y1,y2):
#    return y1-x1*slope(x1,x2,y1,y2)
#    # y = slope*x + i
#        
#def factorial(n):
#    if n == 0:
#        return 1
#    else:
#        return n*factorial(n-1)
##write a program to figure out the pattern of trailing zeros with increasing n
#
#def fibbonaci(n):
#    if n == 0 or n == 1:
#        return 1
#    else:
#        return fibbonaci(n-1) + fibbonaci(n-2)
# 
#calcd = {0:1,1:1}
#def fibbonaci2(n, calcd):
#    """faster version of fibbonaci utilizing dictionaries"""
#    if calcd.has_key(n):
#        return calcd[n]
#    else:
#        newFib = fibbonaci2(n-1,calcd) + fibbonaci2(n-2,calcd)
#        calcd[n] = newFib
#        return newFib
#
#storedFibs = [1,1]  #first 2 fibbonaci numbers
#def fibbonaci3(n, storedFibs):
#    """tweaked version of fibbonaci2 to use lists, probably slightly more 
#       straightforward since data is naturally ordered"""
#    if len(storedFibs) > n:
#        return storedFibs[n]
#    else:
#        newFib = fibbonaci3(n-1,storedFibs) + fibbonaci3(n-2,storedFibs)
#        storedFibs.append(newFib)
#        return newFib
#        
#
#def fibbonaci4(n):
#    """trying to make it so it only takes a single argument n, currently still
#        have to make a global variable which I don't like"""
#    if 'storedFibs' not in globals():
#        global storedFibs
#        storedFibs = [1,1]
#    if len(storedFibs) > n:
#        return storedFibs[n]
#    else:
#        newFib = fibbonaci4(n-1) + fibbonaci4(n-2)
#        storedFibs.append(newFib)
#        print storedFibs[-1]
#        return newFib
##What about having the function return a set of all values?  Is a set ordered?
#        
#def fibbonaci5(n):
#    fibs = [1,1]
#    while len(fibs) <= n:
#        newFib = fibs[-1] + fibs[-2]
#        fibs.append(newFib)
#    return fibs[-1]
#        
##import matplotlib.pyplot as plt
##n = 20
##fibList = []
##for i in range(1,n+1):
##    fibList = fibList + [fibbonaci(i)]
##plt.plot(fibList)
#
##def swap0(s1, s2):
##    assert type(s1) == list and type(s2) == list
##    tmp = s1[:]
##    s1 = s2[:]
##    s2 = tmp
##    return s1, s2
##s1 = [1]
##s2 = [2]
##s1, s2 = swap0(s1, s2)
##print s1, s2
##
##def rev(s):
##    assert type(s) == list
##    for i in range(len(s)/2):
##        tmp = s[i]
##        s[i] = s[-(i+1)]
##        s[-(i+1)] = tmp
##s = [1,2,3]
##rev(s)
##print s
#
#def fastMaxVal(w, v, aW):
#    """
#    knapsack problem solution, paired with fastMaxValx
#    takes in a list or tuple of weights (w) and values (v) and returns the highest
#    value you can pack within a weight limit (available weight == aW)
#    """
#    i = len(w) - 1  #forms index
#    m = {} #memoization
#    return fastMaxValx(w, v, i, aW, m)
#
#def fastMaxValx(w, v, i, aW, m):
#    #check if we've already solved for this particular index and available weight pair
#    try: return m[(i,aW)]
#    except KeyError:
#        global numCalls
#        numCalls += 1
#        if i == 0:
#            if w[i] <= aW: return v[i]
#            else: return 0
#        without_i = fastMaxValx(w, v, i-1, aW, m)
#        if w[i] > aW: return without_i
#        else: with_i = v[i] + fastMaxValx(w, v, i-1, aW - w[i], m)
#        m[(i,aW)] = max(with_i, without_i)
#        return m[(i,aW)]
#        
##w = [5,3,2,2,5,4,7,8,2,4,3,5,2,2,3,3,7,6,4,9,9,6,5,4,3,5,6,7,5,4,3]
##v = [9,7,8,8,6,3,8,4,5,2,6,7,4,2,1,6,7,4,3,5,7,5,6,8,2,3,4,5,7,9,9]
##numCalls = 0
##print fastMaxVal(w,v,40)
##print numCalls
#
#
#class cPoint:
#    def __init__(self,x,y):
#        self.x = x
#        self.y = y
#        self.radius = math.sqrt(self.x*self.x + self.y*self.y)
#        self.angle = math.atan2(self.y,self.x)
#    def cartesian(self):
#        return (self.x, self.y)
#    def polar(self):
#        return (self.radius, self.angle)
#    def __str__(self):
#        return '(' + str(self.x) + ', ' + str(self.y) + ')'
#    def __cmp__(self,other):
#        return (self.x > other.x) and (self.y > other.y)


class time:
    def __init__(self,hour=0,minute=0,second=0):
        self.hour = hour
        self.minute = minute
        self.second = second
    def __str__(self):
        return 'time - %s:%s:%s' %(self.hour, self.minute, self.second)
    def isLater(self,other):
        if self.hour > other.hour:
            return True
        if self.hour == other.hour:
            if self.minute > other.minute:
                return True
            if self.minute == other.minute:
                if self.second > other.second:
                    return True
        return False
    def inSeconds(self):
        return self.second + self.minute*60 + self.hour*3600
    def makeTime(self,seconds):
        hours = (seconds//3600)%24
        minutes = (seconds%3600)//60
        seconds = seconds%60
        return time(hours,minutes,seconds)
    def addTime(self,other):
        sum = self.inSeconds() + other.inSeconds()
        return self.makeTime(sum)
        
        
t1 = time(22,48,36)
t2 = time(4,48,1)
#print t1
#print t2
#print t1.isLater(t2)
#print t2.isLater(t1)
#print t1.addTime(t2)
#x = t1.inSeconds

def find(str, ch, start=0, end=None): 
    if end == None:
        end = len(str)
    elif end < 0:
        end = end + len(str)
    index = start 
    while index < end: 
        if str[index] == ch: 
            return index 
        index = index + 1 
    return -1 

#after writint this I realized that it would probably be cleaner/more intuitive
#to have separate classes for polar and cartesian with methods to convert one into the other
#maybe have 'point' be a superClass and the two types be subclasses so they can inherit other attributes?
class point():
    import math
    def __init__(self,coord1,coord2,coordType='cartesian'):
        self.type = coordType
        if coordType == 'cartesian':
            self.x = coord1
            self.y = coord2
            self.l = math.sqrt(self.x**2 + self.y**2)
            self.theta = math.atan(self.y/self.x)
        elif coordType == 'polar':
            self.l = coord1
            self.theta = coord2
            self.x = math.cos(self.theta)*self.l
            self.y = math.sin(self.theta)*self.l
    def __str__(self):
        if self.type == 'cartesian':
            return 'cartesian point: ' + str((self.x, self.y))
        if self.type == 'polar':
            return 'polar point: ' + str((self.l, self.theta))























