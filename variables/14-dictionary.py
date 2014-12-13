#!/usr/bin/python3
__author__ = 'anas@al-far.com'

# Python has several sequential types
# I can insert elements after its created
# I can append things after its created
# I can delete things after its created
print('=========== dictionary ===========')
dictionaryList = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5}
#print('printing dictionaryList: ', dictionaryList)
#print('printing element #3 of dictionaryList: ', dictionaryList['three'])

listOfMonths = dict(
    January = 1, February = 2, March = 3,
    April = 4, May = 5, June = 6,
    July = 7, August = 8, September = 9,
)

listOfMonths['October'] = 10
listOfMonths['November'] = 11
listOfMonths['December'] = 12
listOfMonths.pop('February')

#print('listOfMonths.items : ', listOfMonths.items())
#print('listOfMonths.keys: ', listOfMonths.keys())
#print('listOfMonths.values: ', listOfMonths.values())
#print('printing listOfMonths: ', listOfMonths)
#print('printing listOfMonths sorted: ', sorted(listOfMonths.items()))
print('printing March numeric representation: ', listOfMonths['March'])

