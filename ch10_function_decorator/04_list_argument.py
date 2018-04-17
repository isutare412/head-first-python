def myfunc(*args):
    for a in args:
        print(a, end=' ')
    if args:
        print()


myfunc(1, 2, 3, 4, 5, 6)

values = [3, 2, 1]
myfunc(*values)
