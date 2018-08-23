# Problem Set 11: Simulating robots
# Name:
# Collaborators:
# Time:

#Tiles are whole numbers, positions need not be
#To ID which tile robot is in, round down each position

import math
import random
import time
import pylab
import ps11_visualize

# === Provided classes

class Position(object):
    """
    A Position represents a location in a two-dimensional room.
    """
    def __init__(self, x, y):
        """
        Initializes a position with coordinates (x, y).

        x: a real number indicating the x-coordinate
        y: a real number indicating the y-coordinate
        """
        self.x = float(x)
        self.y = float(y)
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'
    def getNewPosition(self, angle, speed):
        """
        Computes and returns the new Position after a single clock-tick has
        passed, with this object as the current position, and with the
        specified angle and speed.

        Does NOT test whether the returned position fits inside the room.

        angle: integer representing angle in degrees, 0 <= angle < 360
        speed: positive float representing speed

        Returns: a Position object representing the new position.
        """
        old_x, old_y = self.getX(), self.getY()
        # Compute the change in position
        delta_y = speed * math.cos(math.radians(angle))
        delta_x = speed * math.sin(math.radians(angle))
        # Add that to the existing position
        new_x = old_x + delta_x
        new_y = old_y + delta_y
        return Position(new_x, new_y)


# === Problems 1 and 2

class RectangularRoom(object):
    """
    A RectangularRoom represents a rectangular region containing clean or dirty
    tiles.

    A room has a width and a height and contains (width * height) tiles. At any
    particular time, each of these tiles is either clean or dirty.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangular room with the specified width and height.
        Initially, no tiles in the room have been cleaned.

        width: an integer > 0
        height: an integer > 0
        """
        self.width = width
        self.height = height
        
        self.tiles = {}
        for i in range(height):
            for j in range(width):
                self.tiles[(i,j)] = False  #True = clean, False = dirty   
        
    def cleanTileAtPosition(self, pos):
        """
        Mark the tile under the position POS as cleaned.
        Assumes that POS represents a valid position inside this room.

        pos: a Position
        """
        x = int(pos.getX())   #rounds down to put on room grid
        y = int(pos.getY())  #rounds down to put on room grid
        self.tiles[(x,y)] = True
        
    def isTileCleaned(self, m, n):
        """
        Return True if the tile (m, n) has been cleaned.

        Assumes that (m, n) represents a valid tile inside the room.

        m: an integer
        n: an integer
        returns: True if (m, n) is cleaned, False otherwise
        """
        x = int(m)
        y = int(n)
        return self.tiles[(x,y)]
        
    def getNumTiles(self):
        """
        Return the total number of tiles in the room.

        returns: an integer
        """
        return self.width*self.height

    def getNumCleanedTiles(self):
        """
        Return the total number of clean tiles in the room.

        returns: an integer
        """
        numCleaned = 0
        for tile in self.tiles.values():
            if tile == True:
                numCleaned += 1
        return numCleaned
        
    def getRandomPosition(self):
        """
        Return a random position inside the room.

        returns: a Position object.
        """
        x = random.random()*self.width
        y = random.random()*self.height
        return Position(x,y)
        
    def isPositionInRoom(self, pos):
        """
        Return True if POS is inside the room.

        pos: a Position object.
        returns: True if POS is in the room, False otherwise.
        """
        return 0 <= pos.getX() <= self.width and 0 <= pos.getY() <= self.height

class BaseRobot(object):
    """
    Represents a robot cleaning a particular room.

    At all times the robot has a particular position and direction in
    the room.  The robot also has a fixed speed.

    Subclasses of BaseRobot should provide movement strategies by
    implementing updatePositionAndClean(), which simulates a single
    time-step.
    """
    def __init__(self, room, speed):
        """
        Initializes a Robot with the given speed in the specified
        room. The robot initially has a random direction d and a
        random position p in the room.

        The direction d is an integer satisfying 0 <= d < 360; it
        specifies an angle in degrees.

        p is a Position object giving the robot's position.

        room:  a RectangularRoom object.
        speed: a float (speed > 0)
        """
        self.room = room
        self.speed = speed
        self.position = room.getRandomPosition()
        self.direction = random.random()*360
    
    def __str__(self):
        return 'Robot with \nPosition: ' + str(self.getRobotPosition()) + '\nDirection: ' + str(self.direction)

    def getRobotPosition(self):
        """
        Return the position of the robot.

        returns: a Position object giving the robot's position.
        """
        return self.position
        
    def getRobotDirection(self):
        """
        Return the direction of the robot.

        returns: an integer d giving the direction of the robot as an angle in
        degrees, 0 <= d < 360.
        """
        return self.direction
        
    def setRobotPosition(self, position):
        """
        Set the position of the robot to POSITION.

        position: a Position object.
        """
        self.position = position

    def setRobotDirection(self, direction):
        """
        Set the direction of the robot to DIRECTION.

        direction: integer representing an angle in degrees
        """
        self.direction = direction

class Robot(BaseRobot):
    """
    A Robot is a BaseRobot with the standard movement strategy.

    At each time-step, a Robot attempts to move in its current
    direction; when it hits a wall, it chooses a new direction
    randomly.
    """
    def updatePositionAndClean(self):
        """
        Simulate the passage of a single time-step.

        Move the robot to a new position and mark the tile it is on as having
        been cleaned.
        """
