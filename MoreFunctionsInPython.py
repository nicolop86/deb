#!/usr/bin/python3.5
def ask_ok(prompt, retries=4, message='Please, try again!'):
	while True:
		ok=input(prompt)
		if ok in('y', 'yes', 'ye', 'Y'):
			return True
		elif ok in ('no', 'nope', 'n', 'N'):
			return False
		retries=retries-1
		if retries < 0:
			raise ValueError('Invalid User Response')
		print(message)

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    keys = sorted(keywords.keys())
    for kw in keys:
        print(kw, ":", keywords[kw])

times=5
question=('Are you happy?')
ask_ok(question, times)

print(f(1))
print(f(2))
print(f(3))

parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")
