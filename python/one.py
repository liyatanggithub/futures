#!/usr/bin/python

from urllib import urlopen
#from numpy import *
import string
import time

LONG=30
SHORT=15
TIMEVALUE=6.0
URL="http://hq.sinajs.cn/list=AG1512"

NowTime=float(int(time.time()))
LastTime=NowTime
FirstTime=NowTime
#FileName=str(NowTime)
dataMat=[]
CountNum=0
More=0
Empty=0

Account={'InitMoney':1000.0,'Crash':1000.0,'FutureNum':0,'NowMoney':1000.0,'Profit':0.0,'BuyPrice':0.0}

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
            #f=open(FileName,"a")
            #f.writelines("%f," % NowTime + GetStr)
            #f.close()

            dataMat.insert(0,(string.atoi(GetStr[65:69])))
            if CountNum>LONG:
                dataMat.pop()

                TimeStyle=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(int(NowTime)))
                if dataMat[0]>max(dataMat[1:]) and More==0:
                    print TimeStyle+" 买多"
                    print '最新价:'+dataMat[0]
                    print '账户余额:'+Account['Crash']
                    More=1
                if dataMat[0]<min(dataMat[1:SHORT]) and More==1:
                    print dataMat
                    print TimeStyle+" Sell more"
                    More=0
                if dataMat[0]<min(dataMat[1:]) and Empty==0:
                    print dataMat
                    print TimeStyle+" Buy Empty"
                    Empty=1
                if dataMat[0]>max(dataMat[1:SHORT]) and Empty==1:
                    print dataMat
                    print TimeStyle+" Sell Empty"
                    Empty=0
