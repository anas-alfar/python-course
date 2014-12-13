#!/usr/bin/python3
__author__ = 'anas@al-far.com'

import mymath

def main():
    print('=========== main ===========')
    mymath.getAvgFloatingPoint(1245, 13)
    mymath.getAvgInteger(1245, 13)
    mymath.getAvgIntegerCasting(1245, 13)
    mymath.getAvgRounded(1245, 13)
    mymath.getAvgRoundedWithDecimalPoint(1245, 13)
    mymath.getAvgMod(1245, 13)
    mymath.getAvgWithSecondParamDefault(750)
    mymath.getAvgWithAllParamsDefault()

main()
