import random

rows = 1001
cols = 10001
# rows = 5
# cols = 5
mylist = []

for x in range(1, rows):
    for y in range(1, cols):
        mylist.append([x,y])
# mylist = random.sample(list,10000000)
# mylist = random.sample(list,10)
mylist.append([1020,10003])
mylist.append([800,10020])
mylist.append([0,10010])
mylist.append([0,0])
mylist.append([450,0])



mylist.sort()

print(mylist)
with open('data_10000000.txt', 'w') as filehandle:
    for listitem in mylist:
        filehandle.write(str(listitem[0])+" "+str(listitem[1]))
        filehandle.write('\n')
