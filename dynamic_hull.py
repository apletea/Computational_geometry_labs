import random
from graphics import *


min_x = 700
max_x = 0
min_y = 700
max_y = 0

def newPoint():
    return Point(random.randint(350,500), random.randint(350,500))

def initWin():
    return GraphWin("Where is Point",700, 700)

def is_right(a,b,c):
    return ((b.x-a.x)*(c.y-a.y) - (b.y-a.y)*(c.x-a.x)) < 0

def is_in_line(a,b,c):
    return ((b.x-a.x)*(c.y-a.y) - (b.y-a.y)*(c.x-a.x)) == 0


def find_max_min(set):
    global min_x
    global min_y
    global max_x
    global max_y
    for p in set:
        if (p.x > max_x ):
            max_x = p.x
        if (p.x < min_x):
            min_x = p.x
        if (p.y > max_y):
            max_y = p.y
        if (p.y < min_y):
            min_y = p.y

def first3(set):
    p = newPoint()
    while (p == set[0]):
        p = newPoint()
    set.append(p)
    p = newPoint()
    while(p == set[0] or p == set[1]):
        p = newPoint()
    set.append(p)
    find_max_min(set)

def



def main():
    set = []
    set.append(newPoint())
    first3(set)
    b= 1
    while (b==1):
        p = newPoint()
        if (notInConvex(p2)):




        b = input()


main()