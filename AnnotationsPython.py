#!/usr/bin/python3.5
def f(ham: str, eggs: str = 'eggs') -> str:
    print("Annotations:", f.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs


def my_function():
    """Do nothing, but document it.

    No, really, it doesn't do anything.

    But I can do something.
    """
    pass

print(f('spam'))
print(my_function.__doc__)
