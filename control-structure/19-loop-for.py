#!/usr/bin/python3
__author__ = 'anas@al-far.com'


def main():
    print('=========== main ===========')
    #s
    # canPorts([80, 21, 22, 8080])
    # scanNetwork()
    # scanAllPortsWithBreak(breakAt = 5)
    # scanAllPortsWithStep(stepOver = 130)
    # convertToAscii('Python')
    # indexChar('Python', 'n')
    # hideChars('This is a secret message', 'Tisce')
    #printAllMonths()

def printAllMonths():
    print('=========== printAllMonths ===========')
    listOfMonths = dict({
        "January" : 1, "February" : 2, "March" : 3,
        "April" : 4, "May" : 5, "June" : 6,
        "July" : 7, "August" : 8, "September" : 9,
        "October" : 10, "November" : 11, "December" : 12
    })

    for month in listOfMonths:
        print(month, ' => ', listOfMonths[month])

def scanPorts(portsList):
    print('=========== scanPorts ===========')
    for port in portsList:
        print('scanning port#: ', port)

def scanNetwork():
    print('=========== scanNetwork ===========')
    ipList = [101, 102, 103, 104, 105, 106, 107, 108, 109, 110]

    for ip in ipList[:]: # for ip in ipList:
        print('scanning ip (192.168.1.{}) '.format(ip))
    # for ip in ipList:
    #     print('scanning ip (192.168.1.{}) '.format(ip))
    # for ip in ipList[0:6]:
    #     print('scanning ip (192.168.1.{}) '.format(ip))
    # for ip in ipList[5:]:
    #     print('scanning ip (192.168.1.{}) '.format(ip))
    # for ip in ipList[:4]:
    #     print('scanning ip (192.168.1.{}) '.format(ip))

def scanAllPortsWithBreak(breakAt):
    print('=========== scanAllPortsWithBreak ===========')
    for port in range(1, 65536):
        print('scanning port#: ', port)
        if port >= breakAt: break

def scanAllPortsWithStep(stepOver):
    print('=========== scanAllPortsWithStep ===========')
    portsList = range(1,900)
    for port in portsList[0:900:stepOver]:
        print('scanning port#: ', port)

def convertToAscii(string):
    print('=========== convertToAscii ===========')
    for char in string:
        print('ASCII for char ({}) is {}'.format(char, ord(char)))

def indexChar(string, char):
    print('=========== indexChar ===========')
    for i, c in enumerate(string):
        if char == c:
            print('index for char ({}) at index {}'.format(char, i))

def hideChars(string, secretChars):
    print('=========== hideChars ===========')
    for c in string:
        if c in secretChars:
            print('x', end='')
        else:
            print(c, end='')
    else:
        print('\ndone')

main()
