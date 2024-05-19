class ListChar:
    def word_char(self, lst):
        words = []
        for word in lst:
            words.append(list(word))

        return words


if __name__ == '__main__':
    lc = ListChar()
    lst = ['hello', 'world']
    print(lc.word_char(lst))