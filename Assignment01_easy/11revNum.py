class RevNum:
    def reverse(self, num):
        rev = 0
        while num > 0:
            rev = rev * 10 + num % 10
            num = num // 10
        return rev


if __name__ == '__main__':
    r = RevNum()
    num = 1234
    print(r.reverse(num))
