#!/usr/bin/python3
__author__ = 'anas@al-far.com'


def main():
    #series()
    #collectMarks()
    #handleConnections1()
    #handleConnections2(40)

def series():
    a, b = 0, 1
    while b < 100:
        print(b, end=' ')
        a, b = b, a + b

def collectMarks():
    mark = ''
    total = count = 0
    while True:
        mark = input('Please enter mark:')
        if mark == 'exit': break
        count += 1
        total += int(mark)
    print('Total marks: {}'.format(total))
    print('Marks average: {}'.format(total/count))


def handleConnections1():
    currentConnections = 0
    maxConnections = 35
    while True :
        # this is the same as
        # while 1
        # while 1 == 1
        if currentConnections >= maxConnections: break
        currentConnections += 1
        # in a real world application we'll do a connection string
    print()
    print('Current connections: ', currentConnections)

def handleConnections2(currentConnections = 0):
    maxConnections = 35
    while currentConnections < maxConnections:
        currentConnections +=  1
    else:
        print('Cannot open more connections')

    print('Current connections: ', currentConnections)

main()
