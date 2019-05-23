#!/usr/bin/python3.5
print("This is some more python....")
print("Testing control flow statements - IF")
x = int(input("Please enter an integer: "))
if x < 0:
	x = 0
	print('Negative changed to zero')
elif x == 0:
	print('Zero')
elif x == 1:
	print('Single')
else:
	print('More')

print("Testing control flow statements - FOR")
animals = ['Cat', 'Dog', 'Crocodile', 'Tortoise', 'Lion']
for animal in animals:
	print(animal, len(animal))
print('Testing modifying arays in for statement')
for animal in animals[:]:
	if(len(animal)>8):
		animals.insert(0, animal)
for animal in animals:
	print(animal, len(animal))
print('Testing control flow statements - RANGE OBJECT')
print(range(10))
print('Range is an object useful in for statements (pay attention, animals was modified)')
for index in range(len(animals)):
	print('Range animal', animals[index])
print('Testing control flow statements - ELSE in FOR loop with break (pay attention to indentation)')
for n in range(2, 10):
	for x in range(2, n):
		if n % x == 0:
			print(n, 'equals', x, '*', n//x)
			break
	else:
		# loop fell through without finding a factor
		print(n, 'is a prime number')
print('Testing control flow statments - CONTINUE')
for n in range(2,10):
	if(n % 2 == 0):
		print('Found an even number', n)
		continue
	print('Found an odd number', n)

