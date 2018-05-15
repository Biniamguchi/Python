# try this either as a .py file or in the python shellcopy
import turtle
# the distance we want the pointer to travel each time
DIST = 100
for x in range(0,6):
    print "x", x
    for y in range(1,5):
        print "y", y
        # turn the pointer 90 degrees to the right
        turtle.right(90)
        # advance according to set distance
        turtle.forward(DIST)
    # add to set distance
    DIST += 20

# from turtle import *

# tanenbaum = Turtle()

# tanenbaum.hideturtle()
# tanenbaum.speed(20)

# for i in range(350):
#     tanenbaum.forward(i)
#     tanenbaum.right(98)

# import turtle
# import math

# dist = 1
# ang  = 0

# for i in range(0,1000):
#     turtle.right(ang)
#     turtle.forward(dist)
    
#     ang = 1.618*i
#     dist += 4