#        deltaX = math.cos(self.direction*math.pi/180)*self.speed
#        deltaY = math.sin(self.direction*math.pi/180)*self.speed
#        newX = self.position.getX() + deltaX
#        newY = self.position.getY() + deltaY
        newPosition = self.position.getNewPosition(self.direction, self.speed)
        if self.room.isPositionInRoom(newPosition):
            self.setRobotPosition(newPosition)
            self.room.cleanTileAtPosition(newPosition)
        else:
            #for now just going to pretend the robot can see ahead and turn if it's going to hit a wall
            self.setRobotDirection(random.random()*360)
            
# === Problem 3

def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type, visualize):
    """
    Runs NUM_TRIALS trials of the simulation and returns a list of
    lists, one per trial. The list for a trial has an element for each
    timestep of that trial, the value of which is the percentage of
    the room that is clean after that timestep. Each trial stops when
    MIN_COVERAGE of the room is clean.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE,
    each with speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    Visualization is turned on when boolean VISUALIZE is set to True.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. Robot or
                RandomWalkRobot)
    visualize: a boolean (True to turn on visualization)
    """
    
    trialList = []
     
    for trial in range(num_trials):
        if visualize == True:
            anim = ps11_visualize.RobotVisualization(num_robots, height, width, .1)
        room = RectangularRoom(width,height)
        currentCoverage = 0.0   
        #initialize robots
        robotList = []
        for i in range(num_robots):
            currentRobot = Robot(room, speed)
            robotList.append(currentRobot)
            room.cleanTileAtPosition(currentRobot.getRobotPosition())  #clean initial tile
        currentCoverage = float(room.getNumCleanedTiles())/room.getNumTiles()
        coverageList = [currentCoverage]
        while currentCoverage < min_coverage:
            if visualize == True:
                anim.update(room, robotList)
            for robot in robotList:
                robot.updatePositionAndClean()
            currentCoverage = float(room.getNumCleanedTiles())/room.getNumTiles()
            coverageList.append(currentCoverage)
        trialList.append(coverageList)
    if visualize == True:
        anim.done()
    return trialList

# === Provided function
def computeMeans(list_of_lists):
    """
    Returns a list as long as the longest list in LIST_OF_LISTS, where
    the value at index i is the average of the values at index i in
    all of LIST_OF_LISTS' lists.

    Lists shorter than the longest list are padded with their final
    value to be the same length.
    """
    # Find length of longest list
    longest = 0
    for lst in list_of_lists:
        if len(lst) > longest:
           longest = len(lst)
    # Get totals
    tots = [0]*(longest)
    for lst in list_of_lists:
        for i in range(longest):
            if i < len(lst):
                tots[i] += lst[i]
            else:
                tots[i] += lst[-1]
    # Convert tots to an array to make averaging across each index easier
    tots = pylab.array(tots)
    # Compute means
    means = tots/float(len(list_of_lists))
    return means


# === Problem 4
def showPlot1():
    """
    Produces a plot showing dependence of cleaning time on room size.
    """
    # TODO: Your code goes here

def showPlot2():
    """
    Produces a plot showing dependence of cleaning time on number of robots.
    """
    # TODO: Your code goes here

def showPlot3():
    """
    Produces a plot showing dependence of cleaning time on room shape.
    """
    # TODO: Your code goes here

def showPlot4():
    """
    Produces a plot showing cleaning time vs. percentage cleaned, for
    each of 1-5 robots.
    """
    # TODO: Your code goes here


# === Problem 5

class RandomWalkRobot(BaseRobot):
    """
    A RandomWalkRobot is a robot with the "random walk" movement
    strategy: it chooses a new direction at random after each
    time-step.
    """
    # TODO: Your code goes here


# === Problem 6

def showPlot5():
    """
    Produces a plot comparing the two robot strategies.
    """
    # TODO: Your code goes here

#runSimulation(num_robots, speed, width, height, min_coverage, num_trials, robot_type, visualize):

trialLists = runSimulation(1, 1, 10, 10, .5, 20, Robot, False)
#print trialLists
meansList = computeMeans(trialLists)
lenList = []
listSum = 0
for i in trialLists:
    listSum += len(i)
    lenList.append(len(i))
print lenList
print listSum/float(len(trialLists))


""" Test Code """

#pos1 = Position(3,4)
#print pos1
#print pos1.getX
#print pos1.getY
#pos2 = pos1.getNewPosition(90,1)
#pos3 = pos2.getNewPosition(45,2)
#print pos2
#print pos3
#print '\n'
#
#room1 = RectangularRoom(5,5)
##print room1.tiles.items()
#room1.cleanTileAtPosition(pos1)
#print room1.tiles[(3,4)]
#print room1.getNumCleanedTiles()
#print room1.getNumTiles()
#print '\n'
#
#randPos = room1.getRandomPosition()
#print randPos
#room1.cleanTileAtPosition(randPos)
#print room1.getNumCleanedTiles()
#print room1.getNumTiles()
#print '\n'
#
#print room1.isPositionInRoom(pos2)
#print room1.isPositionInRoom(pos3)
#print room1.isTileCleaned(3,4)
#print room1.isTileCleaned(1,1)
#print '\n'
#
#robot1 = Robot(room1, 1)
#print robot1
#print robot1.getRobotDirection()
#print robot1.getRobotPosition()
#robot1.setRobotDirection(random.random()*360)
#robot1.setRobotPosition(room1.getRandomPosition())
#print robot1
#print '\n'
#
#print room1.getNumCleanedTiles()
#robot1.updatePositionAndClean()
#print room1.getNumCleanedTiles()

















