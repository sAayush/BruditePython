class Anagram:
    def __init__(self):
        self.str1 = input("Enter first string: ")
        self.str2 = input("Enter second string: ")

    def checkAnagram(self):
        if sorted(self.str1) == sorted(self.str2):
            print("Strings are anagram")
        else:
            print("Strings are not anagram")


if __name__ == '__main__':
    anagram = Anagram()
    anagram.checkAnagram()
