def ifPalindrome(word):
    return word == word[::-1]


if __name__ == '__main__':
    word = str(input('Enter a word: '))
    if ifPalindrome(word):
        print(f'{word} is a palindrome')
    else:
        print(f'{word} is not a palindrome')
