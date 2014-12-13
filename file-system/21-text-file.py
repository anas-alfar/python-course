# send email to
m='psutinfosecclub@gmail.com'
m='text file URL: http://goo.gl/dpeZKa'
s='PERSHINGSAILSFROMNYJUNEI'
Real Message is: PERSHING SAILS FROM NY JUNE I

def readTextFile():
    print('=========== readTextFile ===========')
    fileName = input('Please enter file name:')
    fh = open(fileName, 'r')
    for line in fh.readlines():
        print(line, end='')
    fh.close()

readTextFile()
