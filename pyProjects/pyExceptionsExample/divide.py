def divide(x,y):
    try:
        result = x/y
    except ZeroDivisionError:
        print('Divide by zero!')
    else:
        print('Result is {0}'.format(result))
    finally:
        print('Finished!')

