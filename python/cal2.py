#!/usr/bin/python

import string
import time
import matplotlib.pyplot as plt

FileName = raw_input("Please enter file name : ")
f        = open(FileName, "r")

dataMat = [0]
Vertex  = [[0],[0],[0]]
Aaa     = 0
Bbb     = 0
Ccc     = 0
xMax    = 10
yMin    = 10000
yMax    = 0

while True:
    s=f.readline()
    if s == "" :
        break
    NowPrice = string.atoi(s[85:89])
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

    dataMat.append(Bbb)

    if len(Vertex[1]) == 1 :
        Vertex[1][0] = dataMat[1]
        Vertex[0][0] = 1
    if len(dataMat) > 2 and ((dataMat[-2] > dataMat[-1] and dataMat[-2] > dataMat[-3]) or (dataMat[-2] < dataMat[-1] and dataMat[-2] < dataMat[-3])) :
        if len(Vertex[1]) > 1 and  (Vertex[1][-2] == dataMat[-2] or Vertex[1][-1] == dataMat[-2]) :
            continue
        if Vertex[2][-1] == 1 and dataMat[-2] > dataMat[-1] and dataMat[-2] > dataMat[-3] :
            if Vertex[1][-1] > dataMat[-2] :
                continue
            if Vertex[1][-1] < dataMat[-2] :
                Vertex[1][-1] = dataMat[-2]
                continue
        if Vertex[2][-1] == -1 and dataMat[-2] < dataMat[-1] and dataMat[-2] < dataMat[-3] :
            if Vertex[1][-1] < dataMat[-2] :
                continue
            if Vertex[1][-1] > dataMat[-2] :
                Vertex[1][-1] = dataMat[-2]
                continue

        Vertex[1].append(dataMat[-2])
        Vertex[0].append(Vertex[0][-1]+1)
        if dataMat[-2] > dataMat[-1] and dataMat[-2] > dataMat[-3] :
            Vertex[2].append(1)
        if dataMat[-2] < dataMat[-1] and dataMat[-2] < dataMat[-3] :
            Vertex[2].append(-1)

    if Vertex[0][-1]>=xMax :
        xMax = xMax +10
        plt.axis([0, xMax, yMin, yMax])
    if Vertex[1][-1]<=yMin :
        yMin = Vertex[1][-1]-10
        plt.axis([0, xMax, yMin, yMax])
    if Vertex[1][-1]>=yMax :
        yMax = Vertex[1][-1]+10
        plt.axis([0, xMax, yMin, yMax])
        plt.axis([0, xMax, yMin, yMax])
    plt.plot(Vertex[0], Vertex[1],color="blue", linewidth=1.0, linestyle="-")
    plt.pause(0.00001)

f.close()
while True:
    time.sleep(1)
