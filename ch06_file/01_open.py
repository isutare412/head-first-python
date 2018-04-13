if __name__ == '__main__':
    # write to file
    todos = open('todo.txt', 'w')
    print('Put out the trash.', file=todos)
    print('Feed the cat.', file=todos)
    print('Prepare tax return', file=todos)
    todos.close()

    # read from file
    tasks = open('todo.txt', 'r')
    for task in tasks:
        print(task, end='')
    tasks.close()
