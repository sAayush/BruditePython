class vowels:
    def __init__(self, string):
        self.string = string
        self.vowels = ['a', 'e', 'i', 'o', 'u']
        self.count = 0

    def count_vowels(self):
        for char in self.string:
            if char in self.vowels:
                self.count += 1
        print(f"Number of vowels in the string: {self.count}")


if __name__ == '__main__':
    v = vowels('hello')
    v.count_vowels()
