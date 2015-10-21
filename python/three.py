#!/usr/bin/python
#coding=utf-8

#from urllib import urlopen
import urllib2
import socket
#from numpy import *
import string
import time
import matplotlib.pyplot as plt

LONG=30
SHORT=15
TIMEVALUE=6.0
INITMONEY=1000.0
URL="http://hq.sinajs.cn/list=AG1512"

xMax=100
yMin=10000
yMax=0
socket.setdefaulttimeout(4)
NowTime=float(int(time.time()))
LastTime=NowTime
FirstTime=NowTime
#FileName=str(NowTime)
dataMat=[[0],[0]]
More=0
Empty=0
Aaa=0
Bbb=0

#m00=time.mktime(time.strptime('2000-01-01 00:00:00',"%Y-%m-%d %H:%M:%S"))
m23=time.mktime(time.strptime('2000-01-01 02:30:00',"%Y-%m-%d %H:%M:%S"))
m90=time.mktime(time.strptime('2000-01-01 09:00:00',"%Y-%m-%d %H:%M:%S"))
m113=time.mktime(time.strptime('2000-01-01 11:30:00',"%Y-%m-%d %H:%M:%S"))
m133=time.mktime(time.strptime('2000-01-01 13:30:00',"%Y-%m-%d %H:%M:%S"))
m150=time.mktime(time.strptime('2000-01-01 15:00:00',"%Y-%m-%d %H:%M:%S"))
m210=time.mktime(time.strptime('2000-01-01 21:00:00',"%Y-%m-%d %H:%M:%S"))
#m235=time.mktime(time.strptime('2000-01-01 23:59:59',"%Y-%m-%d %H:%M:%S"))

Account={'InitMoney':INITMONEY,'Crash':INITMONEY,'FutureNum':0,'AllMoney':INITMONEY,'OneProfit':0.0,'Profit':0.0,'BuyPrice':0,'SellPrice':0}

while True:
    cpStrNowTime=time.strftime("%Y-%m-%d %H:%M:%S")
    cpListNowTime=list(cpStrNowTime)
    cpListNowTime[:10]=['2','0','0','0','-','0','1','-','0','1']
    cpStr2000Time=''.join(cpListNowTime)
    cp2000Time=time.mktime(time.strptime(cpStr2000Time,"%Y-%m-%d %H:%M:%S"))
    if (cp2000Time>=m23 and cp2000Time<=m90) or (cp2000Time>=m113 and cp2000Time<=m133) or (cp2000Time>=m150 and cp2000Time<=m210):
        print "ÐÝÊÐÊ±¼ä\t".decode('gbk')+cpStrNowTime
        time.sleep(10)
        continue

    time.sleep(1)
    NowTime=time.time()
    if (NowTime-LastTime)>=TIMEVALUE:
        LastTime=NowTime
        try:
            GetStr=urllib2.urlopen(URL).read()
        except :
            print "Get URL ERROR"
        else:
            plt.pause(0.00001)
            if Aaa == 0 :
                Aaa = string.atoi(GetStr[65:69])
                continue

            if Aaa != string.atoi(GetStr[65:69]) and Bbb == 0 :
                Bbb = string.atoi(GetStr[65:69])
                continue

            if Aaa != string.atoi(GetStr[65:69]) and Bbb != string.atoi(GetStr[65:69]) :
                Aaa = Bbb
                Bbb = string.atoi(GetStr[65:69])

                TimeStyle=time.strftime("%Y-%m-%d %H:%M:%S")
                print TimeStyle+"\t%f"%((Aaa + Bbb)/2.0)
                dataMat[1].append((Aaa + Bbb)/2.0)
                dataMat[0].append(dataMat[0][-1]+1)
                if dataMat[0][-1]>=xMax :
                    xMax = xMax +100
                    plt.axis([0, xMax, yMin, yMax])
                if dataMat[1][-1]<=yMin :
                    yMin = dataMat[1][-1]-10
                    plt.axis([0, xMax, yMin, yMax])
                if dataMat[1][-1]>=yMax :
                    yMax = dataMat[1][-1]+10
                    plt.axis([0, xMax, yMin, yMax])
                plt.plot(dataMat[0], dataMat[1],color="blue", linewidth=1.0, linestyle="-")
                plt.pause(0.00001)
