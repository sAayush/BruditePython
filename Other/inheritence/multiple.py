class One:
    def do_something(self):
        print("Method in One")


class Two:
    def do_something(self):
        print("Method in Two")


    def do_something_two(self):
        print("Method in Two Two")


class Three(One, Two):
    pass


if __name__ == '__main__':
    t = Three()
    t.do_something()
    t.do_something_two()
