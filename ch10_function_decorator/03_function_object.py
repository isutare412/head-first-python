def outer():
    def inner():
        print('This is inner')

    print('This is outer, returning inner...')
    return inner


i = outer()
i()
