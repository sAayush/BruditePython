class Super:
    def method(self):
        print('in Super.method')


class Inheritor(Super):
    pass


if __name__ == '__main__':
    i = Inheritor()
    i.method()
