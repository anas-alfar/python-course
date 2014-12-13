#!/usr/bin/python3
__author__ = 'anas@al-far.com'

def main():
    switchCase('jo')
    switchCase('eg')
    switchCase('sa')
    switchCase('ae')
    switchCase('uk')

def switchCase(code):
    countryCode = dict(
        jo = jordanCase,
        sa = saudiArabiaCase,
        eg = egyptCase,
        ae = arabEmiratesCase,
        _ = defaultCase
    )

    countryCode.get(code, defaultCase)()

def jordanCase():
    print('Executing switchCaseJordan function...')

def saudiArabiaCase():
    print('Executing switchCaseSaudiArabia function...')

def egyptCase():
    print('Executing switchCaseEgypt function...')

def arabEmiratesCase():
    print('Executing switchCaseArabEmirates function...')

def defaultCase():
    print('Executing other function...')

main()