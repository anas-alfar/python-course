#########################
#  DIY 7 Answer
#########################
count = 0
f = open('msg.txt','r')
for line in f:
    count += len(line.split())
print(count)
f.close()
