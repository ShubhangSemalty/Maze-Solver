# Maze-Solver

Breadth First algorithm to solve mazes from an input image.

Input
Some example mazes are included in the repository. These were generated by using the following website: https://hereandabove.com/maze/mazeorig.form.html

Each maze is black and white. White represents paths, black represents walls.
All mazes are surrounded entirely by black walls.
Two white square exists on the boundary walls of the image, and are marked as either the start or the goal of the maze(supposed).
Steps
The image is initially converted into grayscale and then a threshold operation is performed to eliminate the possibility of the different shades of grey and white the could occur while snipping or downloading the image from the generator site
It is then converted into a matrix of 0s and 1s having the exact size as that of the maze in terms of the blocks.
0s represent the walls and 1s represent the path of the image to be followed from the start to reach the end.
The start and end points for the maze are found and are allocated the values 2 and 3 respectively in the block matrix.
Once the matrix is ready, the maze is recreated using the turtle module in python and the is solved by using the breadth-first search algorithm.
Using this we traverse the maze while exploring all the possible paths and once the traversal is complete and an optimum path is calculated, it is marked on the maze using a backtracking algorithm
