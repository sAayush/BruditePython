class Shape:
    def circle(self, r):
        return 3.14 * r * r

    def rectangle(self, l, b):
        return l * b

    def triangel(self, b, h):
        return 0.5 * b * h

    def square(self, s):
        return s * s


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return self.circle(self.r)


class Rectangle(Shape):
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def area(self):
        return self.rectangle(self.l, self.b)


class Triangle(Shape):
    def __init__(self, b, h):
        self.b = b
        self.h = h

    def area(self):
        return self.triangel(self.b, self.h)


class Square(Shape):
    def __init__(self, s):
        self.s = s

    def area(self):
        return self.square(self.s)


if __name__ == '__main__':
    c = Circle(5)
    print(c.area())

    r = Rectangle(5, 3)
    print(r.area())

    t = Triangle(5, 3)
    print(t.area())

    s = Square(5)
    print(s.area())
