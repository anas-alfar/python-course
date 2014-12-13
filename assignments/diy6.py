#########################
#  DIY 6 Answer
#########################
line = int(input("Enter number of lines: "))
for i in range(line):
    print("Line #%d" % i, end=" ")
    for j in range(i+1):
        print(j, end=" ")
    print()
#or
for i in range(line):
    print("Line #%d" % i, end=" ")
    for j in range(i+1):
        print("*", end=" ")
    print()

