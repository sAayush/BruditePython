def vals(n):
    for i in range(n + 1):
        yield i


def is_prime(i):
    if i < 2:
        return next(p)
    for j in range(2, i // 2 + 1):
        if i % j == 0:
            next(p)


if __name__ == '__main__':
    p = vals(100)
    for i in p:
        is_prime(i)
        print(i)



# def is_prime(i):
#     if i < 2:
#         return False
#     for j in range(2, i // 2 + 1):
#         if i % j == 0:
#             return False
#     return True
#
#
# if __name__ == '__main__':
#     p = vals(100)
#     for i in p:
#         if is_prime(i):
#             print(i)
