#!/usr/bin/python3
__author__ = 'anas@al-far.com'

# Python has several sequential types

# I can insert elements after its created
# I can append things after its created
# I can delete things after its created
print('=========== list ===========')
listVar = [1, 2, 3, 4, 5, 3]
print('printing listVar: ', listVar)
listVar.append(6)       # append new element at the end of the list
listVar.append(7)       # append new element at the end of the list
print('printing listVar: ', listVar)
listVar.insert(0, -1)   # insert new element at index 0 of the list
listVar.insert(3, 9)    # insert new element at index 3 of the list
print('printing listVar: ', listVar)
print('printing element #6 of listVar: ', listVar[5])
listVar.pop(3) # pop the element with index 3
listVar.pop() # pop the last element
listVar.pop() # pop the last element
print('printing listVar: ', listVar)
