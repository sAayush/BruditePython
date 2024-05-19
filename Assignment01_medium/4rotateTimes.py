class Rotate:
    def rotateArray(self, arr, n):
        return arr[-n:] + arr[:-n]


if __name__ == '__main__':
    r = Rotate()
    arr = [1, 2, 3, 4, 5, 6]
    n = 3
    print(r.rotateArray(arr, n))
