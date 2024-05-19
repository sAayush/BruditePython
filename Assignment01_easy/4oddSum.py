def oddSum(n1 , n2):
    sum = 0
    for i in range(n1, n2+1):
        if i % 2 != 0:
            sum += i
    return sum


if __name__ == '__main__':
    n1 = 1
    n2 = 10
    print(oddSum(n1, n2))
