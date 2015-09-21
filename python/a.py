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

NowTime=float(int(time.time()))
LastTime=NowTime
FirstTime=NowTime
FileName=str(NowTime)
dataMat=[];lablMat=[]
ws=[]
CountNum=0
while True:
    NowTime=time.time()
    if (NowTime-LastTime)>=TIMEVALUE:
        CountNum += 1
        LastTime=NowTime
        try:
            GetStr=urlopen(URL).read()
        except:
            print "Get URL ERROR"
        else:
           # f=open(FileName,"a")
           # f.writelines("%f," % NowTime + GetStr)
           # f.close()

            dataMat.insert(0,([1.0,NowTime-FirstTime]))
            lablMat.insert(0,(string.atof(GetStr[65:69])))
            if CountNum>LONG:
                dataMat.pop()
                lablMat.pop()
                ws=standRegres(dataMat,lablMat)
                print ws[1][0]*10000
        #print GetStr+'%f' % NowTime
        #print GetStr[65:69]
