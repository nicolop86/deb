#!/usr/bin/python
numLines=0
with open('prova') as fileRead:
    for line in fileRead:
        print(line, end='')
        numLines += 1 
print('###########')

f = open('prova', 'a')
f.write('Dato{0} Altro saluto\n'.format(numLines+1))
f.close()

for line in open('prova'):
    print(line, end='')

print('JSON test')
import json
print(json.dumps([1, 'simple', 'list']))

fnew = open('provaJSON', 'w')
json.dump({'prova':'json'}, fnew)
fnew.close()

