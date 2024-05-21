def even_numbers(n):
    for i in range(2, n+1, 2):
        yield i


if __name__ == '__main__':
    en = even_numbers(10)
    for i in en:
        print(i)