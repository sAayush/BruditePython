def whatIf(num):
    if num % 3 == 0:
        if num % 5 == 0:
            return "Brudite - Python Training"
        else:
            return "Brudite"
    elif num % 5 == 0:
        return "Python Training"
    else:
        return num


if __name__ == '__main__':
    for i in range(1, 101):
        print(whatIf(i))