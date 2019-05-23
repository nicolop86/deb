#!/usr/bin/python3.5
def my_lambda_fun(n):
	return lambda x:x+n
f=my_lambda_fun(3)
print(f(0))
print(f(2)) 
print(f(3))

pairs=[('1','one'), ('2', 'two'), ('3', 'three'), ('4', 'four')]
pairs.sort(key=lambda pair:pair[1])
print(pairs)

