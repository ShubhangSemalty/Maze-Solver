import cv2
import numpy as np
from numpy import *

maze = cv2.imread('capture_BINARY.png')
maze = cv2.cvtColor(maze, cv2.COLOR_BGR2GRAY)
binary = cv2.threshold(maze, 200, 255, cv2.THRESH_BINARY)[1]
cv2.imshow('maze',binary)

#The size of each block of the maze (path and the wall currently)
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

#Finding the starting and ending points of the Maze 
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
print(imgMat)
               