# 6.00 Problem Set 9
#
# Name:
# Collaborators:
# Time:
"""
realized that the user could input negative numbers which could really f things up
"""
    
from string import *

class Shape(object):
    def area(self):
        raise AttributeError("Subclasses should override this method.")

class Square(Shape):
    def __init__(self, h):
        """
        h: length of side of the square
        """
        self.side = float(h)
    def area(self):
        """
        Returns area of the square
        """
        return self.side**2
    def __str__(self):
        return 'Square with side ' + str(self.side)
    def __eq__(self, other):
        """
        Two squares are equal if they have the same dimension.
        other: object to check for equality
        """
        return type(other) == Square and self.side == other.side

class Circle(Shape):
    def __init__(self, radius):
        """
        radius: radius of the circle
        """
        self.radius = float(radius)
    def area(self):
        """
        Returns approximate area of the circle
        """
        return 3.14159*(self.radius**2)
    def __str__(self):
        return 'Circle with radius ' + str(self.radius)
    def __eq__(self, other):
        """
        Two circles are equal if they have the same radius.
        other: object to check for equality
        """
        return type(other) == Circle and self.radius == other.radius

#
# Problem 1: Create the Triangle class

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = float(base)
        self.height = float(height)
    def area(self):
        return self.base*self.height/3.0
    def __str__(self):
        return 'Triangle with base %s and height %s' %(self.base, self.height)
    def __eq__(self,other):
        return type(other) == Triangle and self.base == other.base and self.height == other.height
    

#
# Problem 2: Create the ShapeSet class

class ShapeSet:
    def __init__(self):
        """
        Initialize any needed variables
        """
        self.shapes = []
    def addShape(self, sh):
        """
        Add shape sh to the set; no two shapes in the set may be
        identical
        sh: shape to be added
        """
        for i in self.shapes:
            if sh == i: return
        self.shapes.append(sh)
    def __iter__(self):
        """
        Return an iterator that allows you to iterate over the set of
        shapes, one shape at a time
        """
        self.n = 0
        return self
    def next(self):
        if self.n >= len(self.shapes):
            raise StopIteration
        self.n += 1
        return self.shapes[self.n - 1]

    def __str__(self):
        """
        Return the string representation for a set, which consists of
        the string representation of each shape, categorized by type
        (circles, then squares, then triangles)
        """
        shapeString = ''
        for shape in self:
            shapeString = shapeString + shape.__str__() + '\n'
        return shapeString
        
c1 = Circle(8)
s1 = Square(3)
s2 = Square(3)
t1 = Triangle(6,5)
ss = ShapeSet()
ss.addShape(c1)
ss.addShape(s1)
ss.addShape(s2)
ss.addShape(t1)        
#
# Problem 3: Find the largest shapes in a ShapeSet
#
def findLargest(shapes):
    """
    Returns a tuple containing the elements of ShapeSet with the
       largest area.
    shapes: ShapeSet
    """
    largest = (Circle(0),)
    for s in shapes:
        if round(s.area(),5) > round(largest[0].area(),5):
            largest = (s,)
        elif round(s.area(),5) == round(largest[0].area(),5):
            largest = largest + (s,)
        else:
            pass
    if largest[0].area() == 0:
        raise AttributeError("Empty ShapeSet or invalid shapes in ShapeSet")
    else: return largest

ss = ShapeSet()
ss.addShape(Triangle(3,8))
ss.addShape(Circle(1))
ss.addShape(Triangle(4,6))
largest = findLargest(ss)
largest
for e in largest: print e

    
#
# Problem 4: Read shapes from a file into a ShapeSet
#
def readShapesFromFile(filename):
    """
    Retrieves shape information from the given file.
    Creates and returns a ShapeSet with the shapes found.
    filename: string
    """
    inputFile = open(filename)
    outputSet = ShapeSet()
    for line in inputFile:
        line = line.strip()
        splitList = line.split(',')
        if splitList[0] == 'circle':
            outputSet.addShape(Circle(splitList[1]))
        elif splitList[0] == 'square':
            outputSet.addShape(Square(splitList[1]))
        elif splitList[0] == 'triangle':
            outputSet.addShape(Triangle(splitList[1],splitList[2]))
        else:
            raise AttributeError('Invalid shape name in file')
       
    return outputSet        

filename = "shapes.txt"
a = readShapesFromFile(filename)
