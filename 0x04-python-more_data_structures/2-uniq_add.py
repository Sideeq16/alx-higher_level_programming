#!/usr/bin/python3

def uniq_add(mylist=[]):
    uniqNum = []
    totalNum = 0
    for i in mylist:
        if i not in uniqNum:
            totalNum +=i
            uniqNum.append(i)
    return totalNum
