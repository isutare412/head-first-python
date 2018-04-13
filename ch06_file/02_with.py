if __name__ == '__main__':
    # write to file
    with open('todo.txt', 'w') as todos:
        print('Put out the trash.', file=todos)
        print('Feed the cat.', file=todos)
        print('Prepare tax return', file=todos)

    # read from file
    with open('todo.txt', 'r') as tasks:
        for task in tasks:
            print(task, end='')
