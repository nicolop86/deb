#!/usr/bin/python
for line in open('prova'):
    print(line, end='')
print('###########')

f = open('prova', 'a')
f.write('DatoX	XXX\n')
f.close()

for line in open('prova'):
    print(line, end='')

print('JSON test')
import json
print(json.dumps([1, 'simple', 'list']))

fnew = open('provaJSON', 'w')
json.dump({'prova':'json'}, fnew)
fnew.close()

