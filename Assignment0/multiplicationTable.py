def printTable(num):
    for i in range(1, 11):
        print(f'{num} * {i} = {num*i}')


if __name__ == '__main__':
    num = int(input('Enter a number: '))
    printTable(num)