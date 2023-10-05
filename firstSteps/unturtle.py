import math
from swampy.TurtleWorld import *

world = TurtleWorld()
bob = Turtle()



def square(t, length, degrees):
    for x in range(80):
        for i in range(4):
            fd(t,length)
            lt(bob, degrees)
        fd(t,length)


bob.delay=0.01
square(bob, 20, 90)

#bob2 = Turtle()
def polygon(t, n, length):
    angle = 360.0 / n
    for i in range(n):
        fd(t, length)
        lt(t, angle)


#polygon(bob2, 7,70)

bob3 = Turtle()
bob3.delay = 0.01
def circle(t, r):
    circumference = 2 * math.pi * r
    n = int(circumference / 3) + 1
    length = circumference / n
    polygon(t, n, length)


#circle(bob3,500 )



wait_for_user()