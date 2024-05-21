class Uniq:
    def unique_elements(self, arr):
        return list(set(arr))


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 4, 5, 5, 6]
    u = Uniq()
    print(u.unique_elements(arr))