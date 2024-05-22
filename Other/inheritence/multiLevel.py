class FirstLevel:
    def __init__(self):
        print("FirstLevel.__init__()")

    def do_something(self):
        print("Method in FirstLevel")

    def do_this(self):
        print("Method in FirstLevel this")


class SecondLevel(FirstLevel):
    def __init__(self):
        super().__init__()
        print("SecondLevel.__init__()")

    def do_something(self):
        print("Method in SecondLevel")

    def do_that(self):
        print("Method in SecondLevel that")


class ThirdLevel(SecondLevel):
    def __init__(self):
        super().__init__()
        print("ThirdLevel.__init__()")


if __name__ == '__main__':
    t = ThirdLevel()
    t.do_something()
    t.do_this()
    t.do_that()

        