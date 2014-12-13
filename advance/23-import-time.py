#!/usr/bin/python3
__author__ = 'anas@al-far.com'

import time, datetime, math, os, sys

def main():
    print('=========== main ===========')
    now = datetime.datetime.now()
    print("The current time is: ", time.ctime())
    print("The current month is: ", now.month)
    print("Factorial of 5 is: ", math.factorial(5))
    print("The current working directory is: ", os.getcwd())
    print("My OS platform is: ", sys.platform)
    print("PATH env is : ", os.getenv('PATH'))

main()
