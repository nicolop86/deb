#!/usr/bin/python3.5
def fibonacci(maxNum):
	"""This function prints Fibonacci series until result is less than maxNum."""	
	a,b = 0,1
	while a < maxNum:
		print('Fibonacci series number:', a, end='\n')
		a,b = b, (a+b)

fibonacci(10000)
#print (fibonacci.__doc__)
# Fibonacci series results returned as an array
def fibonacci_results(maxNum):
	"""This function returns Fibonacci series until result is less than maxNum as an array."""
	a,b = 0,1
	results = []
	while a < maxNum:
		results.append(a)
		a,b = b, (a+b)
	return results
f10000=fibonacci_results(10000)
print(f10000)

