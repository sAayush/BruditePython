class Vowels:
    def count_vowels(self, s):
        count = 0
        vowels = ['a', 'e', 'i', 'o', 'u']
        for i in s:
            if i in vowels:
                count += 1
        return count


if __name__ == '__main__':
    v = Vowels()
    print(v.count_vowels("hello"))
