def count(s):
    alph = 0
    num = 0
    for i in s:
        if i.isalpha():
            alph += 1
        elif i.isdigit():
            num += 1
    return f'Alphabets: {alph}, Numbers: {num}'


if __name__ == '__main__':
    s = 'asdf1234'
    print(count(s))