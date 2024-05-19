class Unique:
    def uniq(self, l):
        return list(set(l))


if __name__ == '__main__':
    u = Unique()
    l = [1, 2, 3, 4, 1, 2, 1, 3, 4, 5]
    print(u.uniq(l))