#!/usr/bin/python

import string
import time
import matplotlib.pyplot as plt

FileName=raw_input("Please enter file name : ")
f=open(FileName, "r")

dataMat=[[0],[0]]
Aaa=0
Bbb=0
Ccc=0
xMax=100
yMin=10000
yMax=0

Money=1000
BuyPrice=0
MoreOrEmpty=0
LineHigh=0
LineLow=10000

Vertex=[]

while True:
    s=f.readline()
    if s == "" :
        break
    NowPrice = string.atoi(s[85:89])
    #print "%d"%NowPrice
    if NowPrice >= Aaa and NowPrice <= Ccc :
        continue
    if Ccc < NowPrice :
        Ccc = NowPrice
        Bbb = Ccc-1
        Aaa = Bbb-1
    if Aaa > NowPrice :
        Aaa = NowPrice
        Bbb = Aaa+1
        Ccc = Bbb+1

    dataMat[1].append(Bbb)
    dataMat[0].append(dataMat[0][-1]+1)
    if len(dataMat[1])>10:
        dataMat[1].pop(0)
        dataMat[0].pop(0)
    if dataMat[0][-1]>=xMax :
        xMax = xMax +100
        plt.axis([0, xMax, yMin, yMax])
    if dataMat[1][-1]<=yMin :
        yMin = dataMat[1][-1]-10
        plt.axis([0, xMax, yMin, yMax])
    if dataMat[1][-1]>=yMax :
        yMax = dataMat[1][-1]+10
        plt.axis([0, xMax, yMin, yMax])
        plt.axis([0, xMax, yMin, yMax])
    plt.plot(dataMat[0], dataMat[1],color="blue", linewidth=1.0, linestyle="-")
    plt.pause(0.00001)

    if len(Vertex) == 0 :
        Vertex.append(dataMat[1][1])
    if len(dataMat[1]) > 2 and ((dataMat[1][-2] > dataMat[1][-1] and dataMat[1][-2] > dataMat[1][-3]) or (dataMat[1][-2] < dataMat[1][-1] and dataMat[1][-2] < dataMat[1][-3])) :
        Vertex.append(dataMat[1][-2])
        if MoreOrEmpty == 1 and Vertex[-1] > LineHigh :
            LineHigh = Vertex[-1]
            LineLow = Vertex[-2]
        if MoreOrEmpty == -1 and Vertex[-1] < LineLow :
            LineLow = Vertex[-1]
            LineHigh = Vertex[-2]

    if MoreOrEmpty == 1 and len(Vertex) > 1  and Bbb < LineLow :
        print "Sell More with Price\t"+"%d"%NowPrice
        print "Money\t"+"%d"%Money+"+("+"%d"%NowPrice+"-"+"%d"%BuyPrice+")="+"%d"%(Money+NowPrice-BuyPrice)
        Money=Money+NowPrice-BuyPrice
        MoreOrEmpty=0
        LineHigh=0
        LineLow=10000
    if MoreOrEmpty == -1 and len(Vertex) > 1 and Bbb > LineHigh :
        print "Sell Empty with Price\t"+"%d"%NowPrice
        print "Money\t"+"%d"%Money+"-("+"%d"%NowPrice+"-"+"%d"%BuyPrice+")="+"%d"%(Money-NowPrice+BuyPrice)
        Money=Money-NowPrice+BuyPrice
        MoreOrEmpty=0
        LineHigh=0
        LineLow=10000

    if MoreOrEmpty == 0 :
        if len(dataMat[1]) > 2 and dataMat[1][-2] < dataMat[1][-1] :
            print "Buy More\t"+" %d"%NowPrice
            BuyPrice=NowPrice
            MoreOrEmpty=1
            LineLow=Vertex[-1]
        if len(dataMat[1]) > 2 and dataMat[1][-2] > dataMat[1][-1] :
            print "Buy Empty\t"+"%d"%NowPrice
            BuyPrice=NowPrice
            MoreOrEmpty=-1
            LineHigh=Vertex[-1]
f.close()
while True:
    time.sleep(1)
