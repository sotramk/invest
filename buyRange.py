#!/bin/python

# This is a program to calculate a buy range for a proper buy point.
# 5% added to the proper buy point.


def stkData():
    ni = i.upper()
    b = input('Buy point? ')
    t = float(b) * 1.05
    t = round(t,2)
    print(str(i) + ' -- ' + str(b) + ' -- ' + str(t))
    txt = str(ni) + ' -- ' + str(b) + ' -- ' + str(t)
    f.write(str(txt))
    f.write("\n")
    f.write("\n")

f = open("buyRange.txt", "a")
while True:
    i = input('Symbol? ')
    if i == '':
        f.close()
        break
    stkData()
