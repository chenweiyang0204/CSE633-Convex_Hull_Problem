import random
import csv

l = []
while(len(l)<40):
    a = [random.randint(0,300),random.randint(0,300)]
    if a in l:
        continue
    else:
        l.append(a)
l.sort()

with open('data_40.txt', 'w') as filehandle:
    for listitem in l:
        filehandle.write(str(listitem[0])+" "+str(listitem[1]))
        filehandle.write('\n')
