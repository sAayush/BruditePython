class Calculator:
    def power(self, n, p):
        try:
            if n < 0 or p < 0:
                raise ValueError("n and p should be non-negative")
        except ValueError as e:
            return e
        return n ** p


if __name__ == '__main__':
    c = Calculator()
    print(c.power(5, 2))
    print(c.power(-5, 3))
    print(c.power(2, 5))