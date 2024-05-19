def ifPerfect(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    return sum == num


if __name__ == '__main__':
    num = int(input('Enter a number: '))
    if ifPerfect(num):
        print(f'{num} is a perfect number')
    else:
        print(f'{num} is not a perfect number')

