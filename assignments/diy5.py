#########################
#  DIY 5 Answer
import random
f = open("file2.txt", "w")
for count in range(100):
    rnumber = random.randint(0,99)
    f.write(str(rnumber) + '\n')
f.close()

odd = []
even = []
f = open('file2.txt','r')
for line in f:
    row = line.split()
    for i in row:
        if int(i) % 2 == 0:
            even.append(int(i))
        else:
            odd.append(int(i))
print ("Even list is: ", even)
print ("Odd list is: ", odd)

