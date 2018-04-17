def printargs(*args, **kwargs):
    print('%+7s' % 'args:', args)
    print('%+7s' % 'kwargs:', kwargs)


list_values = [7, 8]
values = {'c': 5, 'd': 6}
printargs(1, 2, a=3, b=4, *list_values, **values)
