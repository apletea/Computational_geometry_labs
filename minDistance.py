import random
import math
from graphics import *

length = 30
mindist = 700
ansa = Point(0,0)
ansb = Point(700,700)
a = []

def cmp_x(a,b):
    return a.x < b.x or a.x == b.x and a.y < b.y

def cmp_y(a,b):
    return a.y < b.y

def cmp_to_key(comparator):
    class K(object):
        def __init__(self, obj, *args):
            self.obj = obj
        def __lt__(self, other):
            return comparator(self.obj, other.obj) < 0
        def __gt__(self, other):
            return comparator(self.obj, other.obj) > 0
        def __eq__(self, other):
            return comparator(self.obj, other.obj) == 0
        def __le__(self, other):
            return comparator(self.obj, other.obj) <= 0
        def __ge__(self, other):
            return comparator(self.obj, other.obj) >= 0
        def __ne__(self, other):
            return comparator(self.obj, other.obj) != 0
    return K



def newPoint():
    return Point(random.randint(350,500), random.randint(350,500))

def init():
    points = []
    for i in range (0,length):
        points.append(newPoint())
    return points

def initWin():
    return GraphWin("Where is Point",700, 700)

def upd_ans(a,b):
    dist = math.sqrt((a.x-b.x)**2+(a.y-b.y)**2)
    global mindist, ansa, ansb
    if (dist < mindist):
        mindist = dist
        ansa = a
        ansb = b

def rec(l,r):
    print('happens')

def main():
    global a
    a = init()
    a.sort(key = cmp_to_key(cmp_x))
    rec = (0, length)
    
    print('hi')
main()