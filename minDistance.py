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
    return Point(random.randint(150,600), random.randint(150,600))

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

def merge(start,to,start2,t2,ans, comparator):


def copy(ans,)

def rec(l,r):
    global a
    if (r - l <= 3):
        for i in (l,r):
            for j in (i+1,r):
                upd_ans(a[i],a[j])
    median = (l+r)/2
    medianx = a[median].x
    rec(l,median),rec(median+1,r)
    t = []
    t = merge(a+l,a+m+1,a+m+1,a+r+1)


    tsz = 0
    for i in (l,r):
        if (math.fabs(a[i].x-medianx) < mindist):
            j = tsz
            while(j >= 0):
                if (a[i].y-t[j].y >= mindist):
                    break
                upd_ans(a[i],t[j])
                j-=1
            tsz+=1
            t[tsz] =a[i]
    print('happens')

def main():
    global a
    a = init()
    window = initWin()
    a.sort(key = cmp_to_key(cmp_x))
    rec = (0, length)
    for i in a:
        i.draw(window)
    l = Line(ansa,ansb)
    l.draw(window)
    print('hi')
    a = input()
main()