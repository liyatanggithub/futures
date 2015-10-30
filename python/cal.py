#!/usr/bin/python

import string
import time

FileName=raw_input("Please enter file name : ")
f=open(FileName, "r")

while True:
    s=f.readline()
    if s == "" :
        break
    NowPrice = string.atoi(s[85:89])
    print "%d"%NowPrice
f.close()
while True:
    time.sleep(1)
