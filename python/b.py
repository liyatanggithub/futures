#!/usr/bin/python

def ifMax(a,Arr):
    if len(Arr)>=2*a+1:
        if Arr[a]==max(Arr[:2*a+1]):
            print "a is max"
            return 1
        else:
            print "a is not the max"
    else:
        print "Arr is not long enough"
    return 0

def ifMin(a,Arr):
    if len(Arr)>=2*a+1:
        if Arr[a]==min(Arr[:2*a+1]):
            print "a is min"
            return 1
        else:
            print "a is not the min"
    else:
        print "Arr is not long enough"
    return 0

