#!/usr/bin/python3
__author__ = 'anas@al-far.com'


s = 'This is a single quote string.'
#print(s)
s = "This is a double quote string."
#print(s)
s = "This is a \nnew line."
#print(s)
s = r"This \t \\is a \nnew line."
#print(s)
s = 'This is a formatted string{}'.format('.')
#print(s)
s = '''This is a treble string.'''
#print(s)
s = '''
This is
a multi-line
string.'''
#print(s)
s = """\
this is
a multi-line
string."""
#print(s)
s = 'Coding Hazard'
print(s)
print('Upper case: ', s.upper())
print('Lower case: ', s.lower())
print('Capitalize case: ', s.capitalize())
print('Swap case: ', s.swapcase())
print('Replace (Hazard/Dangerous): ', s.replace('Hazard', 'Dangerous'))
print('Find (z): ', s.find('z'))
print('Print byte with index #2: ', s[2])
print('Print byte with index -2 from the end of the string: ', s[-2])
print('Print bytes from index #0 to index #6: ', s[0:6])
print('Print bytes from index #-6 to the end of the string: ', s[-6:])
print('Print bytes from index #7 to the end of the string: ', s[7:])
print('This is a Python workshop'.split())
print('Python is a word with ({}) chars length'.format(len('Python')))
print('     This is a string with a lot of whitespace    ')
print('     This is a string with a lot of whitespace removed     '.strip())
print('This is {} workshop.    '.format('Python').upper().strip())

'''
This is a multi line comment
You can use this feature to
define a multi-line comment
'''
