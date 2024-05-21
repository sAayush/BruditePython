class a:
    def __init__(self):
        self.x = 10


class b():
    def __init__(self):
        self.x = 20


class c(a, b):
    def __init__(self):
        a.__init__(self)
        b.__init__(self)
        print(self.x)


if __name__ == '__main__':
    c()
