################################################################
# 		 Challenge
# 	Hidden code is: PERSHINGSAILSFROMNYJUNEI
# 
#	Which means: PERSHING SAILS FROM NY JUNE I
################################################################
f = open('HiddenMsg.txt', 'r')
lst = []
for line in f:
    l = line.split()
    for i in l:
        lst.append(i)
print(lst)

for word in lst:
    print(word[0], end="")



