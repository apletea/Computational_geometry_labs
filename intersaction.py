import random
import math
from graphics import *
import GrahamAlg as createHull


length = 30

def newPoint():
    return Point(random.randint(150,600), random.randint(150,600))

def init():
    points = []
    for i in range (0,length):
        points.append(newPoint())
    return points

def initWin():
    return GraphWin("Where is Point",700, 700)


def drawHulls(set1,set2,win):
    first = set1[0]
    cur = first
    for point in set1:
        line = Line(cur,point)
        line.draw(win)
        cur = point
    line = Line(cur,first)
    line.draw(win)
    first = set2[0]
    cur = first
    for point in set2:
        line = Line(cur, point)
        line.draw(win)
        cur = point
    line = Line(cur, first)
    line.draw(win)




def main():
    set1 = init()
    set2 = init()
    set1 = createHull.draw(set1)
    set2 = createHull.draw(set2)
    window = initWin()
    drawHulls(set1,set2,window)
    polygon = Polygon(set1)
    polygon.setFill('red')
    polygon.draw(window)
    a = input()
main()

