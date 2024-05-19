class SumSingle:
    def sumNum(self, num):
        if num < 10:
            return num
        else:
            sum = 0
            while num > 0:
                sum += num % 10
                num = num // 10
            return self.sumNum(sum)


if __name__ == '__main__':
    s = SumSingle()
    num = 1234
    print(s.sumNum(num))