class StringManipulator:
    def reverseString(self, s):
        return s[::-1]


if __name__ == '__main__':
    s = "hello"
    sm = StringManipulator()
    print(sm.reverseString(s))