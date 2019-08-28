#!/usr/bin/python
tel={'nico':3384150517, 'miki':3475934338}
print(tel)
print(tel['nico'])
print(list(tel.keys()))
print(sorted(tel.keys()))

newDict=dict([('one', 1), ('two', 2), ('three', 3)])
print(newDict)

print('Looping over tel')
for k, v in tel.items():
	print(k, v)

print('Looping over a sequence')
for i, v in enumerate(['tic', 'tac', 'toe']):
	print(i, v)

print('Use of zip function')
teams = ['Milan', 'Sporting Lisbona', 'Ajax']
definitions = ['AC', 'FC', 'FC']
for q, a in zip(definitions, teams):
	print('My favourite team is {0} {1}'.format(q, a))

a = (1, 2, 3)
b = (1, 2, 5)

if (a < b): 
	print('True')
else:
	print('False')

