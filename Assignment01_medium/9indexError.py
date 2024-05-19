def modify_list_element(lst, index, value):
    try:
        lst[index] = value
        print(f'List after modification: {lst}')
    except IndexError:
        print(f'Error: Index {index} is out of range for the list.')


if __name__ == '__main__':
    lst = [1, 2, 3, 4, 5]

    try:
        index = int(input('Enter the index to modify: '))
        value = int(input('Enter the new value: '))

        modify_list_element(lst, index, value)
    except ValueError:
        print('Error: Please enter valid integers for index and value.')
