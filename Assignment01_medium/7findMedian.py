def median(lst):
    lst.sort()
    n = len(lst)
    if n % 2 == 0:
        return (lst[n//2] + lst[n//2 - 1]) / 2
    else:
        return lst[n//2]


if __name__ == '__main__':
    lst = [4, 5, 6, 1, 2, 3]
    print(median(lst))
