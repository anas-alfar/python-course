##################################################
#  DIY 8 Answer MODULE
#  Module used for DIY #8
##################################################
def countWords(filename):
    count = 0
    f = open(filename,'r')
    for line in f:
        count += len(line.split())
    f.close()
    return count

def printStars(lines):
    for i in range(lines):
        print("Line #%d" % i, end=" ")
        for j in range(i+1):
            print(j, end=" ")
        print()
