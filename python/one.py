#!/usr/bin/python
#coding=utf-8

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

Account={'InitMoney':1000.0,'Crash':1000.0,'FutureNum':0,'AllMoney':1000.0,'OneProfit':0.0,'Profit':0.0,'BuyPrice':0,'SellPrice':0}

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
                    print "********************************************************************************"
                    print '时间\t'.decode('gbk')+TimeStyle
                    print "方向\t买多".decode('gbk')
                    print '买入价\t'.decode('gbk')+dataMat[0]
                    print "***************************************"
                    print '账户余额\t'.decode('gbk')+Account['Crash']+'\t账户总额\t'.decode('gbk')+Account['AllMoney']+'\t盈利\t'.decode('gbk')+Account['Profit']
                    Account['BuyPrice']=dataMat[0]
                    Account['SellPrice']=0
                    Account['FutureNum']=1
                    Account['Crash']=Account['Crash']-219.9
                    Account['OneProfit']=0.0
                    Account['AllMoney']=Account['Crash']+180
                    Account['Profit']=Account['AllMoney']-Account['InitMoney']
                    print '账户余额\t'.decode('gbk')+Account['Crash']+'\t账户总额\t'.decode('gbk')+Account['AllMoney']+'\t盈利\t'.decode('gbk')+Account['Profit']
                    print "********************************************************************************"
                    More=1
                if dataMat[0]<min(dataMat[1:SHORT]) and More==1:
                    print "********************************************************************************"
                    print '时间\t'.decode('gbk')+TimeStyle
                    print "方向\t卖多".decode('gbk')
                    print '卖出价\t'.decode('gbk')+dataMat[0]
                    print "***************************************"
                    print '账户余额\t'.decode('gbk')+Account['Crash']+'\t账户总额\t'.decode('gbk')+Account['AllMoney']+'\t盈利\t'.decode('gbk')+Account['Profit']
                    Account['SellPrice']=dataMat[0]
                    Account['FutureNum']=0
                    Account['OneProfit']=(Account['SellPrice']-Account['BuyPrice'])*30
                    Account['Crash']=Account['Crash']+180+Account['OneProfit']
                    Account['AllMoney']=Account['Crash']
                    Account['Profit']=Account['AllMoney']-Account['InitMoney']
                    print '账户余额\t'.decode('gbk')+Account['Crash']+'\t账户总额\t'.decode('gbk')+Account['AllMoney']+'\t盈利\t'.decode('gbk')+Account['Profit']+'\t单笔盈亏\t'.decode('gbk')+Account['OneProfit']
                    print "********************************************************************************"
                    More=0
                if dataMat[0]<min(dataMat[1:]) and Empty==0:
                    print "********************************************************************************"
                    print '时间\t'.decode('gbk')+TimeStyle
                    print "方向\t买空".decode('gbk')
                    print '买入价\t'.decode('gbk')+dataMat[0]
                    print "***************************************"
                    print '账户余额\t'.decode('gbk')+Account['Crash']+'\t账户总额\t'.decode('gbk')+Account['AllMoney']+'\t盈利\t'.decode('gbk')+Account['Profit']
                    Account['BuyPrice']=dataMat[0]
                    Account['SellPrice']=0
                    Account['FutureNum']=-1
                    Account['Crash']=Account['Crash']-219.9
                    Account['OneProfit']=0.0
                    Account['AllMoney']=Account['Crash']+180
                    Account['Profit']=Account['AllMoney']-Account['InitMoney']
                    print '账户余额\t'.decode('gbk')+Account['Crash']+'\t账户总额\t'.decode('gbk')+Account['AllMoney']+'\t盈利\t'.decode('gbk')+Account['Profit']
                    print "********************************************************************************"
                    Empty=1
                if dataMat[0]>max(dataMat[1:SHORT]) and Empty==1:
                    print "********************************************************************************"
                    print '时间\t'.decode('gbk')+TimeStyle
                    print "方向\t卖空".decode('gbk')
                    print '卖出价\t'.decode('gbk')+dataMat[0]
                    print "***************************************"
                    print '账户余额\t'.decode('gbk')+Account['Crash']+'\t账户总额\t'.decode('gbk')+Account['AllMoney']+'\t盈利\t'.decode('gbk')+Account['Profit']
                    Account['SellPrice']=dataMat[0]
                    Account['FutureNum']=0
                    Account['OneProfit']=(Account['BuyPrice']-Account['SellPrice'])*30
                    Account['Crash']=Account['Crash']+180+Account['OneProfit']
                    Account['AllMoney']=Account['Crash']
                    Account['Profit']=Account['AllMoney']-Account['InitMoney']
                    print '账户余额\t'.decode('gbk')+Account['Crash']+'\t账户总额\t'.decode('gbk')+Account['AllMoney']+'\t盈利\t'.decode('gbk')+Account['Profit']+'\t单笔盈亏\t'.decode('gbk')+Account['OneProfit']
                    print "********************************************************************************"
                    Empty= 0
