#!/usr/bin/python3
__author__ = 'anas@al-far.com'
__version__ = "1.0.0"

def main():
    print('=========== main ===========')
    getAvgFloatingPoint(1245, 13)
    getAvgInteger(1245, 13)
    getAvgIntegerCasting(1245, 13)
    getAvgRounded(1245, 13)
    getAvgRoundedWithDecimalPoint(1245, 13)
    getAvgMod(1245, 13)
    getAvgWithSecondParamDefault(750)
    getAvgWithAllParamsDefault()

def getAvgFloatingPoint(total, count):
    print('The (Float) average is: {}'.format(total/count))

def getAvgInteger(total, count):
    print('The (Integer) average is: {}'.format(total//count))

def getAvgIntegerCasting(total, count):
    print('The (Integer) average is: {}'.format(int(total/count)))

def getAvgRounded(total, count):
    print('The (Rounded) average is: {}'.format(round(total/count)))

def getAvgRoundedWithDecimalPoint(total, count):
    print('The (Rounded) average is: {}'.format(round(total/count, 2)))

def getAvgMod(total, count):
    print('The (Modulus of) average is: {}'.format(total%count))

def getAvgWithSecondParamDefault(total, count=10):
    print('The (Float) average is: {}'.format(total/count))

def getAvgWithAllParamsDefault(total=1000, count=10):
    print('The (Float) average is: {}'.format(total/count))

if __name__ == '__main__': main()