#!/usr/bin/python

import urllib2
import socket
import string
import time
import matplotlib.pyplot as plt

TIMEVALUE=6.0
URL="http://hq.sinajs.cn/list=AG1512"

socket.setdefaulttimeout(4)
NowTime=float(int(time.time()))
LastTime=NowTime
FirstTime=NowTime
FileName=str(NowTime)

#m00=time.mktime(time.strptime('2000-01-01 00:00:00',"%Y-%m-%d %H:%M:%S"))
m23=time.mktime(time.strptime('2000-01-01 02:30:00',"%Y-%m-%d %H:%M:%S"))
m90=time.mktime(time.strptime('2000-01-01 09:00:00',"%Y-%m-%d %H:%M:%S"))
m113=time.mktime(time.strptime('2000-01-01 11:30:00',"%Y-%m-%d %H:%M:%S"))
m133=time.mktime(time.strptime('2000-01-01 13:30:00',"%Y-%m-%d %H:%M:%S"))
m150=time.mktime(time.strptime('2000-01-01 15:00:00',"%Y-%m-%d %H:%M:%S"))
m210=time.mktime(time.strptime('2000-01-01 21:00:00',"%Y-%m-%d %H:%M:%S"))
#m235=time.mktime(time.strptime('2000-01-01 23:59:59',"%Y-%m-%d %H:%M:%S"))

while True:
    plt.pause(0.00001)
    cpStrNowTime=time.strftime("%Y-%m-%d %H:%M:%S")
    cpListNowTime=list(cpStrNowTime)
    cpListNowTime[:10]=['2','0','0','0','-','0','1','-','0','1']
    cpStr2000Time=''.join(cpListNowTime)
    cp2000Time=time.mktime(time.strptime(cpStr2000Time,"%Y-%m-%d %H:%M:%S"))
    if (cp2000Time>=m23 and cp2000Time<=m90) or (cp2000Time>=m113 and cp2000Time<=m133) or (cp2000Time>=m150 and cp2000Time<=m210):
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
            TimeStyle=time.strftime("%Y-%m-%d %H:%M:%S")
            f=open(FileName,"a")
            f.writelines(TimeStyle + " " + GetStr)
            f.close()
