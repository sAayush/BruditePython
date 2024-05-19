class RevWords:
    def sentance(self, s):
        return ' '.join(s.split()[::-1])


if __name__ == '__main__':
    rw = RevWords()
    s = "Hello World"
    print(rw.sentance(s))
