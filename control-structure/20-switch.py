#!/usr/bin/python3
__author__ = 'anas@al-far.com'

def main():
    switchCase('jo')
    switchCase('eg')
    switchCase('sa')
    switchCase('ae')
    #switchCase('uk')

def switchCase(code):
    countryCode = dict(
        jo = 'Jordan',
        sa = 'Saudi Arabia',
        eg = 'Egypt',
        ae = 'United Arab Emirates'
    )

    print(countryCode[code])


main()