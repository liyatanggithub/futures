#!/usr/bin/python

from urllib import urlopen
import string
import time

LONG=200
TIMEVALUE=6.0
URL="http://hq.sinajs.cn/list=AG1512"

NowTime=time.time()
LastTime=NowTime
FileName=str(NowTime)
while True:
    NowTime=time.time()
    if (NowTime-LastTime)>=TIMEVALUE:
        LastTime=NowTime
        GetStr=urlopen(URL).read()
        f=open(FileName,"a")
        f.writelines("%f," % NowTime + GetStr)
        f.close()
        print GetStr+'%f' % NowTime
        print GetStr[65:69]
