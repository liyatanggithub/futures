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

NowTime=time.time()
LastTime=NowTime
FirstTime=NowTime
FileName=str(NowTime)
dataMat=[];lablMat=[]
while True:
    NowTime=time.time()
    if (NowTime-LastTime)>=TIMEVALUE:
        LastTime=NowTime
        GetStr=urlopen(URL).read()
        f=open(FileName,"a")
        f.writelines("%f," % NowTime + GetStr)
        f.close()
        dataMat.append([1.0,NowTime-FirstTime])
        lablMat.append(string.atof(GetStr[65:69]))
        ws=standRegres(dataMat,lablMat)
        print ws
        #print GetStr+'%f' % NowTime
        #print GetStr[65:69]
