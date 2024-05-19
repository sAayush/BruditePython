class Lcm:
    def lcm(self, a, b):
        if a > b:
            greater = a
        else:
            greater = b
        while True:
            if greater % a == 0 and greater % b == 0:
                lcm = greater
                break
            greater += 1
        return lcm


if __name__ == '__main__':
    l = Lcm()
    print(l.lcm(12, 18))
