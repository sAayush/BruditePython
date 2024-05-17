class Factorial:
    def __init__(self, num):
        self.num = num

    def cal(self):
        try:
            if self.num < 0:
                raise ValueError
            if self.num == 0:
                return 1
            else:
                return self.num * Factorial(self.num-1).cal()
        except ValueError:
            return 'Factorial of negative number is not possible'


if __name__ == '__main__':
    f = Factorial(5)
    print(f.cal())
    f = Factorial(-5)
    print(f.cal())
    f = Factorial(10)
    print(f.cal())

