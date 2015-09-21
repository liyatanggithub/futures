#!/usr/bin/python

from urllib import urlopen
from numpy import *
import string
import time

LONG=200
TIMEVALUE=6.0
URL="http://hq.sinajs.cn/list=AG1512"

def standRegres(xArr,yArr):
    xMat = mat(xArr); yMat = mat(yArr).T
    xTx = xMat.T*xMat
    if linalg.det(xTx) == 0.0:
        print "This matrix is singular, cannot do inverse"
        return
    ws = xTx.I * (xMat.T*yMat)
    return ws

class TimeLine:
    def SetStart(start):
        self.start = start

    def SetTime(second):
        self.count=second/TIMEVALE

    def ifMax(a,Arr):
        if len(Arr)>=2*a+1:
            if Arr[a]==max(Arr[:2*a+1]):
                print "a is max"
                return 1
            else:
                print "a is not the max"
        else:
            print "Arr is not long enough"
        return 0

    def ifMin(a,Arr):
        if len(Arr)>=2*a+1:
            if Arr[a]==min(Arr[:2*a+1]):
                print "a is min"
                return 1
            else:
                print "a is not the min"
        else:
            print "Arr is not long enough"
        return 0
