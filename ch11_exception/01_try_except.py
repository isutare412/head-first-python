try:
    with open('myfile.txt') as fh:
        file_data = fh.read()
    print(file_data)
except FileNotFoundError:
    print('The data file is missing.')
except PermissionError:
    print('Accessing the file is not allowed.')
except Exception as err:
    print('Some other error occurred:', str(err))
