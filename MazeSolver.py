import cv2
import numpy as np
from numpy import *
import turtle
import time
import sys
from collections import deque


maze = cv2.imread('maze.png')
maze = cv2.cvtColor(maze, cv2.COLOR_BGR2GRAY)
binary = cv2.threshold(maze, 200, 255, cv2.THRESH_BINARY)[1]
cv2.imshow('maze',binary)
#the size of each block of the maze (path and the wall currently)
pixX = 0
pixY = 0
prevLim = 0
lim = 0
block = 1
height = np.size(binary, 0)
width = np.size(binary, 1)
while(pixY<height and pixX<width):
               pixY= 0
               prevLim = lim
               while(binary[pixY,pixX] == binary[pixX,pixY]):
                              pixY = pixY+1
                              
               lim =pixY
               pixX = pixX+1
               if(prevLim != 0 and prevLim == lim):
                              block = block +1
               elif(prevLim != 0 and prevLim != lim):
                              break
print("BlockSize")
print(block)
#Conversion of the maze Image to a matrix where the a wall block will represent a 0 element and path block will represent a 1 element
pixX = 0
pixY = 0
col = 0
row = 0
blockHeight = int(height/block)
blockWidth = int(width/block)
print("blockHeight")
print(blockHeight)
print("blockWidth")                              
print(blockWidth)
imgMat = zeros((blockHeight,blockWidth))
while(pixY<height):
               col=0
               pixX=0
               while(pixX<width):
                              i=int(block/2)+pixY
                              j=int(block/2)+pixX
                              if(int(binary[i,j]) == 255):
                                             imgMat[row][col] = 1
                              else:
                                             imgMat[row][col] = int(binary[i,j])
                              pixX=pixX+block
                              col=col+1
               pixY=pixY+block
               row=row+1
count=0
for i in range(blockWidth):
               if(count == 0):
                              if(imgMat[i][0] == 1):
                                             imgMat[i][0]= '2'
                                             count=1
                              elif(imgMat[0][i] == 1):
                                             imgMat[0][i]= '2'
                                             count=1
                              elif(imgMat[blockHeight-1][i] == 1):
                                             imgMat[blockHeight-1][i] = '2'
                                             count=1
                              elif(imgMat[i][blockHeight-1] == 1):
                                             imgMat[i][blockHeight-1] = '2'
                                             count=1
               if(count == 1):
                              if(imgMat[i][0] == 1):
                                             imgMat[i][0]= '3'
                              elif(imgMat[0][i] == 1):
                                             imgMat[0][i]= '3'
                              elif(imgMat[blockHeight-1][i] == 1):
                                             imgMat[blockHeight-1][i] = '3'
                              elif(imgMat[i][blockHeight-1] == 1):
                                             imgMat[i][blockHeight-1] = '3'

#setting up the animation part
wn = turtle.Screen()               # define the turtle screen
wn.bgcolor("white")                # set the background colour
wn.title("A BFS Maze Solving Program")
wn.setup(1300,700)                  # setup the dimensions of the working window


# this is the class for the Maze
class Maze(turtle.Turtle):               # define a Maze class
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")            # the turtle shape
        self.color("black")             # colour of the turtle
        self.penup()                    # lift up the pen so it do not leave a trail
        self.speed(0)

# this is the class for the finish line - green square in the maze
class Green(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("green")
        self.penup()
        self.speed(0)

class Blue(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        self.penup()
        self.speed(0)


# this is the class for the yellow or turtle
class Red(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("red")
        self.penup()
        self.speed(0)

class Yellow(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("yellow")
        self.penup()
        self.speed(0)
        
grid = imgMat


def setup_maze(grid):                          # define a function called setup_maze
    global start_x, start_y, end_x, end_y      # set up global variables for start and end locations
    for y in range(len(grid)):                 # read in the grid line by line
        for x in range(len(grid[y])):          # read each cell in the line
            character = grid[y][x]             # assign the varaible "character" the the x and y location od the grid
            screen_x = -588 + (x * 24)         # move to the x location on the screen staring at -588
            screen_y = 288 - (y * 24)          # move to the y location of the screen starting at 288

            if character == 0:
                maze.goto(screen_x, screen_y)         # move pen to the x and y locaion and
                maze.stamp()                          # stamp a copy of the turtle on the screen
                walls.append((screen_x, screen_y))    # add coordinate to walls list

            if character == 1 or character == 3:
                path.append((screen_x, screen_y))     # add " " and e to path list

            if character == 3:
                yellow.color("purple")
                yellow.goto(screen_x, screen_y)       # send green sprite to screen location
                end_x, end_y = screen_x,screen_y     # assign end locations variables to end_x and end_y
                yellow.stamp()
                yellow.color("yellow")

            if character == 2:
                start_x, start_y = screen_x, screen_y  # assign start locations variables to start_x and start_y
                red.goto(screen_x, screen_y)


def endProgram():
    wn.exitonclick()
    sys.exit()

def search(x,y):
    frontier.append((x, y))
    solution[x,y] = x,y

    while len(frontier) > 0:          # exit while loop when frontier queue equals zero
        time.sleep(0)
        x, y = frontier.popleft()     # pop next entry in the frontier queue an assign to x and y location

        if(x - 24, y) in path and (x - 24, y) not in visited:  # check the cell on the left
            cell = (x - 24, y)
            solution[cell] = x, y    # backtracking routine [cell] is the previous cell. x, y is the current cell
            #blue.goto(cell)        # identify frontier cells
            #blue.stamp()
            frontier.append(cell)   # add cell to frontier list
            visited.add((x-24, y))  # add cell to visited list

        if (x, y - 24) in path and (x, y - 24) not in visited:  # check the cell down
            cell = (x, y - 24)
            solution[cell] = x, y
            #blue.goto(cell)
            #blue.stamp()
            frontier.append(cell)
            visited.add((x, y - 24))
            print(solution)

        if(x + 24, y) in path and (x + 24, y) not in visited:   # check the cell on the  right
            cell = (x + 24, y)
            solution[cell] = x, y
            #blue.goto(cell)
            #blue.stamp()
            frontier.append(cell)
            visited.add((x +24, y))

        if(x, y + 24) in path and (x, y + 24) not in visited:  # check the cell up
            cell = (x, y + 24)
            solution[cell] = x, y
            #blue.goto(cell)
            #blue.stamp()
            frontier.append(cell)
            visited.add((x, y + 24))
        yellow.goto(x,y)
        yellow.stamp()


def backRoute(x, y):
    red.goto(x, y)
    red.stamp()
    while (x, y) != (start_x, start_y):    # stop loop when current cells == start cell
        red.goto(solution[x, y])        # move the yellow sprite to the key value of solution ()
        red.stamp()
        x, y = solution[x, y]               # "key value" now becomes the new key

# set up classes
maze = Maze()
red = Red()
blue = Blue()
green = Green()
yellow = Yellow()

# setup lists
walls = []
path = []
visited = set()
frontier = deque()
solution = {}                           # solution dictionary


# main program starts here ####
setup_maze(grid)
search(start_x,start_y)
backRoute(end_x, end_y)
wn.exitonclick()