#!/usr/bin/python
from math import pi

vec = [-4, -2, 0, 4]
print([x*2 for x in vec])
print([(x, x**2) for x in vec])
piApprox=[str(round(pi, i)) for i in range(1,6)]
print(piApprox)

matrix=[
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
print('Matrix')
print(matrix)
print('Transposed')
transp=[[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(transp)
print('... which is the same as...')
transpZip=list(zip(*matrix))
print(transpZip)
print('...deleting row...')
del(transpZip[0])
print(transpZip)

