#!/usr/bin/python3
__author__ = 'anas@al-far.com'

import csv

def main():
    print('=========== main ===========')
    #csvFileDictReader()
    #csvFileListReader()

def csvFileDictReader():
    print('=========== csvFileDictReader ===========')
    fh = open('python-course.csv')
    reader = csv.DictReader(fh)
    for row in reader:
        print(row['student name'], ' mark is ', row['mark'])
    fh.close()

def csvFileListReader():
    print('=========== csvFileListReader ===========')
    fh = open('python-course.csv')
    reader = csv.reader(fh, delimiter=',', quotechar='"')
    for row in reader:
        print(row[0], ' mark is ', row[1])
    fh.close()

main()
