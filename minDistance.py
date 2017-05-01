import random
from graphics import *

length = 30


def newPoint():
    return Point(random.randint(350,500), random.randint(350,500))

def init():
    points = []
    for i in range (0,length):
        points.append(newPoint())
    return points


def initWin():
    return GraphWin("Where is Point",700, 700)

def main():
    print('hi')
main()