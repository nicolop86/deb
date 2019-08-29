#!/usr/bin/python
import sys

for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except IOError:
        print('cannot open {0}'.format(arg))
    else:
        print('{0} has {1} lines'.format(arg, len(f.readlines())))
        f.close()
 
