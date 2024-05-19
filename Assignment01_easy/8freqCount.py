class Freq:
    def count(self, l):
        freq = {}
        for i in l:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        return freq


if __name__ == '__main__':
    f = Freq()
    l = [1, 2, 3, 4, 1, 2, 1, 3, 4, 5]
    print(f.count(l))
