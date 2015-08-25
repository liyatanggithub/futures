#!/usr/bin/python
from urllib import urlopen
out=urlopen('http://hq.sinajs.cn/list=AG1512').read()
import string
test=string.atof(out[35:39])
print out
print test
