def power_of_two_recursion(n):
    if n == 1:
        return True
    elif n % 2 != 0:
        return False
    return power_of_two_recursion(n // 2)

if __name__ == '__main__':
    print(power_of_two_recursion(32))
    print(power_of_two_recursion(31))
