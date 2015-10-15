#!/usr/bin/python
#coding=utf-8

#from urllib import urlopen
import urllib2
import socket
#from numpy import *
import string
import time

LONG=30
SHORT=15
TIMEVALUE=6.0
INITMONEY=1000.0
URL="http://hq.sinajs.cn/list=AG1512"

socket.setdefaulttimeout(4)
NowTime=float(int(time.time()))
LastTime=NowTime
FirstTime=NowTime
#FileName=str(NowTime)
dataMat=[]
More=0
Empty=0

Account={'InitMoney':INITMONEY,'Crash':INITMONEY,'FutureNum':0,'AllMoney':INITMONEY,'OneProfit':0.0,'Profit':0.0,'BuyPrice':0,'SellPrice':0}

while True:
    NowTime=time.time()
    if (NowTime-LastTime)>=TIMEVALUE:
        LastTime=NowTime
        try:
            GetStr=urllib2.urlopen(URL).read()
        except :
            print "Get URL ERROR"
        else:
            #f=open(FileName,"a")
            #f.writelines("%f," % NowTime + GetStr)
            #f.close()

            dataMat.insert(0,(string.atoi(GetStr[65:69])))
            print dataMat
            if len(dataMat)==LONG:
                dataMat.pop()

                TimeStyle=time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(int(NowTime)))
                if Account['FutureNum'] != 0 :
                    if (dataMat[0]-Account['BuyPrice'])*30 >= 180 or (dataMat[0]-Account['BuyPrice'])*30 <= -180 :
                        print "********************************************************************************"
                        print '时间\t'.decode('gbk')+TimeStyle
                        print '方向\t溢出清仓'.decode('gbk')
                        print '清仓价\t'.decode('gbk')+'%d'%dataMat[0]
                        print "***************************************"
                        print '账户余额\t'.decode('gbk')+'%f'%Account['Crash']+'\t账户总额\t'.decode('gbk')+'%f'%Account['AllMoney']+'\t盈利\t'.decode('gbk')+'%f'%Account['Profit']
                        Account['BuyPrice']=0
                        Account['SellPrice']=0
                        Account['FutureNum']=0
                        Account['OneProfit']=-219.9
                        Account['AllMoney']=Account['Crash']
                        Account['Profit']=Account['AllMoney']-Account['InitMoney']
                        print '账户余额\t'.decode('gbk')+'%f'%Account['Crash']+'\t账户总额\t'.decode('gbk')+'%f'%Account['AllMoney']+'\t盈利\t'.decode('gbk')+'%f'%Account['Profit']+'\t单笔盈亏\t'.decode('gbk')+'%f'%Account['OneProfit']
                        print "********************************************************************************"
                        More=0
                        Empty= 0
                        continue

                if dataMat[0]>max(dataMat[1:]) and More==0:
                    More=1
                    print "********************************************************************************"
                    print '时间\t'.decode('gbk')+TimeStyle
                    print '预备购多'.decode('gbk')
                    print "********************************************************************************"
                    continue
                if More>0 :
                    More=More+1
                    if More==12:
                        print "********************************************************************************"
                        print '时间\t'.decode('gbk')+TimeStyle
                        print '取消预备购多'.decode('gbk')
                        print "********************************************************************************"
                        More=0
                        continue
                if dataMat[0]<min(dataMat[1:]) and Empty==0:
                    print "********************************************************************************"
                    print '时间\t'.decode('gbk')+TimeStyle
                    print '预备购空'.decode('gbk')
                    print "********************************************************************************"
                    Empty=1
                    continue
                if Empty>0 :
                    Empty=Empty+1
                    if Empty==12:
                        print "********************************************************************************"
                        print '时间\t'.decode('gbk')+TimeStyle
                        print '取消预备购空'.decode('gbk')
                        print "********************************************************************************"
                        Empty=0
                        continue
                if dataMat[0]<min(dataMat[1:SHORT]) and More==-1:
                    print "********************************************************************************"
                    print '时间\t'.decode('gbk')+TimeStyle
                    print '方向\t卖多'.decode('gbk')
                    print '卖出价\t'.decode('gbk')+'%d'%dataMat[0]
                    print "***************************************"
                    print '账户余额\t'.decode('gbk')+'%f'%Account['Crash']+'\t账户总额\t'.decode('gbk')+'%f'%Account['AllMoney']+'\t盈利\t'.decode('gbk')+'%f'%Account['Profit']
                    Account['SellPrice']=dataMat[0]
                    Account['FutureNum']=0
                    Account['OneProfit']=(Account['SellPrice']-Account['BuyPrice'])*30-39.9
                    Account['Crash']=Account['Crash']+180+Account['OneProfit']+39.9
                    Account['AllMoney']=Account['Crash']
                    Account['Profit']=Account['AllMoney']-Account['InitMoney']
                    print '账户余额\t'.decode('gbk')+'%f'%Account['Crash']+'\t账户总额\t'.decode('gbk')+'%f'%Account['AllMoney']+'\t盈利\t'.decode('gbk')+'%f'%Account['Profit']+'\t单笔盈亏\t'.decode('gbk')+'%f'%Account['OneProfit']
                    print "********************************************************************************"
                    More=0
                    continue
                if dataMat[0]>max(dataMat[1:SHORT]) and Empty==-1:
                    print "********************************************************************************"
                    print '时间\t'.decode('gbk')+TimeStyle
                    print '方向\t卖空'.decode('gbk')
                    print '卖出价\t'.decode('gbk')+'%d'%dataMat[0]
                    print "***************************************"
                    print '账户余额\t'.decode('gbk')+'%f'%Account['Crash']+'\t账户总额\t'.decode('gbk')+'%f'%Account['AllMoney']+'\t盈利\t'.decode('gbk')+'%f'%Account['Profit']
                    Account['SellPrice']=dataMat[0]
                    Account['FutureNum']=0
                    Account['OneProfit']=(Account['BuyPrice']-Account['SellPrice'])*30-39.9
                    Account['Crash']=Account['Crash']+180+Account['OneProfit']+39.9
                    Account['AllMoney']=Account['Crash']
                    Account['Profit']=Account['AllMoney']-Account['InitMoney']
                    print '账户余额\t'.decode('gbk')+'%f'%Account['Crash']+'\t账户总额\t'.decode('gbk')+'%f'%Account['AllMoney']+'\t盈利\t'.decode('gbk')+'%f'%Account['Profit']+'\t单笔盈亏\t'.decode('gbk')+'%f'%Account['OneProfit']
                    print "********************************************************************************"
                    Empty= 0
                    continue
                if dataMat[0]>max(dataMat[1:]) and More>0:
                    print "********************************************************************************"
                    print '时间\t'.decode('gbk')+TimeStyle
                    print '方向\t买多'.decode('gbk')
                    print '买入价\t'.decode('gbk')+'%d'%dataMat[0]
                    print "***************************************"
                    print '账户余额\t'.decode('gbk')+'%f'%Account['Crash']+'\t账户总额\t'.decode('gbk')+'%f'%Account['AllMoney']+'\t盈利\t'.decode('gbk')+'%f'%Account['Profit']
                    Account['BuyPrice']=dataMat[0]
                    Account['SellPrice']=0
                    Account['FutureNum']=1
                    Account['Crash']=Account['Crash']-219.9
                    Account['OneProfit']=0.0
                    Account['AllMoney']=Account['Crash']+180
                    Account['Profit']=Account['AllMoney']-Account['InitMoney']
                    print '账户余额\t'.decode('gbk')+'%f'%Account['Crash']+'\t账户总额\t'.decode('gbk')+'%f'%Account['AllMoney']+'\t盈利\t'.decode('gbk')+'%f'%Account['Profit']
                    print "********************************************************************************"
                    More=-1
                    continue
                if dataMat[0]<min(dataMat[1:]) and Empty>0:
                    print "********************************************************************************"
                    print '时间\t'.decode('gbk')+TimeStyle
                    print '方向\t买空'.decode('gbk')
                    print '买入价\t'.decode('gbk')+'%d'%dataMat[0]
                    print "***************************************"
                    print '账户余额\t'.decode('gbk')+'%f'%Account['Crash']+'\t账户总额\t'.decode('gbk')+'%f'%Account['AllMoney']+'\t盈利\t'.decode('gbk')+'%f'%Account['Profit']
                    Account['BuyPrice']=dataMat[0]
                    Account['SellPrice']=0
                    Account['FutureNum']=-1
                    Account['Crash']=Account['Crash']-219.9
                    Account['OneProfit']=0.0
                    Account['AllMoney']=Account['Crash']+180
                    Account['Profit']=Account['AllMoney']-Account['InitMoney']
                    print '账户余额\t'.decode('gbk')+'%f'%Account['Crash']+'\t账户总额\t'.decode('gbk')+'%f'%Account['AllMoney']+'\t盈利\t'.decode('gbk')+'%f'%Account['Profit']
                    print "********************************************************************************"
                    Empty=-1
                    continue
