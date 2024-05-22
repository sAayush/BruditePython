class Main:
    def __init__(self):
        print("Main class constructor")

    def do_something(self):
        print("Method in Main")

class First(Main):
    def __init__(self):
        super().__init__()
        print("First class constructor")


class Second(Main):
    def __init__(self):
        super().__init__()
        print("Second class constructor")


class Third(Main):
    def __init__(self):
        super().__init__()
        print("Third class constructor")


if __name__ == '__main__':
    f = First()
    s = Second()
    t = Third()
    f.do_something()
    s.do_something()
    t.do_something()