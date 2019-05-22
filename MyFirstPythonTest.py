#!/usr/bin/python3.5
print ("This is my first python test!")
# this is a comment

spam = 1  # and this is the second comment
          # ... and now a third!
text = "# This is not a comment because it's inside quotes."
print (text)
sum=2+2
div=6.0/5
carry=6.0%5
print (sum)
print (div)
print('The value of carry is ', carry)
i = 256*256
print('The value of i is', i)
a,b=0,1
while a < 1000:
	print(a, end=',')
	a,b = b, a+b
